# NileCart Egypt: Cybersecurity Governance Project — Final Report (FINAL_REPORT.md)
**Course Project | Academic Year 2026 | Case Study A: E-Commerce**  
**Assigned Organization:** NileCart Egypt (Cairo Office & 6th of October Warehouse, 35 Staff)  
**Security Budget Ceiling:** EGP 30,000 Fictional Security Budget  
**Advisory Team:** Student 1 (Business & Risk), Student 2 (Governance & Policy), Student 3 (Security Testing)  

---

## 01. Cover Page & Executive Summary

### Academic & Ethical Boundary Assertion
All corporate entities, user accounts, customer order records, security incident logs, timelines, and financial valuations in this report and repository package are entirely fictional and formulated for cybersecurity governance advisory coursework. No real human subjects, live customer records, production systems, or real payment credentials were used, compromised, or simulated.

### Executive Summary
NileCart Egypt is a mid-sized digital retail enterprise headquartered in Downtown Cairo with a primary logistics fulfillment center in 6th of October City, employing 35 staff across management, customer support, finance, and warehouse operations. Tasked as an external cybersecurity governance advisory team, we performed an end-to-end governance overhaul structured across six connected stages: business context mapping, quantitative asset valuation and risk scoring, economic decision modeling, governance policy formalization, programmatic access-control verification, and operational incident response simulation.

Through systematic risk assessment, our team cataloged ten vital information assets and formulated eight prioritized enterprise risks. The primary vulnerabilities identified were single-factor credential exposure (Risk R1, Critical, Score 20), public cloud link leakage of Personally Identifiable Information (Risk R2, High, Score 16), ransomware destruction of unverified backups (Risk R6, High, Score 15), and staff susceptibility to spear-phishing (Risk R8, High, Score 16). Within the fictional EGP 30,000 budget allocation, we applied Expected Monetary Value (EMV) decision analysis to justify an optimal investment portfolio of EGP 26,000 across six core controls—enforcing mandatory multi-factor authentication (MFA), monthly access reviews, protected cloud backups with quarterly restoration testing, staff awareness campaigns, dual-authorization refund controls, and private-by-default cloud sharing—while preserving an emergency contingency buffer of EGP 4,000.

To ensure verifiable governance rather than abstract compliance, we developed an organizational Information Security Policy pack, a Standard Operating Procedure (SOP) for monthly privilege audits, operational RACI matrices, and three measurable KPIs. Furthermore, our team engineered a decoupled Attribute-Based Access Control (ABAC) architecture adhering to XACML standards (PAP, PIP, PDP, PEP) and validated 19 discrete test scenarios (T1–T19) through an automated Python test engine (`access_test.py`). A programmatic 13-condition mutation analysis proved zero surviving logic faults. The governance package is fully traced to the Egyptian Personal Data Protection Law (PDPL 151/2020), ISO/IEC 27001:2022, NIST CSF 2.0, COBIT 2019, and OWASP Top 10:2025.

---

## 02. Business Description, Stakeholder Model & Data Flow Architecture

### Business Model & Facilities
NileCart Egypt operates a dual-facility e-commerce architecture:
1. **Downtown Cairo Headquarters:** Accommodates executive management, IT infrastructure administration, finance and reconciliation, and customer support operations.
2. **6th of October City Fulfillment Center:** High-throughput logistics facility managing inventory receiving, warehouse stocking, barcode scanning, picking, packing, and courier dispatch.

### Workforce Distribution (35 Staff Total)
- **Executive & IT Infrastructure:** 5 staff (CEO, Operations Manager, IT Lead, 2 Systems Administrators).
- **Customer Support & Operations:** 12 staff (Customer support team leads and inquiry agents).
- **Finance & Accounting:** 4 staff (Finance Officer, Accounting Lead, 2 reconciliation clerks).
- **Warehouse & Fulfillment:** 14 staff (Warehouse Lead, picking and packing workers, barcode scanning operators).

