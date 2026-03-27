import streamlit as st
st.title("🛡️ Phishing Response Playbook")
try:
    with open("policies/phishing_response_playbook.md", "r", encoding="utf-8") as f:
        st.markdown(f.read())
except FileNotFoundError:
    st.error("Playbook file not found. Please add it to policies/")