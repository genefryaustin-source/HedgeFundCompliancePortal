# integrations.py - Simplified version for testing (Google Drive disabled)
import os
import base64
from datetime import datetime
import streamlit as st
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Document, Recipients

def get_docusign_access_token():
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

def generate_and_sign_policy(title: str, content: str, username: str, email: str, folder_id: str = "Compliance_Policies"):
    from utils import generate_pdf_from_markdown
    
    safe_title = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in title)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    pdf_path = f"pdfs/{safe_title}_{username}_{timestamp}.pdf"
    
    try:
        pdf_path = generate_pdf_from_markdown(title, content, pdf_path)
        # Google Drive temporarily disabled to isolate DocuSign
        drive_id = "GOOGLE_DRIVE_DISABLED_FOR_TESTING"
        envelope_id = create_docusign_envelope(pdf_path, title, email, username)
        
        return drive_id, envelope_id, pdf_path
    except Exception as e:
        raise Exception(f"Integration failed: {str(e)}")