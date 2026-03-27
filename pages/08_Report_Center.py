import streamlit as st
import pandas as pd
from database import log_audit_trail

st.title("📊 Report Center")

report_type = st.selectbox("Select Report", [
    "Annual Compliance Review (206(4)-7 + Reg S-P WISP)",
    "Training Records",
    "Incident Log",
    "AI Risk Testing Summary",
    "Full Audit Trail"
])

if st.button("Generate Report"):
    # Example export
    df = pd.DataFrame({"Report": [report_type], "Generated": [datetime.now()]})
    csv = df.to_csv(index=False).encode()
    st.download_button("Download CSV", csv, "compliance_report.csv")
    log_audit_trail(st.session_state.username, "Report Generated", report_type, "Unknown")