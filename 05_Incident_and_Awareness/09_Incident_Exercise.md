# Incident Tabletop Exercise (09_Incident_Exercise.md)
**Owner:** Incident Response Team | **Reviewer:** Business & Risk Lead

---

## 1. Tabletop Scenario: Public Order-Export Link Discovered
- **Scenario:** An operations staff member discovers that an internal cloud-storage link containing a spreadsheet of customer orders (Order Export #104) was inadvertently pasted into a public team communication channel, making it accessible externally without authentication.

### 5-Stage Tabletop Simulation (Logs in UTC Z; Table in Cairo Local Time UTC+2)
| Stage | Timeline (UTC vs Cairo Local UTC+2) | Role / Decision-Maker | Decision Taken | Action Taken | Evidence Produced |
|---|---|---|---|---|---|
| **1. Detect** | 10:15 UTC (12:15 Cairo) | Operations Staff (`sup-04`) | Escalate immediately to IT Lead and Operations Manager | Report discovery via emergency security channel; do not forward file | Incident Alert Log (`INC-2026-04_alert.log`) |
| **2. Contain** | 10:25 UTC (12:25 Cairo) | IT Administrator (`it-admin`) | Revoke public sharing permissions immediately | Disable public cloud link, invalidate active session tokens, and preserve access logs | Containment Action Report (`INC-2026-04_contain.log`) |
| **3. Investigate**| 10:35 UTC (12:35 Cairo) | IT Admin & Operations Manager | Audit export link access history and scope | Extract access and sharing logs to identify external IP access and volume of exposed records (142 PII records) | Investigation Audit Trail (`INC-2026-04_audit.log`) |
| **4. Recover** | 14:00 UTC (16:00 Cairo) | Operations Manager (`ops-mgr`) | Issue secure internal replacement channel and notify management | Reissue order file via encrypted internal storage with strict IAM policy; resume operations | Recovery Verification Log (`INC-2026-04_recovery.log`) |
| **5. Learn & Review** | 17:30 UTC (19:30 Cairo / PIR Scheduled 2026-11-18) | Incident Response Team (All Leads) | Implement corrective controls and update sharing policy | Enforce private-by-default cloud sharing, mandate monthly access review, conduct staff refresher | Post-Incident Review & Action Plan (`INC-2026-04_pir.pdf`) |

---

## 2. Fictional Investigation Logs (Loaded from `INC-2026-04_alert.log`)
```text
[2026-11-16T10:15:22Z] SEVERITY=HIGH ALERT=Public_Link_Detected USER=sup-04 SRC_IP=192.168.1.45 RECORDS_EXPOSED=142
[2026-11-16T10:18:05Z] ACTION=NOTIFY_IT INCIDENT_ID=INC-2026-04 STATUS=ACKNOWLEDGED RESPONDER=it-admin
[2026-11-16T10:25:10Z] ACTION=REVOKE_LINK TARGET_URL=https://cloud.nilecart.internal/share/x89K2p RESOURCE=order_export_104.xlsx
[2026-11-16T10:25:12Z] RESULT=SUCCESS LINK_STATUS=DISABLED EXPIRED_SESSIONS_REVOKED=3
[2026-11-16T10:35:00Z] AUDIT_START INCIDENT_ID=INC-2026-04 FILE=order_export_104.xlsx OWNER=Operations
[2026-11-16T10:40:15Z] LOG_ENTRY IP=203.0.113.42 TIME=10:12:04Z METHOD=GET STATUS=200 BYTES=45120 AGENT=Mozilla/5.0
[2026-11-16T10:40:18Z] LOG_ENTRY IP=203.0.113.42 TIME=10:12:05Z METHOD=GET STATUS=200 BYTES=1240 AGENT=Mozilla/5.0
[2026-11-16T10:42:00Z] IP_ANALYSIS IP=203.0.113.42 GEO=External_ISP_Cairo ACCESS_COUNT=2 DOWNLOAD_CONFIRMED=TRUE
[2026-11-16T11:00:00Z] SCOPE_ASSESSMENT RECORDS_EXPOSED=142 PII_FIELDS="Name, Delivery Address, Phone, Order Summary"
[2026-11-16T12:30:00Z] CONTAINMENT_VERIFIED NO_FURTHER_ACCESS_DETECTED
[2026-11-16T14:00:00Z] RECOVERY_ACTION SECURE_CHANNEL_ESTABLISHED IAM_RESTRICTED=TRUE
[2026-11-16T16:15:00Z] MANAGEMENT_BRIEFING COMPLETED ASSUMPTION_NOTIFY=CONSIDERED_UNDER_PDPL
[2026-11-16T17:00:00Z] ACTION_ITEM ENFORCE_PRIVATE_DEFAULT_SHARING ASSIGNED=Operations OWNER=ops-mgr
[2026-11-16T17:30:00Z] STATUS INCIDENT=CLOSED PIR_SCHEDULED=2026-11-18
```
*Log Analysis:* The logs show that at 10:15 UTC (12:15 Cairo local time) an employee reported the link. IT revoked it within 10 minutes (10:25 UTC). Subsequent audit logs revealed an external IP (`203.0.113.42`) accessed the file twice, downloading 142 fictional customer order records before revocation. Severity is classified as **High** due to the exposure volume of 142 PII records.

---

## 3. Impact, Notification Assumption & Lessons Learned
- **Impact Assessment:** Fictional exposure of 142 customer order records containing names, phone numbers, delivery addresses, and purchased items. No payment card numbers (PAN/CVV) were exposed (payment gateway is external).
- **Notification Decision (Assumption):** Under internal incident procedures, management reviewed Egypt PDPL 151/2020 reporting guidelines (assumed advisory/legal review required); management prepared a notification draft but no definitive legal conclusion of mandatory breach notification is asserted without qualified counsel.
- **5 Concrete Changes Linked to Policies & Risks:**
  1. *Default-Private Sharing (Risk R2):* Cloud storage rules updated to block public link creation organization-wide.
  2. *Access Reviews (Risk R1):* Monthly export permission reviews instituted under Access Control Policy.
  3. *Staff Training (Risk R8):* Mandatory awareness refresher on safe file sharing and link handling.
  4. *Data Minimization (Risk R7):* Order exports restricted to contain only necessary operational fields.
  5. *Incident Playbook:* Updated incident response SOP with clearer containment steps.
