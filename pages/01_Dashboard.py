import streamlit as st
from database import log_audit_trail

st.title("🛡️ Compliance Dashboard – $1B AUM Hedge Fund RIA")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Training Completion", "98%", "↑ 2%")
with col2:
    st.metric("Open Incidents", "0", "↓ 1")
with col3:
    st.metric("Policy Attestations", "100%")
with col4:
    st.metric("AI Risk Score", "94%")

st.success("✅ Overall Compliance Posture: Strong")
st.info("Next deadline: Annual Reg S-P WISP Review & Compliance Program Assessment – 45 days")

# Log visit
if 'username' in st.session_state:
    log_audit_trail(st.session_state.username, "Dashboard View", "Viewed compliance dashboard", "Unknown")