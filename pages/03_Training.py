import streamlit as st
from datetime import datetime
from utils import generate_and_sign_policy
from database import log_training_record

st.title("📚 Training & Certification Center")
st.markdown("**Mandatory Annual Training** – 80% pass required for certificate. All completions are logged and certificates are sent for DocuSign.")

training_modules = {
    "AML_BSA": {
        "title": "AML / BSA 5-Pillar Training",
        "video": "https://www.youtube.com/watch?v=dYwH-ogWyoM",
        "description": "Comprehensive overview of the Bank Secrecy Act and Anti-Money Laundering requirements for investment advisers."
    },
    "RegSP_Cyber": {
        "title": "Reg S-P WISP & Cybersecurity Training",
        "video": "https://www.youtube.com/watch?v=hcLRZL0FfRA",
        "description": "SEC Regulation S-P amendments – incident response, customer notification (30 days), and vendor requirements (72 hours)."
    },
    "AI_Ethics": {
        "title": "AI Ethics & Compliance Training",
        "video": "https://www.youtube.com/watch?v=thEF0ZKr0xw",
        "description": "AI ethics, compliance, and regulatory expectations for investment advisers."
    },
    "Incident_Reporting": {
        "title": "Incident Reporting & Reg S-P Training",
        "video": "https://www.youtube.com/watch?v=Wqp9S24xDRY",
        "description": "Incident response programs under Reg S-P and general compliance incident handling."
    },
    "Phishing_Response": {
        "title": "Phishing Awareness & Response Playbook",
        "video": "https://www.youtube.com/watch?v=L8s65vuF0Go",
        "description": "Practical phishing recognition and response training tailored for financial professionals."
    }
}

selected_module = st.selectbox("Select Module", list(training_modules.keys()))
module = training_modules[selected_module]

st.subheader(module["title"])
st.video(module["video"])

st.markdown("**Description**")
st.write(module["description"])

st.markdown("---")
st.subheader("Knowledge Check – Quiz (80% to pass)")

# ====================== QUIZ QUESTIONS ======================

if selected_module == "AML_BSA":
    questions = [
        {"q": "What are the five pillars of an AML program?", "options": ["Policies, BSA Officer, Training, Testing, CDD", "Risk Assessment, SAR, OFAC, Training, Audit"], "correct": "Policies, BSA Officer, Training, Testing, CDD"},
        {"q": "When must a SAR generally be filed with FinCEN?", "options": ["Within 30 days", "Within 72 hours", "Within 1 year"], "correct": "Within 30 days"},
        {"q": "What is strictly prohibited when a SAR is being considered?", "options": ["Tipping off the subject", "Documenting the investigation", "Escalating to the CCO"], "correct": "Tipping off the subject"},
        {"q": "Which is a common AML red flag in hedge funds?", "options": ["Rapid capital contribution followed by early redemption", "Regular quarterly distributions"], "correct": "Rapid capital contribution followed by early redemption"},
        {"q": "What does EDD stand for?", "options": ["Enhanced Due Diligence", "Early Detection Duty"], "correct": "Enhanced Due Diligence"},
        {"q": "What is the minimum retention period for AML records?", "options": ["5 years", "2 years", "10 years"], "correct": "5 years"},
        {"q": "Who is typically designated as the BSA Officer?", "options": ["Chief Compliance Officer or delegate", "Portfolio Manager"], "correct": "Chief Compliance Officer or delegate"},
        {"q": "What must be done when a PEP is identified?", "options": ["Apply Enhanced Due Diligence", "Accept immediately"], "correct": "Apply Enhanced Due Diligence"},
        {"q": "What is a key purpose of the AML program?", "options": ["Prevent money laundering", "Improve marketing"], "correct": "Prevent money laundering"},
        {"q": "Annual independent testing is required under which pillar?", "options": ["Pillar 4", "Pillar 1"], "correct": "Pillar 4"}
    ]

elif selected_module == "RegSP_Cyber":
    questions = [
        {"q": "Under amended Reg S-P, what is the maximum timeframe for customer notification?", "options": ["30 days", "72 hours", "7 days"], "correct": "30 days"},
        {"q": "Service providers must notify the firm within how many hours?", "options": ["72 hours", "30 days"], "correct": "72 hours"},
        {"q": "What does WISP stand for?", "options": ["Written Information Security Program", "Weekly Incident Security Plan"], "correct": "Written Information Security Program"},
        {"q": "A key 2026 SEC exam focus for cybersecurity is:", "options": ["Incident response and recovery", "Only software cost"], "correct": "Incident response and recovery"},
        {"q": "The WISP must include which types of safeguards?", "options": ["Administrative, technical, and physical", "Only technical"], "correct": "Administrative, technical, and physical"},
        {"q": "Penetration testing should be conducted at least:", "options": ["Annually", "Every 5 years"], "correct": "Annually"},
        {"q": "Who is responsible for overseeing the WISP?", "options": ["Qualified individual (often CCO)", "CEO only"], "correct": "Qualified individual (often CCO)"},
        {"q": "Contracts with service providers must require notification within:", "options": ["72 hours", "30 days"], "correct": "72 hours"},
        {"q": "Recordkeeping for Reg S-P incidents must be retained for:", "options": ["5 years", "1 year"], "correct": "5 years"},
        {"q": "The incident response program must include:", "options": ["Detection, response, and recovery", "Only marketing"], "correct": "Detection, response, and recovery"}
    ]

