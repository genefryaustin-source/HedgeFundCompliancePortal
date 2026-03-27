import streamlit as st
from datetime import datetime
from database import log_audit_trail, log_attestation

st.title("AML / BSA 5-Pillar Program")
st.caption("$1B AUM Hedge Fund RIA – FinCEN IA Rule Ready (Effective Jan 1, 2028)")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Risk Assessment",
    "2. Enhanced Due Diligence (EDD)",
    "3. Training",
    "4. Independent Testing",
    "5. CIP / KYC / CDD / SAR / Monitoring"
])

with tab1:
    st.subheader("Annual AML Risk Assessment")
    st.markdown("**Pillar 1** – Risk-Based Approach")
    # Your existing risk assessment code can go here

with tab2:
    st.subheader("Enhanced Due Diligence (EDD) Procedures")
    st.markdown("**Pillar 2 & 5** – Applied when risk is elevated.")
    # Your existing EDD section can go here

with tab3:
    st.subheader("Pillar 3 – Ongoing Training")
    st.info("Complete the AML/BSA 5-Pillar Training in the Training Center.")
    st.page_link("pages/03_Training.py", label="Go to Training Center →", icon="📚")

with tab4:
    st.subheader("Pillar 4 – Independent Testing & Audit")
    st.write("Annual independent test of all 5 pillars required.")

with tab5:
    st.subheader("Pillar 5 – CIP, KYC, CDD, SAR Filing & Transaction Monitoring")
    st.markdown("Tools for onboarding, due diligence, suspicious activity reporting, and ongoing monitoring.")

    sub1, sub2, sub3, sub4 = st.tabs(["CIP & KYC", "CDD Form", "SAR Filing", "Transaction Monitoring"])

    with sub1:
        st.subheader("CIP (Customer Identification Program) & KYC Onboarding")
        st.markdown("""
        **Required CIP Elements** (FinCEN IA Rule):
        - Full legal name
        - Date of birth (individuals) or formation (entities)
        - Residential or principal business address
        - Identification number (SSN, EIN, passport, etc.)
        """)

        st.write("**Verification Methods**")
        cip_methods = [
            "Government-issued photo ID (passport, driver’s license, national ID)",
            "Address verification (utility bill, bank statement, lease – within 3 months)",
            "Tax ID validation (SSN/EIN or foreign equivalent)",
            "Video call verification for high-risk or non-face-to-face investors",
            "Third-party identity verification service",
            "Corporate documents for entities (Certificate of Incorporation, ownership chart)"
        ]
        for method in cip_methods:
            st.checkbox(method)

        with st.form("cip_form"):
            name = st.text_input("Investor / Entity Name")
            id_type = st.selectbox("ID Type", ["Passport", "Driver’s License", "National ID", "Other"])
            id_number = st.text_input("ID Number")
            address = st.text_area("Verified Address")
            tin = st.text_input("Tax ID Number")
            if st.form_submit_button("Complete CIP/KYC & Sign"):
                st.success(f"CIP/KYC completed for **{name}**.")
                log_audit_trail(st.session_state.username, "CIP/KYC Completed", f"Investor: {name}", "Unknown")
                log_attestation(st.session_state.username, f"CIP/KYC - {name}")

    with sub2:
        st.subheader("Customer Due Diligence (CDD) Form")
        with st.form("cdd_form"):
            investor = st.text_input("Investor Name")
            amount = st.number_input("Investment Amount ($)", min_value=0.0)
            source = st.selectbox("Source of Funds", ["Employment", "Investment Returns", "Inheritance", "Business Revenue", "Other"])
            owners = st.text_area("Beneficial Owners (% ownership)")
            if st.form_submit_button("Submit CDD & Sign"):
                st.success(f"CDD submitted for **{investor}**.")
                log_audit_trail(st.session_state.username, "CDD Submitted", f"Investor: {investor}", "Unknown")

    with sub3:
        st.subheader("SAR Filing Procedures")
        st.markdown("**Timeline**: Escalate within 24 hours → File with FinCEN within 30 days.")
        st.warning("**No tipping-off**: Never inform the subject of a SAR.")

        with st.form("sar_form"):
            suspect = st.text_input("Suspect Name / Entity")
            desc = st.text_area("Description of Suspicious Activity")
            reason = st.selectbox("Reason", ["Structuring", "Unusual wires", "Inconsistent strategy", "PEP involvement", "High-risk jurisdiction"])
            if st.form_submit_button("Log & Escalate SAR"):
                st.success(f"SAR logged for **{suspect}**.")
                log_audit_trail(st.session_state.username, "SAR Filed", f"Suspect: {suspect}", "Unknown")

    with sub4:
        st.subheader("Transaction Monitoring Rules")
        st.write("Ongoing monitoring to detect suspicious patterns.")

        rules = [
            "Monitor capital calls, redemptions, and wires for unusual patterns",
            "Flag rapid inflows followed by quick redemptions",
            "Alert on wires to high-risk jurisdictions",
            "Review sudden changes in wire instructions",
            "Flag investments disproportionate to known net worth",
            "Detect structuring attempts",
            "Monitor frequency of distributions vs. fund strategy"
        ]
        for rule in rules:
            st.checkbox(rule)

        if st.button("Acknowledge Transaction Monitoring Rules"):
            st.success("Monitoring rules acknowledged.")
            log_audit_trail(st.session_state.username, "Transaction Monitoring Acknowledged", "Signed policy", "Unknown")

st.sidebar.info("BSA Officer: Chief Compliance Officer\nAll actions logged with full audit trail.")