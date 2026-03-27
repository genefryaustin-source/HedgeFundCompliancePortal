# Phishing Response Playbook  
[Your Hedge Fund Group Name] – Registered Investment Adviser ($1B AUM)  
Part of the overall Incident Response Plan (IRP) and Reg S-P Written Information Security Program (WISP).  
Adopted pursuant to Regulation S-P (Safeguards Rule), Rule 206(4)-7, and 2026 SEC Examination Priorities on cybersecurity (including AI-enhanced phishing and polymorphic malware).

**Purpose**: Provide clear, actionable steps for detecting, responding to, containing, eradicating, recovering from, and documenting phishing incidents. Phishing is a primary vector for ransomware, business email compromise (BEC), credential theft, and malware delivery.

**Trigger**: Suspected or confirmed phishing email, malicious link/attachment, credential compromise, or related suspicious activity.

**Incident Response Officer**: Chief Compliance Officer (CCO) – immediate escalation contact.

## Step-by-Step Response Procedures (Execute in Parallel Where Possible)

### Phase 1: Identification & Immediate Reporting (0–1 Hour)
1. **Recognize Indicators**:
   - Unsolicited emails with urgent language, unexpected attachments/links, sender address anomalies, or requests for credentials.
   - AI-enhanced signs: Deepfake voice/video calls, sophisticated grammar errors, or personalized content based on public data.
   - Post-click signs: Unusual system behavior, pop-ups, or login attempts from unknown locations.

2. **Do Not Interact**:
   - Do **not** click links, open attachments, or reply.
   - Forward suspicious email as attachment (not link) to security@yourfirm.com or use the portal’s “Report Phishing” button.

3. **Report Immediately**:
   - High-severity (clicked link or entered credentials): Report **within 1 hour** via portal Incident Reporting form (select “Cybersecurity / Phishing” category).
   - Low-severity: Report **within 24 hours**.
   - Include: Screenshot, email headers, actions taken, and potential impact (e.g., accessed client data?).

### Phase 2: Containment (Immediate – 4 Hours)
1. **Isolate Affected User/Account**:
   - Disable compromised account(s) or force password reset + MFA re-enrollment.
   - Quarantine device if malware suspected (disconnect from network).

2. **Block Malicious Indicators**:
   - Block sender domain/IP, malicious URLs, and file hashes in email gateway, firewall, and endpoint protection.
   - Scan all users who received the same campaign.

3. **Preserve Evidence**:
   - Do not delete the original email or logs. Capture full headers, timestamps, and system logs. Maintain chain-of-custody in Google Drive.

### Phase 3: Eradication & Investigation (4–24 Hours)
1. **Full Scan & Removal**:
   - Run endpoint detection and response (EDR) scans on affected and similar systems.
   - Remove malware, reset all potentially compromised credentials, and review for lateral movement.

2. **Scope Assessment** (Critical for Reg S-P):
   - Determine if customer information (nonpublic personal information) was accessed or exfiltrated.
   - Review logs for data access during the incident window.
   - Engage forensics if material impact suspected.

3. **AI-Specific Considerations** (if AI tools involved):
   - Check if phishing targeted AI systems (e.g., prompt injection via email).
   - Re-validate affected AI models for drift or compromised training data.

### Phase 4: Recovery & Notification (Within Regulatory Timelines)
1. **Restore Operations**:
   - Verify systems are clean before re-enabling accounts.
   - Test controls post-recovery.

2. **Regulatory & Customer Notifications (Reg S-P)**:
   - If sensitive customer information was (or is reasonably likely to have been) accessed/used without authorization: Provide clear notice **as soon as practicable, but no later than 30 days**.
   - Notify service providers/vendors per contract (they must report to you within **72 hours** if they detect an incident).
   - File any required SEC reports (e.g., significant cybersecurity incident via Form ADV-C if applicable).

3. **Internal Communications**:
   - Notify senior management and IR Team.
   - Issue firm-wide reminder on phishing awareness without revealing sensitive details.

### Phase 5: Post-Incident Review & Lessons Learned (Within 30 Days)
1. **Root-Cause Analysis**: Document how the phishing succeeded (e.g., bypassed filters, user clicked due to urgency).
2. **Remediation**:
   - Update email filters, MFA policies, or training.
   - Conduct targeted phishing simulation for at-risk users.
3. **Update Playbook/WISP**: Incorporate lessons into annual review.
4. **Documentation**: Log full incident in portal with evidence, timeline, notifications, and remediation plan. Retain for **5 years** in Google Drive with DocuSign audit trail.

**Annual Testing**: Include phishing scenarios in table-top exercises and live simulations.

**Training**: All employees complete annual “Phishing Awareness & Response” module (integrated in Training Center with quiz and DocuSign attestation). Quarterly simulated phishing tests recommended.

**Approval**: Reviewed and approved by CCO and senior management via DocuSign annually or after material incidents.