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

    st.markdown("### Risk Scoring Methodology")
    st.write("""
    **Inherent Risk** = Average of Investor Risk + Product Risk + Geographic Risk (1–10 scale)  
    **Control Effectiveness** = Strength of CIP, CDD, screening, monitoring, and training (1–10 scale)  
    **Residual Risk** = Inherent Risk – (Control Effectiveness / 2)
    """)

    col1, col2 = st.columns(2)
    with col1:
        investor_risk = st.slider("Investor Base Risk", 1, 10, 5)
        product_risk = st.slider("Product / Strategy Risk", 1, 10, 6)
        geo_risk = st.slider("Geographic / Sanctions Risk", 1, 10, 3)
    
    with col2:
        control_strength = st.slider("Control Effectiveness", 1, 10, 7)

    inherent_risk = round((investor_risk + product_risk + geo_risk) / 3, 1)
    residual_risk = round(inherent_risk - (control_strength / 2), 1)

    risk_color = "🔴 High" if residual_risk >= 8 else "🟠 Medium" if residual_risk >= 5 else "🟢 Low"
    st.metric("Residual Risk Score", f"{residual_risk} {risk_color}")

    if st.button("Save & Sign Annual Risk Assessment"):
        st.success("Risk Assessment signed and saved.")
        log_audit_trail(st.session_state.username, "AML Risk Assessment", f"Residual Risk: {residual_risk}", "Unknown")

with tab2:
    st.subheader("Enhanced Due Diligence (EDD) Procedures")
    st.markdown("**Expanded EDD Triggers**")
    edd_triggers = [
        "Investor or beneficial owner is a PEP or close associate",
        "Investor resides in or funds originate from high-risk jurisdiction",
        "Investment > $5M or >10% of fund AUM",
        "Complex corporate/trust structure with unidentified beneficial owners",
        "Unusual transaction patterns (rapid inflows + early redemptions)",
        "Requests for preferential treatment via side letters",
        "Negative adverse media or sanctions hits",
        "Source of funds/wealth unclear or inconsistent with profile"
    ]
    for trigger in edd_triggers:
        st.checkbox(trigger)

    st.markdown("**Required EDD Procedures**")
    edd_steps = [
        "In-depth Source of Wealth verification",
        "Full Beneficial Ownership mapping",
        "Enhanced adverse media & sanctions screening",
        "Senior management approval via DocuSign",
        "Enhanced ongoing monitoring (monthly reviews)",
        "All documentation retained for 5 years"
    ]
    for step in edd_steps:
        st.checkbox(step, value=True)

with tab3:
    st.subheader("Pillar 3 – Ongoing Training")
    st.info("Go to Training Center to complete AML/BSA modules.")
    st.page_link("pages/03_Training.py", label="Go to Training Center →", icon="📚")

with tab4:
    st.subheader("Pillar 4 – Independent Testing & Audit")
    st.write("Annual independent test of all 5 pillars required.")

with tab5:
    st.subheader("Pillar 5 – CIP / KYC / CDD / SAR / Monitoring")
    st.info("CIP, KYC, CDD, SAR filing, and transaction monitoring tools are available here.")

st.sidebar.info("BSA Officer: Chief Compliance Officer")