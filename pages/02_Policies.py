import streamlit as st
from utils import generate_and_sign_policy
from database import log_attestation, log_audit_trail

st.title("📘 Policies & Procedures Library")

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
    with st.expander(title):
        try:
            with open(f"policies/{filename}", "r", encoding="utf-8") as f:
                content = f.read()
            st.markdown(content[:600] + "..." if len(content) > 600 else content)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Attest via DocuSign – {title}", key=f"attest_{title}"):
                    drive_id, envelope_id, _ = generate_and_sign_policy(
                        title, content, st.session_state.username, st.session_state.email, st.secrets["GOOGLE_DRIVE_FOLDER_ID"]
                    )
                    log_attestation(st.session_state.username, title, drive_id, envelope_id)
                    log_audit_trail(st.session_state.username, "Policy Attestation", f"Attested to {title}", "Unknown")
                    st.success(f"✅ Sent for DocuSign. Envelope: {envelope_id}")
            with col2:
                if st.button(f"Download PDF – {title}", key=f"pdf_{title}"):
                    # Use your generate_pdf_from_markdown function here
                    st.info("PDF download logic from utils")
        except FileNotFoundError:
            st.error(f"File {filename} not found in policies/ folder")