# Access Control Design & Test Results (08_Access_Control.md)
**Owner:** Student 3 (Security Testing) | **Reviewer:** Student 1 (Business & Risk)

---

## 1. Access Control Matrix (4 Roles × 5 Resources)
| Role | Customer Order Files (order_file) | Inventory Database (inventory) | Refunds (refunds) | Admin Settings (admin_settings) | Payment Reports (payment_reports) |
|---|---|---|---|---|---|
| **Customer Support** | **Read** (assigned orders only; Rule 1)<br>_Least privilege: Required for customer support inquiries._<br>_Risks: R1, R2_ | **Deny**<br>_Least privilege: Support does not manage warehouse stock._<br>_Risks: R4_ | **Request** (no approval authority)<br>_Least privilege: Can log refund requests but cannot approve funds._<br>_Risks: R5_ | **Deny**<br>_Least privilege: App settings require IT administration._<br>_Risks: R3_ | **Deny**<br>_Least privilege: Payment reports are restricted to Finance._<br>_Risks: R5_ |
| **Warehouse Staff** | **Read** (per script ROLE_PERMISSIONS; Note: proposed change or policy alignment: if restricted, note as policy vs test script divergence)<br>_Least privilege: Fulfillment operations._<br>_Risks: R1, R2_ | **Update** (Base RBAC)<br>_Least privilege: Necessary for picking, packing, and inventory accuracy._<br>_Risks: R4_ | **Deny**<br>_Least privilege: Warehouse staff do not handle financial refunds._<br>_Risks: R5_ | **Deny**<br>_Least privilege: Store configuration is restricted to IT._<br>_Risks: R3_ | **Deny**<br>_Least privilege: Payment reports belong to Finance reconciliation._<br>_Risks: R5_ |
| **Finance Officer** | **Read** (Base RBAC)<br>_Least privilege: Required for payment reconciliation and refunds._<br>_Risks: R1, R5_ | **Deny**<br>_Least privilege: Inventory is managed by warehouse staff._<br>_Risks: R4_ | **Approve** (Rule 2: independent dual approval, mfa, approver != requester)<br>_Least privilege: Finance approves refunds with segregation of duties._<br>_Risks: R5_ | **Deny**<br>_Least privilege: System settings are restricted to IT._<br>_Risks: R3_ | **Read** (Base RBAC)<br>_Least privilege: Core duty for reconciling gateway payouts._<br>_Risks: R5_ |
| **IT Administrator** | **Deny** (Base RBAC without rule match; note: IT read on orders is denied per T13)<br>_Least privilege: IT maintains infrastructure, not routine business data._<br>_Risks: R1, R2_ | **Deny**<br>_Least privilege: IT provides database support, not stock updates._<br>_Risks: R4_ | **Deny**<br>_Least privilege: Financial records are outside IT administrative duties._<br>_Risks: R5_ | **Configure** (Rule 3: mfa + change ticket approved)<br>_Least privilege: IT administers store apps and infrastructure with change control._<br>_Risks: R3_ | **Deny**<br>_Least privilege: Financial settlement data is managed by Finance._<br>_Risks: R5_ |

*(Note: Permissions with no explicit rule function in access_test.py fall back to Base RBAC or are governed by Rules 1-3 as defined in access_test.py.)*

---

## 2. Logic Rules & Baseline RBAC (Matching access_test.py)
1. **Rule 1 (rule1_read_order):**  
   ALLOW_READ_ORDER = account_active AND correct_role AND object_assigned  
   _Plain English:_ Customer support or authorized staff may read order records only if their account is active, they hold the correct role, and the specific order is assigned to their fixture set. Implements Data Protection & Sharing Policy / InfoSec §3.2 (Risk R1, R2).
2. **Rule 2 (rule2_refund_approve):**  
   ALLOW_REFUND_APPROVE = account_active AND correct_role AND mfa_verified AND approver_not_requester  
   _Plain English:_ Finance officers may approve a refund if their account is active, MFA is verified, they hold the approval role, and the user approving the refund is different from the user who requested it (Segregation of Duties). Implements Access Control Policy segregation of duties (Risk R5).
3. **Rule 3 (rule3_admin_config):**  
   ALLOW_ADMIN_CONFIG = account_active AND correct_role AND mfa_verified AND change_ticket_approved  
   _Plain English:_ IT administrators may configure store settings only if their account is active, MFA is verified, they hold the correct role, and an approved change ticket exists. Implements InfoSec Policy §4 Change Control (Risk R3).
4. **Base RBAC Rule (rbac_base):**  
   BASE_RBAC = account_active AND correct_role  
   _Plain English:_ For all other actions (such as inventory updates), access is permitted if the account is active and holds the correct role. Implements least-privilege role separation (Risks R4).

---

## 3. Test Cases (T1-T19) & Execution Results
The test suite consists of 19 automated tests (T1-T19) executed via access_test.py. Account names do not use '@nilecart' suffixes in the script fixtures.

