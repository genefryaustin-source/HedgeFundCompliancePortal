import streamlit as st
from datetime import datetime
from utils import generate_and_sign_policy
from database import log_audit_trail, log_attestation

st.title("📋 Policies & Procedures Library")
st.caption("$1B AUM Hedge Fund RIA – SOC 2 Type 2 + SEC + FinCEN IA + CFIUS Compliance")

st.info("""
All policies below are required for SOC 2 Type 2 audit readiness, SEC Rule 206(4)-7, Reg S-P, AML/BSA, and CFIUS compliance.  
Each policy is shown in full detail. Click **"Generate PDF & Send for DocuSign"** to create a signed auditable record.
""")

# Full detailed policy library
policy_library = {
    "Access Control Policy": """**Access Control Policy** (SOC 2 Security Criterion)

**Purpose**: Ensure only authorized individuals have appropriate access to systems, data, and physical facilities.

**Key Requirements**:
- Principle of Least Privilege
- Role-Based Access Control (RBAC)
- Multi-Factor Authentication (MFA) mandatory
- Quarterly access reviews and recertification
- Immediate revocation upon termination
- Segregation of Duties (SoD)

**Responsibility**: Chief Compliance Officer and IT Security Lead.""",

    "Change Management Policy": """**Change Management Policy** (SOC 2 Security & Processing Integrity)

**Process**:
1. Formal change request with risk assessment
2. Testing in non-production
3. Peer review and CAB approval
4. Deployment with rollback plan
5. Post-implementation monitoring

**Responsibility**: IT Lead and CCO.""",

    "Third-Party / Vendor Risk Management Policy": """**Third-Party / Vendor Risk Management Policy** (SOC 2 Security & Confidentiality)

**Requirements**:
- Pre-engagement risk assessment
- Annual SOC 2 / ISO 27001 review
- Contracts with data protection and breach notification clauses
- Ongoing monitoring of high-risk vendors

**Responsibility**: CCO and Procurement.""",

    "Data Classification & Handling Policy": """**Data Classification & Handling Policy** (SOC 2 Confidentiality & Privacy)

**Levels**: Public, Internal, Confidential, Highly Confidential (PII, KYC, AML data).

**Rules**: Encryption at rest/transit, secure disposal, labeling requirements.""",

    "Encryption Policy": """**Encryption Policy** (SOC 2 Security & Confidentiality)

**Requirements**:
- AES-256 for data at rest
- TLS 1.2+ for data in transit
- Key management with rotation
- Full-disk encryption on endpoints""",

    "Vulnerability Management & Patch Management Policy": """**Vulnerability Management & Patch Management Policy** (SOC 2 Security)

**Requirements**:
- Monthly scanning
- Critical patches within 7 days
- Annual penetration testing""",

    "Backup & Recovery Policy": """**Backup & Recovery Policy** (SOC 2 Availability)

**Requirements**:
- Daily encrypted backups
- Quarterly restore testing
- Defined RTO/RPO targets""",

    "Logging & Monitoring Policy": """**Logging & Monitoring Policy** (SOC 2 Security)

Centralized logging with 90-day retention and real-time alerting.""",

    "Physical Security Policy": """**Physical Security Policy** (SOC 2 Security)

Badge access, visitor logs, clean desk policy, secure hardware disposal.""",

    "Acceptable Use Policy": """**Acceptable Use Policy** (SOC 2 Security)

Defines permitted and prohibited use of company systems and data. Annual acknowledgment required.""",

    "Employee Onboarding / Offboarding Policy": """**Employee Onboarding / Offboarding Policy** (SOC 2 Security)

Background checks, security training on onboarding, immediate access revocation on offboarding.""",

    "Cybersecurity & Reg S-P WISP": """**Cybersecurity Policy & Written Information Security Program (WISP)** (Reg S-P & SOC 2)

Includes 30-day customer notification, 72-hour vendor notification, annual risk assessment, and incident response.""",

    "AI Governance & Risk Management Policy": """**AI Governance & Risk Management Policy**

Pre-deployment bias/explainability testing, model registry, human oversight, prohibition on AI washing.""",

    "Incident Response Policy": """**Incident Response Policy**

Phases: Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned.
Notification timelines per Reg S-P and GDPR.""",

    "AML / BSA Program Policy": """**AML / BSA 5-Pillar Program Policy**

Pillar 1: Risk Assessment  
Pillar 2 & 5: Enhanced Due Diligence (EDD)  
Pillar 3: Ongoing Training  
Pillar 4: Independent Testing  
Pillar 5: CIP/KYC/CDD/SAR/CTR/UBO/PEP/Transaction Monitoring + OFAC screening.""",

    # NEW: CFIUS Compliance Policy (fully detailed)
    "CFIUS Compliance Policy": """**CFIUS Compliance Policy**

**Purpose**: Ensure compliance with the Committee on Foreign Investment in the United States (CFIUS) regulations when foreign investors are involved in fund investments or the firm itself.

**Scope**: All investments involving foreign persons, entities, or funds with foreign limited partners, especially those involving critical technologies, critical infrastructure, or sensitive personal data.

**Key Requirements**:

**1. CFIUS Triggers**
- Foreign investor acquiring control or significant influence (≥25% voting interest)
- Investment in critical technology
- Investment in critical infrastructure
- Access to sensitive personal data of U.S. citizens
- Foreign government-linked investors

**2. CFIUS Critical Technologies Examples**
- Artificial Intelligence and machine learning systems
- Semiconductors and semiconductor manufacturing equipment
- Quantum computing and quantum information sciences
- Biotechnology and biological technologies
- Advanced robotics and autonomous systems
- Additive manufacturing (3D printing) for defense applications
- Advanced materials and metamaterials
- Aerospace and defense-related technologies
- Nuclear technologies
- Encryption and cybersecurity technologies

**3. Mandatory Declarations**
- Required for certain covered transactions involving critical technologies or TID U.S. businesses
- Submitted to CFIUS before closing

**4. CFIUS Mitigation Agreements** (when required)
- Establish a U.S.-based security committee with independent directors
- Appoint a CFIUS-approved security officer with veto rights
- Implement strict data segregation and access controls
- Limit foreign investor access to critical technology or sensitive data
- Require prior CFIUS approval for key changes in ownership, personnel, or technology transfers
- Undergo regular third-party audits and submit periodic compliance reports
- Include termination or divestiture rights for non-compliance
- Restrict foreign investor board observer or information rights
- Establish physical and logical separation of sensitive U.S. operations from foreign entities

**5. Procedures**
- Pre-investment CFIUS risk assessment for all foreign investor commitments
- Engagement of outside CFIUS counsel for high-risk transactions
- Maintenance of detailed records of all foreign investment reviews
- Annual CFIUS compliance training for deal teams and compliance staff
- Integration of CFIUS considerations into AML/EDD processes

**6. Recordkeeping**
- Retain all CFIUS-related documentation for at least 5 years

**Responsibility**: Chief Compliance Officer, with support from legal counsel and investment team.

**Annual Review**: This policy shall be reviewed and updated annually or upon material changes in CFIUS regulations.""",
}

