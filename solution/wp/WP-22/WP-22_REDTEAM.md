# WP-22 three-source — adversarial red-team + adopt map

**Date:** 2026-09-18  
**Target:** `WP-22_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** see §0  
**Against:** WP-00 Q4; WP-01 cite rules; WP-05 H7; WP-11 corpora; WP-23 T1/T3; repo map (no LLM-as-reconciler).

---

## 0. DM answers (binding)

| Q | Decision |
|---|---|
| **1 S1↔S3** | **Yes** — block **record-facing H2 accept** until H7 resolves |
| **2 Demo conflict** | **Yes** — jury script forces **policy vs user** conflict |
| **3 NOT FOUND** | **Yes** — must-work showable |
| **4 Scope** | **Material findings + any cited assertion** (not every sentence) |
| **5 User overrides file** | **Allowed only via H7 + audit**; still **not SoR write** |
| **6 Attach-only** | **Yes** — three-level remains **optional** without KB grant |

---

## Verdict

| | |
|---|---|
| Direction | **Yes** |
| Missing | M1–M8 (claim unit, H2 block, audit fields, friendliest-sentence ban, attach-only clarity) |
| Overhyped | Full NLI on every token; three-level without KB = always |
| Confidence after freeze | **~0.88** → GO WP-07 |

---

## 1. Missing → fill

| ID | Gap | Fill |
|---|---|---|
| **M1** | What is a “material finding” | Findings fields + any span that carries a citation or grounded plant/policy assertion |
| **M2** | H2 blocked on open conflict | Record-facing accept denied while `status=conflict` unresolved |
| **M3** | H7 audit payload | person, role, claim_id, sources, choice, timestamp |
| **M4** | Friendliest-sentence ban | Explicit Never: merge S1/S2/S3 without labels |
| **M5** | NOT FOUND ≠ empty draft failure | Valid artefact; may still draft with gap labels |
| **M6** | S2-wins after H7 | Label claim `human_resolved_prefer_user`; file cite retained as disagreed |
| **M7** | No KB grant | Three-level optional; do not fake policy cites |
| **M8** | Machine “auto-resolve” | Forbidden; H7 only |

---

## 2. Overhyped

| Attack | Fix |
|---|---|
| Every sentence scored | Scope = material + cited (DM) |
| Three-level = complete truth | Still HITL; citations can be wrong OCR |
| NOT FOUND demo = product failure | Valid status |
| User override = SoR change | Explicitly not |

---

## 3. Disposition

**Applied.** → `WP-22_FREEZE.md` rev 1.0. Confidence **0.88**. **GO** → **WP-07**.
