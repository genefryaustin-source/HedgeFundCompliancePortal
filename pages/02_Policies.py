import streamlit as st
from datetime import datetime
from utils import generate_and_sign_policy
from database import log_attestation, log_audit_trail

st.title("📘 Policies & Procedures Library")
st.caption("All policies are version-controlled, attestable via DocuSign, and stored in Google Drive.")

policies = {
    "Compliance Manual (Rule 206(4)-7)": "compliance_manual.md",
    "Code of Ethics (Rule 204A-1)": "code_of_ethics.md",
    "AML/BSA 5-Pillar Program": "aml_bsa.md",
    "Cybersecurity & Reg S-P WISP": "cybersecurity_policy.md",
    "Incident Reporting & Response": "incident_reporting.md",
    "Phishing Response Playbook": "phishing_response_playbook.md",
    "AI Policy & Procedures": "ai_policy.md",
    "GDPR Data Privacy": "gdpr_data_privacy.md",
    "CCPA Privacy": "ccpa_privacy.md"
}

for title, filename in policies.items():
    with st.expander(f"📄 {title}", expanded=False):
        try:
            with open(f"policies/{filename}", "r", encoding="utf-8") as f:
                content = f.read()
            
            # Show full detailed content on the page
            st.markdown(content)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(f"✅ Attest via DocuSign – {title}", key=f"attest_{title}"):
                    drive_id, envelope_id, _ = generate_and_sign_policy(
                        title, content, st.session_state.username, st.session_state.email, st.secrets["GOOGLE_DRIVE_FOLDER_ID"]
                    )
                    log_attestation(st.session_state.username, title, drive_id, envelope_id)
                    log_audit_trail(st.session_state.username, "Policy Attestation", f"Attested to {title}", "Unknown")
                    st.success(f"✅ Document sent for DocuSign signature. Envelope ID: {envelope_id}")
            
            with col2:
                if st.button(f"📥 Download PDF – {title}", key=f"pdf_{title}"):
                    pdf_path = f"pdfs/{title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
                    generate_pdf_from_markdown(title, content, pdf_path)
                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            label="Download PDF Now",
                            data=f,
                            file_name=f"{title}.pdf",
                            mime="application/pdf"
                        )
            
            with col3:
                st.caption("Version-controlled • Signed versions stored in Google Drive")
                
        except FileNotFoundError:
            st.error(f"Policy file '{filename}' not found in the policies/ folder. Please add it.")

st.sidebar.info("All policy attestations and downloads are logged with full audit trail.")