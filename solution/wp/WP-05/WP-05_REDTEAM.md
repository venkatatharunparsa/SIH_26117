# WP-05 HITL — adversarial red-team + adopt map

**Date:** 2026-09-18  
**Target:** `WP-05_ARCHITECT_PERSPECTIVE.md`  
**Decision-maker answers (binding input):** see §0  
**Against:** WP-00–04 freezes; Official Background (approval notes; human owns decisions); `DESIGN_REPO_MAP_v1.md` WP-05; Expected Solution inspection→Word DRAFT.

**Stack:** not locked. No claim that HITL = complete security.

---

## 0. Decision-maker answers (locked for freeze)

| Q | Architect asked | Decision |
|---|---|---|
| **1** | Who clicks export / approve pattern | **Re-approval rule:** the responsible **role/individual must explicitly approve again after every material change**, even if the artefact was already verified/checked. Prior accept does **not** survive edits. |
| **2** | H1 OCR vs DRAFT | **Yes — hard-block:** inspection spine does **not** treat extract as verified or proceed to KB-as-truth / clean DRAFT path until **H1** OCR confirm. |
| **3** | H7 contradiction | **Yes — must-work** (MOCK contradiction banner / choose-escalate OK until WP-22 detail). |
| **4** | H4 / editorial | **After editorial, approval required again** (invalidates prior H2). Worker may edit; Approver must re-accept before record-facing / export. |
| **5** | Sandbox / code decision | **Always human responsible** for the decision — machine pass ≠ decision. Explicit human gate on code deliverable acceptance. |
| **6** | PDF | **Yes:** generate PDF in-place ≠ export; **H3** applies to **download/export** of docx/PDF/zip off KWB. |

---

## Verdict

| Question | Answer |
|---|---|
| Directionally correct vs PS/WP-00? | **Yes** — human owns decisions; OCR→human; DRAFT gate |
| Missing before freeze? | **Yes** — re-approval / stale-accept state; material-change definition; code H-gate; H1 hard-block; H7 must-work |
| Overhyped risk? | **Yes** — “approve every change” if read as every UI tick → unusable rubber-stamp |
| Within solution bounds? | **Yes** if scoped to **gated artefacts + material content change** |
| Confidence architect as-written | **0.70** |
| Confidence after fills + your answers | **~0.86** |

---

## 1. Missing (must fill)

| ID | Gap | Why | Fill |
|---|---|---|---|
| **M1** | **Stale approval / re-approval** | Your Q1+Q4 | Acceptance binds to **artefact version** (content fingerprint). Any **material change** → status `stale` / `needs_reapproval`; prior accept **void** for record-facing & export |
| **M2** | **What counts as material change** | Else every autosave = Approver spam | Material = OCR text edit, DRAFT body/ substantive fields, findings used in note, export package contents, code artefact body. **Not** material: monitor refresh, routing log, grant TTL tick, UI theme |
| **M3** | **H1 hard-block** (your Q2) | Architect left optional banner | No KB-as-verified; no “clean” inspection DRAFT path until H1 accept |
| **M4** | **Editorial → re-H2** (your Q4) | Architect said worker edit ∉ H4 | Edit allowed; **H2 accept invalidated**; export blocked until re-accept |
| **M5** | **Code deliverable human gate H9→hard** (your Q5) | Architect left review-only | Explicit human accept/reject of code outcome as **decision**; sandbox pass only machine evidence |
| **M6** | **H7 must-work** (your Q3) | Was ambition-leaning | MOCK contradiction surface required in demo contract |
| **M7** | **Approval event audit** | WP-17 feed | Each accept/reject/stale/re-approve logs person, role, artefact version id |
| **M8** | **Agent/tool mid-edit** | Model rewrites DRAFT after H2 | Auto or tool edit = material change → stale (same as human edit) |
| **M9** | **Role-correct clicker** | “Individual” vs any click | Gate must be satisfied by **allowed role** for that gate (worker H1; Approver H2/H3 record-facing; Admin H5). Dual-role demo = same human, **labelled**, still explicit click |
| **M10** | **Export after stale** | W2 | H3 denied while any required upstream accept is stale/missing |

**Not missing:** wet-signature product; replacing plant DMS workflow; LangGraph as dependency.

---

## 2. Overhyped / attack → fix

| Attack | Overclaim | Reality / fix |
|---|---|---|
| **A1 Approve fatigue** | “Approve after every change” literally every keystroke | **Scope:** material change to **gated artefacts** only; debounce edits into one new version before re-approve |
| **A2 Rubber-stamp security** | More clicks = safer | Clicks without reading ≠ safety; still need air-gap, grants, Never list. HITL **helps**, not complete security |
| **A3 Dual-role theatre** | Same user clicking Approver after own edit looks strong | Allowed for demo if labelled; org paper keeps separation; audit shows role used |
| **A4 Machine “verified”** | Sandbox green = approved | Forbidden (your Q5); H9 human decision gate |
| **A5 Prior verify forever** | Once checked, always good | Explicitly **false** under re-approval rule |
| **A6 Interrupt pattern = product** | Adopting LangGraph means safe HITL | Pattern only — gates are product policy |
| **A7 H3 = security boundary alone** | Export gate stops all leaks | Chat residue / screen / `.md` still exist (WP-04) |
| **A8 Review-only remains** | Soft gates for citations | OK for non-decision skim; **must not** be used for H1/H2/H3/H9 decisions |

---

## 3. Bound check vs solution requirements

| Requirement | Hit? |
|---|---|
| Expected Solution: inspection → Word **DRAFT** + human verification | Yes — H1+H2+re-approve |
| Human ultimate decision-maker (WP-00) | Yes — Q5 reinforced |
| Never auto-file / auto-promote | Yes |
| OCR→human→KB (WP-00) | Yes — H1 hard-block |
| Export HITL (WP-04) | Yes — H3 + stale block |
| Grant ≠ HITL | Yes |
| Beyond solution? Full DMS e-sign / approve every log line | **Out** — refuse |

---

## 4. Adopt / add / refuse

| Source | Adopt | Why | Refuse |
|---|---|---|---|
| **LangGraph interrupt/resume** *pattern* | Checkpoint at hard gate; resume after accept | Matches H1/H2/H3/H9 | Lock runtime to LangGraph |
| **Hermes-like** approve before sensitive file ops | Behaviour for export/write | Matches H3/H4 | Hermes agent as product |
| **GBrain/Atlas** propose → human promote | Org skill / canonical | H6 | Auto-merge to SOP |
| **Document control practice** (Observed) | Approval binds to **revision**; edit ⇒ new rev needing re-approve | Your Q1/Q4 | Claiming ISO cert |
| **Our Add** | Gate table; stale-accept; material-change; code human decision; H7 MOCK | SIH KWB | Skill-restrictions-as-security; chat LGTM as Approver |

---

## 5. Disposition

**Applied.** DM answers §0 + fills M1–M10 → **`WP-05_FREEZE.md` rev 1.0**. Next: **WP-03**.

No stack lock. No app code.