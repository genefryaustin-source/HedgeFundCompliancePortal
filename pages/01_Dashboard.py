import streamlit as st
import sqlite3
from datetime import datetime

st.title("🛡️ Compliance Dashboard – $1B AUM Hedge Fund RIA")
st.caption("Real-time status based on actual data")

# Direct SQLite connection (works on Streamlit Cloud without secrets)
try:
    conn = sqlite3.connect('data/compliance.db')
    c = conn.cursor()

    # Training completion %
    c.execute("SELECT COUNT(*) FROM training_records WHERE passed = 1")
    completed_training = c.fetchone()[0]
    c.execute("SELECT COUNT(DISTINCT username) FROM training_records")
    total_users = c.fetchone()[0] or 1
    training_pct = round((completed_training / total_users) * 100, 1) if total_users > 0 else 0

    # Attestations %
    c.execute("SELECT COUNT(*) FROM attestations")
    attestations = c.fetchone()[0]
    c.execute("SELECT COUNT(DISTINCT policy_title) FROM attestations")
    total_policies = c.fetchone()[0] or 1
    attestation_pct = round((attestations / total_policies) * 100, 1) if total_policies > 0 else 0

    # Open incidents
    c.execute("SELECT COUNT(*) FROM incidents WHERE status = 'Open'")
    open_incidents = c.fetchone()[0]

    conn.close()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Training Completion", f"{training_pct}%", "No completions yet" if training_pct == 0 else "")
    with col2:
        st.metric("Open Incidents", open_incidents, "All clear" if open_incidents == 0 else "")
    with col3:
        st.metric("Policy Attestations", f"{attestation_pct}%", "No attestations yet" if attestation_pct == 0 else "")
    with col4:
        st.metric("AI Risk Score", "0%", "No tests completed")

    if training_pct == 0 and attestation_pct == 0 and open_incidents == 0:
        st.warning("⚠️ No training completed and no policy attestations signed yet. Please complete the Training modules and attest to policies.")

    st.info("**Next deadline**: Annual Reg S-P WISP Review & Compliance Program Assessment – 45 days")

except Exception as e:
    st.error(f"Database error: {e}")
    st.info("Run `init_db()` from database.py to create tables.")

# Log dashboard view
if 'username' in st.session_state:
    from database import log_audit_trail
    log_audit_trail(st.session_state.username, "Dashboard View", "Viewed main compliance dashboard", "Unknown")