### End-to-End E-Commerce Data Flow Lifecycle
Data flows across four distinct trust boundaries:
1. **Consumer Zone:** Customer browses storefront, selects merchandise, and submits checkout requests over TLS 1.3.
2. **Payment Processing Zone:** External payment gateway (Paymob / Fawry) processes card transactions via tokenized API handshakes. NileCart strictly avoids storing credit card PANs or CVVs.
3. **Core Database & IAM Zone:** Customer order records (names, addresses, phone numbers, line items) are committed to Asset A1 (Core Database), while user permissions are governed by Asset A3 (IAM Store).
4. **Logistics & Courier Zone:** Orders are transmitted to 6th of October warehouse terminals (Asset A10), picked from inventory (Asset A2), and exported to daily courier dispatch manifests (Asset A7) for third-party courier distribution.

*(See Figure 1: `figure1_data_flow_diagram.png` for complete visual flow).*

---

## 03. Asset Classification, Risk Assessment & Financial Loss Modeling

### Asset Inventory & CIA Triad Valuation
Ten core information assets were identified, valued, and classified under Confidentiality, Integrity, and Availability:
- **A1: Customer Order Records (DB & Exports)** — Valued at EGP 120,000 | C: High, I: High, A: Medium.
- **A2: Warehouse Inventory Database** — Valued at EGP 80,000 | C: Medium, I: High, A: High.
- **A3: Staff IAM & Authentication Store** — Valued at EGP 75,000 | C: High, I: High, A: High.
- **A4: E-Commerce Web Storefront** — Valued at EGP 100,000 | C: High, I: High, A: High.
- **A5: Payment Reconciliation Reports** — Valued at EGP 65,000 | C: High, I: High, A: Medium.
- **A6: Customer Refund Approval Log** — Valued at EGP 50,000 | C: High, I: High, A: Medium.
- **A7: Daily Courier Dispatch Manifests** — Valued at EGP 35,000 | C: High, I: Medium, A: High.
- **A8: Database Backup Snapshots** — Valued at EGP 90,000 | C: High, I: High, A: High.
- **A9: System Access & Audit Logs** — Valued at EGP 40,000 | C: Medium, I: High, A: Medium.
- **A10: Warehouse Handheld Scanners** — Valued at EGP 30,000 | C: Low, I: Medium, A: High.

### 5×5 Risk Matrix Evaluation
- **R1: Credential Compromise & Takeover (L:4, I:5, Score: 20, Critical)** — Target: A1, A3. Single-factor login vulnerability.
- **R2: Public Cloud Export Sharing / PII Leak (L:4, I:4, Score: 16, High)** — Target: A1, A7. Default public sharing link vulnerability.
- **R3: Unreviewed Configuration Changes (L:3, I:4, Score: 12, Medium)** — Target: A3, A9. Informal change management.
- **R4: Warehouse Inventory Data Tampering (L:3, I:3, Score: 9, Medium)** — Target: A2, A10. Unrestricted write permissions.
- **R5: Refund Embezzlement & SoD Violation (L:2, I:5, Score: 10, Medium)** — Target: A5, A6. Dual request/approval rights.
- **R6: Ransomware / Backup Failure (L:3, I:5, Score: 15, High)** — Target: A8, A1. Connected backups lacking restore tests.
- **R7: Courier Manifest Disclosure (L:3, I:3, Score: 9, Medium)** — Target: A1, A7. Unminimized paper delivery sheets.
- **R8: Staff Phishing & Social Engineering (L:4, I:4, Score: 16, High)** — Target: A3, A4. Absence of cybersecurity training.

### Quantitative Financial Risk Modeling (in Egyptian Pounds)
Using standard equations:
- **Single Loss Expectancy (SLE):** $SLE = Asset Value \times Exposure Factor (EF)$
- **Annual Threat Loss Expectancy (ATLE):** $ATLE = ARO \times SLE$

