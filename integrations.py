# integrations.py - Fixed version (no st at top level)
import os
import json
import base64
from datetime import datetime
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Document, Recipients
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def get_docusign_access_token():
    """Get JWT token using secrets."""
    import streamlit as st  # Import inside function
    
    api_client = ApiClient(base_path=st.secrets["DOCUSIGN"].get("BASE_PATH", "https://demo.docusign.net/restapi"))
    
    private_key = st.secrets["DOCUSIGN"]["PRIVATE_KEY"].encode("utf-8")
    
    token_response = api_client.request_jwt_user_token(
        client_id=st.secrets["DOCUSIGN"]["INTEGRATION_KEY"],
        user_id=st.secrets["DOCUSIGN"]["USER_ID"],
        oauth_host_name=st.secrets["DOCUSIGN"].get("OAUTH_HOST", "account-d.docusign.com"),
        private_key_bytes=private_key,
        expires_in=3600,
        scopes=["signature", "impersonation"]
    )
    return token_response.access_token

def create_docusign_envelope(pdf_path: str, document_name: str, signer_email: str, signer_name: str = "Chief Compliance Officer"):
    """Create and send real DocuSign envelope."""
    import streamlit as st
    
    try:
        access_token = get_docusign_access_token()
        
        api_client = ApiClient(base_path=st.secrets["DOCUSIGN"].get("BASE_PATH", "https://demo.docusign.net/restapi"))
        api_client.set_default_header("Authorization", f"Bearer {access_token}")
        
        envelopes_api = EnvelopesApi(api_client)
        
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        
        document = Document(
            document_base64=base64.b64encode(pdf_bytes).decode("utf-8"),
            name=document_name,
            file_extension="pdf",
            document_id="1"
        )
        
        signer = Signer(
            email=signer_email,
            name=signer_name,
            recipient_id="1",
            routing_order="1"
        )
        
        sign_here = SignHere(
            document_id="1",
            page_number="1",
            recipient_id="1",
            tab_label="Sign Here",
            x_position="300",
            y_position="500"
        )
        
        signer.tabs = {"sign_here_tabs": [sign_here]}
        
        envelope_definition = EnvelopeDefinition(
            email_subject=f"Compliance Policy Signature Required: {document_name}",
            documents=[document],
            recipients=Recipients(signers=[signer]),
            status="sent"
        )
        
        results = envelopes_api.create_envelope(
            account_id=st.secrets["DOCUSIGN"]["ACCOUNT_ID"],
            envelope_definition=envelope_definition
        )
        
        return results.envelope_id
        
    except Exception as e:
        raise Exception(f"DocuSign Error: {str(e)}")

def upload_to_google_drive(file_path: str, folder_id: str = None):
    """Upload to Google Drive."""
    import streamlit as st
    try:
        creds_info = json.loads(st.secrets["GOOGLE"]["SERVICE_ACCOUNT_JSON"])
        credentials = service_account.Credentials.from_service_account_info(
            creds_info, scopes=['https://www.googleapis.com/auth/drive']
        )
        
        service = build('drive', 'v3', credentials=credentials)
        
        file_metadata = {'name': os.path.basename(file_path)}
        if folder_id:
            file_metadata['parents'] = [folder_id]
        
        media = MediaFileUpload(file_path, resumable=True)
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        
        return file.get('id')
    except Exception as e:
        raise Exception(f"Google Drive Error: {str(e)}")

def generate_and_sign_policy(title: str, content: str, username: str, email: str, folder_id: str = "Compliance_Policies"):
    """Main entry point - called from Policies page."""
    from utils import generate_pdf_from_markdown
    
    safe_title = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in title)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    pdf_path = f"pdfs/{safe_title}_{username}_{timestamp}.pdf"
    
    try:
        pdf_path = generate_pdf_from_markdown(title, content, pdf_path)
        drive_id = upload_to_google_drive(pdf_path, folder_id)
        envelope_id = create_docusign_envelope(pdf_path, title, email, username)
        
        return drive_id, envelope_id, pdf_path
    except Exception as e:
        raise Exception(f"Integration failed: {str(e)}")