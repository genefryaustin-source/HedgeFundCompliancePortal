import streamlit as st
from datetime import datetime
from utils import generate_and_sign_policy
from database import log_training_record

st.title("📚 Training & Certification Center")
st.markdown("**Mandatory Annual Training** – 80% pass required for certificate.")

training_modules = {
    "AML_BSA": {
        "title": "AML / BSA 5-Pillar Training",
        "video": "https://www.youtube.com/watch?v=dYwH-ogWyoM",
        "description": "Comprehensive overview of the Bank Secrecy Act and Anti-Money Laundering requirements for investment advisers.",
        "objectives": "Understand the 5 pillars, SAR filing, red flags, and FinCEN IA Rule obligations."
    },
    "RegSP_Cyber": {
        "title": "Reg S-P WISP & Cybersecurity Training",
        "video": "https://www.youtube.com/watch?v=hcLRZL0FfRA",
        "description": "SEC Regulation S-P amendments – incident response, customer notification (30 days), and vendor requirements (72 hours).",
        "objectives": "Learn WISP requirements, incident response programs, and 2026 SEC cybersecurity priorities."
    },
    "AI_Ethics": {
        "title": "AI Ethics & Compliance Training",
        "video": "https://www.youtube.com/watch?v=thEF0ZKr0xw",
        "description": "AI ethics, compliance, and regulatory expectations for investment advisers.",
        "objectives": "Cover bias, explainability, human oversight, AI washing prohibition, and SEC 2026 priorities."
    },
    "Incident_Reporting": {
        "title": "Incident Reporting & Reg S-P Training",
        "video": "https://www.youtube.com/watch?v=Wqp9S24xDRY",
        "description": "Incident response programs under Reg S-P and general compliance incident handling.",
        "objectives": "Learn detection, containment, notification timelines, and post-incident review."
    },
    "Phishing_Response": {
        "title": "Phishing Awareness & Response Playbook",
        "video": "https://www.youtube.com/watch?v=L8s65vuF0Go",
        "description": "Practical phishing recognition and response training tailored for financial professionals.",
        "objectives": "Identify phishing indicators, immediate response steps, and Reg S-P reporting requirements."
    }
}

selected_module = st.selectbox("Select Module", list(training_modules.keys()))
module = training_modules[selected_module]

st.subheader(module["title"])
st.video(module["video"])   # Embedded video player

st.markdown("**Description**")
st.write(module["description"])

st.markdown("**Learning Objectives**")
st.write(module["objectives"])

st.markdown("---")
st.subheader("Knowledge Check – Quiz")

# Example quiz (customize per module as needed)
questions = [
    {"q": "What is the customer notification timeline under Reg S-P for a qualifying incident?", "options": ["30 days", "72 hours", "7 days"], "correct": "30 days"},
    {"q": "What is strictly prohibited when considering a SAR filing?", "options": ["Tipping off the subject", "Documenting the investigation", "Escalating to CCO"], "correct": "Tipping off the subject"},
    # Add more realistic questions for each module
]

score = 0
for i, q in enumerate(questions):
    ans = st.radio(q["q"], q["options"], key=f"q_{selected_module}_{i}")
    if ans == q["correct"]:
        score += 1

if st.button("Submit Quiz & Generate Certificate"):
    passed = score >= 8  # 80% pass (adjust as needed)
    if passed:
        cert_title = f"{module['title']}_Certificate"
        content = f"Employee: {st.session_state.get('name', 'User')}\nModule: {module['title']}\nScore: {score}/10\nDate: {datetime.now().strftime('%Y-%m-%d')}"
        drive_id, envelope_id, pdf_path = generate_and_sign_policy(
            cert_title, content, st.session_state.username, st.session_state.email, st.secrets["GOOGLE_DRIVE_FOLDER_ID"]
        )
        log_training_record(st.session_state.username, module["title"], score, passed, pdf_path, envelope_id)
        st.success(f"✅ Passed! Certificate generated and sent for DocuSign. Envelope: {envelope_id}")
        st.balloons()
    else:
        st.error("❌ Did not pass. Please review the video and policy, then retake the quiz.")

st.sidebar.info("All training completions are logged and certificates are stored in Google Drive with DocuSign.")