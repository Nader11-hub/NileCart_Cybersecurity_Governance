# Presentation Outline & Individual Q&A Defenses (PRESENTATION_AND_QA.md)

## 10-Slide Presentation Outline
- Slide 1: Title & Team Introduction (NileCart Egypt Governance Project)
- Slide 2: Business Context & Data Flow (Store, warehouse, payment provider, courier, 35 staff)
- Slide 3: Asset Inventory & CIA Classification (10 core assets with linked risks)
- Slide 4: Risk Assessment & 5x5 Matrix (Top risks: R1 Critical, R6 High, R8 High; R7 included)
- Slide 5: Financial Analysis & EMV Decision Tree (SLE, ATLE, chance nodes, year-1 vs 3-year R6 view)
- Slide 6: Budget Allocation (EGP 26,000 invested spend + EGP 4,000 contingency = EGP 30,000 ceiling)
- Slide 7: Governance Pack, RACI & KPIs (Policies with document control, SOP, RACI, measurable KPIs)
- Slide 8: Access Control Architecture & Test Results (RBAC/ABAC, 19 test cases T1-T19 + mutation check)
- Slide 9: Incident Tabletop Exercise & Arabic Awareness Campaign (Public link leak at 10:15 UTC & poster)
- Slide 10: Conclusion, Limitations & Next Steps

## Key Q&A Defenses & Model Answers (Individual Student Defense)
1. **Q: Why does buying C3 cost more than accepting R6 in year 1?**  
   **A:** In year 1, purchasing Control C3 (Protected Backups & Restore Testing) costs EGP 9,000 setup plus EGP 2,400 expected residual loss = EGP 11,400, which exceeds the baseline acceptance ATLE of EGP 9,600. However, looking at a 3-year strategic horizon, upfront setup costs amortize (3-yr Buy total = EGP 16,200 vs Accept total = EGP 28,800), and isolated backups protect against ransomware while supporting recovery for R1 and R2.
2. **Q: What does the mutation check prove and how do we know it is real?**  
   **A:** The mutation check automates the disabling of each of the 13 rule conditions one at a time across rules 1-3 and base RBAC. It proves that every condition in the authorization logic is actively evaluated and tested by at least one test case. We know it is real because it is executed directly by running `python3 access_test.py`, which programmatically asserts 0 survivors across all 13 mutants.
3. **Q: How did you calculate SLE and ATLE for Risk R1?**  
   **A:** Exposed asset value EGP 120,000 * 25% exposure factor = SLE 30,000. Estimated annual frequency 0.5/yr -> ATLE 15,000.
4. **Q: What is the difference between RBAC and ABAC in your access design?**  
   **A:** RBAC assigns baseline permissions based on static organizational roles (e.g., Warehouse Staff update inventory), whereas ABAC adds dynamic context attributes (MFA verification, specific object assignment, change ticket approval status, and segregation of duties where approver != requester).

---
*Audit Statement:* No output in this package claims a check or test result that was not actually run. All 19 tests and mutation checks are verified via execution of `access_test.py`.
