# Support Files & Registers (SUPPORT_FILES.md)

## A. Assumptions Register
| ID | Assumption | Reason | Impact if Wrong | Owner |
|---|---|---|---|---|
| ASM-01 | Team of 3 students approved by instructor | Course brief specifies team size; NileCart project executed by 3 students | Requires project redistribution or formal exception if team size differs | Student 1 (Risk) |
| ASM-02 | Payment provider handles card data (no PAN/CVV stored on NileCart servers) | Scope reduction for small e-commerce model | Increases PCI DSS compliance scope and financial liability | Student 1 (Risk) |
| ASM-03 | Financial figures and valuations are estimated projections | No actual proprietary supplier quotes or financials available | Figures may not reflect exact market pricing in Cairo | Student 1 (Risk) |
| ASM-04 | Hosted cloud store and SaaS services utilized | Small enterprise architecture model for NileCart | Operational dependencies change technical controls | Student 2 (Governance) |
| ASM-05 | Egypt PDPL 151/2020 applies to Cairo customer PII processing | NileCart operates within Egypt serving Egyptian customers | Legal notification obligations during data breaches | Student 2 (Governance) |
| ASM-06 | Standard employee count: 35 staff across Cairo office and warehouse | Sets baseline for MFA enrollment and awareness training scale | Staff training coverage metrics require adjustment if headcount varies | Student 2 (Governance) |

## B. Evidence Register
| ID | Evidence Item | File Name | Date | Owner | Linked Item |
|---|---|---|---|---|---|
| EV-01 | Business Map & Data Flow | `01_Business_Map_and_Data_Flow.md` | 2026-11-16 | Student 1 | Deliverable 1 |
| EV-02 | Asset Inventory CSV | `02_Asset_Inventory.csv` | 2026-11-16 | Student 1 | Deliverable 2 |
| EV-03 | Risk Register CSV | `03_Risk_Register.csv` | 2026-11-16 | Student 1 | Deliverable 3 |
| EV-04 | Financial Calculations | `04_Financial_Analysis.md` | 2026-11-16 | Student 1 | Deliverable 4 |
| EV-05 | Control Budget & Decision | `05_Control_Decision_and_Budget.md` | 2026-11-16 | Student 1 | Deliverable 5 |
| EV-06 | Governance Pack & SOP | `06_Governance_Pack.md` | 2026-11-16 | Student 2 | Deliverable 6 |
| EV-07 | Compliance Mapping CSV | `07_Compliance_Mapping.csv` | 2026-11-16 | Student 2 | Deliverable 7 |
| EV-08 | Access Control & Test Cases | `08_Access_Control.md` | 2026-11-16 | Student 3 | Deliverable 8 |
| EV-09 | Runnable Access Test Script | `access_test.py` | 2026-11-16 | Student 3 | Deliverable 8 |
| EV-10 | Access Test Execution Output | `T1-T19_output.txt` | 2026-11-16 | Student 3 | Deliverable 8 |
| EV-11 | Incident Tabletop Exercise | `09_Incident_Exercise.md` | 2026-11-16 | Incident Team | Deliverable 9 |
| EV-12 | Incident Log File | `INC-2026-04_alert.log` | 2026-11-16 | Incident Team | Deliverable 9 |
| EV-13 | Awareness Campaign & Quiz | `10_Awareness_Campaign.md` | 2026-11-16 | Incident Team | Deliverable 10 |
| EV-14 | Awareness Poster (Plain Text) | `awareness_poster.txt` | 2026-11-16 | Incident Team | Deliverable 10 |
| EV-15 | Final Report Skeleton | `FINAL_REPORT_SKELETON.md` | 2026-11-16 | All Members | Final Submission |
| EV-16 | Presentation Outline & Q&A | `PRESENTATION_AND_QA.md` | 2026-11-16 | All Members | Presentation |
| EV-17 | Traceability Matrix | `TRACEABILITY_MATRIX.md` | 2026-11-16 | Student 2 | Matrix Mapping |

## C. Team Contribution Log (Real Names & Hours)
| Team Member | Role & Responsibilities | Hours Logged |
|---|---|---|
| **R3D Nader** (Student 1) | Business Context, Asset Inventory, Financial Analysis, Risk Register, Budget Decision | 18 hours |
| **Governance Lead** (Student 2) | Information Security Policies, Access & Backup Policies, RACI, KPIs, Compliance Mapping | 18 hours |
| **Security Testing Lead** (Student 3) | Access Control Architecture, Python Test Script (`access_test.py`), Mutation Check, Incident Exercise | 18 hours |

## D. References & Official Links
1. ISO/IEC 27001:2022 Information Security Management Standards — [ISO Standard 27001](https://www.iso.org/standard/27001)
2. NIST Special Publication 800-53 Rev. 5 Security and Privacy Controls — [NIST SP 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
3. Egypt Personal Data Protection Law (PDPL) Law 151 of 2020 — [MCIT Egypt](https://www.MCIT.gov.eg)
4. OWASP Top 10 (2021) A01:2021 Broken Access Control — [OWASP Top 10](https://owasp.org/Top10/A01_2021_Broken_Access_Control/)
