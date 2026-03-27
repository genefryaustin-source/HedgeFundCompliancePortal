import streamlit as st
import pandas as pd
from datetime import datetime
from database import log_audit_trail, log_attestation

st.title("AML / BSA 5-Pillar Program")
st.caption("$1B AUM Hedge Fund RIA – FinCEN IA Rule Ready (Effective Jan 1, 2028)")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Annual Risk Assessment",
    "2. Enhanced Due Diligence (EDD)",
    "3. Training",
    "4. Independent Testing",
    "5. CIP / KYC / CDD / SAR / Monitoring"
])

with tab1:
    st.subheader("Annual AML Risk Assessment")
    st.markdown("**Pillar 1** – Risk-Based Approach")

    st.markdown("""
    **FinCEN IA Rule Requirement**:  
    The AML program must include a risk-based assessment of the money laundering and terrorist financing risks presented by the adviser’s business, clients, products, and geographic exposure.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Inherent Risk Factors")
        investor_risk = st.slider("Investor Base Risk (PEPs, high-net-worth, non-U.S., funds-of-funds)", 1, 10, 5, help="Higher score = higher risk")
        product_risk = st.slider("Product / Strategy Risk (illiquid assets, derivatives, side pockets)", 1, 10, 6)
        geo_risk = st.slider("Geographic / Sanctions Risk", 1, 10, 4)

    with col2:
        st.markdown("### Control Effectiveness")
        control_strength = st.slider("Overall Control Strength (screening, monitoring, training)", 1, 10, 7)
        third_party = st.slider("Third-party (admin, prime broker) oversight", 1, 10, 8)

    # Calculate scores
    inherent_risk = round((investor_risk + product_risk + geo_risk) / 3, 1)
    residual_risk = round(inherent_risk - (control_strength / 2), 1)

    risk_level = "🔴 HIGH" if residual_risk >= 8 else "🟠 MEDIUM" if residual_risk >= 5 else "🟢 LOW"

    st.metric("**Residual Risk Score**", f"{residual_risk} {risk_level}", f"Inherent Risk: {inherent_risk}")

    st.divider()

    # Risk Assessment Summary Table
    st.subheader("Risk Assessment Summary")
    data = {
        "Category": ["Investor Base", "Product/Strategy", "Geographic/Sanctions", "Inherent Risk", "Control Effectiveness", "Residual Risk"],
        "Score": [investor_risk, product_risk, geo_risk, inherent_risk, control_strength, residual_risk],
        "Notes": ["", "", "", "", "", ""]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True)

    # Downloadable Risk Assessment Report
    if st.button("📄 Generate & Download Risk Assessment Report (for Audit)"):
        report_content = f"""
AML / BSA Annual Risk Assessment Report
Firm: [Your Hedge Fund Group Name] – $1B AUM RIA
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Prepared by: {st.session_state.get('name', 'CCO')}

INHERENT RISK FACTORS
• Investor Base Risk: {investor_risk}/10
• Product / Strategy Risk: {product_risk}/10
• Geographic / Sanctions Risk: {geo_risk}/10
→ Inherent Risk Score: {inherent_risk}

CONTROL EFFECTIVENESS
• Overall Controls: {control_strength}/10
• Third-Party Oversight: {third_party}/10

RESIDUAL RISK SCORE: {residual_risk} ({risk_level})

Risk Rating: {risk_level}
Recommendation: {'Enhanced controls and senior management review required.' if residual_risk >= 8 else 'Standard controls sufficient.' if residual_risk >= 5 else 'Low risk – routine monitoring sufficient.'}
        """

        # Generate PDF and offer download
        pdf_path = f"reports/AML_Risk_Assessment_{datetime.now().strftime('%Y%m%d')}.pdf"
        # You can call your existing generate_pdf_from_markdown function here
        # For now, we simulate with a download button
        st.download_button(
            label="⬇️ Download Risk Assessment Report (PDF Ready)",
            data=report_content,
            file_name=f"AML_Risk_Assessment_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )
        st.success("Risk Assessment Report generated. Ready for audit and DocuSign signature.")

        log_audit_trail(st.session_state.username, "AML Risk Assessment Completed", f"Residual Risk: {residual_risk} ({risk_level})", "Unknown")
        log_attestation(st.session_state.username, "Annual AML Risk Assessment")

    st.info("**Best Practice**: Save this assessment annually and present to senior management / Board.")

with tab2:
    st.subheader("Enhanced Due Diligence (EDD) Procedures")
    # (Your existing EDD content can stay here)

with tab3:
    st.subheader("Pillar 3 – Ongoing Training")
    st.info("Complete AML/BSA training in the Training Center.")
    st.page_link("pages/03_Training.py", label="Go to Training Center →", icon="📚")

with tab4:
    st.subheader("Pillar 4 – Independent Testing & Audit")
    st.write("Annual independent test required.")

with tab5:
    st.subheader("Pillar 5 – CIP / KYC / CDD / SAR / Monitoring")
    st.info("CIP, KYC, CDD, SAR, and transaction monitoring tools are available here.")

st.sidebar.info("BSA Officer: Chief Compliance Officer\nAll risk assessments are logged for audit purposes.")