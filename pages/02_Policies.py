import streamlit as st
from datetime import datetime
from utils import generate_and_sign_policy
from database import log_audit_trail, log_attestation

st.title("📋 Policies & Procedures Library")
st.caption("$1B AUM Hedge Fund RIA – SOC 2 Type 2 + SEC + FinCEN IA + CFIUS Compliance")

st.info("""
All policies below are required for SOC 2 Type 2, SEC Rule 206(4)-7, Reg S-P, and FinCEN IA compliance.  
Click **"Generate PDF & Send for DocuSign"** on any policy to create an auditable signed record.
""")

# Full Policy Library with Detailed Content
policy_library = {
    "Access Control Policy": """**Access Control Policy** (SOC 2 Security)

**Purpose**: Ensure only authorized individuals have appropriate access to systems, data, and physical facilities.

**Key Requirements**:
- Principle of Least Privilege: Users receive only the minimum access needed to perform their job.
- Role-Based Access Control (RBAC) implemented across all systems.
- Multi-Factor Authentication (MFA) mandatory for all accounts accessing sensitive data or production systems.
- Quarterly access reviews and recertification by department managers.
- Immediate revocation of access upon termination or role change.
- Segregation of Duties (SoD) enforced for financial, compliance, and IT functions.
- Privileged access requires additional approval and full logging.

**Enforcement**:
- All access requests must be submitted in writing and approved by manager + CCO.
- Automated provisioning/de-provisioning integrated with HRIS where possible.
- Annual policy review and employee attestation required.

**Responsibility**: Chief Compliance Officer and IT Security Lead.""",

    "Change Management Policy": """**Change Management Policy** (SOC 2 Security & Processing Integrity)

**Purpose**: Ensure all changes to production systems, code, infrastructure, or configurations are authorized, tested, and documented.

**Process**:
1. Formal change request with business justification and risk assessment.
2. Testing in non-production environment.
3. Peer/code review and Change Advisory Board (CAB) approval for high-risk changes.
4. Deployment with documented rollback plan.
5. Post-implementation monitoring for 30 days.

**Emergency Changes**: Allowed with post-facto approval and full documentation within 24 hours.

**Recordkeeping**: All changes logged with approver, tester, and outcome for audit purposes.

**Responsibility**: IT Lead and CCO.""",

    "Third-Party / Vendor Risk Management Policy": """**Third-Party / Vendor Risk Management Policy** (SOC 2 Security & Confidentiality)

**Purpose**: Manage risks from vendors and service providers that access or process company or client data.

**Requirements**:
- Pre-engagement risk assessment (security, privacy, financial stability).
- Annual review of SOC 2, ISO 27001, or equivalent reports for critical vendors.
- Contracts must include data protection clauses, right-to-audit, and 72-hour breach notification.
- Ongoing monitoring of high-risk vendors (quarterly).
- Termination procedures including secure data return or destruction.

**Responsibility**: CCO and Procurement.""",

    "Data Classification & Handling Policy": """**Data Classification & Handling Policy** (SOC 2 Confidentiality & Privacy)

**Classification Levels**:
- Public
- Internal
- Confidential (client data, financials)
- Highly Confidential (PII, KYC, AML data, encryption keys)

**Handling Rules**:
- Storage: AES-256 encryption for Confidential and higher.
- Transmission: TLS 1.2+ required.
- Disposal: Secure shredding or cryptographic wipe.
- Labeling required on all documents and files.

**Annual Review**: Policy reviewed and updated yearly.""",

    "Encryption Policy": """**Encryption Policy** (SOC 2 Security & Confidentiality)

**Requirements**:
- Data at rest: AES-256 or stronger.
- Data in transit: TLS 1.2 or higher (TLS 1.3 preferred).
- Key management using approved KMS or HSM with regular rotation.
- Full-disk encryption on all laptops and mobile devices.
- Prohibition on storing unencrypted sensitive data in email or unsecured cloud storage.""",

    "Vulnerability Management & Patch Management Policy": """**Vulnerability Management & Patch Management Policy** (SOC 2 Security)

**Requirements**:
- Monthly vulnerability scanning of all systems.
- Annual independent penetration testing.
- Patching timelines: Critical (7 days), High (14 days), Medium/Low (30-90 days).
- Risk-based prioritization using CVSS score and business impact.
- Exception process requires CCO approval with compensating controls.""",

    "Backup & Recovery Policy": """**Backup & Recovery Policy** (SOC 2 Availability)

**Requirements**:
- Daily backups of critical systems and data.
- Backups encrypted and stored off-site or in immutable storage.
- Retention: 30 days daily + monthly for 12 months.
- Quarterly restore testing with documented RTO/RPO targets.
- Annual Business Continuity Plan test.""",

    "Logging & Monitoring Policy": """**Logging & Monitoring Policy** (SOC 2 Security)

**Requirements**:
- Centralized logging of security events, access attempts, and system changes.
- Retention: 90 days online, 1 year archived.
- Real-time alerting for anomalous activity.
- Regular log review by security team.""",

    "Physical Security Policy": """**Physical Security Policy** (SOC 2 Security)

**Requirements**:
- Badge access and visitor logs for all office locations.
- Clean desk policy enforced.
- Video surveillance in sensitive areas.
- Secure disposal of hardware containing data.""",

    "Acceptable Use Policy": """**Acceptable Use Policy** (SOC 2 Security)

**Purpose**: Define permitted and prohibited use of company systems and data.
**Prohibited Activities**:
- Unauthorized software installation
- Sharing of credentials
- Downloading unapproved files
- Personal use that creates security risk

All employees must acknowledge annually.""",

    "Employee Onboarding / Offboarding Policy": """**Employee Onboarding / Offboarding Policy** (SOC 2 Security)

**Onboarding**:
- Background checks for all hires.
- Security awareness training within first week.
- Role-based access granted only after training.

**Offboarding**:
- Immediate revocation of all access on last day.
- Return of company assets and data.
- Exit interview including security reminders.""",

    # Previously built core policies (kept in full detail)
    "Cybersecurity & Reg S-P WISP": """**Cybersecurity Policy & Written Information Security Program (WISP)** (Reg S-P)

**Purpose**: Protect customer information and maintain information security.

**Key Controls**:
- Written Information Security Program (WISP) maintained and reviewed annually.
- 30-day customer notification for certain breaches.
- 72-hour vendor notification requirement.
- Annual risk assessment and testing.
- Incident Response Plan with clear escalation paths.""",

    "AI Governance & Risk Management Policy": """**AI Governance & Risk Management Policy**

**Purpose**: Ensure safe, ethical, and compliant use of AI tools.

**Requirements**:
- Pre-deployment bias, explainability, and drift testing.
- Human oversight for high-risk AI decisions.
- Model registry and version control.
- Prohibition on AI washing.
- Annual AI risk assessment.""",

    "Incident Response Policy": """**Incident Response Policy**

**Phases**: Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned.
**Notification Timelines**: Reg S-P (30 days), GDPR (72 hours), vendors (72 hours)."""
}

# Display all policies with full content and attestation buttons
for title, content in policy_library.items():
    with st.expander(f"📄 {title}", expanded=False):
        st.markdown(content)
        
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button(f"Generate PDF & Send for DocuSign", key=f"sign_{title}"):
                try:
                    drive_id, envelope_id, pdf_path = generate_and_sign_policy(
                        title=title,
                        content=content,
                        username=st.session_state.get("username", "CCO"),
                        email=st.session_state.get("email", "cco@hedgefund.com"),
                        folder_id="Compliance_Policies"
                    )
                    st.success(f"✅ {title} PDF generated and sent for electronic signature!")
                    log_audit_trail(
                        st.session_state.get("username", "Unknown"),
                        "Policy Attestation Generated",
                        title,
                        "Unknown"
                    )
                    log_attestation(
                        st.session_state.get("username", "Unknown"),
                        title
                    )
                except Exception as e:
                    st.error(f"Error generating policy: {str(e)}")

st.success("✅ All required regulatory policies are now available with full details and attestation workflow.")
st.caption("Last updated: March 2026")