import streamlit as st
import pandas as pd
from datetime import datetime
from database import log_audit_trail, log_ai_risk_test
from utils import generate_and_sign_policy

st.title("🤖 AI Governance & Risk Testing")
st.caption("NIST AI RMF + SEC 2026 Supervision Priorities")

st.markdown("### AI Model Registry & Risk Testing Checklist")
st.info("Use this interactive tool to document and test all AI models used in portfolio management, compliance, valuation, or marketing.")

# Model Registry
with st.expander("📋 Current AI Model Registry", expanded=True):
    if 'ai_models' not in st.session_state:
        st.session_state.ai_models = []
    
    model_name = st.text_input("Model Name / Tool", placeholder="e.g., Sentiment Analysis LLM v2.1")
    use_case = st.selectbox("Primary Use Case", [
        "Trade Signal Generation",
        "Risk Monitoring",
        "AML / KYC Screening",
        "Valuation of Illiquid Assets",
        "Marketing Content Generation",
        "Investor Sentiment Analysis",
        "Other"
    ])
    
    if st.button("Add Model to Registry"):
        if model_name:
            st.session_state.ai_models.append({
                "name": model_name,
                "use_case": use_case,
                "added_date": datetime.now().strftime("%Y-%m-%d")
            })
            st.success(f"Model '{model_name}' added to registry.")
            log_audit_trail(st.session_state.username, "AI Model Added", f"Model: {model_name} | Use Case: {use_case}", "Unknown")

    if st.session_state.ai_models:
        df = pd.DataFrame(st.session_state.ai_models)
        st.dataframe(df, use_container_width=True)

# Interactive AI Risk Testing Checklist
st.subheader("Interactive AI Risk Testing Checklist")
st.markdown("Complete this checklist for each AI model before deployment or after material changes.")

model_to_test = st.selectbox("Select Model to Test", [m["name"] for m in st.session_state.get("ai_models", [])] or ["No models registered yet"])

if model_to_test != "No models registered yet":
    st.write(f"**Testing: {model_to_test}**")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Pre-Deployment Testing**")
        bias_test = st.checkbox("Bias & Fairness Testing completed (disparate impact, demographic parity)")
        explain_test = st.checkbox("Explainability tested (SHAP/LIME, feature importance)")
        accuracy_test = st.checkbox("Accuracy, robustness & hallucination tested")
        privacy_test = st.checkbox("Data quality & privacy impact assessment completed")

    with col2:
        st.markdown("**Ongoing Monitoring**")
        drift_test = st.checkbox("Model drift detection in place (data/concept drift alerts)")
        fairness_monitor = st.checkbox("Ongoing fairness & bias monitoring")
        human_oversight = st.checkbox("Human-in-the-loop oversight documented")
        vendor_test = st.checkbox("Third-party/vendor AI due diligence completed")

    notes = st.text_area("Additional Notes, Evidence Links, or Remediation Items", height=120)

    overall_score = sum([bias_test, explain_test, accuracy_test, privacy_test, drift_test, fairness_monitor, human_oversight, vendor_test]) * 12.5

    st.metric("AI Risk Testing Completion Score", f"{overall_score:.1f}%", 
              "✅ Production Ready" if overall_score >= 90 else "⚠️ Needs Remediation")

    if st.button("Generate & Sign AI Risk Testing Report"):
        if overall_score < 70:
            st.error("Score too low for approval. Address remediation items first.")
        else:
            report_content = f"""
AI Risk Testing Report
Model: {model_to_test}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Prepared by: {st.session_state.get('name', 'CCO')}

Pre-Deployment Testing:
• Bias & Fairness: {'✅' if bias_test else '❌'}
• Explainability: {'✅' if explain_test else '❌'}
• Accuracy & Robustness: {'✅' if accuracy_test else '❌'}
• Privacy Assessment: {'✅' if privacy_test else '❌'}

Ongoing Monitoring:
• Drift Detection: {'✅' if drift_test else '❌'}
• Fairness Monitoring: {'✅' if fairness_monitor else '❌'}
• Human Oversight: {'✅' if human_oversight else '❌'}
• Vendor Due Diligence: {'✅' if vendor_test else '❌'}

Overall Score: {overall_score:.1f}%
Notes: {notes}
            """

            drive_id, envelope_id, pdf_path = generate_and_sign_policy(
                f"AI_Risk_Testing_{model_to_test}", 
                report_content, 
                st.session_state.username, 
                st.session_state.email, 
                st.secrets["GOOGLE_DRIVE_FOLDER_ID"]
            )

            log_ai_risk_test(st.session_state.username, model_to_test, overall_score, drive_id, envelope_id)
            log_audit_trail(st.session_state.username, "AI Risk Testing Completed", f"Model: {model_to_test} | Score: {overall_score:.1f}%", "Unknown")

            st.success(f"✅ AI Risk Testing Report generated and sent for DocuSign. Envelope: {envelope_id}")
            st.download_button("Download Report", report_content, f"AI_Risk_Testing_{model_to_test}.txt")

st.info("""
**SEC 2026 Priorities for AI**:
- Adequate supervision of AI tools
- Testing for bias, explainability, and drift
- Accurate representations (no "AI washing")
- Human oversight for material decisions
- Proper disclosures in Form ADV
""")

st.sidebar.info("All AI risk testing is logged with full audit trail and stored in Google Drive.")