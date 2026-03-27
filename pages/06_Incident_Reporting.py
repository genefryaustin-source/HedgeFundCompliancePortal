import streamlit as st
from database import log_incident
from utils import generate_and_sign_policy

st.title("🚨 Incident Reporting")

incident_type = st.selectbox("Category", ["Phishing", "Reg S-P Breach", "AI Incident", "AML SAR", "Other"])
severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
description = st.text_area("Description")

if st.button("Submit Incident"):
    drive_id, envelope_id, _ = generate_and_sign_policy("Incident_Report", description, st.session_state.username, st.session_state.email, st.secrets["GOOGLE_DRIVE_FOLDER_ID"])
    log_incident(st.session_state.username, incident_type, severity, description, drive_id, envelope_id)
    st.success(f"Incident logged and sent for CCO review. Envelope: {envelope_id}")