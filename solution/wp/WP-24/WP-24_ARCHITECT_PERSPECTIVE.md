# WP-24 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 (planes, add/remove, open-weight, fail-closed)  
**Status:** **SUPERSEDED by `WP-24_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-24_REDTEAM.md`.  
**Job of WP-24:** Workbench **Model Card catalog** for LLM / VLM / OCR (and related): **add and remove** without redesigning KWB; open-weight on-prem only; gateway routes only to **registered** ids; `GET /v1/models` is **liveness**, not a card.

**Sources:** Official Title/Description/Expected Solution; WP-00 §3/§6/§7; User remove; repo map Continue/OpenHands/LM Studio catalog pattern; prior Model Cards paper (re-confirm).

---

## One sentence (proposed)

Models are **pluggable catalog entities**: Admin stages weights on the runtime and **registers/removes Model Cards** in KWB — the workbench never embeds weights, never pulls Hugging Face at runtime, and **fails closed** if a route asks for an unregistered id.

---

## 1. Card vs runtime vs dropdown

| Concept | Owns | Is not |
|---|---|---|
| **Model Card** (WP-24) | id, modalities, task suitability, context hints, tools vision flags, open-weight attestation | Weight files |
| **Runtime** (WP-10) | Load/unload weights; serve `/v1` | Product policy |
| **`GET /v1/models`** | Live ids currently loaded | Full card (no roles/HITL/classification) |
| **User dropdown** | Optional UX | **Not** Expected Solution auto-select proof |

Hardcoded `qwen-coder` in workbench code = redesign (forbidden pattern).

---

## 2. Model Card minimum fields (proposed — brand-free)

| Field | Purpose |
|---|---|
| `model_id` | Stable id used in gateway requests + routing log |
| `display_name` | UI |
| `kind` | `llm` \| `vlm` \| `ocr` \| `other` |
| `modalities` | text / image / … |
| `task_tags` | e.g. coding, summary, vision, ocr |
| `open_weight` | must be true for allow |
| `base_url` ref | Points at **local** runtime endpoint (not public) |
| `context_window_hint` | For WP-21 packing |
| `status` | `registered` \| `disabled` \| `removed` |
| `notes` / card version | Audit |

Exact JSON schema brand not locked; fields above are contractual.

---

## 3. Add / remove lifecycle

```
Offline media → stage weights on runtime (WP-10/19)
  → Admin registers Model Card in KWB catalog
  → router/gateway may select id
  → Admin disables or removes card (and runtime may unload)
  → no workbench code change
```

**Remove** is mandatory symmetry of add (User). Soft-disable vs hard-remove both allowed.

---

## 4. Demo vs org

| | Demo | Org |
|---|---|---|
| Cards registered | **≥2** distinct `model_id`s available for routing proof (WP-00/01) | Many |
| Single-model run | OK for one specialist path (WP-07 D4) | Prefer distinct when possible |
| Intake | Pre-staged + pre-registered OK | Offline media + Admin UX |
| Cloud providers | Never | Never |

Routing proof: running **≥2 task types** yields **≥2 model ids** in the log when auto-select is demonstrated — catalog must make that possible (two cards), even if some demo paths use one id.

---

## 5. Fail-closed

- Route/gateway request with unknown / disabled `model_id` → **fail closed** (no internet fallback, no silent rewrite to public `base_url`).  
- Missing required card for a must job → fail or degrade per WP-00 — no HF pull.

---

## 6. Must / ambition / deferred / never (proposed)

### Must-work

1. Card catalog with add **and** remove/disable.  
2. Open-weight + local `base_url` only.  
3. ≥2 cards registrable for auto-select proof.  
4. LLM + (VLM and/or OCR) card kinds representable (vision/OCR path).  
5. Gateway/router uses only registered ids.  
6. `GET /v1/models` ≠ replace cards.  
7. Offline stage; no in-app HF download.

### Org-ambition

- Rich card UI; capability matrices; per-role allowed cards; A/B card versions.

### Deferred

- Training/LoRA as product; multi-cloud routers.

### Never

- Cloud LLM as card `base_url`.  
- HF/huggingface download in KWB UI.  
- LiteLLM public provider list as brain.  
- Ollama-as-the-workbench.  
- Hardcoded model id as product lock.  
- Treat live `/v1/models` list as full policy card.

---

## 7. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | Continue/OpenHands/LM Studio *catalog entry* pattern; Dify model-management *UI idea*; Ollama/vLLM `/v1/models` as **liveness only** |
| **Add** | Card schema fields; add+remove; open-weight gate; fail-closed unregistered |
| **Refuse** | HF-in-UI; cloud providers; Ollama-as-KWB; hardcoded model |

---

## 8. Boundary

| Topic | Later |
|---|---|
| Load/unload VRAM policy | **WP-10** |
| Task → card routing | **WP-06** |
| Offline media ops polish | **WP-19** |
| Gateway schema check | **WP-09** |

---

## 9. Open questions for decision maker

1. **Demo card count:** pre-register **exactly 2** vs **≥2** — confirm **≥2**?  
2. **OCR engine:** separate `ocr` card kind (recommended) vs only VLM card for scans?  
3. **Disable vs remove:** both required in must-work (recommended) — yes?  
4. **Worker visibility:** workers see display names; only Admin edits catalog — yes?  
5. **Card without weights staged:** allow register-as-disabled, or refuse register until runtime lists id?  
6. **Max cards (demo):** soft cap (e.g. 5) or unset?

---

## 10. Next after your decisions

**Done.** Frozen as `WP-24_FREEZE.md` rev 1.0. Next: **WP-06**.
