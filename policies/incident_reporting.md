# Incident Reporting & Response Policy (Full Incident Response Plan)  
[Your Hedge Fund Group Name] – Registered Investment Adviser ($1B AUM)  
Adopted pursuant to Rule 206(4)-7, Regulation S-P (Safeguards Rule – amended), FinCEN AML/BSA (effective 2028), and fiduciary duty.

**Incident Response Officer**: Chief Compliance Officer (CCO) – primary escalation point with authority to notify senior management, regulators, or investors.

## 1. Definition of Reportable Incidents
Any actual or suspected event that:
- Violates federal securities laws, firm policies, or fiduciary duty
- Involves unauthorized access, use, or disclosure of customer information (Reg S-P)
- Triggers AML/BSA suspicious activity
- Involves AI model failures (bias, drift, hallucination, privacy leak)
- Causes material operational, financial, reputational, or regulatory harm

## 2. Reporting Requirements (All Employees)
- **High-Severity** (data breach, SAR trigger, material AI impact): Report **within 1 hour**.
- **Medium/Low-Severity**: Report **within 24 hours**.
- Use the portal’s centralized Incident Reporting form.
- Do **not** discuss with affected parties without CCO approval (tipping-off prohibition for AML).

## 3. Detailed Incident Response Plan (IRP) – Step-by-Step Procedures
The firm follows a structured, documented IRP (NIST-aligned + regulatory requirements):

### Phase 1: Preparation (Ongoing)
- Annual training for all staff (Training Center module).
- Designated IR Team (CCO, legal, IT, AI Governance lead).
- Updated contact list, tools, and playbooks maintained in Google Drive.

### Phase 2: Identification & Reporting
- Employee submits incident via portal form (category, severity, description, evidence upload).
- System auto-logs to audit trail and notifies CCO via email (configurable).

### Phase 3: Analysis & Triage (CCO-Led – within 4 hours of report)
- Confirm incident validity and classify severity.
- Assemble IR Team if high-severity.
- Preserve evidence (forensic images, logs) – chain-of-custody documented.

### Phase 4: Containment (Immediate)
- Isolate affected systems (e.g., disable compromised accounts, quarantine AI model).
- Stop ongoing harm (e.g., halt erroneous AI trades, block suspicious wires).

### Phase 5: Eradication & Recovery
- Remove root cause (patch vulnerabilities, retrain AI model, update policies).
- Restore systems with verified clean backups.
- Test restored controls before resuming operations.

### Phase 6: Post-Incident Review & Remediation (within 30 days)
- Root-cause analysis documented in portal.
- Lessons learned and control improvements.
- Remediation plan with owners and deadlines tracked in Report Center.

### Phase 7: Regulatory & Customer Notifications (Strict Timelines)
**Reg S-P (Cybersecurity / Privacy Incidents)**:
- Assess whether sensitive customer information was (or is reasonably likely to have been) accessed/used without authorization.
- **Customer Notification**: Clear and conspicuous written notice **as soon as practicable, but no later than 30 days** after the determination.
- **Service Provider Notification**: Contracts require providers to notify the firm **within 72 hours** of any incident involving customer information they maintain.
- Firm remains ultimately responsible for timely customer notice.

**AML/BSA Incidents**:
- Internal escalation to BSA Officer within 24 hours.
- File Suspicious Activity Report (SAR) with FinCEN **within 30 days** (or 60 days if no suspect identified initially).
- Strict no-tipping-off rule.

**AI-Specific Incidents**:
- Report bias/drift/hallucination events causing material impact to AI Governance Committee within **1 business day**.
- Require immediate re-testing and human oversight remediation.

**General Compliance Incidents**:
- Document in portal; escalate to senior management if material.
- Update Form ADV if required.

## 4. Recordkeeping & Testing
- All incidents, investigations, notifications, and remediation plans retained for **5 years** in Google Drive with DocuSign audit trail.
- Annual IRP testing (table-top exercise + live simulation).
- CCO presents effectiveness to senior management annually.

**Training**: All supervised persons must complete the annual “Incident Reporting & Reg S-P” module (quiz + DocuSign attestation).

**Approval**: Signed by CEO and CCO via DocuSign. Reviewed after every material incident or annually.