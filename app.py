# app.py
import streamlit as st
import streamlit_authenticator as stauth

credentials = {
    'usernames': {
        'cco': {
            'name': 'Chief Compliance Officer',
            'password': 'compliance2026',
        },
        'employee': {
            'name': 'Employee',
            'password': 'compliance2026',
        }
    }
}

authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name='compliance_cookie',
    cookie_key='change_this_to_a_long_random_string_2026',
    cookie_expiry_days=30,
    auto_hash=True
)

authenticator.login(location='main')

name                  = st.session_state.get('name')
authentication_status = st.session_state.get('authentication_status')
username              = st.session_state.get('username')

if authentication_status:
    st.success(f"✅ Logged in as {name}")
    authenticator.logout("Logout", location="sidebar")
elif authentication_status is False:
    st.error("❌ Wrong username or password")
else:
    st.info("Please login")