# WP-24 Model registry (pluggable models) — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 (and WP-07 demo/org model-log rules).  
**Depends on:** WP-00 (must not contradict).  
**Inputs:** `WP-24_ARCHITECT_PERSPECTIVE.md`, `WP-24_REDTEAM.md`, **DM 2026-09-18** (≥2 cards; OCR+other kinds; add/disable/remove; Admin-only edit; demo cap 3; workbench model-agnostic / orchestration passes params; Q5 = pending then enable).  
**Findings SoT:** `WP-24_REDTEAM.md`  
**Verify SoT:** `WP-24_FREEZE_VERIFY.md` (claim ledger + completeness)  
**Product:** **KWB**

**Stack / serving brand:** not locked.

---

## 1. One-sentence contract

KWB keeps a **Model Card catalog** (add / disable / remove) for **open-weight** local models; **orchestration** selects the card for a task and **passes `model_id` (+ parameters)** downstream — the rest of the workbench stays **model-agnostic**; weights live on the **runtime**; unregistered or unserveable ids **fail closed** with **no** cloud/HF fallback.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Cards are catalog metadata | Cards embed weight files in workbench |
| Orchestrator picks model | Each model forks different workbench features/UI |
| `/v1/models` = liveness | `/v1/models` = full Model Card |
| Demo ≤3 cards soft | Org forever capped at 3 |
| Enable ≠ necessarily VRAM-resident | Enable = always loaded (WP-10) |

---

## 3. Closed decisions (DM + Q5)

| ID | Decision |
|---|---|
| **D1** | Demo catalog supports **≥2** distinct `model_id`s for auto-select proof |
| **D2** | **`ocr` card kind required**; also **LLM** (and **VLM** when vision path needs it) |
| **D3** | **Add**, **disable**, and **remove** all must-work |
| **D4** | Workers see display names; **Admin-only** catalog mutate |
| **D5** | Cards may be **added pending/disabled** before weights live; **enable** when runtime lists id or Admin marks ready; invoke **fail-closed** if not serveable |
| **D6** | Demo soft cap **3** registered cards (org may exceed) |
| **D7** | **Workbench software is model-agnostic**; orchestration owns selection and passes model parameters |

---

## 4. Model-agnostic workbench (critical)

| Layer | May depend on card? |
|---|---|
| Jobs, HITL, grants, tools, RAG, UI chrome | **No** — same paths for any registered card |
| Orchestrator / router (WP-06) | **Yes** — chooses `model_id` from cards + task |
| Gateway (WP-09) | Validates id ∈ catalog + local `base_url`; forwards params |
| Runtime (WP-10) | Loads/serves weights for that id |

**Forbidden:** per-model special-case workbench modules, feature flags that rewrite product behaviour by brand name, or UI that only exists for one card.

Orchestration **passes** at least: `model_id`, and task-allowed generation params (defaults may live on the card). Exact param set not brand-locked.

---

## 5. Card vs runtime vs live list

| | Role |
|---|---|
| **Model Card** | Policy/catalog: kind, modalities, task_tags, open_weight, local endpoint ref, defaults, status |
| **Runtime** | Weight files + `/v1` serve/load/unload |
| **`GET /v1/models`** | Which ids are **live now** — not a substitute for cards |

Hardcoded model id in workbench code = redesign pattern → **Never**.

---

## 6. Model Card minimum fields

| Field | Required |
|---|---|
| `model_id` | Yes |
| `display_name` | Yes |
| `kind` | `llm` \| `vlm` \| `ocr` \| `other` |
| `modalities` | Yes |
| `task_tags` | Yes (routing hints) |
| `open_weight` | Yes — must be true to enable |
| `endpoint_ref` | Local runtime only |
| `param_defaults` | Optional (temp, etc.) |
| `status` | `pending` \| `disabled` \| `enabled` \| `removed` |
| `card_version` | Yes for audit |

---

## 7. Lifecycle

```
Offline stage weights (WP-19/10)
  → Admin adds card (pending/disabled OK)
  → enable when live or Admin ready
  → orchestrator selects enabled card → passes model_id + params
  → gateway fail-closed if missing/disabled/unserveable
  → Admin disable or remove (no redesign)
```

Demo: pre-stage + pre-register ≤**3** cards, **≥2** enabled for routing proof script.

---

## 8. Kinds required

| Kind | Must-work |
|---|---|
| **LLM** | Yes (≥1) |
| **OCR** | Yes (≥1 card) |
| **VLM** | Required when demo/org vision path uses VLM (recommended ≥1 if multimodal beyond classical OCR) |

---

## 9. Fail-closed / Never

- Unknown, disabled, removed, or unserveable `model_id` → **fail closed**.  
- No internet fallback; no rewrite to public `base_url`.  
- No HF/download-in-UI.  
- No cloud provider cards.  
- No Ollama-as-the-workbench.  
- Empty catalog cannot run must jobs that need a model.

---

## 10. Must / ambition / deferred / never

### Must-work

1. Catalog add / disable / remove.  
2. Open-weight local only.  
3. ≥2 cards; demo soft cap 3.  
4. OCR + LLM kinds; VLM as needed.  
5. Pending→enable rule (D5).  
6. Model-agnostic workbench; orchestration passes params (D7).  
7. Gateway uses registered ids only.  
8. `/v1/models` ≠ card.

### Org-ambition

- Rich Admin UI; per-role allowed cards; more than 3 cards; card A/B versions.

### Deferred

- Training/LoRA product; multi-cloud.

### Never

- Cloud `base_url`; HF-in-UI; workbench forked per model brand; hardcoded lock-in model; treat live list as card.

---

## 11. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Continue/OpenHands/LM Studio *catalog* pattern | Add without redesign |
| **Adopt** | `/v1/models` as liveness only | Honest split |
| **Add** | Card schema; agnostic workbench rule; pending/enable; OCR required; cap 3 | DM / red-team |
| **Refuse** | HF-in-UI; cloud providers; Ollama-as-KWB; LiteLLM public provider brain |

---

## 12. Demo acceptance

1. Catalog shows ≤3 cards, ≥2 distinct ids.  
2. OCR card present; LLM present.  
3. Auto-select proof across ≥2 task types → ≥2 ids in log (when demonstrating routing).  
4. Remove or disable a card → routes to it fail-closed.  
5. Same inspect/code UI works regardless of which eligible card orchestration picks.  
6. No public base_url / no HF fetch.

---

## 13. Next

**WP-06** — Orchestration + task routing (implements card selection + param pass).

---

## 14. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze + Q5 pending/enable + model-agnostic orchestration rule |

**Confidence:** **0.90** (after verify pass)
