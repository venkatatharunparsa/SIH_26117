# WP-10 Runtime (GPU + weights) — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-09 / WP-24.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-10_ARCHITECT_PERSPECTIVE.md`, `WP-10_REDTEAM.md`, **DM 2026-09-18** (shallow hardware; connect provided models/URL; pre-load 2; LRU; org GPU-only / demo GPU+CPU; show GPU/VRAM; one runtime + single API key multiplex; quantised builds).  
**Findings SoT:** `WP-10_REDTEAM.md`  
**Verify SoT:** `WP-10_FREEZE_VERIFY.md`  
**Product:** **KWB**

**Runtime binary brand:** not locked.

---

## 1. One-sentence contract

The **runtime** is a **shallow hardware plane**: it stages **open-weight** (including **quantised**) weights, serves **many model ids** from **one local `/v1`** behind **one API key**, **pre-loads two** for demo, **LRU-unloads** under pressure, reports **GPU name/VRAM** honestly, and is reached only via the gateway — KWB **connects** to a configured local URL/catalog and **picks models**; it is **not** a deep CUDA product and **not** cloud OpenRouter.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Shallow serve/load/probe contract | Deep hardware redesign as the SIH product |
| Connect to **local** provided URL + capabilities → cards | Trust any public URL; auto-enable without Admin |
| One runtime, one key, many `model` ids (**local** OpenRouter-*shape*) | openrouter.ai / cloud provider mesh |
| Catalog many; warm **2** (demo); rest on demand | All enabled cards always in VRAM |
| Org **GPU-only** | Org may run CPU-only as must-work |
| Demo **GPU+CPU** hybrid OK | Fake NVIDIA name when on CPU |
| Quantised = valid open-weight | Quant = secret full-quality 120B |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D0** | **Shallow hardware:** design for **configurable local endpoint + model catalog**; optional offline deploy guide; **pick proper models** into WP-24 cards — no deep CUDA freeze |
| **D1** | Demo **pre-load 2** models (warm); others on demand (WP-09 one-load) |
| **D2** | **LRU auto-unload** when admitting a load that needs space; **never** unload an **in-flight** id; pin warm pair during auto-select proof |
| **D3** | **Org profile: GPU-only** inference. **Demo profile: GPU + CPU combined** allowed |
| **D4** | **Must-work:** expose **GPU name + VRAM** (or honest `CPU` / `unknown`) to jury via log/monitor |
| **D5** | **One runtime** serves all ids; **single API key** authenticates access; selection = `model` field (local multiplex) |
| **D6** | **Quantised** open-weight builds are first-class |
| **D7** | Enable ≠ loaded (WP-24); jail ≠ GPU (WP-16); no HF-in-operation |

---

## 4. Connect / catalog model (not deep hardware)

```
Local source of truth for what can run:
  (A) Admin-staged weights on disk  and/or
  (B) Venue/org-published list: model_id, capabilities, local URL
       → map into Model Cards (WP-24) + endpoint_ref
       → Admin enable
       → orchestrator picks; gateway verifies; runtime serves
```

- Changing URL/host = config — **no workbench redesign**.  
- Provided capabilities = **routing hints**, not security bypass.  
- Deploy-local-hardware help = **documentation / runbook** (WP-19 adjacent) — not in-app internet download.

---

## 5. Single-key multi-model (local OpenRouter-shape)

| Rule | Must |
|---|---|
| Endpoint | One (or card-local) **allowlisted** `/v1` base |
| Auth | Single shared Bearer (demo) / org secret (WP-09) |
| Model select | Request `model` = card `model_id` |
| Still required | WP-09 full verify (card, grant, local, size, …) |
| Forbidden | Forwarding that key to **public** multi-provider routers |

---

## 6. Load / unload

| Event | Behaviour |
|---|---|
| Demo start | **Pre-load 2** configured warm ids |
| Request for cold id | WP-09 one-load → runtime load; LRU evict coldest non-pinned / non-in-flight if needed |
| OOM / missing files | Fail closed; log |
| Auto-select proof | Keep both warm ids pinned for script duration |
| Card enable | Does not load by itself |

---

## 7. Org vs demo compute

| | Org | Demo |
|---|---|---|
| Device | **GPU required** for must-work inference | **GPU and/or CPU** |
| Warm | Capacity-based; ≥2 when proving multi-id | **2** pre-loaded |
| Probe display | GPU name/VRAM | Same; if CPU-only path, show **CPU** honestly |

---

## 8. Hardware probe (must-work display)

- Probe on **host/runtime** (not OpenAI schema).  
- Jury-visible: **device name + VRAM** (or `unknown` / `CPU`).  
- Advisory only — no auto cloud fetch.  
- Air-gapped probe (no WAN).

---

## 9. Never

- Cloud OpenRouter / public provider mesh.  
- HF/internet weight pull during operation.  
- Deep-hardware product identity.  
- Claim all catalog ids VRAM-resident.  
- Unload in-flight model.  
- Org must-work on CPU-only.  
- Fake GPU telemetry.  
- Inference inside sandbox jail.  
- Runtime decides grants / plant safety.

---

## 10. Must / ambition / deferred / never

### Must-work

1. Local `/v1` multi-id serve behind one key.  
2. Quantised open-weight OK; offline stage.  
3. Pre-load 2; LRU; one-load cold path.  
4. Org GPU-only; demo hybrid.  
5. Show device/VRAM (honest).  
6. Connect via configured URL + cards; shallow contract.  
7. Enable ≠ loaded; fail closed on OOM/missing.  
8. Workstation or server; mid-range + smaller/quant OK.

### Org-ambition

- Multi-GPU; Admin pin UI; richer metrics; dual secrets.

### Deferred

- Training/LoRA product; cluster schedulers.

### Never

- §9.

---

## 11. PS coverage (this WP’s job)

| PS clause | WP-10 |
|---|---|
| Multiple open-weight; not locked to one; addable without redesign | **Yes** |
| At once (honest catalog vs VRAM) | **Yes** |
| Own GPU server (org) / workstation or server mid-range demo | **Yes** |
| Smaller model if no 120B; on-prem serve | **Yes** |
| Auto-select / agent / sandbox / Word / KB / WAN monitor | **Other WPs** (not claimed here) |

---

## 12. Demo acceptance

1. Two warm models listed live; third (if any) loads on demand or proof uses the two.  
2. Auto-select proof ≥2 task types → ≥2 ids (with warm pair).  
3. Single Bearer + `model` field switches ids.  
4. Jury sees device/VRAM (or CPU).  
5. No public OpenRouter/HF calls.  
6. LRU does not kill in-flight request.

---

## 13. Next

**WP-12** — Validation + security gates.

---

## 14. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze: shallow HW; local multiplex key; pre-load 2; LRU; org GPU / demo hybrid; quant; probe |

**Confidence:** **0.88**
