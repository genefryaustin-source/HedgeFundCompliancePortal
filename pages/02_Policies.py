import streamlit as st
from datetime import datetime
from utils import generate_and_sign_policy
from database import log_audit_trail, log_attestation

st.title("📋 Policies & Procedures Library")
st.caption("$1B AUM Hedge Fund RIA – SOC 2 Type 2 + SEC + FinCEN IA + CFIUS Compliance")

st.info("""
All policies are displayed in full detail below.  
Click **"Generate PDF & Send for DocuSign"** to create a signed auditable record.
If nothing happens or you see an error, the full error message will now appear.
""")

# ==================== FULL POLICY LIBRARY ====================
policy_library = {
    "Access Control Policy": """**Access Control Policy** (SOC 2 Security)

**Purpose**: Ensure only authorized individuals have appropriate access to systems, data, and physical facilities.

**Key Requirements**:
- Principle of Least Privilege
- Role-Based Access Control (RBAC)
- Multi-Factor Authentication (MFA) mandatory for all sensitive systems
- Quarterly access reviews and recertification
- Immediate revocation upon termination or role change
- Segregation of Duties (SoD) for financial and compliance functions

**Responsibility**: Chief Compliance Officer and IT Security Lead.""",

    "Change Management Policy": """**Change Management Policy** (SOC 2 Security & Processing Integrity)

**Process**:
1. Formal change request with risk assessment
2. Testing in non-production environment
3. Peer review and CAB approval
4. Deployment with rollback plan
5. Post-implementation monitoring

**Responsibility**: IT Lead and CCO.""",

    "Third-Party / Vendor Risk Management Policy": """**Third-Party / Vendor Risk Management Policy** (SOC 2)

**Requirements**:
- Pre-engagement risk assessment
- Annual review of SOC 2 reports for critical vendors
- Contracts with data protection and 72-hour breach notification
- Ongoing monitoring of high-risk vendors""",

    "Data Classification & Handling Policy": """**Data Classification & Handling Policy** (SOC 2 Confidentiality & Privacy)

**Levels**: Public, Internal, Confidential, Highly Confidential (PII, KYC, AML data).

**Rules**: Encryption at rest/transit, secure disposal, labeling.""",

    "Encryption Policy": """**Encryption Policy** (SOC 2)

**Requirements**:
- AES-256 for data at rest
- TLS 1.2+ for data in transit
- Key management with rotation""",

    "Vulnerability Management & Patch Management Policy": """**Vulnerability Management & Patch Management Policy** (SOC 2)

Monthly scanning, critical patches within 7 days, annual penetration testing.""",

    "Backup & Recovery Policy": """**Backup & Recovery Policy** (SOC 2 Availability)

Daily encrypted backups, quarterly restore testing, defined RTO/RPO.""",

    "Cybersecurity & Reg S-P WISP": """**Cybersecurity Policy & Written Information Security Program (WISP)** (Reg S-P)

Includes 30-day customer notification, 72-hour vendor notification, annual risk assessment, and incident response plan.""",

    "AI Governance & Risk Management Policy": """**AI Governance & Risk Management Policy**

Pre-deployment bias/explainability testing, model registry, human oversight, prohibition on AI washing.""",

    "Incident Response Policy": """**Incident Response Policy**

Phases: Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned.
Notification timelines per Reg S-P and GDPR.""",

    "AML / BSA Program Policy": """**AML / BSA 5-Pillar Program Policy**

Pillar 1: Risk Assessment  
Pillar 2 & 5: Enhanced Due Diligence  
Pillar 3: Ongoing Training  
Pillar 4: Independent Testing  
Pillar 5: CIP/KYC/CDD/SAR/CTR/UBO/PEP/Transaction Monitoring + OFAC screening.""",

    "CFIUS Compliance Policy": """**CFIUS Compliance Policy**

**Purpose**: Ensure compliance with Committee on Foreign Investment in the United States (CFIUS) regulations.

**Key Triggers**:
- Foreign investor acquiring control or significant influence
- Investment in critical technology or critical infrastructure
- Access to sensitive personal data of U.S. citizens

**Critical Technologies** include AI, semiconductors, quantum computing, biotechnology, advanced robotics, etc.

**Mitigation Strategies** (when required):
- U.S.-based security committee with independent directors
- CFIUS-approved security officer with veto rights
- Strict data segregation and access controls
- Limit foreign investor access to critical technology
- Prior CFIUS approval for key changes
- Regular third-party audits and compliance reporting
- Physical and logical separation of sensitive operations

**Procedures**:
- Pre-investment CFIUS risk assessment
- Engagement of outside counsel for high-risk deals
- Maintenance of records for at least 5 years

**Responsibility**: Chief Compliance Officer with legal support.
**Annual Review**: Required.""",
}

# ==================== DISPLAY POLICIES ====================
for title, content in policy_library.items():
    with st.expander(f"📄 {title}", expanded=False):
        st.markdown(content)
        
        if st.button(f"Generate PDF & Send for DocuSign", key=f"btn_{title.replace(' ', '_').replace('/', '_')}"):
            with st.spinner("Generating PDF and sending to DocuSign..."):
                try:
                    drive_id, envelope_id, pdf_path = generate_and_sign_policy(
                        title=title,
                        content=content,
                        username=st.session_state.get("username", "CCO"),
                        email=st.session_state.get("email", "cco@hedgefund.com"),
                        folder_id="Compliance_Policies"
                    )
                    st.success(f"✅ {title} PDF generated and sent for signature!")
                    st.info(f"Envelope ID: {envelope_id} | PDF: {pdf_path}")
                    
                    log_audit_trail(
                        st.session_state.get("username", "Unknown"),
                        "Policy Sent for Signature",
                        title,
                        "Unknown"
                    )
                    log_attestation(
                        st.session_state.get("username", "Unknown"),
                        title
                    )
                except Exception as e:
                    st.error(f"❌ Failed to generate/send {title}")
                    st.error(str(e))
                    st.exception(e)  # Shows full traceback for debugging

st.write("---")
st.subheader("🔧 DocuSign Consent Setup")

if st.button("Generate DocuSign Consent URL"):
    client_id = st.secrets["DOCUSIGN"]["INTEGRATION_KEY"]
    # Use your exact deployed app URL
    redirect_uri = "https://hedgefundcompliance.streamlit.app"   # ← CHANGE IF YOUR APP NAME IS DIFFERENT
    
    consent_url = (
        f"https://account-d.docusign.com/oauth/auth?"
        f"response_type=code&"
        f"scope=signature%20impersonation&"
        f"client_id={client_id}&"
        f"redirect_uri={redirect_uri}&"
        f"state=consent_test"
    )
    
    st.success("Consent URL ready")
    st.markdown(f"[🔗 Open Consent Page]({consent_url})")
    st.info("1. Make sure the Redirect URI is registered in DocuSign\n2. Log in with the CCO account\n3. Click Accept")
st.success("✅ All policies are loaded with full details and attestation workflow.")
st.caption("Last updated: March 2026")