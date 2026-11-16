# End-to-End Traceability Matrix (TRACEABILITY_MATRIX.md)
**Owner:** Student 2 (Governance & Policy) | **Reviewer:** Student 1 (Business & Risk)

---

## Traceability Table (Risk -> Control -> Budget -> Policy -> Verification -> Evidence -> Owners)

| Risk ID & Title | Register Control | Budget Control | Policy Section | Verification Method & Tests | Real Evidence Files | Owner | Reviewer |
|---|---|---|---|---|---|---|---|
| **R1:** Credential Compromise (Crit) | Mandatory MFA + least-privilege review | C1 (MFA) + C2 (Access Review) | InfoSec Policy §3.1 (Authentication) & §3.2 | T1, T3, T7, T10, T12, T15, T16, T19; monthly review | access_test.py, 08_Access_Control.md, 06_Governance_Pack.md | IT Admin | Operations |
| **R2:** Export Sharing / PII Leak (High) | Private-by-default sharing + monthly reviews | C2 (Access Review) + C6 (Cloud Sharing) | Data Protection & Sharing Policy | T1, T2, T13; tabletop simulation | 08_Access_Control.md, 09_Incident_Exercise.md, access_test.py | Operations | IT Admin |
| **R3:** Unreviewed Changes (Med) | Change approval workflow + admin separation | Policy / process (change control) | InfoSec Policy §4 (Change & Configuration) | T8, T11, T12, T16, T17 | 08_Access_Control.md, access_test.py | IT Admin | Finance Officer |
| **R4:** Unrestricted Inventory (Med) | Role-restricted inventory updates & logs | Policy / process (Base RBAC) | InfoSec Policy §3.2 (Least Privilege) | T6, T14, T18 | 08_Access_Control.md, access_test.py | Warehouse Lead | Operations |
| **R5:** Refund Fraud / SoD (Med) | Independent dual approval & logging | C5 (Refund Dual Approval) | Access Control Policy req. 3 | T4, T5, T9, T10, T15 | 08_Access_Control.md, access_test.py | Finance Officer | IT Admin |
| **R6:** Backup Failure / Ransomware (High) | Protected/isolated backups & quarterly restore test | C3 (Protected Backups & Test) | Backup & Recovery Policy | Quarterly restore test procedure | 06_Governance_Pack.md (Restore Test Template) | IT Admin | Operations |
| **R7:** Courier Dispatch PII Loss (Med) | Data minimization & remote device revocation | Policy / process (not budgeted) | Data Protection & Sharing Policy | Courier dispatch checklist audit | 06_Governance_Pack.md (Courier Dispatch Checklist Template) | Operations | IT Admin |
| **R8:** Phishing / Lack of Training (High) | Staff awareness training + MFA + quick reporting | C1 (MFA) + C4 (Awareness Training) | InfoSec Policy §6 (Awareness) & §3.1 | Quiz Q1-Q5, tabletop reporting | 10_Awareness_Campaign.md, 09_Incident_Exercise.md | All Managers | Governance Lead (Student 2) |

---
*Audit Assertion:* No output in this traceability package or governance repository claims a check or test result that was not actually executed and verified via access_test.py.