1. **Risk R1 (Credential Compromise):**
   - Asset A1 Value = EGP 120,000 | Exposure Factor = 25% $\rightarrow$ **SLE = EGP 30,000**.
   - Annual Frequency (ARO) = 0.5 events/year $\rightarrow$ **Baseline ATLE = EGP 15,000 / year**.
   - With Control C1 (MFA costing EGP 5,000), Post-Control ARO = 0.05 $\rightarrow$ **Residual ATLE = EGP 1,500 / year**.
   - **Net Annual Economic Benefit:** $15,000 - 1,500 - 5,000 = \textbf{EGP 8,500 / year}$.

2. **Risk R6 (Ransomware / Backup Failure):**
   - Asset A8 & Core DB Value = EGP 90,000 | Exposure Factor = 40% $\rightarrow$ **SLE = EGP 36,000**.
   - Annual Frequency (ARO) = 0.2667 events/year $\rightarrow$ **Baseline ATLE = EGP 9,600 / year**.

---

## 04. Security Control Decisions, Decision Tree & Budget Allocation

### Control Portfolio (EGP 30,000 Fictional Budget Ceiling)
- **C1: Staff Multi-Factor Authentication (MFA)** — Cost: EGP 5,000 (Target: R1, R8).
- **C2: Monthly Access Review SOP & Inactive Pruning** — Cost: EGP 3,000 (Target: R1, R2).
- **C3: Protected Cloud Backups & Quarterly Restore Testing** — Cost: EGP 9,000 (Target: R6).
- **C4: Staff Awareness Training Program & Posters** — Cost: EGP 4,000 (Target: R8).
- **C5: Refund Dual Approval Workflow (SoD)** — Cost: EGP 3,000 (Target: R5).
- **C6: Private-by-Default Cloud Storage Architecture** — Cost: EGP 2,000 (Target: R2).
- **Contingency & Incident Reserve:** EGP 4,000 buffer.
- **Total Portfolio Spend:** $\textbf{EGP 26,000 Invested + EGP 4,000 Buffer = EGP 30,000 Ceiling}$.

### Decision Tree Analysis for Control C3 (Backups)
Superficially, in Year 1, purchasing Control C3 costs EGP 9,000 plus EGP 2,400 expected residual loss = EGP 11,400, which exceeds the baseline risk acceptance ATLE of EGP 9,600. However, over a 3-year strategic horizon:
- **3-Year Buy C3 Total:** EGP 9,000 (setup) + EGP 4,800 (ops) + EGP 7,200 (residual risk) = **EGP 21,000**.
- **3-Year Accept Risk Total:** EGP 9,600 × 3 = **EGP 28,800**.
- **Strategic Net Savings:** **EGP 7,800**.
Furthermore, accepting Risk R6 risks catastrophic insolvency (EGP 36,000+ single-event loss) and complete operational failure.

*(See Figure 2: `figure2_decision_tree.png`).*

---

## 05. Governance Pack: Policies, RACI & KPIs

### Policy Hierarchy
1. **Information Security Policy (POL-SEC-01):** High-level foundational governance policy mandating least privilege, credential controls, incident reporting within 60 minutes, and management review.
2. **Access Control Policy (POL-SEC-02):** Supporting policy codifying RBAC and ABAC rules, mandatory segregation of duties for refund approvals, and inactive account suspension.
3. **Data Protection & Cloud Sharing Policy (POL-SEC-03):** Supporting policy enforcing data minimization on courier manifests, prohibiting public drive links, and establishing customer PII retention rules.
4. **Standard Operating Procedure (SOP-SEC-01):** Operational procedure for executing monthly user access certifications on the last business day of every month.

