import streamlit as st
import docusign_esign as docusign
from docusign_esign import ApiClient, EnvelopesApi
import base64
import os
from datetime import datetime, timedelta
import jwt  # PyJWT
from cryptography.hazmat.primitives import serialization
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# ====================== GOOGLE DRIVE (Service Account - Headless) ======================
def get_drive_service():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file(
        'service_account.json', scopes=SCOPES)
    return build('drive', 'v3', credentials=credentials)

def upload_to_drive(file_path, folder_id, mime_type='application/pdf'):
    service = get_drive_service()
    file_metadata = {'name': os.path.basename(file_path), 'parents': [folder_id]}
    media = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')

# ====================== DOCUSIGN JWT AUTH (Headless) ======================
DS_CONFIG = {
    "client_id": st.secrets["DOCUSIGN_CLIENT_ID"],      # Integration Key (GUID)
    "user_id": st.secrets["DOCUSIGN_USER_ID"],          # Impersonated User GUID
    "account_id": st.secrets["DOCUSIGN_ACCOUNT_ID"],
    "private_key": st.secrets["DOCUSIGN_PRIVATE_KEY"],  # Full PEM string (or load from file)
    "auth_server": "account-d.docusign.net",            # Sandbox; change to "account.docusign.com" for prod
    "base_path": "https://demo.docusign.net/restapi"    # Sandbox; change for prod
}

def get_jwt_token():
    """Generate JWT and request access token (caches via session for ~1hr)."""
    if "docusign_token" in st.session_state and st.session_state.docusign_token_expiry > datetime.utcnow():
        return st.session_state.docusign_api_client

    # Load private key
    private_key_bytes = DS_CONFIG["private_key"].encode('utf-8') if isinstance(DS_CONFIG["private_key"], str) else DS_CONFIG["private_key"]
    private_key = serialization.load_pem_private_key(private_key_bytes, password=None)

    now = datetime.utcnow()
    payload = {
        "iss": DS_CONFIG["client_id"],
        "sub": DS_CONFIG["user_id"],
        "aud": f"https://{DS_CONFIG['auth_server']}/oauth/token",
        "scope": "signature impersonation",
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(seconds=3600)).timestamp())
    }
    jwt_token = jwt.encode(payload, private_key, algorithm="RS256")

    api_client = ApiClient()
    api_client.host = DS_CONFIG["base_path"]
    try:
        token_response = api_client.request_jwt_user_token(
            client_id=DS_CONFIG["client_id"],
            user_id=DS_CONFIG["user_id"],
            oauth_host_name=DS_CONFIG["auth_server"],
            private_key_bytes=private_key_bytes,
            expires_in=3600,
            scopes=["signature", "impersonation"]
        )
        api_client.set_access_token(token_response.access_token, token_response.expires_in)
        st.session_state.docusign_api_client = api_client
        st.session_state.docusign_token_expiry = now + timedelta(seconds=3500)
        return api_client
    except Exception as e:
        st.error(f"DocuSign JWT Error: {str(e)} – Verify consent, scopes, and key.")
        return None

def create_docusign_envelope(document_path, signer_name, signer_email, policy_title):
    api_client = get_jwt_token()
    if not api_client:
        return None
    envelopes_api = EnvelopesApi(api_client)

    with open(document_path, "rb") as doc:
        doc_b64 = base64.b64encode(doc.read()).decode("utf-8")

    document = docusign.Document(
        document_base64=doc_b64,
        name=policy_title,
        file_extension="pdf",
        document_id="1"
    )

    signer = docusign.Signer(
        email=signer_email,
        name=signer_name,
        recipient_id="1",
        routing_order="1",
        tabs=docusign.Tabs(
            sign_here_tabs=[docusign.SignHere(
                document_id="1",
                page_number="1",
                recipient_id="1",
                tab_label="Sign Here",
                x_position="300",
                y_position="500"
            )]
        )
    )

    envelope_definition = docusign.EnvelopeDefinition(
        email_subject=f"Compliance Attestation: {policy_title}",
        documents=[document],
        recipients=docusign.Recipients(signers=[signer]),
        status="sent"
    )

    try:
        results = envelopes_api.create_envelope(
            account_id=DS_CONFIG["account_id"],
            envelope_definition=envelope_definition
        )
        return results.envelope_id
    except Exception as e:
        st.error(f"Envelope Error: {str(e)}")
        return None

def get_envelope_status(envelope_id):
    """Placeholder – implement webhooks for production."""
    api_client = get_jwt_token()
    envelopes_api = EnvelopesApi(api_client)
    results = envelopes_api.get_envelope(DS_CONFIG["account_id"], envelope_id)
    return results.status, results