elif selected_module == "AI_Ethics":
    questions = [
        {"q": "What is 'AI washing'?", "options": ["Overstating AI capabilities", "Using open-source AI"], "correct": "Overstating AI capabilities"},
        {"q": "High-stakes AI decisions require:", "options": ["Human-in-the-loop oversight", "Fully autonomous execution"], "correct": "Human-in-the-loop oversight"},
        {"q": "NIST AI RMF functions include:", "options": ["Govern, Map, Measure, Manage", "Buy, Sell, Hold"], "correct": "Govern, Map, Measure, Manage"},
        {"q": "Material AI use must be disclosed in:", "options": ["Form ADV Part 2A", "Only internal memos"], "correct": "Form ADV Part 2A"},
        {"q": "A major risk with third-party AI tools is:", "options": ["Bias and lack of explainability", "They are always cheaper"], "correct": "Bias and lack of explainability"},
        {"q": "Fully autonomous AI trading without oversight is:", "options": ["Prohibited", "Encouraged"], "correct": "Prohibited"},
        {"q": "If an AI model shows bias or drift, you should:", "options": ["Document, test, and remediate", "Ignore if performance is good"], "correct": "Document, test, and remediate"},
        {"q": "AI-generated marketing content must be:", "options": ["Substantiated and CCO-reviewed", "Published immediately"], "correct": "Substantiated and CCO-reviewed"},
        {"q": "A key SEC 2026 focus on AI is:", "options": ["Supervision and accurate representations", "Only cost of tools"], "correct": "Supervision and accurate representations"},
        {"q": "When using AI for compliance tasks, what is required?", "options": ["Human oversight", "Complete reliance on AI"], "correct": "Human oversight"}
    ]

elif selected_module == "Incident_Reporting":
    questions = [
        {"q": "Under Reg S-P, customer notification timeframe for qualifying incidents is:", "options": ["30 days", "72 hours"], "correct": "30 days"},
        {"q": "Service providers must notify the firm within:", "options": ["72 hours", "30 days"], "correct": "72 hours"},
        {"q": "High-severity incidents must be reported internally within:", "options": ["1 hour", "24 hours"], "correct": "1 hour"},
        {"q": "The phase that involves isolating affected systems is:", "options": ["Containment", "Eradication"], "correct": "Containment"},
        {"q": "What is prohibited when considering a SAR?", "options": ["Tipping off the subject", "Documenting"], "correct": "Tipping off the subject"},
        {"q": "AI incidents with material impact must be reported within:", "options": ["1 business day", "30 days"], "correct": "1 business day"},
        {"q": "How often should the Incident Response Plan be tested?", "options": ["Annually", "Only after incident"], "correct": "Annually"},
        {"q": "Incident records must be retained for:", "options": ["5 years", "1 year"], "correct": "5 years"},
        {"q": "The WISP must include an incident response program to:", "options": ["Detect, respond, recover", "Only market products"], "correct": "Detect, respond, recover"},
        {"q": "Who is typically the Incident Response Officer?", "options": ["Chief Compliance Officer", "Portfolio Manager"], "correct": "Chief Compliance Officer"}
    ]

elif selected_module == "Phishing_Response":
    questions = [
        {"q": "First action on receiving a suspicious email?", "options": ["Forward as attachment and do not click", "Reply to verify"], "correct": "Forward as attachment and do not click"},
        {"q": "Common phishing indicator?", "options": ["Urgent language and unexpected attachments", "Standard company logo"], "correct": "Urgent language and unexpected attachments"},
        {"q": "If you clicked a suspicious link, what should you do?", "options": ["Report and disconnect device", "Continue working"], "correct": "Report and disconnect device"},
        {"q": "Phishing-related Reg S-P incident may require notification within:", "options": ["30 days", "72 hours"], "correct": "30 days"},
        {"q": "What to do with evidence from phishing email?", "options": ["Preserve and capture headers", "Delete immediately"], "correct": "Preserve and capture headers"},
        {"q": "AI-enhanced phishing may include:", "options": ["Deepfake voice/video calls", "Perfect grammar only"], "correct": "Deepfake voice/video calls"},
        {"q": "High-severity phishing must be reported internally within:", "options": ["1 hour", "24 hours"], "correct": "1 hour"},
        {"q": "After phishing incident, critical step is:", "options": ["Assess if customer data was accessed", "Ignore if no money lost"], "correct": "Assess if customer data was accessed"},
        {"q": "Best way to report suspected phishing?", "options": ["Forward as attachment", "Reply to sender"], "correct": "Forward as attachment"},
        {"q": "Phishing is a common entry point for:", "options": ["Ransomware and BEC", "Routine updates"], "correct": "Ransomware and BEC"}
    ]

# ====================== QUIZ LOGIC ======================
score = 0
for i, q in enumerate(questions):
    ans = st.radio(q["q"], q["options"], key=f"{selected_module}_q{i}")
    if ans == q["correct"]:
        score += 1

if st.button("Submit Quiz & Generate Certificate"):
    passed = score >= 8  # 80% pass rate
    if passed:
        cert_title = f"{module['title']}_Certificate"
        content = f"""
Training Certificate
Employee: {st.session_state.get('name', 'User')}
Module: {module['title']}
Score: {score}/10
Date: {datetime.now().strftime('%Y-%m-%d')}
        """
        drive_id, envelope_id, pdf_path = generate_and_sign_policy(
            cert_title, content, st.session_state.username, st.session_state.email, st.secrets["GOOGLE_DRIVE_FOLDER_ID"]
        )
        log_training_record(st.session_state.username, module["title"], score, passed, pdf_path, envelope_id)
        st.success(f"✅ Passed! Certificate generated and sent for DocuSign. Envelope: {envelope_id}")
        st.balloons()
    else:
        st.error(f"❌ Score: {score}/10 – Did not pass. Please review the video and retake.")

st.sidebar.info("All training completions are logged with full audit trail.")