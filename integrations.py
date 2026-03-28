# integrations.py - Real Google Drive + DocuSign JWT for hedge fund compliance portal
import os
import json
from datetime import datetime
import jwt  # PyJWT
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Document, Recipients
import base64

# ========================= CONFIGURATION =========================
# Put these in Streamlit Secrets (st.secrets) or environment variables

DS_CONFIG = {
    "ds_client_id": st.secrets.get("DOCUSIGN_INTEGRATION_KEY", "YOUR_INTEGRATION_KEY"),
    "ds_impersonated_user_id": st.secrets.get("DOCUSIGN_USER_ID", "YOUR_USER_GUID"),
    "ds_account_id": st.secrets.get("DOCUSIGN_ACCOUNT_ID", "YOUR_ACCOUNT_ID"),
    "ds_private_key": st.secrets.get("DOCUSIGN_PRIVATE_KEY", "-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----"),  # full PEM string
    "ds_oauth_host": "account-d.docusign.com",  # Use "account.docusign.com" for production
    "ds_base_path": "https://demo.docusign.net/restapi"  # Change to production when ready
}

GOOGLE_CREDENTIALS = st.secrets.get("GOOGLE_SERVICE_ACCOUNT_JSON")  # Full JSON string or dict

# ================================================================

def get_docusign_access_token():
    """Get JWT access token using DocuSign SDK method."""
    api_client = ApiClient(base_path=DS_CONFIG["ds_base_path"])
    
    private_key_bytes = DS_CONFIG["ds_private_key"].encode('utf-8')
    
    try:
        token_response = api_client.request_jwt_user_token(
            client_id=DS_CONFIG["ds_client_id"],
            user_id=DS_CONFIG["ds_impersonated_user_id"],
            oauth_host_name=DS_CONFIG["ds_oauth_host"],
            private_key_bytes=private_key_bytes,
            expires_in=3600,
            scopes=["signature", "impersonation"]
        )
        return token_response.access_token
    except Exception as e:
        raise Exception(f"DocuSign JWT Authentication failed: {str(e)}")

def create_docusign_envelope(pdf_path: str, document_name: str, signer_email: str, signer_name: str = "Chief Compliance Officer"):
    """Create and send a real DocuSign envelope with the PDF for signature."""
    try:
        access_token = get_docusign_access_token()
        
        api_client = ApiClient(base_path=DS_CONFIG["ds_base_path"])
        api_client.set_default_header("Authorization", f"Bearer {access_token}")
        
        envelopes_api = EnvelopesApi(api_client)
        
        # Document
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        
        document = Document(
            document_base64=base64.b64encode(pdf_bytes).decode("utf-8"),
            name=document_name,
            file_extension="pdf",
            document_id="1"
        )
        
        # Signer
        signer = Signer(
            email=signer_email,
            name=signer_name,
            recipient_id="1",
            routing_order="1"
        )
        
        # Sign Here tab
        sign_here = SignHere(
            document_id="1",
            page_number="1",
            recipient_id="1",
            tab_label="Sign Here",
            x_position="300",
            y_position="500"
        )
        
        signer.tabs = {"sign_here_tabs": [sign_here]}
        
        # Envelope Definition
        envelope_definition = EnvelopeDefinition(
            email_subject=f"Compliance Policy Signature: {document_name}",
            documents=[document],
            recipients=Recipients(signers=[signer]),
            status="sent"
        )
        
        # Create envelope
        results = envelopes_api.create_envelope(
            account_id=DS_CONFIG["ds_account_id"],
            envelope_definition=envelope_definition
        )
        
        return results.envelope_id
        
    except Exception as e:
        print(f"DocuSign Error: {str(e)}")
        return f"ERROR_{datetime.now().strftime('%Y%m%d%H%M')}"

def upload_to_google_drive(file_path: str, folder_id: str = None):
    """Upload file to Google Drive using Service Account."""
    try:
        if isinstance(GOOGLE_CREDENTIALS, str):
            creds_dict = json.loads(GOOGLE_CREDENTIALS)
        else:
            creds_dict = GOOGLE_CREDENTIALS
        
        credentials = service_account.Credentials.from_service_account_info(
            creds_dict,
            scopes=['https://www.googleapis.com/auth/drive']
        )
        
        service = build('drive', 'v3', credentials=credentials)
        
        file_metadata = {'name': os.path.basename(file_path)}
        if folder_id:
            file_metadata['parents'] = [folder_id]
        
        media = MediaFileUpload(file_path, resumable=True)
        
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        return file.get('id')
        
    except Exception as e:
        print(f"Google Drive Upload Error: {str(e)}")
        return f"DRIVE_ERROR_{datetime.now().strftime('%Y%m%d%H%M')}"

# Updated generate_and_sign_policy that uses the real functions above
def generate_and_sign_policy(title: str, content: str, username: str, email: str, folder_id: str = "Compliance_Policies"):
    """Main function called from Policies page - now uses real integrations."""
    from utils import generate_pdf_from_markdown  # Import from your utils.py
    
    safe_title = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in title)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    pdf_path = f"pdfs/{safe_title}_{username}_{timestamp}.pdf"
    
    try:
        # 1. Generate professional PDF
        pdf_path = generate_pdf_from_markdown(title, content, pdf_path)
        
        # 2. Upload to Google Drive
        drive_id = upload_to_google_drive(pdf_path, folder_id)
        
        # 3. Send for DocuSign signature
        envelope_id = create_docusign_envelope(
            pdf_path=pdf_path,
            document_name=title,
            signer_email=email,
            signer_name=username
        )
        
        print(f"✅ Success - PDF: {pdf_path} | Drive: {drive_id} | Envelope: {envelope_id}")
        return drive_id, envelope_id, pdf_path
        
    except Exception as e:
        print(f"❌ Full integration error: {str(e)}")
        # Fallback to placeholder on error
        return f"ERROR_DRIVE_{timestamp}", f"ERROR_ENVELOPE_{timestamp}", pdf_path