| Test | Scenario | Account | Resource / Action | Rule | Expected | Actual | Pass/Fail | Risk | Why denied / allowed |
|---|---|---|---|---|---|---|---|---|---|
| T1 | Support reads an order assigned to them | sup-01 | order_file / read | Rule 1 | ALLOW | ALLOW | PASS | R1/R2 | - |
| T2 | Support reads an order NOT assigned to them | sup-02 | order_file / read | Rule 1 | DENY | DENY | PASS | R2 | object_assigned |
| T3 | Inactive (leaver) support account reads order | sup-03 | order_file / read | Rule 1 | DENY | DENY | PASS | R1 | account_active |
| T4 | Warehouse staff tries to approve a refund | wh-01 | refunds / approve | Rule 2 | DENY | DENY | PASS | R5 | correct_role |
| T5 | Finance approves a refund they requested | fin-01 | refunds / approve | Rule 2 | DENY | DENY | PASS | R5 | approver_not_requester |
| T6 | Warehouse staff updates inventory | wh-01 | inventory / update | RBAC | ALLOW | ALLOW | PASS | R4 | - |
| T7 | Account with no role reads an assigned order | orphan-01 | order_file / read | Rule 1 | DENY | DENY | PASS | R1 | correct_role |
| T8 | IT admin changes settings, ticket NOT approved | it-01 | admin_settings / configure | Rule 3 | DENY | DENY | PASS | R3 | change_ticket_approved |
| T9 | Finance (other person) approves a refund | fin-02 | refunds / approve | Rule 2 | ALLOW | ALLOW | PASS | R5 | - |
| T10 | Finance without MFA approves a refund | fin-03 | refunds / approve | Rule 2 | DENY | DENY | PASS | R1/R5 | mfa_verified |
| T11 | IT admin changes settings with approved ticket | it-01 | admin_settings / configure | Rule 3 | ALLOW | ALLOW | PASS | R3 | - |
| T12 | IT admin without MFA changes settings | it-02 | admin_settings / configure | Rule 3 | DENY | DENY | PASS | R1/R3 | mfa_verified |
| T13 | IT admin reads an order (even if assigned) | it-01 | order_file / read | Rule 1 | DENY | DENY | PASS | R2 | correct_role |
| T14 | Support tries to update inventory | sup-01 | inventory / update | RBAC | DENY | DENY | PASS | R4 | correct_role |
| T15 | Inactive finance account approves a refund | fin-04 | refunds / approve | Rule 2 | DENY | DENY | PASS | R1/R5 | account_active |
| T16 | Inactive IT admin changes settings | it-03 | admin_settings / configure | Rule 3 | DENY | DENY | PASS | R1/R3 | account_active |
| T17 | Finance officer changes admin settings | fin-02 | admin_settings / configure | Rule 3 | DENY | DENY | PASS | R3 | correct_role |
| T18 | Inactive warehouse account updates inventory | wh-03 | inventory / update | RBAC | DENY | DENY | PASS | R4 | account_active |
| T19 | Unknown account reads an order | ghost-99 | order_file / read | N/A | DENY | DENY | PASS | R1 | unknown_account |

### How to Run and Verify
1. Run `python3 access_test.py` or `python3 access_test.py --markdown` in the terminal.
2. Confirm output reports 19 passed, 0 failed.
3. Screenshot terminal output as `T1-T19_output.png`.

---

## 4. Mutation Check
The script includes an automated **Mutation Check** that switches off each of the 13 rule conditions one at a time across all rules (rule1, rule2, rule3, rbac). The test suite successfully catches every single disabled condition (each is caught by at least 1 test, with 0 survivors). This proves that every condition in the access control logic is actively tested and necessary.

---

## 5. PAP / PIP / PDP / PEP Architecture
| Component | Function in NileCart Access Control |
|---|---|
| **PAP** (Policy Administration Point) | Stores ROLE_PERMISSIONS and Rules 1-3 logic. |
| **PIP** (Policy Information Point) | Stores ACCOUNTS, REFUNDS, and CHANGE_TICKETS attributes (e.g., fin-02, RF-1001, sup-01). |
| **PDP** (Policy Decision Point) | `decide()`: evaluates requests against PAP policy and PIP attributes without seeing test IDs or expected results. |
| **PEP** (Policy Enforcement Point) | `pep()`: intercepts requests, enforces PDP decision, and appends to audit log. |

* **Mermaid Sequence Diagram:**
  ```mermaid
  sequenceDiagram
      autonumber
      actor User as Staff User (fin-02)
      participant PEP as PEP (Store API Gateway)
      participant PIP as PIP (Identity & DB Store)
      participant PDP as PDP (Decision Engine)
      User->>PEP: Request Refund Approval RF-1001 (requester: sup-01)
      PEP->>PIP: Fetch attributes (Role=Finance, MFA=True, Active=True, Req=sup-01, App=fin-02)
      PIP-->>PEP: Return attributes
      PEP->>PDP: Evaluate rule2_refund_approve(Attributes)
      PDP-->>PEP: DECISION: ALLOW
      PEP->>User: Action Approved & Logged in Audit Trail
  ```

---

## 6. RBAC vs. ABAC
- **RBAC (Role-Based Access Control):** Baseline permission assignment tied to static organizational roles.
- **ABAC (Attribute-Based Access Control):** Dynamic conditional evaluation incorporating contextual attributes (MFA verification, specific object assignment, change ticket approval status, segregation of duties).

---

## 7. Honest Limitations
- Implemented as standard library Python code and markdown documentation for academic coursework validation.
- Fictional data and test accounts only.
