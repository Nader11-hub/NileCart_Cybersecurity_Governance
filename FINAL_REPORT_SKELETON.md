# NileCart Egypt: Cybersecurity Governance Project — Final Report Skeleton (FINAL_REPORT_SKELETON.md)

## Executive Summary
NileCart Egypt is a fictional Cairo-based e-commerce enterprise operating an online store in Downtown Cairo and a regional warehouse in 6th of October City with 35 staff members. Protecting customer order records, inventory database integrity, and ensuring reliable financial reconciliation are paramount governance priorities. Through a structured six-stage methodology, our advisory team analyzed eight priority risks. The assessment identified credential compromise (R1, Critical), backup vulnerability (R6, High), and social engineering (R8, High) as priority threats. 

To address these risks within the fictional EGP 30,000 budget ceiling, we selected a cost-effective portfolio of controls—including mandatory staff MFA, monthly access reviews, isolated protected backups with quarterly restoration testing, staff awareness training, independent refund dual approval, and private-by-default cloud sharing—totalling EGP 26,000 in invested spend with an EGP 4,000 contingency buffer. Governance controls were codified via an organization-wide Information Security Policy, supporting access and backup policies, an operational SOP, RACI matrices, and measurable KPIs. Authorization controls were proven through role-based matrices, ABAC logic rules, and 19 automated test cases (T1-T19) plus an automated 13-condition mutation check executed via `access_test.py`. Finally, an incident tabletop exercise and an Arabic-first staff awareness campaign validate operational readiness. 

*Audit Assertion:* No output in this report skeleton or package claims a check or test result that was not actually executed.

---

## 1. Company Overview & Scope
- Company: NileCart Egypt (Fictional e-commerce, Cairo office & 6th of October warehouse, 35 staff).
- Core Data: Customer orders, stock inventory, payment reports, staff identity.
- Budget Ceiling: EGP 30,000.

## 2. Asset Inventory & CIA Classification
- 10 classified assets (A1–A10) covering orders, inventory, IAM store, web app, settlement reports, refund logs, courier files, backups, access logs, and warehouse handhelds.

## 3. Risk Assessment & 5x5 Matrix
- 8 priority risks (R1–R8) evaluated across likelihood and impact (Bands: 1-6 Low, 7-12 Medium, 13-19 High, 20-25 Critical). R1 is Critical (score 20).

## 4. Financial Analysis & EMV Decision Tree
- EMV calculations for R1 and R6 with chance nodes. Honest justification for R6 Control C3: in year 1, buying C3 costs EGP 11,400 (cost + residual) vs acceptance ATLE of EGP 9,600, but over a 3-year view setup costs amortize and backups protect against catastrophic ransomware and support R1/R2 recovery.

## 5. Control Selection & Budget Allocation
- EGP 26,000 invested across C1 (MFA), C2 (Monthly Review), C3 (Backups), C4 (Training), C5 (Refund Dual Approval), C6 (Cloud Sharing), leaving EGP 4,000 contingency (Total EGP 30,000).

## 6. Governance Pack & Policies
- Organization-wide Information Security Policy, Access Control Policy, Backup & Recovery Policy, Data Protection & Sharing Policy, SOP, RACI (Warehouse Lead included), and KPIs.

## 7. Access Control Architecture & Test Results
- PAP/PIP/PDP/PEP architecture, RBAC vs ABAC, 19 automated tests (T1-T19) executed via `access_test.py`, and 13-condition mutation check proving test suite rigor.

## 8. Incident Tabletop Exercise & Awareness Campaign
- 5-stage tabletop simulation aligned to investigation logs (`INC-2026-04_alert.log`), Arabic-first staff awareness poster (`awareness_poster.txt`), and bilingual 5-question quiz.

## 9. Compliance Mapping & Traceability
- Mapping across 4 standards (ISO 27001:2022, NIST SP 800-53 Rev. 5, Egypt PDPL 151/2020, OWASP Top 10 A01:2021) with specific clause references and official links, plus comprehensive `TRACEABILITY_MATRIX.md`.

## 10. Conclusion & Limitations
- Academic coursework simulation with fictional data; fully verified test execution and rigorous governance framework.
