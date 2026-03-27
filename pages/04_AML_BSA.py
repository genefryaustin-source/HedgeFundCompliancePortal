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
    # (Your existing risk assessment code can stay here)

with tab2:
    st.subheader("Enhanced Due Diligence (EDD) Procedures")
    st.markdown("**Pillar 2 & 5** – Applied when risk is elevated.")

    st.write("### EDD Triggers (Hedge Fund Specific)")
    triggers = [
        "Investor or any beneficial owner is a Politically Exposed Person (PEP) or close associate",
        "Investor or funds originate from a high-risk or FATF grey/black-listed jurisdiction",
        "Investment amount exceeds $5 million or represents >10% of the fund’s AUM",
        "Complex or layered corporate/trust/offshore structure with unidentified beneficial owners",
        "Unusual transaction patterns (e.g., large capital contribution followed by rapid redemption requests)",
        "Investor requests preferential treatment via side letters (liquidity, fees, reporting, etc.)",
        "Negative adverse media hits, regulatory actions, or sanctions history",
        "Source of funds or wealth is unclear, undocumented, or inconsistent with known profile",
        "Investor shows reluctance to provide complete beneficial ownership information",
        "Multiple related entities or family members investing with similar or coordinated patterns",
        "Use of third-party intermediaries or nominees without clear economic justification"
    ]
    for trigger in triggers:
        st.checkbox(trigger)

    st.write("### Required EDD Procedures")
    edd_procedures = [
        "In-depth Source of Wealth (SoW) and Source of Funds (SoF) verification using bank statements, tax returns, audited financial statements, and third-party wealth reports",
        "Full Beneficial Ownership identification and verification (≥25% owners) including corporate registry searches and ownership charts",
        "Enhanced adverse media screening and sanctions checks using World-Check, LexisNexis, or equivalent databases",
        "Senior management approval (BSA Officer + CEO or designee) via DocuSign before accepting the subscription",
        "Enhanced ongoing transaction monitoring with monthly reviews and automated alerts for red flags",
        "Video calls, virtual meetings, or in-person site visits with investor representatives when appropriate",
        "Detailed documentation of all EDD steps, findings, and approval decisions retained for a minimum of 5 years in secure Google Drive",
        "Periodic re-screening of high-risk investors (at least annually or upon trigger events)"
    ]
    for procedure in edd_procedures:
        st.checkbox(procedure, value=True)

    st.write("### EDD Documentation & Sign-off")
    investor_name = st.text_input("Investor Name for EDD Record", placeholder="e.g., ABC Capital Partners LP")
    notes = st.text_area("Additional EDD Notes / Findings / Mitigation Steps", height=100)

    if st.button("Complete EDD Procedures & Sign"):
        if investor_name:
            content = f"EDD Procedures Completed\nInvestor: {investor_name}\nDate: {datetime.now().strftime('%Y-%m-%d')}\nNotes: {notes}"
            st.success(f"✅ Enhanced Due Diligence completed and signed for **{investor_name}**.")
            log_audit_trail(st.session_state.username, "EDD Completed", f"Investor: {investor_name}", "Unknown")
            log_attestation(st.session_state.username, f"EDD - {investor_name}")
        else:
            st.warning("Please enter the investor name.")

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
    # (You can keep or expand your existing Pillar 5 content here)

st.sidebar.info("BSA Officer: Chief Compliance Officer\nAll EDD actions are logged with full audit trail.")