# Display all policies with full detailed content
for title, content in policy_library.items():
    with st.expander(f"📄 {title}", expanded=False):
        st.markdown(content)
        
                col1, col2 = st.columns([4, 1])
                                 with col2:
                                     if st.button(f"Generate PDF & Send for DocuSign", key=f"sign_{title.replace(' ', '_').replace('/', '_')}"):
                                         with st.spinner("Generating PDF and sending to DocuSign..."):
                                             try:
                                                 drive_id, envelope_id, pdf_path = generate_and_sign_policy(
                                                     title=title,
                                                     content=content,
                                                      username=st.session_state.get("username", "CCO"),
                                                      email=st.session_state.get("email", "cco@hedgefund.com"),
                                                     folder_id="Compliance_Policies"
                                                  )
                                                  st.success(f"✅ PDF generated and envelope sent! Envelope ID: {envelope_id}")
                                                  st.info(f"PDF saved locally: {pdf_path}")
                                                  log_audit_trail(st.session_state.get("username", "Unknown"), "Policy Sent for Signature", title, "Unknown")
                                                  log_attestation(st.session_state.get("username", "Unknown"), title)
                                              except Exception as e:
                                                  st.error(f"❌ Failed: {str(e)}")
                                                  st.exception(e)   # This shows the full traceback on the page


st.write("---")
if st.button("Test Button - Click Me"):
    st.success("Button works! If you see this, the issue is inside generate_and_sign_policy()")

st.success("✅ All required SOC 2 Type 2, SEC, AML/BSA, CFIUS, and regulatory policies are now displayed in full detail with attestation workflow.")
st.caption("Policies updated: March 2026 | Ready for SOC 2 Type 2 and CFIUS audit")