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
    # Your existing risk assessment code can stay here

with tab2:
    st.subheader("Enhanced Due Diligence (EDD) Procedures")
    # Your existing EDD section can stay here

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
    st.subheader("CFIUS & Export Controls Compliance")
    st.markdown("**National Security Requirements** – Critical for hedge funds with foreign investors or technology exposure.")

    # ====================== CFIUS SECTION ======================
    st.write("### CFIUS (Committee on Foreign Investment in the United States)")
    st.write("CFIUS reviews transactions involving foreign investment in U.S. businesses that could affect national security.")

    st.write("**CFIUS Critical Technologies Examples**")
    critical_tech = [
        "Artificial Intelligence and machine learning systems",
        "Semiconductors and semiconductor manufacturing equipment",
        "Quantum computing and quantum information sciences",
        "Biotechnology and biological technologies (including synthetic biology)",
        "Advanced robotics and autonomous systems",
        "Additive manufacturing (3D printing) for defense applications",
        "Advanced materials (e.g., metamaterials, high-performance composites)",
        "Aerospace and defense-related technologies",
        "Nuclear technologies and nuclear power systems",
        "Encryption and cybersecurity technologies with national security applications"
    ]
    for item in critical_tech:
        st.checkbox(item)

    st.write("**CFIUS Mandatory Declaration Triggers**")
    st.write("A short-form declaration is **mandatory** if the investment involves critical technology **and** the foreign investor gains certain rights (board observer, access to technical information, or substantive decision-making).")

    # ====================== EXPORT CONTROLS SECTION ======================
    st.subheader("Export Controls Compliance (ITAR & EAR)")
    st.markdown("""
    U.S. export control laws (ITAR and EAR) restrict the export of defense articles, dual-use items, and technical data. 
    Hedge funds must ensure compliance when investing in or providing funding to companies involved in controlled technologies.
    """)

    st.write("**Key Export Controls Requirements**")
    export_controls = [
        "Screen all investments for involvement in ITAR-controlled defense articles or services",
        "Screen for EAR-controlled dual-use items and technology (especially items on the Commerce Control List)",
        "Implement controls to prevent unauthorized export of technical data or software",
        "Obtain export licenses when required before sharing controlled technology with foreign investors",
        "Maintain records of all export control assessments and licenses (minimum 5 years)",
        "Train relevant staff (deal teams, compliance, legal) on export control obligations",
        "Include export control clauses in subscription agreements and side letters",
        "Conduct periodic audits of portfolio companies for export compliance",
        "Immediately escalate any suspected violations to senior management and legal counsel"
    ]
    for item in export_controls:
        st.checkbox(item, value=True)

    st.info("""
    **Practical Hedge Fund Considerations**:
    - Even minority investments can trigger export control issues if the fund gains access to controlled technical data.
    - Side letters requesting information rights can inadvertently create export control violations.
    - Portfolio companies developing dual-use technologies require heightened scrutiny.
    """)

    # Interactive CFIUS / Export Controls Assessment Form
    st.subheader("CFIUS & Export Controls Risk Assessment Form")
    with st.form("cfius_export_form"):
        entity = st.text_input("Investor / Entity Name")
        country = st.selectbox("Country of Origin", ["China", "Russia", "Other Country of Concern", "Allied Country", "Other"])
        involves_critical_tech = st.checkbox("Involves Critical Technology?")
        involves_export_control = st.checkbox("Involves Export-Controlled Items or Technical Data?")
        notes = st.text_area("Assessment Notes / Mitigation Steps")
        submitted = st.form_submit_button("Submit Assessment & Sign")
        if submitted:
            risk_level = "High" if (country in ["China", "Russia", "Other Country of Concern"] and (involves_critical_tech or involves_export_control)) else "Medium"
            st.success(f"Assessment completed for **{entity}** – Risk Level: **{risk_level}**")
            log_audit_trail(st.session_state.username, "CFIUS/Export Controls Assessment", f"Entity: {entity} | Risk: {risk_level}", "Unknown")
            log_attestation(st.session_state.username, f"CFIUS/Export Controls - {entity}")

st.sidebar.info("BSA Officer: Chief Compliance Officer\nCFIUS and Export Controls are critical national security requirements.")