import streamlit as st
from datetime import datetime
from database import log_audit_trail, log_attestation

st.title("AML / BSA 5-Pillar Program + CFIUS & FCPA Compliance")
st.caption("$1B AUM Hedge Fund RIA – FinCEN IA Rule + National Security & Anti-Corruption Requirements")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1. Risk Assessment",
    "2. Enhanced Due Diligence (EDD)",
    "3. Training",
    "4. Independent Testing",
    "5. CIP / KYC / CDD / SAR / Monitoring",
    "6. CFIUS & FCPA Compliance"
])

with tab1:
    st.subheader("Annual AML Risk Assessment")
    # (Your existing risk assessment code remains here)

with tab2:
    st.subheader("Enhanced Due Diligence (EDD) Procedures")
    # (Your existing EDD section remains here)

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

with tab6:
    st.subheader("CFIUS & FCPA Compliance")
    st.markdown("**National Security & Anti-Corruption Requirements** – Critical for hedge funds with foreign investors or international activities.")

    st.write("### CFIUS (Committee on Foreign Investment in the United States)")
    st.write("CFIUS reviews transactions that could result in foreign control or influence over U.S. businesses involving critical technology, infrastructure, or sensitive data.")

    # CFIUS Triggers and Procedures (kept from previous)
    st.write("**Key CFIUS Triggers**")
    cfius_triggers = [
        "Foreign investor acquiring control or significant influence",
        "Investment in critical technology (AI, semiconductors, biotech)",
        "Investment in critical infrastructure",
        "Access to sensitive personal data of U.S. citizens",
        "Foreign government-linked investors"
    ]
    for trigger in cfius_triggers:
        st.checkbox(trigger)

    st.write("**Required CFIUS Procedures**")
    cfius_procedures = [
        "Pre-investment CFIUS risk assessment for foreign investors",
        "Determine mandatory declaration or voluntary notice filing",
        "Engage specialized CFIUS counsel",
        "Ongoing monitoring of foreign ownership and influence"
    ]
    for procedure in cfius_procedures:
        st.checkbox(procedure, value=True)

    # === NEW: Expanded CFIUS Mitigation Agreements ===
    st.write("### CFIUS Mitigation Agreements")
    st.markdown("""
    When CFIUS identifies national security concerns, it may require **mitigation agreements** before approving the transaction. 
    These are legally binding agreements between the parties and CFIUS.
    """)

    mitigation_steps = [
        "Establish a U.S.-based security committee with independent directors",
        "Appoint a CFIUS-approved security officer with veto rights over certain decisions",
        "Implement strict information security protocols and data segregation",
        "Limit foreign investor access to critical technology or sensitive data",
        "Require CFIUS approval for any change in ownership or key personnel",
        "Undergo regular third-party audits and compliance reporting",
        "Maintain detailed records of all mitigation measures for CFIUS review",
        "Include termination rights or divestiture requirements if compliance fails"
    ]
    for step in mitigation_steps:
        st.checkbox(step, value=True)

    st.info("**Hedge Fund Note**: Mitigation agreements often require governance changes (e.g., board observer rights limitations) and can be costly to implement and monitor.")

    # === NEW: Full FCPA Compliance Procedures ===
    st.subheader("FCPA (Foreign Corrupt Practices Act) Compliance Procedures")
    st.markdown("""
    The FCPA prohibits bribery of foreign officials and requires accurate books and records. 
    Hedge funds must have robust anti-corruption controls, especially when dealing with foreign investors, deal sourcing, or emerging markets.
    """)

    fcpa_procedures = [
        "Adopt a written Anti-Bribery & Corruption Policy",
        "Conduct FCPA due diligence on all foreign investors, intermediaries, and deal partners",
        "Implement gifts, hospitality, and entertainment approval procedures with clear monetary limits",
        "Prohibit facilitation payments (grease payments)",
        "Require anti-corruption clauses in all contracts with foreign parties",
        "Maintain accurate books and records of all payments and expenses",
        "Provide annual FCPA training to deal teams, compliance, and senior management",
        "Establish confidential reporting mechanisms (hotline) for suspected violations",
        "Conduct periodic risk assessments and third-party audits of high-risk relationships",
        "Immediately investigate and report any suspected FCPA violations to senior management and legal counsel"
    ]
    for procedure in fcpa_procedures:
        st.checkbox(procedure, value=True)

    st.info("**FCPA Penalties**: Civil and criminal fines, disgorgement of profits, and potential debarment from U.S. government contracts. Individuals can face imprisonment.")

    # Interactive CFIUS / FCPA Assessment Form
    st.subheader("CFIUS / FCPA Risk Assessment Form")
    with st.form("cfius_fcpa_form"):
        entity = st.text_input("Investor / Entity Name")
        country = st.selectbox("Country of Origin", ["China", "Russia", "Other Country of Concern", "Allied Country", "Other"])
        risk_area = st.selectbox("Primary Risk Area", ["CFIUS (National Security)", "FCPA (Anti-Bribery)", "Both"])
        notes = st.text_area("Assessment Notes / Mitigation Steps")
        submitted = st.form_submit_button("Submit Assessment & Sign")
        if submitted:
            st.success(f"Assessment completed for **{entity}**.")
            log_audit_trail(st.session_state.username, "CFIUS/FCPA Assessment", f"Entity: {entity} | Area: {risk_area}", "Unknown")
            log_attestation(st.session_state.username, f"CFIUS/FCPA - {entity}")

st.sidebar.info("BSA Officer: Chief Compliance Officer\nCFIUS and FCPA compliance are critical national security and anti-corruption requirements.")