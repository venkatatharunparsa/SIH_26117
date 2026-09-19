# WP-18 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** All prior freezes especially WP-03/04/05/06/09/11/12/13/16/21/22/23/24  
**Status:** **SUPERSEDED by `WP-18_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-18_REDTEAM.md`. Verify: `WP-18_FREEZE_VERIFY.md`.  
**Job of WP-18:** **Fail-closed behaviour + eval suite** — define what happens when OCR, retrieve, model, plugin, grant, gateway, pack, or gates fail (**no cloud / no silent default model**), and publish **golden tasks** that prove Expected Solution + frozen Never rules. This is the org quality bar and later the **prototype test list**.

**Sources:** Official Expected Solution (demonstrable list); User grants/citations/plugins; WP-00 fail-closed + Never; follow-list golden list; all WP deny paths.

---

## One sentence (proposed)

When something required is missing or unsafe, KWB **stops or degrades safely with a logged reason** — never fails open to the internet or an unregistered model — and a **fixed golden suite** must pass before we call the demo “done.”

---

## 1. Fail-closed vs degrade (proposed)

| Mode | Meaning |
|---|---|
| **Fail-closed** | Privileged step **does not proceed**; user sees deny; audit event |
| **Degrade** | Continue only on an **explicit safe subset** (e.g. attach-only without KB) with banners — never widen privilege |
| **Fail-open (forbidden)** | Cloud URL, HF pull, skip card check, skip HITL, invent cites |

**Rule:** Prefer fail-closed for security boundaries; degrade only where a prior freeze already allows (e.g. attach-only omit org cites; `lineage_degraded`).

---

## 2. Failure matrix (must cover)

| Failure | Expected behaviour (from freezes) |
|---|---|
| OCR / extract refuse (inject) | WP-23 refuse+log; no side-effect |
| H1 not done | Hard-block verified path (WP-05) |
| Grant missing / revoked | Deny retrieve/MCP; cancel in-flight (WP-04) |
| Retrieve empty / unauthorized | Miss / deny — no invent (WP-11) |
| Claim conflict / NOT FOUND | H7 / honesty (WP-22) |
| Unregistered / disabled model | Gateway deny (WP-09/24) |
| Unserveable model | One load then fail; failover ≤2 (WP-06/09/10) |
| Oversize pack | Shrink or gateway hard-reject (WP-21/09) |
| Audit write fail | Fail-closed privileged action (WP-17) |
| Gate secret / sandbox red | Block view/H3 per WP-12 |
| MCP not allowlisted | Deny (WP-08) |
| Sandbox OOM/timeout | Report fail; no plant-safe claim (WP-16) |
| WAN / public peer on A | Audience A fail (WP-13) |
| Internet skill | Unload (WP-15) |

---

## 3. Golden eval suite (proposed must)

Map 1:1 to Expected Solution + critical Never proofs:

| ID | Golden task | Pass looks like |
|---|---|---|
| **G1** | Auto-select ≥2 task types | ≥2 distinct `model_id` in log |
| **G2** | Scan → findings → DRAFT Word | docx path + H1/H2 story |
| **G3** | Code + sandbox verify | Report + H9; calc-in-jail |
| **G4** | Multimodal image/scan understand | Vision/OCR path used |
| **G5** | WAN=0 Audience A | Host snapshot pass + green local hop |
| **G6** | Missing citation / NOT FOUND | Honest gap — no fake cite |
| **G7** | Expired/revoked grant | Deny-after-revoke |
| **G8** | Unregistered model | Gateway deny |
| **G9** | Secret in DRAFT | Unmasked block / H3 deny |
| **G10** | Sandbox red | H3 export blocked |

Org-ambition goldens: plugin deny, failover chain, lineage badge, personal pin load, etc.

---

## 4. How eval is run (proposed)

| | Demo | Org |
|---|---|---|
| Form | Checklist + script + evidence folder (logs, snapshots, artefacts) | Same + CI later |
| Automation | Manual/scripted OK for SIH | Ambition automated |
| Sign-off | Team marks pass/fail per G# | QA gate |

**Not:** Claiming Ragas/LLM-as-judge as required runtime (WP-22 refused).

---

## 5. Must / ambition / deferred / never (proposed)

### Must-work

1. Failure matrix §2 documented and implemented as product behaviour.  
2. Golden G1–G10 executable on demo stack.  
3. No fail-open to cloud/HF/unregistered model.  
4. Each fail produces audit reason code where applicable.  
5. Eval evidence retained for jury (align WP-17 demo window).  
6. This suite = prototype acceptance spine after WP-20.

### Org-ambition

- Automated runner; more goldens; chaos inject harness.

### Deferred

- Formal certification test lab.

### Never

- Pass golden by skipping HITL/air-gap.  
- Fail-open “for demo convenience.”  
- Replace human verifier with auto-green.

---

## 6. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | Expected Solution as test oracle |
| **Add** | Numbered golden IDs; fail matrix; evidence pack |
| **Refuse** | Happy-path video as sole “done” |

---

## 7. Boundaries

| Topic | Owner |
|---|---|
| Individual deny rules | Prior WPs |
| Offline media update tests | **WP-19** |
| Org picture | **WP-20** |
| Prototype REAL/MOCK/LATER | After WP-20 |

---

## 8. Open questions for decision maker

1. **Must goldens:** Freeze **G1–G10** as must-work, or trim demo to **G1–G5** only (rest org)?  
2. **Runner:** Demo eval = **manual checklist**, or require a **script** that exits non-zero on fail?  
3. **Inject faults:** Must-work includes **deliberate fault injection** (revoke mid-task, bad model id), or happy-path + separate deny demos?  
4. **Evidence pack:** Single **`eval/` folder** with logs+snapshots+docx required for “suite passed”?  
5. **Owner:** Who signs the checklist — **any teammate**, or named **QA/Admin role**?  
6. **Block ship:** If any must golden fails, **block “demo ready” claim** (hard), or allow with waivers?

---

## 9. Next after your decisions

**Done.** Frozen as `WP-18_FREEZE.md` rev 1.0. Next: **WP-19**.
