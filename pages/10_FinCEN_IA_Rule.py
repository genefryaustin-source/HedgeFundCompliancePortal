import streamlit as st
from datetime import datetime
from database import log_audit_trail

st.title("FinCEN IA AML Rule Overview")
st.caption("Investment Adviser Anti-Money Laundering Program Requirements")

st.markdown("### Current Status (March 2026)")
st.info("""
**Effective Date**: January 1, 2028 (delayed from original January 1, 2026)

FinCEN issued a two-year delay to allow for further review and tailoring of the rule to better fit the diverse business models of investment advisers.
""")

st.subheader("Who Is Covered?")
col1, col2 = st.columns(2)
with col1:
    st.success("**Covered**")
    st.write("- SEC-Registered Investment Advisers (RIAs)")
    st.write("- Exempt Reporting Advisers (ERAs)")
with col2:
    st.error("**Generally Not Covered**")
    st.write("- State-registered advisers")
    st.write("- Foreign private advisers")
    st.write("- Family offices")

st.subheader("Core Requirements – The 5 Pillars")
st.markdown("""
When the rule becomes effective on **January 1, 2028**, covered investment advisers must implement a **risk-based AML/CFT program** with these five pillars:

1. **Written Policies, Procedures, and Internal Controls**  
   Reasonably designed to prevent money laundering and terrorist financing. Must be tailored to the firm’s size, client types, products (e.g., private funds, illiquid assets), and risk profile.

2. **Designation of a BSA Officer**  
   A qualified person (often the CCO or delegate) with sufficient authority and resources to oversee the program.

3. **Ongoing Training**  
   Regular AML training for relevant employees on risks, red flags, and responsibilities.

4. **Independent Testing / Audit**  
   Annual testing of the program’s effectiveness by an independent party (internal audit or qualified third party).

5. **Customer Due Diligence (CDD)**  
   Identify and verify investors and beneficial owners. Includes Enhanced Due Diligence (EDD) for higher-risk clients.
""")

st.subheader("Additional Key Obligations")
st.write("- File **Suspicious Activity Reports (SARs)** with FinCEN")
st.write("- Conduct **OFAC sanctions screening**")
st.write("- Maintain robust **recordkeeping** (generally 5 years)")
st.write("- Implement **transaction monitoring** procedures")

st.subheader("Why This Rule Was Created")
st.info("""
FinCEN’s risk assessment found that the investment adviser sector had been a significant regulatory gap.  
Criminal actors, corrupt officials, sanctioned persons, and nation-state actors have used U.S. private funds and advisers to move illicit funds and acquire sensitive technologies.
""")

st.subheader("How This Portal Supports Compliance")
st.success("""
Your compliance portal already includes strong coverage of the future FinCEN IA Rule requirements:
- 5-Pillar AML/BSA dashboard with risk assessment tool
- Enhanced Due Diligence (EDD) procedures and triggers
- CIP / KYC onboarding forms
- SAR filing workflow and examples
- OFAC & PEP screening tools
- Transaction monitoring rules
- Dedicated training modules
- Full audit trail and reporting
""")

st.info("**Recommendation**: Begin building and testing your AML program now as a best practice. The portal can serve as your central operational and audit tool when the rule takes effect in 2028.")

if st.button("Acknowledge & Log Review"):
    log_audit_trail(
        st.session_state.get("username", "Unknown"),
        "FinCEN IA Rule Review",
        "Reviewed FinCEN IA AML Rule overview and portal coverage",
        "Unknown"
    )
    st.success("Review logged successfully.")

st.sidebar.info("Effective Date: January 1, 2028\nBSA Officer: Chief Compliance Officer")