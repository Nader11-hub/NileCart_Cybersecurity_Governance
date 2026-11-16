# Governance Pack (06_Governance_Pack.md)
**Owner:** Student 2 (Governance & Policy) | **Reviewer:** Student 3 (Security Testing)

---

## 1. Information Security Policy (Organization-Wide)
- **Document Control:** Version 1.0 | Owner: IT Administrator & Management | Approver: Executive Board | Effective Date: 2026-11-16

§1 Purpose: Establish mandatory baseline security rules to protect NileCart Egypt's business information assets, customer privacy, and ensure reliable order fulfilment.
§2 Scope: Applies to all employees, contractors, endpoints, systems, customer order records, and backup archives across Cairo office and warehouse locations.
§3 Policy Statements:
1. Authentication: Every user must access systems using a unique individual account protected by multi-factor authentication (MFA). Shared accounts are strictly prohibited.
2. Least Privilege: Access is restricted strictly to what is required for job performance and validated against assigned roles.
3. Data Minimization: Customer PII and order exports must not be stored on unapproved personal devices or shared via public links.
4. Logging & Monitoring: Security events, administrative actions, and financial approvals must be logged and reviewed regularly.
5. Business Continuity: Critical databases and system configurations must be backed up securely and tested for restoration quarterly.
6. Incident Reporting: Any suspected security breach, phishing email, or anomalous activity must be reported to IT immediately.
§4 Change & Configuration: Unreviewed or unauthorized configuration changes to store systems are prohibited; all changes require documented approval and testing.
§5 Roles & Responsibilities: Management is accountable for governance; IT administers technical safeguards; asset owners approve business access; all staff are responsible for adhering to controls.
§6 Awareness & Incident Reporting: Mandatory staff awareness training must be completed semi-annually; incidents are reported immediately via #sec-alert.
§7 Enforcement: Non-compliance may result in disciplinary action up to and including termination of employment or contract.
§8 Review: Reviewed annually by management and IT, or immediately following any material security incident.
*Measurement Line:* Compliance is measured via monthly audits, MFA enrollment rates, and access review completion tracking.

---

## 2. Supporting Policy 1: Access Control Policy
- **Document Control:** Version 1.0 | Owner: IT Administrator | Approver: Operations Manager | Effective Date: 2026-11-16
- **Purpose:** Ensure that access to systems and financial records is formally requested, approved, provisioned, reviewed, and revoked securely.
- **Scope:** All NileCart staff and internal/external systems.
- **Requirements:**
  1. Account provisioning requires manager endorsement and asset owner approval.
  2. Privileged IT administrator accounts must be distinct from standard user accounts and used only via approved change-ticket windows.
  3. Segregation of duties must be enforced: financial refund requesters cannot approve their own requests.
  4. Access must be reviewed monthly, and leaver access must be revoked immediately upon departure.
- **Responsibilities:** IT Admin (provisioning/revocation), Operations/Finance (approval), Warehouse Lead (inventory access), Management (oversight).
- **Measurement:** 100% timely leaver revocation and monthly access review completion.
- **Linked Risks:** R1 (Credentials), R2 (Export sharing), R3 (Store config), R4 (Inventory edits), R5 (Refund fraud), R8 (Phishing / Lack of security awareness training).

---

## 3. Supporting Policy 2: Backup & Recovery Policy & Data Protection Policy
### A. Backup & Recovery Policy
- **Document Control:** Version 1.0 | Owner: IT Administrator | Approver: IT Lead | Effective Date: 2026-11-16
- **Purpose:** Guarantee operational resilience and data recoverability in the event of ransomware, accidental deletion, or hardware failure.
- **Scope:** Inventory database, store configuration, and core customer records.
- **Requirements:** Automated daily backups; secure storage with separate restore credentials; quarterly restoration testing.
- **Responsibilities:** IT Administrator.
- **Measurement:** Quarterly restoration test success rate (Target: 100%).
- **Linked Risks:** R6 (Backup failure / ransomware).

### B. Data Protection & Sharing Policy
- **Document Control:** Version 1.0 | Owner: Operations Manager | Approver: Management | Effective Date: 2026-11-16
- **Purpose:** Protect customer PII and operational data against unauthorized disclosure.
- **Scope:** Customer order records, courier handoff dispatch files.
- **Requirements:** Private-by-default cloud storage sharing; strict prohibition of public export links; data minimization for courier dispatches.
- **Responsibilities:** Operations Manager, Warehouse Lead, all staff.
- **Measurement:** Zero unauthorized public data leaks.
- **Linked Risks:** R2 (Export sharing), R7 (Courier device/file loss).

---

