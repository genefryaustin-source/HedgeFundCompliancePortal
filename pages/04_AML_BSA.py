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
    # Keep your existing risk assessment code

with tab2:
    st.subheader("Enhanced Due Diligence (EDD) Procedures")
    st.markdown("**Pillar 2 & 5** – Applied when risk is elevated.")

    st.write("### Expanded EDD Triggers (Hedge Fund Specific)")
    edd_triggers = [
        "Investor or beneficial owner is a Politically Exposed Person (PEP) or close associate",
        "Investor resides in or funds originate from a high-risk jurisdiction (FATF grey/black list, OFAC-sanctioned countries)",
        "Investment amount exceeds $5 million or represents more than 10% of the fund’s AUM",
        "Complex corporate, trust, or offshore structure with layered entities or unidentified beneficial owners",
        "Unusual transaction patterns: rapid capital contributions followed by early redemption requests",
        "Investor requests preferential treatment (side letters for liquidity, fees, or reporting)",
        "Negative adverse media hits or regulatory sanctions history",
        "Source of funds/wealth is unclear, undocumented, or inconsistent with known profile",
        "Investor shows reluctance to provide complete beneficial ownership information",
        "Multiple related entities or family members investing with coordinated patterns",
        "Investor uses third-party intermediaries or nominees without clear justification"
    ]
    for trigger in edd_triggers:
        st.checkbox(trigger)

    st.write("### Required EDD Procedures")
    edd_steps = [
        "In-depth Source of Wealth verification (bank statements, tax returns, audited financials, third-party reports)",
        "Full Beneficial Ownership mapping (corporate registry searches, ownership charts, interviews)",
        "Enhanced adverse media and sanctions screening (World-Check, LexisNexis, or equivalent)",
        "Senior management approval (BSA Officer + CEO) via DocuSign before accepting subscription",
        "Enhanced ongoing monitoring (monthly transaction reviews + automated alerts)",
        "Video calls or site visits with investor representatives for high-risk cases",
        "All documentation retained for minimum 5 years in secure Google Drive folder"
    ]
    for step in edd_steps:
        st.checkbox(step, value=True)

    investor_name = st.text_input("Investor Name for EDD Record")
    if st.button("Complete EDD & Sign Documentation"):
        st.success(f"EDD procedures completed and signed for **{investor_name}**.")
        log_audit_trail(st.session_state.username, "EDD Completed", f"Investor: {investor_name}", "Unknown")
        log_attestation(st.session_state.username, f"EDD - {investor_name}")

with tab3:
    st.subheader("Pillar 3 – Ongoing Training")
    st.info("Complete the **AML/BSA 5-Pillar Training** in the Training Center.")
    st.page_link("pages/03_Training.py", label="Go to Training Center →", icon="📚")

with tab4:
    st.subheader("Pillar 4 – Independent Testing & Audit")
    # Keep your existing testing section

with tab5:
    st.subheader("Pillar 5 – CIP / KYC / CDD / SAR / Transaction Monitoring")

    subtab1, subtab2, subtab3, subtab4 = st.tabs(["CIP / KYC", "CDD Form", "SAR Filing", "Transaction Monitoring"])

    with subtab1:
        # Keep your existing CIP / KYC section

    with subtab2:
        # Keep your existing CDD form

    with subtab3:
        # Keep your existing SAR section with examples

    with subtab4:
        st.subheader("Transaction Monitoring Rules")
        st.markdown("**Ongoing Monitoring** – Pillar 5 requirement to detect suspicious activity throughout the relationship.")

        st.write("### Key Transaction Monitoring Rules")
        monitoring_rules = [
            "Monitor all capital contributions, redemptions, and wire transfers for unusual patterns",
            "Flag rapid inflows followed by early redemption requests without market justification",
            "Alert on wires to/from high-risk jurisdictions or accounts not previously disclosed",
            "Review changes in wire instructions or beneficiary details",
            "Flag investments significantly larger than the investor’s known net worth or source of funds",
            "Monitor for structuring (multiple transfers just below reporting thresholds)",
            "Review frequency and size of distributions relative to fund strategy",
            "Flag any transaction inconsistent with the investor’s stated investment objective",
            "Automated alerts for PEP-related accounts or sanctioned country exposure"
        ]
        for rule in monitoring_rules:
            st.checkbox(rule)

        st.write("**Escalation Thresholds**")
        st.write("- Any transaction ≥ $1 million from high-risk jurisdiction → Automatic EDD review")
        st.write("- Multiple redemptions within 90 days of subscription → SAR consideration")
        st.write("- Change in wire instructions without explanation → Immediate investigation")

        if st.button("Sign Transaction Monitoring Policy Acknowledgment"):
            st.success("Transaction Monitoring Rules acknowledged and signed.")
            log_audit_trail(st.session_state.username, "Transaction Monitoring Acknowledged", "Signed policy", "Unknown")
            log_attestation(st.session_state.username, "Transaction Monitoring Rules")

st.sidebar.info("BSA Officer: Chief Compliance Officer\nAll EDD, SAR, and monitoring actions are fully logged.")