import streamlit as st
from datetime import datetime
from database import log_audit_trail, log_attestation

st.title("AML / BSA 5-Pillar Program + CFIUS, FOCI & Export Controls")
st.caption("$1B AUM Hedge Fund RIA – FinCEN IA Rule + National Security Requirements")

st.info("""
**FinCEN IA Rule Summary**  
Effective Date: **January 1, 2028**  
Requires a risk-based AML program with 5 pillars: written policies, BSA Officer, training, independent testing, and customer due diligence.
""")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1. Risk Assessment",
    "2. Enhanced Due Diligence (EDD)",
    "3. Training",
    "4. Independent Testing",
    "5. CIP / KYC / CDD / SAR / CTR / UBO / PEP",
    "6. CFIUS, FOCI & Export Controls"
])

with tab1:
    st.subheader("Annual AML Risk Assessment")
    st.markdown("**Pillar 1** – Risk-Based Approach")
    st.info("Complete the assessment below. Inherent Risk is calculated from all categories. Residual Risk is adjusted for mitigation strength.")

    # Products and Services
    st.write("### Products and Services")
    products = [
        "Automated Clearing House transactions", "Brokered deposits", "Bulk shipments of currency",
        "Concentration accounts", "Correspondent Accounts (Domestic)", "Correspondent Accounts (Foreign)",
        "Electronic banking", "Foreign exchange", "Funds transfers", "Insurance", "Lending Activities",
        "Nondeposit investment products", "Payable through accounts", "Pouch activities", "Prepaid access",
        "Private banking", "Privately owned automated teller machines", "Purchase and sale of monetary instruments",
        "Third-party payment processors", "Trade finance activities", "Trust and asset management services",
        "U.S. dollar drafts"
    ]
    product_risks = {}
    for p in products:
        product_risks[p] = st.selectbox(f"{p}", ["Low", "Moderate", "High"], key=f"prod_{p}")

    # Customers and Entities
    st.write("### Customers and Entities")
    customers = [
        "Cash-intensive businesses", "Customer Base Growth", "Employee Turnover", "Deposit brokers",
        "Foreign corporations and domestic business entities", "Foreign Deposit Brokers", "Foreign financial institutions",
        "Nonbank financial institutions", "Nongovernmental organizations and charities", "Nonresident Alien",
        "Politically Exposed Persons", "Professional Service Providers"
    ]
    customer_risks = {}
    for c in customers:
        customer_risks[c] = st.selectbox(f"{c}", ["Low", "Moderate", "High"], key=f"cust_{c}")

    # Geography
    st.write("### Geography")
    geographies = [
        "Countries identified as supporting international terrorism",
        "Countries subject to OFAC sanctions",
        "Domestic higher-risk geographies (HIDTA/HIFCA)",
        "Jurisdictions determined to be of primary money laundering concern",
        "Jurisdictions monitored for AML deficiencies",
        "Major money laundering countries",
        "Offshore financial centers"
    ]
    geo_risks = {}
    for g in geographies:
        geo_risks[g] = st.selectbox(f"{g}", ["Low", "Moderate", "High"], key=f"geo_{g}")

    # Delivery Channel Risks
    st.write("### Delivery Channel Risks")
    delivery_channels = [
        "Online / Internet banking", "Mobile banking / apps", "ATM / ITM", "Branch / In-person services",
        "Telephone banking", "Third-party payment processors", "Correspondent banking channels"
    ]
    delivery_risks = {}
    for d in delivery_channels:
        delivery_risks[d] = st.selectbox(f"{d}", ["Low", "Moderate", "High"], key=f"del_{d}")

    # Refined Risk Calculation
    all_risks = list(product_risks.values()) + list(customer_risks.values()) + list(geo_risks.values()) + list(delivery_risks.values())
    high_count = all_risks.count("High")
    moderate_count = all_risks.count("Moderate")
    inherent_score = round((high_count * 3 + moderate_count * 2 + (len(all_risks) - high_count - moderate_count) * 1) / max(len(all_risks), 1), 1)

    mitigation_strength = st.selectbox("Overall Strength of Mitigation/Controls", ["Weak", "Satisfactory", "Strong"])
    
    if mitigation_strength == "Strong":
        residual_risk = round(inherent_score * 0.4, 1)
    elif mitigation_strength == "Satisfactory":
        residual_risk = round(inherent_score * 0.7, 1)
    else:
        residual_risk = inherent_score

    risk_level = "🔴 HIGH" if residual_risk >= 8 else "🟠 MEDIUM" if residual_risk >= 5 else "🟢 LOW"

    st.metric("Inherent Risk Score", inherent_score)
    st.metric("Residual Risk After Mitigation", f"{residual_risk} {risk_level}")

    if st.button("📄 Generate & Download Risk Assessment Report for Audit"):
        report = f"""
AML / BSA Annual Risk Assessment Report
Firm: Your Hedge Fund Group – $1B AUM RIA
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Prepared by: {st.session_state.get('name', 'CCO')}

INHERENT RISK SUMMARY
Overall Inherent Risk Score: {inherent_score}

MITIGATION SUMMARY
Strength of Controls: {mitigation_strength}
Residual Risk Level: {residual_risk} ({risk_level})

Full category details and raw inputs are available in the portal for audit purposes.
        """

        st.download_button(
            label="⬇️ Download Audit-Ready Risk Assessment Report",
            data=report,
            file_name=f"AML_Risk_Assessment_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )
        st.success("Report generated successfully.")
        log_audit_trail(st.session_state.username, "AML Risk Assessment Completed", f"Residual Risk: {residual_risk}", "Unknown")
        log_attestation(st.session_state.username, "Annual AML Risk Assessment")

with tab2:
    st.subheader("Enhanced Due Diligence (EDD) Procedures")
    st.markdown("**Pillar 2 & 5** – Applied when risk is elevated.")

    st.write("**EDD Triggers (Hedge Fund Specific)**")
    edd_triggers = [
        "Investor or beneficial owner is a PEP or close associate",
        "Investor resides in or funds originate from high-risk jurisdiction",
        "Investment > $5M or >10% of fund AUM",
        "Complex corporate/trust structure with unidentified beneficial owners",
        "Unusual transaction patterns (rapid inflows + early redemptions)",
        "Requests for preferential treatment via side letters",
        "Negative adverse media or sanctions hits",
        "Source of funds/wealth unclear or inconsistent with profile"
    ]
    for trigger in edd_triggers:
        st.checkbox(trigger)

    st.write("**Required EDD Procedures**")
    edd_procedures = [
        "In-depth Source of Wealth verification",
        "Full Beneficial Ownership mapping",
        "Enhanced adverse media & sanctions screening",
        "Senior management approval via DocuSign",
        "Enhanced ongoing monitoring (monthly reviews)",
        "All documentation retained for 5 years"
    ]
    for procedure in edd_procedures:
        st.checkbox(procedure, value=True)

with tab3:
    st.subheader("Pillar 3 – Ongoing Training")
    st.info("Complete the AML/BSA 5-Pillar Training in the Training Center.")
    st.page_link("pages/03_Training.py", label="Go to Training Center →", icon="📚")

with tab4:
    st.subheader("Pillar 4 – Independent Testing & Audit")
    st.write("Annual independent test of all 5 pillars required.")

with tab5:
    st.subheader("Pillar 5 – CIP / KYC / CDD / SAR / CTR / UBO / PEP")

    sub1, sub2, sub3, sub4, sub5 = st.tabs(["CIP & KYC", "CDD Form", "SAR & CTR Filing", "UBO Verification Tool", "PEP Screening Tool"])

    with sub1:
        st.subheader("CIP & KYC Onboarding")
        st.write("**CIP Requirements**: Name, DOB/formation date, address, TIN, photo ID verification.")
        with st.form("cip_form"):
            name = st.text_input("Investor Name")
            if st.form_submit_button("Complete CIP/KYC & Sign"):
                st.success(f"CIP/KYC completed for {name}.")
                log_audit_trail(st.session_state.username, "CIP/KYC Completed", f"Investor: {name}", "Unknown")

    with sub2:
        st.subheader("Customer Due Diligence (CDD) Form")
        with st.form("cdd_form"):
            investor = st.text_input("Investor Name")
            amount = st.number_input("Investment Amount ($)", min_value=0)
            if st.form_submit_button("Submit CDD & Sign"):
                st.success(f"CDD submitted for {investor}.")
                log_audit_trail(st.session_state.username, "CDD Submitted", f"Investor: {investor}", "Unknown")

    with sub3:
        st.subheader("SAR & CTR Filing Procedures")

        st.markdown("**SAR Filing Procedures**")
        st.write("1. Identify suspicious activity")
        st.write("2. Document facts")
        st.write("3. Escalate to BSA Officer within **24 hours**")
        st.write("4. File SAR with FinCEN within **30 days** (60 days if no suspect)")
        st.warning("**No tipping-off**: Never inform the subject.")

        with st.form("sar_form"):
            suspect = st.text_input("Suspect Name / Entity")
            desc = st.text_area("Description of Suspicious Activity")
            reason = st.selectbox("Primary Reason", ["Structuring", "Unusual wire activity", "Inconsistent with strategy", "PEP involvement", "High-risk jurisdiction"])
            if st.form_submit_button("Log & Escalate SAR"):
                st.success(f"SAR for **{suspect}** logged and escalated.")
                log_audit_trail(st.session_state.username, "SAR Filed", f"Suspect: {suspect}", "Unknown")

        st.subheader("FinCEN CTR (Currency Transaction Report) Procedures")
        st.markdown("""
        **CTR Aggregation Rules**:
        - File CTR for cash transactions **exceeding $10,000** in a single business day.
        - **Aggregation**: Multiple cash transactions by or on behalf of the same person in one business day are combined if they total $10,000 or more.
        - Filing deadline: **15 calendar days** after the transaction date.
        """)

        with st.form("ctr_form"):
            ctr_amount = st.number_input("Individual Cash Transaction Amount ($)", min_value=0)
            ctr_date = st.date_input("Transaction Date", value=datetime.now().date())
            ctr_party = st.text_input("Party Involved")
            is_aggregated = st.checkbox("This transaction is part of aggregated daily activity")
            total_aggregated = st.number_input("Total Aggregated Amount Today ($)", min_value=0) if is_aggregated else 0

            if st.form_submit_button("Validate & Log CTR"):
                if (ctr_amount > 10000) or (is_aggregated and total_aggregated > 10000):
                    st.success(f"CTR required for aggregated amount ${max(ctr_amount, total_aggregated):,} – Log for filing within 15 days.")
                    log_audit_trail(st.session_state.username, "CTR Triggered", f"Amount: ${max(ctr_amount, total_aggregated):,}", "Unknown")
                else:
                    st.info("Transaction below CTR threshold – No filing required.")

    with sub4:
        st.subheader("UBO (Ultimate Beneficial Owner) Verification Tool")
        st.markdown("**UBO Threshold**: Identify and verify all individuals who own or control **≥25%** of the entity (FinCEN IA Rule).")

        with st.form("ubo_form"):
            entity_name = st.text_input("Entity Name")
            ubo_name = st.text_input("Ultimate Beneficial Owner Name")
            ownership_pct = st.number_input("Ownership / Control Percentage (%)", min_value=0.0, max_value=100.0, step=0.1)
            verification_method = st.selectbox("Verification Method", ["Government-issued Photo ID", "Corporate Registry Search", "Third-Party Service", "Video Call Verification"])
            if st.form_submit_button("Verify UBO & Sign"):
                if ownership_pct >= 25:
                    st.success(f"UBO **{ubo_name}** ({ownership_pct}%) verified for **{entity_name}**.")
                    log_audit_trail(st.session_state.username, "UBO Verification Completed", f"Entity: {entity_name} | UBO: {ubo_name} ({ownership_pct}%)", "Unknown")
                    log_attestation(st.session_state.username, f"UBO Verification - {entity_name}")
                else:
                    st.info(f"Ownership below 25% threshold – Standard CDD sufficient.")

    with sub5:
        st.subheader("PEP Screening Tool")
        st.write("**PEP Screening** – Politically Exposed Persons require Enhanced Due Diligence.")

        with st.form("pep_form"):
            pep_name = st.text_input("Name / Entity to Screen for PEP Status")
            self_declaration = st.radio("Self-Declared PEP Status?", ["No", "Yes"])
            screening_result = st.selectbox("PEP Screening Result", ["Not a PEP", "Confirmed PEP", "Close Associate of PEP"])
            if st.form_submit_button("Log PEP Screening"):
                st.success(f"PEP screening for **{pep_name}** logged as **{screening_result}**.")
                log_audit_trail(st.session_state.username, "PEP Screening Completed", f"Entity: {pep_name} | Result: {screening_result}", "Unknown")
                if screening_result != "Not a PEP":
                    st.warning("PEP identified – Enhanced Due Diligence (EDD) required.")

with tab6:
    st.subheader("CFIUS & Export Controls Compliance")
    st.markdown("**National Security Requirements**")

    st.write("### CFIUS Compliance")
    st.write("**Key CFIUS Triggers**")
    cfius_triggers = [
        "Foreign investor acquiring control or significant influence",
        "Investment in critical technology",
        "Investment in critical infrastructure",
        "Access to sensitive personal data of U.S. citizens",
        "Foreign government-linked investors"
    ]
    for trigger in cfius_triggers:
        st.checkbox(trigger)

    st.write("**CFIUS Critical Technologies Examples**")
    critical_tech = [
        "Artificial Intelligence and machine learning systems",
        "Semiconductors and semiconductor manufacturing equipment",
        "Quantum computing and quantum information sciences",
        "Biotechnology and biological technologies",
        "Advanced robotics and autonomous systems",
        "Additive manufacturing (3D printing) for defense applications",
        "Advanced materials and metamaterials",
        "Aerospace and defense-related technologies",
        "Nuclear technologies",
        "Encryption and cybersecurity technologies"
    ]
    for item in critical_tech:
        st.checkbox(item)

    st.write("**CFIUS Mitigation Agreements** (when required by CFIUS)")
    st.markdown("CFIUS may require legally binding mitigation agreements to address national security concerns. Common mitigation strategies include:")
    mitigation = [
        "Establish a U.S.-based security committee with independent directors to oversee sensitive operations",
        "Appoint a CFIUS-approved security officer with veto rights over decisions involving critical technology or data",
        "Implement strict information security protocols, including data segregation and access controls",
        "Limit foreign investor access to critical technology, intellectual property, or sensitive personal data",
        "Require prior CFIUS approval for any change in ownership, key personnel, or technology transfers",
        "Undergo regular third-party audits and submit periodic compliance reports to CFIUS",
        "Include termination or divestiture rights if compliance with the mitigation agreement fails",
        "Restrict foreign investor board observer rights or information access rights",
        "Establish physical and logical separation of sensitive U.S. operations from foreign parent entities"
    ]
    for item in mitigation:
        st.checkbox(item, value=True)

    st.write("### Export Controls Compliance (ITAR & EAR)")
    st.write("**Required Procedures**")
    export_controls = [
        "Screen investments for ITAR-controlled defense articles",
        "Screen for EAR-controlled dual-use items and technology",
        "Implement controls to prevent unauthorized export of technical data",
        "Obtain export licenses when required",
        "Include export control clauses in subscription agreements",
        "Train deal teams and compliance staff on export controls"
    ]
    for item in export_controls:
        st.checkbox(item, value=True)

    st.info("**Note**: CFIUS mitigation agreements can significantly impact fund governance and operational flexibility.")

st.sidebar.info("BSA Officer: Chief Compliance Officer\nAll actions are logged with full audit trail.")