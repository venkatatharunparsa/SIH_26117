# Hardware vs software — model ownership (WP-00 clarification)

**Date:** 2026-09-17  
**Status:** Clarification for WP-00. Aligns with user suggestion. Not a full WP-00 freeze.

---

## Your question

Does the **software** hold full model **weights**, or only a **name / reference**, with weights on **hardware**?

## Answer (agreed direction)

**Weights live on the hardware / runtime only.**  
**Software holds a model reference (catalog / Model Card), not the GGUF/safetensors files.**

| Plane | Owns | Does **not** own |
|---|---|---|
| **Workbench (software)** | `base_url`, auth, **model id**, capability flags (vision/tools/roles), routing rules, agents, tools, HITL, RAG, plugins, skill library | Weight files, CUDA, VRAM load/unload |
| **Runtime (hardware + serving)** | GPU/CPU, staged **open-weight** files, OpenAI-compatible `/v1` server, load/unload | Workbench UI, Word templates, plant ACL, HITL policy |

When the workbench needs inference it sends a **valid request** such as: “run `model_id=X` with these messages.” The runtime loads or already has X. The workbench never ships X inside the app binary.

---

## Why this matches the PS

- **Not locked to one model** / **add without redesigning the system** → software must not bake weights or hardcode one path.  
- **Workstation or server** / **smaller model if 120B absent** → change runtime (or which ids are staged), not rewrite the workbench.  
- **Software** category → product is the workbench; GPU is infrastructure.

---

## Your suggestion (accepted as design intent)

1. Model **weights** → hardware / runtime only.  
2. Software → **model reference** (registry / cards): id, display name, what tasks it may serve, vision/tools flags.  
3. Hardware changes (new GPU, new venue, new weights, remove a model) → software **adopts** by refreshing the catalog / pointing `base_url` — **no workbench redesign**.

Add a model = stage weights on runtime (offline) + register/update the card.  
Remove a model = unregister the card (software stops routing to it) + unload/delete weights on runtime.

---

## What “adopt hardware change” means in practice

| Hardware change | Software change required? |
|---|---|
| Swap laptop GPU ↔ plant/venue server | No rebuild. Point `base_url` at the new `/v1`. |
| Stage a new open-weight id | No rebuild. Add/update **Model Card**; runtime lists the id. |
| Remove a model | No rebuild. Drop card; stop routing. |
| Mid-range only; no 120B | No rebuild. Cards point at smaller ids that fit. |

Software **does** need a card that matches reality (do not route vision to a text-only id). That is **config**, not a code fork.

---

## Trap to avoid

- Shipping GGUF inside the workbench installer → locks hardware and breaks “add without redesign.”  
- Software that only stores a pretty name with no link to a live runtime catalog → routing to dead ids.  
- Treating `/v1` cloud OpenAI as “just another reference” → fails air-gap.

---

## Freeze later

This intent belongs in **WP-00** (planes) and freezes in detail at **WP-24** (registry) + **WP-10** (runtime). Stack brand (Ollama vs vLLM vs llama.cpp) still **not** locked.
