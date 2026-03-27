import streamlit as st
from datetime import datetime
from utils import generate_and_sign_policy
from database import log_training_record

st.title("📚 Training & Certification Center")
st.markdown("**Mandatory Annual Training** – 80% pass required for certificate.")

training_modules = {
    "AML_BSA": {"title": "AML/BSA 5-Pillar Training", "file": "aml_bsa.md"},
    "RegSP_Cyber": {"title": "Reg S-P WISP & Cybersecurity Training", "file": "cybersecurity_policy.md"},
    "AI_Ethics": {"title": "AI Ethics & Compliance Training", "file": "ai_policy.md"},
    "Incident_Reporting": {"title": "Incident Reporting & Response", "file": "incident_reporting.md"},
    "Phishing_Response": {"title": "Phishing Awareness & Response Playbook", "file": "phishing_response_playbook.md"}
}

selected = st.selectbox("Select Module", list(training_modules.keys()))
module = training_modules[selected]

st.subheader(module["title"])

# Example quiz logic (expand with full questions per module as provided earlier)
questions = [
    {"q": "Under Reg S-P, customer notification timeframe for qualifying incidents?", "options": ["30 days", "72 hours"], "correct": "30 days"},
    # Add 8-10 realistic questions per module (from previous responses)
]

score = 0
for i, q in enumerate(questions[:5]):  # truncated for brevity
    ans = st.radio(q["q"], q["options"], key=f"{selected}_q{i}")
    if ans == q["correct"]:
        score += 1

if st.button("Submit & Generate Certificate"):
    passed = score >= 4  # example threshold
    if passed:
        cert_title = f"{module['title']}_Certificate"
        content = f"Employee: {st.session_state.name}\nScore: {score}/10\nDate: {datetime.now().strftime('%Y-%m-%d')}\nModule: {module['title']}"
        drive_id, envelope_id, pdf_path = generate_and_sign_policy(
            cert_title, content, st.session_state.username, st.session_state.email, st.secrets["GOOGLE_DRIVE_FOLDER_ID"]
        )
        log_training_record(st.session_state.username, module["title"], score, passed, pdf_path, envelope_id)
        st.success(f"✅ Certificate sent for DocuSign! Envelope: {envelope_id}")
    else:
        st.error("❌ Did not pass. Review the policy and retake.")