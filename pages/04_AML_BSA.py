import streamlit as st
from datetime import datetime
from database import log_audit_trail, log_attestation

st.title("AML / BSA 5-Pillar Program + CFIUS & Export Controls")
st.caption("$1B AUM Hedge Fund RIA – FinCEN IA Rule + National Security Requirements")

# Row 1: Core AML Pillars
row1 = st.tabs([
    "1. Risk Assessment",
    "2. Enhanced Due Diligence (EDD)",
    "3. Training"
])

# Row 2: Remaining Compliance Areas
row2 = st.tabs([
    "4. Independent Testing",
    "5. CIP / KYC / CDD / SAR / Monitoring",
    "6. CFIUS & Export Controls"
])

# ====================== TAB 1 ======================
with row1[0]:
    st.subheader("Annual AML Risk Assessment")
    st.markdown("**Pillar 1** – Risk-Based Approach")
    # Add your existing risk assessment code here if desired

# ====================== TAB 2 ======================
with row1[1]:
    st.subheader("Enhanced Due Diligence (EDD) Procedures")
    st.markdown("**Pillar 2 & 5** – Applied when risk is elevated.")
    # Add your existing EDD content here

# ====================== TAB 3 ======================
with row1[2]:
    st.subheader("Pillar 3 – Ongoing Training")
    st.info("Complete the AML/BSA 5-Pillar Training in the Training Center.")
    st.page_link("pages/03_Training.py", label="Go to Training Center →", icon="📚")

# ====================== TAB 4 ======================
with row2[0]:
    st.subheader("Pillar 4 – Independent Testing & Audit")
    st.write("Annual independent test of all 5 pillars required.")

# ====================== TAB 5 ======================
with row2[1]:
    st.subheader("Pillar 5 – CIP / KYC / CDD / SAR / Monitoring")
    st.info("CIP, KYC, CDD, SAR filing, and transaction monitoring tools are available here.")

# ====================== TAB 6 ======================
with row2[2]:
    st.subheader("CFIUS & Export Controls Compliance")
    st.markdown("**National Security Requirements**")

    st.write("### CFIUS (Committee on Foreign Investment in the United States)")
    st.write("CFIUS reviews foreign investments that could affect U.S. national security.")

    st.write("**Key CFIUS Triggers**")
    cfius_triggers = [
        "Foreign investor acquiring control or significant influence",
        "Investment in critical technology",
        "Investment in critical infrastructure",
        "Access to sensitive personal data of U.S. citizens",
        "Foreign government-linked investors"
    ]
    for trigger in cfius_triggers:
        st.checkbox(trigger)

    st.write("**CFIUS Critical Technologies Examples**")
    critical_tech = [
        "Artificial Intelligence and machine learning systems",
        "Semiconductors and semiconductor manufacturing equipment",
        "Quantum computing and quantum information sciences",
        "Biotechnology and biological technologies",
        "Advanced robotics and autonomous systems",
        "Additive manufacturing (3D printing) for defense applications",
        "Advanced materials and metamaterials",
        "Aerospace and defense-related technologies",
        "Nuclear technologies",
        "Encryption and cybersecurity technologies"
    ]
    for item in critical_tech:
        st.checkbox(item)

    st.write("**CFIUS Mitigation Agreements** (when required)")
    mitigation = [
        "Establish a U.S.-based security committee with independent directors",
        "Appoint a CFIUS-approved security officer",
        "Implement strict data segregation and access controls",
        "Limit foreign investor access to critical technology",
        "Require CFIUS approval for key changes in ownership or personnel",
        "Undergo regular third-party audits and compliance reporting"
    ]
    for item in mitigation:
        st.checkbox(item, value=True)

    st.write("### Export Controls Compliance (ITAR & EAR)")
    st.write("**Required Procedures**")
    export_controls = [
        "Screen investments for ITAR-controlled defense articles",
        "Screen for EAR-controlled dual-use items and technology",
        "Implement controls to prevent unauthorized export of technical data",
        "Obtain export licenses when required",
        "Include export control clauses in subscription agreements",
        "Train deal teams and compliance staff on export controls"
    ]
    for item in export_controls:
        st.checkbox(item, value=True)

    st.info("**Note**: CFIUS and Export Controls often overlap with investor onboarding and due diligence processes.")

st.sidebar.info("BSA Officer: Chief Compliance Officer\nCFIUS and Export Controls are critical national security requirements.")