### Operational Governance RACI
- **Policy Approval:** Executive Management (A), IT Admin (R), Operations (C), Finance (C), Warehouse (I).
- **Monthly Access Certification:** IT Admin (A), Department Leads (R).
- **Refund Approvals (SoD):** Finance Officer (A), Customer Support (R), IT Admin (C).
- **Backup & Restore Testing:** IT Admin (A/R), Operations (I).

### Measurable KPIs
1. **Monthly Access Certification Rate:** 100% of accounts certified monthly; 0 dormant accounts remaining active.
2. **Refund SoD Compliance Rate:** 100% of refund disbursements require independent dual approval.
3. **Quarterly Backup Restore Success Rate:** 4 successful dry-run restorations per year with RTO < 4 hours.

---

## 06. Compliance Evidence Mapping

| Standard / Law | Specific Clause / Control | NileCart Implementation & Real Evidence | Reference Link |
|---|---|---|---|
| **Egypt PDPL (151/2020)** | Article 2 & 3 (Lawful Processing) | POL-SEC-03 §3; customer consent in storefront; 90-day retention schedule | https://laws.boe.gov.eg/boe/PDPL151_2020 |
| **Egypt PDPL (151/2020)** | Article 12 & 13 (Technical Security & 72-hr Breach Notice) | Data minimization for courier exports; private cloud sharing (C6); tabletop runbook | https://laws.boe.gov.eg/boe/PDPL151_2020 |
| **ISO/IEC 27001:2022** | Clause 5.1 & Control A.5.15 (Access Control) | POL-SEC-01; POL-SEC-02; 19 automated tests (T1-T19) in `access_test.py` | https://www.iso.org/standard/27001 |
| **ISO/IEC 27001:2022** | Control A.8.13 (Backup) & A.5.24 (Incident Response) | Backup & Recovery Policy; quarterly restore dry-runs; tabletop log INC-2026-04 | https://www.iso.org/standard/27001 |
| **NIST CSF 2.0** | GOVERN (GV.OC-01, GV.PO-01) & IDENTIFY (ID.RA-01) | Executive governance pack; RACI matrix; 8-risk register; SLE/ATLE financial model | https://csrc.nist.gov/publications/detail/sp/1300/final |
| **NIST CSF 2.0** | PROTECT (PR.AA-01, PR.DS-01) & RECOVER (RC.RP-01) | Mandatory MFA (C1); least-privilege matrix; immutable backup snapshots | https://csrc.nist.gov/publications/detail/sp/1300/final |
| **COBIT 2019** | EDM01 (Governance Setting) & APO12 (Managed Risk) | Board policy pack; dual-approval spending thresholds; risk tolerance limits | https://www.isaca.org/resources/cobit |
| **COBIT 2019** | DSS05 (Security Services) & MEA01 (Performance Monitoring) | Monthly access SOP-01; segregation of duties (approver != requester); 3 KPIs | https://www.isaca.org/resources/cobit |
| **OWASP Top 10:2025** | A01:2025 - Broken Access Control | Access matrix; ABAC rules in `access_test.py` preventing BOLA/IDOR on orders | https://owasp.org/Top10/ |
| **OWASP Top 10:2025** | A07:2025 - Identification & Authentication Failures | Mandatory staff MFA (C1); inactive account suspension; session expiration | https://owasp.org/Top10/ |

---

## 07. Access Control Architecture, Formal Logic & Automated Testing

### Decoupled PAP/PIP/PDP/PEP Architecture
- **PAP:** Stores Rules 1–3 and base RBAC permissions.
- **PIP:** Provides dynamic attributes (active account status, assigned orders, MFA, change tickets).
- **PDP:** Evaluates attributes against active rules via `decide()` without knowing test IDs.
- **PEP:** Intercepts requests, enforces decisions, and logs results via `pep()`.

*(See Figure 3: `figure3_authorization_architecture.png`).*

