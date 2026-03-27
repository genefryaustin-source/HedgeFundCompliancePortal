def check_access(required_role):
    user_role = st.session_state.get("role", "Employee")
    if required_role == "CCO" and user_role != "CCO":
        st.error("🔒 CCO/Admin access only.")
        st.stop()
    elif required_role == "Analyst" and user_role not in ["CCO", "Analyst"]:
        st.error("🔒 Analyst or higher access only.")
        st.stop()
    # Employee can always read/attest/train/report incidents