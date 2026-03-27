import streamlit as st
from datetime import datetime
from database import log_audit_trail

st.title("🔍 SEC Exam Prep & Mock Audit Tool")
st.caption("2026 Division of Examinations Priorities – $1B AUM Hedge Fund RIA")

st.markdown("### 2026 SEC Examination Priorities Checklist")
st.info("Use this tool to assess your firm's readiness for SEC exams. Document your status and remediation plans.")

priorities = {
    "Fiduciary Duty & Conflicts of Interest": {
        "description": "Duty of care and loyalty, full and fair disclosure of conflicts, best execution, fair allocation of opportunities.",
        "status": st.selectbox("Status", ["Fully Compliant", "Partially Compliant", "Needs Improvement", "Not Reviewed"], key="fiduciary"),
        "notes": st.text_area("Notes / Remediation", key="fiduciary_notes", height=80)
    },
    "Marketing Rule Compliance (Rule 206(4)-1)": {
        "description": "Fair and balanced communications, substantiation of claims, testimonials/endorsements disclosures, hypothetical performance policies.",
        "status": st.selectbox("Status", ["Fully Compliant", "Partially Compliant", "Needs Improvement", "Not Reviewed"], key="marketing"),
        "notes": st.text_area("Notes / Remediation", key="marketing_notes", height=80)
    },
    "Reg S-P & Cybersecurity (Safeguards Rule)": {
        "description": "Written Information Security Program (WISP), incident response (30-day notification), vendor oversight (72-hour reporting), annual testing.",
        "status": st.selectbox("Status", ["Fully Compliant", "Partially Compliant", "Needs Improvement", "Not Reviewed"], key="regsp"),
        "notes": st.text_area("Notes / Remediation", key="regsp_notes", height=80)
    },
    "AI Supervision & Governance": {
        "description": "Supervision of AI tools, testing for bias/explainability/drift, accurate representations (no 'AI washing'), human oversight, disclosures in Form ADV.",
        "status": st.selectbox("Status", ["Fully Compliant", "Partially Compliant", "Needs Improvement", "Not Reviewed"], key="ai"),
        "notes": st.text_area("Notes / Remediation", key="ai_notes", height=80)
    },
    "Private Fund Risks": {
        "description": "Valuation of illiquid assets, liquidity management, side letters/preferential treatment, fee/expense allocation, side-by-side management conflicts.",
        "status": st.selectbox("Status", ["Fully Compliant", "Partially Compliant", "Needs Improvement", "Not Reviewed"], key="privatefund"),
        "notes": st.text_area("Notes / Remediation", key="privatefund_notes", height=80)
    },
    "Books & Records / Form ADV & Form PF Accuracy": {
        "description": "Complete and accurate disclosures, timely filings, retention policies (5 years), consistency between marketing and regulatory filings.",
        "status": st.selectbox("Status", ["Fully Compliant", "Partially Compliant", "Needs Improvement", "Not Reviewed"], key="books"),
        "notes": st.text_area("Notes / Remediation", key="books_notes", height=80)
    }
}

st.divider()

overall_score = 0
for priority, data in priorities.items():
    with st.expander(f"{priority} - {data['status']}", expanded=False):
        st.write(data["description"])
        st.write(f"**Current Status**: {data['status']}")
        st.write(f"**Notes**: {data['notes'] if data['notes'] else 'No notes entered'}")
        
        if data['status'] == "Fully Compliant":
            overall_score += 100
        elif data['status'] == "Partially Compliant":
            overall_score += 60
        elif data['status'] == "Needs Improvement":
            overall_score += 30

avg_score = round(overall_score / len(priorities), 1)

st.metric("Overall Exam Readiness Score", f"{avg_score}%", 
          "Strong" if avg_score >= 85 else "Moderate" if avg_score >= 65 else "Needs Significant Improvement")

if st.button("Generate Mock Audit Report & Sign-off"):
    report_content = f"""
SEC 2026 Exam Prep Report
Firm: [Your Hedge Fund Group Name] – $1B AUM RIA
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Prepared by: {st.session_state.get('name', 'CCO')}

Overall Readiness Score: {avg_score}%

Detailed Assessment:
"""
    for priority, data in priorities.items():
        report_content += f"\n• {priority}: {data['status']}\n  Notes: {data['notes'] or 'None'}\n"

    st.success("Mock Audit Report generated successfully!")
    st.download_button(
        label="⬇️ Download Report",
        data=report_content,
        file_name=f"SEC_Exam_Prep_Report_{datetime.now().strftime('%Y%m%d')}.txt",
        mime="text/plain"
    )
    
    log_audit_trail(
        st.session_state.get("username", "Unknown"),
        "SEC Exam Prep Report Generated",
        f"Overall Score: {avg_score}%",
        "Unknown"
    )

st.info("""
**2026 SEC Examination Priorities Summary**:
- Focus on fiduciary duty, conflicts, and best execution
- Marketing Rule compliance and substantiation of claims
- Reg S-P incident response and cybersecurity governance
- Supervision of AI tools and prevention of "AI washing"
- Private fund risks including valuation, liquidity, and preferential treatment
""")

st.caption("Use this tool regularly to maintain exam readiness. All reports are logged in the audit trail.")