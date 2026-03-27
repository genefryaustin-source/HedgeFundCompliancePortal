# Artificial Intelligence (AI) Policy & Procedures  
[Your Hedge Fund Group Name] – Registered Investment Adviser ($1B AUM)  
Adopted pursuant to fiduciary duty (Rule 206(4)-7), SEC 2026 Examination Priorities on AI supervision and "AI washing," and NIST AI Risk Management Framework (Govern, Map, Measure, Manage).

**AI Governance Committee**: Chief Compliance Officer (CCO) + Chief Investment Officer (CIO) + senior management. Meets quarterly. All material AI use must be inventoried and pre-approved.

## 1. Scope
This policy governs all AI/ML/LLM tools used for portfolio management, trade execution, risk monitoring, compliance testing, valuation, investor communications, marketing, AML screening, or any other advisory functions.

## 2. Permitted & Prohibited Uses
**Permitted** (with oversight): Research assistance, sentiment analysis on public data, automated KYC/AML screening, back-testing, anomaly detection.  
**Prohibited**: Fully autonomous trading without human pre-approval; generation of marketing materials or performance claims without CCO review and substantiation; processing of MNPI or confidential client data without anonymization and explicit approval.

## 3. Risk Management & Controls – Detailed AI Risk Testing Protocol
All AI systems follow a structured lifecycle testing protocol aligned with NIST AI RMF and SEC expectations for supervision and accurate representations.

### Pre-Deployment Testing (Validation Phase)
1. **Bias & Fairness Testing**  
   - Test outputs across protected characteristics and demographic segments (where relevant).  
   - Metrics: Disparate impact ratio, equalized odds, demographic parity, adverse impact ratio.  
   - Acceptable thresholds defined per use case (e.g., <20% disparity).  
   - Mitigation: Re-sampling, re-weighting, or fairness constraints. Third-party audit required for high-impact models.

2. **Explainability & Interpretability Testing**  
   - High-stakes decisions require human-interpretable rationale.  
   - Techniques: SHAP, LIME, feature importance, partial dependence plots.  
   - Minimum standard: Top contributing factors must be explainable; fallback to non-AI methods if score is insufficient.

3. **Accuracy, Robustness & Hallucination Testing**  
   - Back-testing, out-of-sample validation, stress testing under volatility.  
   - For LLMs/RAG: Groundedness, hallucination rate (<5% target), toxicity/PII leakage.  
   - Adversarial testing: Prompt injection, data poisoning, evasion attacks.

4. **Data Quality & Privacy Testing**  
   - Lineage tracking.  
   - Privacy impact assessment (GDPR/CCPA/Reg S-P compliant).  
   - Proxy discrimination testing.

### Ongoing / Post-Deployment Testing (Monitoring Phase)
1. **Model Drift Detection**  
   - Monitor data drift, concept drift, performance degradation (AUC drop >10%).  
   - Automated alerts; retraining with full re-validation.

2. **Fairness & Bias Monitoring**  
   - Monthly segment performance re-testing; document trade-offs and remediation.

3. **Human-in-the-Loop Oversight**  
   - All material outputs require documented human review and approval.

4. **Third-Party / Vendor AI Testing**  
   - Require model cards, SOC 2 + AI attestations.  
   - Independent validation and contractual audit rights.

**Documentation**: Maintain a model registry in Google Drive with version control, test results, approvals, and remediation plans. Retention: 5 years.

**AI Washing Prohibition**: Any representation of AI capabilities must be accurate, substantiated, and not overstated.

## 4. Disclosures to Investors
- Form ADV Part 2A: Describe material AI use, risks, and controls.  
- Investor reports: Note AI involvement with clear disclaimers.

## 5. Training & Attestation
- Annual “AI Ethics & Compliance” module in the Training Center (quiz + DocuSign attestation).  
- Targeted training for portfolio managers and compliance staff.

## 6. Incident Response
- AI-related incidents reported to Governance Committee within 1 business day.  
- Root-cause analysis and post-incident testing required.

## 7. Annual Review
- CCO documents effectiveness (including summary of all risk testing results).  
- Presented to senior management with DocuSign approval.

**Approval**: Signed by CEO and CCO via DocuSign.  
**Version Control**: Maintained in Google Drive; all users attest to the latest version.