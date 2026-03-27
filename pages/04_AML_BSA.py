import streamlit as st
from datetime import datetime
from database import log_audit_trail, log_attestation

st.title("AML / BSA 5-Pillar Program + CFIUS & Export Controls")
st.caption("$1B AUM Hedge Fund RIA – FinCEN IA Rule + National Security Requirements")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1. Risk Assessment",
    "2. Enhanced Due Diligence (EDD)",
    "3. Training",
    "4. Independent Testing",
    "5. CIP / KYC / CDD / SAR / Monitoring",
    "6. CFIUS & Export Controls"
])

with tab1:
    st.subheader("Annual AML Risk Assessment")
    st.markdown("**Pillar 1** – Risk-Based Approach")
    st.info("Use the interactive sliders below to calculate residual risk.")

    col1, col2 = st.columns(2)
    with col1:
        investor_risk = st.slider("Investor Base Risk", 1, 10, 5)
        product_risk = st.slider("Product / Strategy Risk", 1, 10, 6)
        geo_risk = st.slider("Geographic / Sanctions Risk", 1, 10, 4)
    with col2:
        control_strength = st.slider("Control Effectiveness", 1, 10, 7)

    inherent = round((investor_risk + product_risk + geo_risk) / 3, 1)
    residual = round(inherent - (control_strength / 2), 1)
    risk_level = "🔴 HIGH" if residual >= 8 else "🟠 MEDIUM" if residual >= 5 else "🟢 LOW"

    st.metric("Residual Risk Score", f"{residual} {risk_level}")

    if st.button("Save & Sign Risk Assessment"):
        st.success("Risk Assessment signed and saved.")
        log_audit_trail(st.session_state.username, "AML Risk Assessment", f"Residual: {residual}", "Unknown")

with tab2:
    st.subheader("Enhanced Due Diligence (EDD) Procedures")
    st.markdown("**Pillar 2 & 5** – Applied when risk is elevated.")

    st.write("**EDD Triggers**")
    for item in [
        "PEP or close associate", "High-risk jurisdiction", "Investment > $5M or >10% AUM",
        "Complex ownership structure", "Unusual transaction patterns", "Side letter requests",
        "Adverse media hits", "Unclear source of wealth"
    ]:
        st.checkbox(item)

    st.write("**Required EDD Procedures**")
    for item in [
        "In-depth Source of Wealth verification",
        "Full Beneficial Ownership mapping",
        "Enhanced sanctions & media screening",
        "Senior management approval via DocuSign",
        "Enhanced ongoing monitoring",
        "All records retained 5 years"
    ]:
        st.checkbox(item, value=True)

with tab3:
    st.subheader("Pillar 3 – Ongoing Training")
    st.info("Complete the AML/BSA 5-Pillar Training in the Training Center.")
    st.page_link("pages/03_Training.py", label="Go to Training Center →", icon="📚")

with tab4:
    st.subheader("Pillar 4 – Independent Testing & Audit")
    st.write("Annual independent test of all 5 pillars required.")

with tab5:
    st.subheader("Pillar 5 – CIP / KYC / CDD / SAR / Monitoring")
    st.info("CIP, KYC, CDD, SAR filing, and transaction monitoring tools are available here.")

    sub1, sub2, sub3, sub4 = st.tabs(["CIP & KYC", "CDD Form", "SAR Filing", "Transaction Monitoring"])

    with sub1:
        st.subheader("CIP & KYC Onboarding")
        st.write("**CIP Requirements**: Name, DOB/formation date, address, TIN, photo ID verification.")
        with st.form("cip_form"):
            name = st.text_input("Investor Name")
            if st.form_submit_button("Complete CIP/KYC & Sign"):
                st.success(f"CIP/KYC completed for {name}.")
                log_audit_trail(st.session_state.username, "CIP/KYC Completed", f"Investor: {name}", "Unknown")

    with sub2:
        st.subheader("Customer Due Diligence (CDD)")
        with st.form("cdd_form"):
            investor = st.text_input("Investor Name")
            amount = st.number_input("Investment Amount ($)", min_value=0)
            if st.form_submit_button("Submit CDD & Sign"):
                st.success(f"CDD submitted for {investor}.")
                log_audit_trail(st.session_state.username, "CDD Submitted", f"Investor: {investor}", "Unknown")

    with sub3:
        st.subheader("SAR Filing")
        st.write("Escalate within 24h → File with FinCEN within 30 days.")
        with st.form("sar_form"):
            suspect = st.text_input("Suspect Name")
            desc = st.text_area("Suspicious Activity")
            if st.form_submit_button("Log SAR"):
                st.success(f"SAR logged for {suspect}.")
                log_audit_trail(st.session_state.username, "SAR Filed", f"Suspect: {suspect}", "Unknown")

    with sub4:
        st.subheader("Transaction Monitoring Rules")
        rules = [
            "Monitor wires to high-risk jurisdictions",
            "Flag rapid inflow + quick redemption",
            "Review changes in wire instructions",
            "Detect structuring attempts"
        ]
        for rule in rules:
            st.checkbox(rule)

with tab6:
    st.subheader("CFIUS & Export Controls")
    st.write("**CFIUS Critical Technologies Examples**")
    for item in [
        "Artificial Intelligence & Machine Learning",
        "Semiconductors & Manufacturing Equipment",
        "Quantum Computing",
        "Biotechnology",
        "Advanced Robotics",
        "Aerospace & Defense Technologies"
    ]:
        st.checkbox(item)

    st.write("**Export Controls Compliance**")
    for item in [
        "Screen for ITAR-controlled items",
        "Screen for EAR dual-use technology",
        "Obtain licenses when required",
        "Include export clauses in agreements"
    ]:
        st.checkbox(item, value=True)

st.sidebar.info("BSA Officer: Chief Compliance Officer")