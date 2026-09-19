# WP-24 model registry — adversarial red-team + Q5 decision

**Date:** 2026-09-18  
**Target:** `WP-24_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** §0  
**Extra DM rule:** Model card selection must **not** reshape workbench software; **orchestration** selects the card and **passes model parameters** into the task path.  
**Against:** Official Description/Expected Solution; WP-00 planes; WP-07 D4; repo map WP-24.

---

## 0. DM answers

| Q | Decision |
|---|---|
| **1** | Catalog **≥2** cards for demo routing proof |
| **2** | **`ocr` card required** + other capability models (LLM / VLM as needed) |
| **3** | **Add** + **disable** + **remove** all must |
| **4** | Workers see display names; **Admin-only** catalog edit |
| **5** | **Decide via adversarial** (below) |
| **6** | Demo soft cap **3** cards |
| **R0** | Workbench UI/features **model-agnostic**; orchestration passes `model_id` (+ params) |

---

## Q5 adversarial research → decision

| Option | Attack | Upside |
|---|---|---|
| A. Register only after `/v1/models` lists id | Blocks offline card prep when GPU offline; couples Admin to live server | No “enabled but unloadable” cards |
| B. Register anytime as enabled | Route hits missing weights → outage / HF temptation | Fast |
| C. Register anytime as **pending/disabled**; **enable** only when staged+live (or Admin force with fail-closed) | Slightly more states | Matches offline media + fail-closed |

**Decision (freeze):** **C.**  
- Admin may **add** card before weights are live → status `pending` or `disabled`.  
- **Enable** when runtime lists id **or** Admin marks ready after staging.  
- Gateway/orchestrator: **fail closed** if enabled id not serveable — **never** cloud fallback.  
- Workbench does not change screens based on card presence beyond catalog Admin UI + routing log.

---

## Verdict

| | |
|---|---|
| Missing | M1–M10 (agnostic workbench, param pass, pending state, OCR required, cap 3, remove symmetry) |
| Overhyped | `/v1/models` = card; more cards = better product; card drives UI features |
| Confidence after freeze | **~0.88** → GO WP-06 |

---

## 1. Missing → fill

| ID | Gap | Fill |
|---|---|---|
| **M1** | Model-agnostic workbench | Jobs, HITL, grants, tools **unchanged** by which card is selected |
| **M2** | Orchestration owns selection | WP-06/orchestrator chooses card; passes `model_id` (+ allowed params) to gateway |
| **M3** | Params boundary | Temperature/etc. from card defaults or task policy — not scattered UI forks per model brand |
| **M4** | Pending/disabled/enabled | Q5 decision C |
| **M5** | OCR card mandatory in catalog kinds | Plus LLM; VLM as needed for vision |
| **M6** | Demo ≤3 cards soft cap | ≥2 for proof |
| **M7** | Add/disable/remove | All three |
| **M8** | Unregistered id | Fail closed |
| **M9** | Public base_url | Never on card |
| **M10** | Card ≠ weight path in workbench | Runtime owns files |

---

## 2. Overhyped

| Attack | Fix |
|---|---|
| **A1** Dropdown = auto-select | Log proof via orchestrator (WP-00) |
| **A2** Live model list = policy | Cards hold task_tags/modalities |
| **A3** UI themes per model | Forbidden — agnostic workbench |
| **A4** 3 cards = full multimodal org | Soft demo cap; org may exceed |
| **A5** Enable = loaded in VRAM | WP-10 load policy |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| Continue/OpenHands/LM Studio catalog pattern | Ollama-as-workbench |
| `/v1/models` liveness only | HF-in-UI; cloud providers |
| Our card fields | Hardcoded model id |

---

## 4. Disposition

**Applied.** → `WP-24_FREEZE.md` rev 1.0. Verify: `WP-24_FREEZE_VERIFY.md`. Confidence **0.90**. **GO** → **WP-06**.
