# WP-17 freeze — verification + source-of-truth + confidence

**Date:** 2026-09-18  
**Target:** `WP-17_FREEZE.md` rev 1.0  
**Against:** Official Expected Solution; WP-00; producers WP-04/05/06/09/12/21; `WP-17_REDTEAM.md`; DM Q1–Q6; CERT-In Directions 20(3)/2022 + FAQ May 2022; DPDP 2023 (org track).

**Grades:** **Official** | **WP-*** | **DM** | **Spec** | **Derived**

---

## Verdict

| Question | Answer |
|---|---|
| DM answers captured (incl. Q3/Q4 parse)? | **Yes** — editable≠mutate; yes→person_id+MOCK name |
| Every substantive claim sourced? | **Yes** (§2) |
| CERT-In cited from Direction (not memory-only)? | **Yes** — No. 20(3)/2022-CERT-In; 180 days |
| Compliance badge claimed? | **No** |
| **Confidence / GO WP-14** | **0.88** |

---

## 1. Completeness (DM)

| ID | In freeze? | Where |
|---|---|---|
| Q1 jury-day | Yes | D1, §6 |
| Q2 full own-task | Yes | D2, §6 |
| Q3 in-app must; download/edit parsed | Yes | D3, Limits, §8 Never |
| Q4 PII yes | Yes | D4 |
| Q5 trusted clock runbook | Yes | D5 |
| Q6 fail-closed | Yes | D6, §7 |

---

## 2. Claim ledger

| Claim | Source | Hold? |
|---|---|---|
| Logs or visible monitor; auto-select with model ids in log | **Official** Expected Solution + **WP-00** | Yes |
| Audit track who/what changed | **WP-00** | Yes |
| Grant lifecycle events | **WP-04** | Yes |
| HITL accept fields | **WP-05** | Yes |
| model_id + request_id / deny codes | **WP-06** / **WP-09** | Yes |
| GateReport logged | **WP-12** | Yes |
| PackManifest refs | **WP-21** | Yes |
| ICT logs enabled; rolling **180 days**; India/producible | **Spec** CERT-In Directions 20(3)/2022 §(iv) | Yes — **shape** |
| Success and unsuccessful events | **Spec** CERT-In FAQ May 2022 Q37 | Yes — flavour |
| Demo jury-day retention | **DM** Q1 | Yes |
| Full own-task list | **DM** Q2 | Yes |
| In-app must-work; no mutable history | **DM** Q3 + **Derived** red-team A | Yes |
| person_id + MOCK display_name | **DM** Q4 parse + **Derived** | Yes |
| Trusted clock runbook; no WAN NTP in-op | **DM** Q5 + air-gap **WP-00** | Yes |
| Fail-closed on audit write fail | **DM** Q6 | Yes |
| DPDP certified | **Not** claimed | Yes |
| CERT-In certified | **Not** claimed | Yes |
| SIEM brand | **Not** locked | Yes |

---

## 3. Residual risks

| Risk | Park |
|---|---|
| Jury-day wipe too early | Tie wipe to official demo end |
| Fail-closed DoS on full disk | Admin alarm + capacity runbook |
| Display_name stalking | Org hide names |
| Ambition download re-import | Never as SoR |

---

## 4. Confidence

| Theme | Score |
|---|---|
| Official log / model_id proof | 0.95 |
| CERT-In shape citation | 0.90 |
| DM Q1–Q6 + Q3 parse | 0.90 |
| Fail-closed integrity | 0.90 |
| Anti-compliance-overclaim | 0.92 |
| **Overall** | **0.88** |

---

## 5. Source map

| Need | File |
|---|---|
| Binding | `WP-17_FREEZE.md` |
| Attacks | `WP-17_REDTEAM.md` |
| Ledger | `WP-17_FREEZE_VERIFY.md` |
| CERT-In PDF | https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf |
| CERT-In FAQ | https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf |
