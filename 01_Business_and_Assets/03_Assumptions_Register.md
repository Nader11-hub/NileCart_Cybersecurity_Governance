# NileCart Egypt — Phase 1: Assumptions Register (03_Assumptions_Register.md)
**Course Project 2026 | Week 1: Understand | Owner:** Student 1 (Business & Risk Lead)

---

## 1. Governance & Boundary Assumptions
| ID | Assumption Statement | Rationale / Source | Operational Impact if Invalid |
|---|---|---|---|
| **ASM-01** | **Academic Simulation Scope** | Project brief requirement; all entities, customers, and incidents are fictional. | None; academic compliance baseline. |
| **ASM-02** | **External Payment Tokenization** | Payment processing is outsourced to Egyptian payment gateways (e.g., Paymob / Fawry). NileCart does NOT store raw credit card numbers (PAN) or CVVs. | If NileCart stored card data, full PCI DSS Level 1 scope would apply, vastly exceeding the EGP 30,000 budget. |
| **ASM-03** | **Employee Baseline (35 Staff)** | 5 Management/IT, 12 Customer Support, 4 Finance, 14 Warehouse workers across Downtown Cairo and 6th of October. | Sets the scale for MFA software licensing (C1), access reviews (C2), and staff training (C4). |
| **ASM-04** | **Regulatory Jurisdiction (PDPL 151/2020)** | NileCart processes personal data of Egyptian citizens residing primarily in Cairo and Giza. | Triggers mandatory 72-hour breach reporting to the Egyptian Data Protection Center (EDPC) under Article 13. |
| **ASM-05** | **Cloud & SaaS Operating Model** | Online store is hosted on cloud infrastructure; office productivity and shared storage use managed cloud drives. | Defines the threat vector for public link sharing (Risk R2) and IAM account takeovers (Risk R1). |
| **ASM-06** | **Fictional Security Budget Ceiling** | The project operates under an exact fictional spending ceiling of EGP 30,000. | All control expenditures (C1–C6) and contingency reserves must sum to exactly EGP 30,000. |
| **ASM-07** | **Physical Facility Segregation** | Commercial operations take place in Downtown Cairo office; inventory picking and dispatch take place exclusively in 6th of October City warehouse. | Requires distinct physical and logical access perimeters (handheld scanners A10 isolated from financial systems A5/A6). |

---
*Cross-Check Verification:* Reviewed and confirmed by Student 2 (Governance & Policy) and Student 3 (Security Testing).