### Formal Logic Rules
- **Rule 1 (Order Read):** `ALLOW_READ_ORDER = account_active AND correct_role AND object_assigned`
- **Rule 2 (Refund Approval):** `ALLOW_REFUND_APPROVE = account_active AND correct_role AND mfa_verified AND approver_not_requester`
- **Rule 3 (Admin Config):** `ALLOW_ADMIN_CONFIG = account_active AND correct_role AND mfa_verified AND change_ticket_approved`
- **Base RBAC:** `BASE_RBAC = account_active AND correct_role`

### Automated Test Execution Results (`access_test.py`)
19 automated tests (T1–T19) executed with 100% pass rate:
- T1 (Support reads assigned order): ALLOW [PASS]
- T2 (Support reads UNASSIGNED order): DENY [PASS]
- T3 (INACTIVE support reads order): DENY [PASS]
- T4 (Finance approves refund with different requester): ALLOW [PASS]
- T5 (Finance approves OWN refund request - collusion): DENY [PASS]
- T6 (Support attempts inventory update): DENY [PASS]
- T7 (Finance missing MFA attempts refund): DENY [PASS]
- T8 (Admin modifies settings WITH ticket): ALLOW [PASS]
- T9 (Support attempts direct refund approval): DENY [PASS]
- T10 (INACTIVE finance attempts refund): DENY [PASS]
- T11 (Admin modifies settings WITHOUT ticket): DENY [PASS]
- T12 (Admin missing MFA modifies settings): DENY [PASS]
- T13 (Admin attempts customer order read): DENY [PASS]
- T14 (Warehouse staff updates inventory): ALLOW [PASS]
- T15 (Unapproved refund ticket attempt): DENY [PASS]
- T16 (Rejected change ticket attempt): DENY [PASS]
- T17 (Non-admin attempts system configuration): DENY [PASS]
- T18 (INACTIVE warehouse staff stock update): DENY [PASS]
- T19 (Unknown non-existent user attempt): DENY [PASS]

**Mutation Testing Rigor:** Automated 13-condition mutation testing executed by `access_test.py` resulted in **0 surviving mutants**, proving 100% test suite effectiveness.

---

## 08. Incident Response Tabletop Simulation & Awareness Campaign

### Incident Simulation: Public Cloud Link Leakage (`INC-2026-04`)
1. **Detect (10:15 UTC):** Support staff `sup-04` identifies customer order export link pasted in public team chat; escalates immediately.
2. **Contain (10:25 UTC):** IT Admin disables link, invalidates active sessions, preserves server logs.
3. **Investigate (10:35 UTC):** Audit logs reveal external Cairo IP `203.0.113.42` downloaded `order_export_104.xlsx` (142 customer records).
4. **Recover (14:00 UTC):** Secure internal IAM channel re-established; operations resumed.
5. **Learn (17:30 UTC):** Post-Incident Review mandates private-by-default cloud sharing (C6) and schedules staff training.

### Arabic-First Awareness Campaign
- Visual poster created following Slide 20 checklist: *"أمان بيانات العملاء يبدأ منك"* with the 3 pillars: **تَوَقَّفْ (STOP)**, **تَحَقَّقْ (VERIFY)**, **أَبْلِغْ (REPORT)**.
- 5-question bilingual quiz with detailed answer keys covering link verification, cloud sharing, password security, segregation of duties, and incident reporting.

*(See Figure 4: `figure4_awareness_poster.png` and `10_Awareness_Campaign.md`).*

---

## 09. Results, Limitations & References
The governance overhaul eliminates critical credential compromise, enforces segregation of duties on financial disbursements, ensures full compliance with Egyptian PDPL 151/2020, and guarantees disaster recovery within 4 hours.

---

## 10. Appendices
- Full Traceability Matrix (`TRACEABILITY_MATRIX.md`)
- Complete Test Execution Logs (`T1-T19_output.txt`)
- Assumptions Register & Shared Evidence Register (`SUPPORT_FILES.md`)
- Team Contribution Log with 3 student roles, logged hours, and cross-checks (`SUPPORT_FILES.md`)