## 4. Standard Operating Procedure (SOP): Monthly Access Review
1. **Inputs:** Active employee roster from HR, active user list from IT identity store, and asset access lists from department owners.
2. **Steps:**
   - *Step 1 (Day 1):* IT generates the current active user account list and privileged access list.
   - *Step 2 (Days 2–3):* Operations, Warehouse, and Finance leads review access lists against current staff rosters to identify departed or transferred personnel.
   - *Step 3 (Days 4–5):* IT disables any identified unauthorized, dormant, or legacy accounts immediately.
   - *Step 4 (Day 6):* Department leads and IT sign off on the review completion report.
3. **Who:** IT Administrator (coordinator), Operations Manager, Warehouse Lead, Finance Officer.
4. **Evidence Produced:** Signed Monthly Access Review Log (access_review_YYYY_MM.pdf) and revocation audit trail.
5. **Exceptions:** Any delayed revocation must be logged as a security exception, approved by management, and remediated within 24 hours.

---

## 5. RACI Table (Single Accountable per Activity)
| Governance Activity | Management | IT Administrator | Operations Manager | Warehouse Lead | Finance Officer | Staff |
|---|---|---|---|---|---|---|
| **Policy Approval** | **A** | **R** | **C** | **C** | **C** | **I** |
| **Access Request (Operations/Warehouse)** | **I** | **R** | **A** (Ops) | **R** | **I** | **I** |
| **Access Request (Finance)** | **I** | **R** | **I** | **I** | **A** (Fin) | **I** |
| **Provisioning / Revocation** | **I** | **A/R** | **C** | **C** | **C** | **I** |
| **Monthly Access Review** | **I** | **R** | **A** (Ops) | **R** | **A** (Fin) | **I** |
| **Refund Approval** | **I** | **I** | **C** | **I** | **A/R** | **I** |
| **Backup Restore Test** | **I** | **A/R** | **C** | **C** | **I** | **I** |
| **Incident Reporting** | **A** | **R** | **R** | **R** | **C** | **R** (Report) |
| **Awareness Training** | **A** | **C** | **C** | **C** | **C** | **R** (Participate) |

---

## 6. KPI Table
| KPI Name | Formula | Target | Frequency | Owner | Data Source | Linked Risk |
|---|---|---|---|---|---|---|
| **MFA Enrollment Rate** | (Staff with MFA / Total Active Staff) * 100 | 100% | Monthly | IT Admin | Identity Store Logs | R1, R8 |
| **Monthly Access Review Completion** | (Reviews Completed / Scheduled Reviews) * 100 | 100% | Monthly | Ops / Finance / WH | Access Review Logs | R1, R2, R4 |
| **Leaver Revocation Timeliness** | (Leavers Revoked on Time / Total Leavers) * 100 | 100% | Monthly | IT Admin | HR Exit & IT Logs | R1 |
| **Backup Restoration Success Rate** | (Successful Restores / Scheduled Tests) * 100 | 100% | Quarterly | IT Admin | Restore Test Reports | R6 |
| **Staff Awareness Training Completion**| (Trained Staff / Total Staff) * 100 | >= 95% | Semi-Annual | Management | Training Portal Logs | R8 |
| **Phishing / Incident Reporting Rate** | (Suspicious messages correctly reported / total test messages) * 100 in tabletop/quiz checks | >= 80% reporting within 24h | Monthly | IT Admin | Ticketing System / Quiz logs | R8 |

---

## 7. Courier Dispatch Data-Minimization Checklist (TEMPLATE)
- **Purpose:** Ensure compliance with Data Protection & Sharing Policy for courier handoffs (Risk R7).
- **Checklist Items:**
  1. [ ] Only essential recipient delivery details (Name, Delivery Address, Phone) included? (Yes/No)
  2. [ ] Are unnecessary financial or order-item details redacted/omitted? (Yes/No)
  3. [ ] Is the dispatch file transmitted via encrypted private channel? (Yes/No)
  4. [ ] Mobile device or courier terminal remote revocation enabled? (Yes/No)
- **Sign-off:** Operations Manager: ___________________ Date: _______________

---

## 8. Backup Restoration Test Record (TEMPLATE)
- **Purpose:** Verify backup recoverability and integrity quarterly (Risk R6 / Backup & Recovery Policy).
- **Test Record Fields:**
  - Test ID: BKP-RESTORE-2026-Q[X]
  - Date & Time: ________________________
  - Database / Asset Restored: Inventory Database & Order Archive
  - Restored From: Isolated Backup Archive (C3)
  - Recovery Time Objective (RTO) Target: < 4 hours | Actual RTO: _______ hours
  - Recovery Point Objective (RPO) Target: < 24 hours | Actual RPO: _______ hours
  - Verification Status: SUCCESS / FAILED
  - IT Administrator Sign-off: ___________________ Date: _______________
