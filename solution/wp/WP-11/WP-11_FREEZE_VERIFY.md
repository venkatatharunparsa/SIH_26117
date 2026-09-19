# WP-11 freeze — verification + source-of-truth + confidence

**Date:** 2026-09-18  
**Target:** `WP-11_FREEZE.md` rev 1.0  
**Against:** Official PS Description; WP-00–04, WP-03, WP-23; `WP-11_REDTEAM.md` D1–D16; DM Q1–Q6; Observed authz-first RAG.

**Grades:** **Official** | **WP-*** | **DM** | **Spec** | **Observed** | **Derived**

---

## Verdict

| Question | Answer |
|---|---|
| All DM answers + deep fills in freeze? | **Yes** |
| Every substantive claim sourced? | **Yes** (ledger §2) |
| Fit for high-volume confidential data handling (org design)? | **Yes** — promote/authz/corpus isolation; demo stays MOCK-honest |
| Contradict prior freezes? | **No** |
| **Confidence to move to WP-22** | **0.89** |
| Prototype exists | **0.00** |

**GO:** Keep WP-11 frozen. Proceed to **WP-22** when you say go.

---

## 1. Completeness (DM + D-fills)

| ID | In freeze? | Where |
|---|---|---|
| Q1 citation | Yes | §3, §7, §12 |
| Q2 lexical MOCK | Yes | §3, §6, §10 |
| Q3 k=5 | Yes | §1, §3, §6 |
| Q4 stale warn ambition | Yes | §2, §3, §7 |
| Q5 policy MOCK three-level | Yes | §3, §5, §12 |
| Q6 never auto promote | Yes | §3, §8, §10 |
| D1 authz-first | Yes | §6 |
| D2 server grant scope | Yes | §6 |
| D3 segregation partition | Yes | §6 |
| D4 chunk parent ACL | Yes | §6 |
| D5 citation binding | Yes | §6–7 |
| D6 empty honesty | Yes | §6, §9 |
| D7 never auto index junk | Yes | §8 |
| D8 corpus isolation | Yes | §5 |
| D9 query non-authority | Yes | §6 |
| D10 live grant check | Yes | §6 |
| D11 chunk bounds | Yes | §6 (unit/page prefer) |
| D12 revision unknown | Yes | §7 |
| D13 k=5 not SLA | Yes | §2 |
| D14 volume honesty | Yes | §2 |
| D15 three-level MOCK | Yes | §5, §12 |
| D16 rank in-auth set | Yes | §6 |

---

## 2. Claim ledger

| Claim | Source | Hold? |
|---|---|---|
| Ground via local KB connector in manuals/SOPs/correspondence | **Official** Description | Yes |
| Nothing external / offline | **Official** + **WP-00** | Yes |
| Three-level: file / user / policy | **WP-00** Q4; policy MOCK **DM** | Yes |
| User claim ≠ retrieve corpus | **WP-23** T1; **WP-22** boundary | Yes |
| Grant-scoped; default-deny | **WP-04** | Yes |
| ACL/grant before model | **WP-00/04** + **Observed** authz-first | Yes |
| Authz-first not post-filter-only | **Observed** research; **REDTEAM** D1 | Yes |
| Index ≠ SoR | **WP-02** | Yes |
| Revision or uncertainty | **WP-02** | Yes |
| Chunks T3 | **WP-23** | Yes |
| Slow OK | **User** / WP-00 | Yes |
| Expected Solution does not require vector DB | **Official** Expected Solution silence + **Derived** | Yes |
| Attach-only may omit org cite | **WP-01** | Yes |
| Never auto promote extract | **DM** Q6 + WP-03/05 | Yes |
| Deny on revoke | **WP-04** | Yes |
| Correspondence ≠ SOP | **Official** list + **Derived** isolation | Yes |
| Haystack/Onyx/GBrain patterns only | **Repo map** | Yes |
| Live plant-scale sync | **Not** claimed — ambition | Yes |
| Stale warn must-work | **Not** — DM ambition | Yes |
| Lewis: retrieve grounds; ≠ gen quality | **Spec** | Yes |

**No invented MRPL DMS APIs or KPI hours.**

---

## 3. Residual risks (do not block WP-22)

| Risk | Park |
|---|---|
| Implementation picks post-filter store by mistake | Eval in WP-18; freeze forbids as primary |
| Top-k=5 misses rare authorized doc | Ambition hybrid + Admin k |
| Promote process under-specified UX | Admin/HITL principle enough; WP-05 H6-like later |
| Three-level conflict rules | **WP-22** |

---

## 4. Confidence breakdown

| Theme | Score |
|---|---|
| Official + WP-00–04 alignment | 0.92 |
| Authz-first / data-leak controls | 0.90 |
| DM Q1–Q6 completeness | 0.95 |
| Volume/honesty (MOCK vs plant scale) | 0.88 |
| Anti-overclaim Limits | 0.90 |
| Ready for WP-22 claim layer | 0.89 |
| **Overall** | **0.89** |
