# WP-10 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-09 / WP-24 (WP-06 failover / one-load; WP-16 jail ≠ GPU; WP-19 offline media peer)  
**Status:** **SUPERSEDED by `WP-10_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-10_REDTEAM.md`. Verify: `WP-10_FREEZE_VERIFY.md`.  
**Job of WP-10:** **Runtime (GPU + weights)** — stage and serve **open-weight** files on **workstation or server**; expose local **`/v1`**; own **load/unload** and **hardware probe**; honour “multiple models at once” **honestly** (catalog ≠ all VRAM-resident); never pull weights through KWB from the internet.

**Sources:** Official Description (org GPU server; multiple open-weight at once) + Expected Solution (workstation or server; mid-range GPU; smaller model if 120B absent); WP-00 planes; WP-24 enable ≠ loaded; WP-09 one load attempt then fail-closed; follow-list WP-10.

---

## One sentence (proposed)

The **runtime** is the hardware plane that **stores and serves** open-weight models over local `/v1`: it **loads/unloads** under explicit policy, reports **what is live**, and can be swapped (`base_url`) **without redesigning** the workbench — it does **not** own cards, grants, packing, or plant policy.

---

## 1. Ownership (locked upstream)

| Actor | Owns | Not |
|---|---|---|
| **Runtime (WP-10)** | Weight files on disk; `/v1` server; load/unload; VRAM/CPU scheduling; hardware probe | Model Card policy; job routing; prompts; HITL |
| **Cards (WP-24)** | Which ids are allowed / enabled | Guaranteeing VRAM residency |
| **Gateway (WP-09)** | Verify + forward; one load request | CUDA |
| **Orchestrator (WP-06)** | Which card to ask for; failover | Talking CUDA directly |
| **Sandbox (WP-16)** | Code jail | Inference process |

**Forbidden:** Workbench embedding weight blobs; in-app HF download; treating “3 cards enabled” as “3×70B in VRAM”; wrapping GPU inside the code sandbox.

---

## 2. Planes reminder

```
Workbench (software) --gateway--> Runtime (GPU/CPU + weights + /v1)
                                      ↑
                         offline media staging (Admin / WP-19)
```

Change laptop ↔ org GPU server = point gateway/card `endpoint_ref` at new local runtime — **no workbench redesign** (WP-00).

---

## 3. “Multiple models at once” (honesty)

| Meaning | Must-work interpretation |
|---|---|
| **Catalog at once** | ≥2 cards registered/enabled; routing can select different ids (WP-24/06) |
| **VRAM at once** | Only as many weights as fit — **sequential load/unload** OK on mid-range GPU |
| **Serve at once** | Runtime may keep **one** (or few) ids **resident**; others on disk until load |

**Overclaim to refuse:** Simultaneous full residency of all catalogued large models on mid-range demo GPU.

Org with bigger hardware may keep more resident — same API, different capacity.

---

## 4. Load / unload policy (proposed)

| Trigger | Behaviour |
|---|---|
| Gateway **one load attempt** (WP-09 D4) | Runtime tries load for that `model_id` if staged; success → appear on `/v1/models`; fail → error |
| Admin explicit load/unload | Org ops; ambition UI |
| OOM / unfit | Fail closed; do not partial-corrupt; log |
| Swap | Unload cold id (LRU or Admin pin) then load requested — **logged** |
| Enable card (WP-24) | Does **not** by itself load VRAM |

**Pinning:** Admin may mark a demo “always warm” id (ambition/org). Demo may pre-load before jury.

---

## 5. Hardware probe (proposed)

| Fact | Rule |
|---|---|
| Where probe lives | **Runtime / host** (`nvidia-smi` or equivalent) — **not** an OpenAI API field |
| What workbench sees | Optional capacity summary via local sidecar/status — brand-free |
| What it decides | **Advisory** for Admin / logs — does **not** auto-download models or break Never |
| Venue mid-range / no 120B | Use **smaller open-weight** already staged (Expected Solution) |

---

## 6. Staging & offline

```
Approved offline media (outside KWB download)
  → Admin stages weight files on runtime disk
  → runtime can load id
  → card enable when ready (WP-24)
```

**Never:** HF/huggingface pull from workbench or runtime “for convenience” during operation.

---

## 7. Demo vs org

| | Demo | Org |
|---|---|---|
| Host | Workstation **or** single server | Org GPU server (may be multi-GPU later) |
| Models | Smaller open-weight OK; ≤3 cards; ≥2 for proof | Many staged; resident subset |
| At once | Sequential load OK; pre-warm for proof script | Capacity-based residency |
| Probe | Optional visible GPU name/VRAM in log | Ops dashboards ambition |
| Binary | Any local `/v1` server (not locked) | Same |

---

## 8. Must / ambition / deferred / never (proposed)

### Must-work

1. Local `/v1` serve for registered ids; liveness via `/v1/models`.  
2. Stage weights offline; no internet pull in operation.  
3. Load/unload policy; enable ≠ loaded.  
4. Honour gateway one-load attempt; fail closed on OOM/missing files.  
5. Workstation **or** server; mid-range + smaller model OK.  
6. Honest “at once” = catalog multi-id; VRAM may be sequential.  
7. Jail ≠ GPU process.  
8. Swap `base_url` / host without workbench redesign.

### Org-ambition

- Multi-GPU; pinned warm set; Admin load UI; richer probe metrics; model quantisation matrix.

### Deferred

- Training/LoRA as product; cluster schedulers; cloud burst.

### Never

- Weights inside workbench install as the product brain.  
- HF-in-operation.  
- Claim all enabled cards always VRAM-resident.  
- Runtime decides plant safety / grants.  
- Inference inside sandbox jail.

---

## 9. Adopt / add / refuse

| | |
|---|---|
| **Adopt** | llama.cpp / vLLM / Ollama / LM Studio / SGLang as **interchangeable `/v1` servers** (pattern) |
| **Add** | Explicit load policy; catalog vs resident honesty; probe-on-host; one-load contract with WP-09 |
| **Refuse** | Runtime brand lock; workbench-bundled-only weights; “venue will give 120B” as plan |

---

## 10. Boundaries

| Topic | Owner |
|---|---|
| Card catalog / enable | **WP-24** |
| Verify before forward | **WP-09** |
| Which id to request | **WP-06** |
| Offline media ops polish | **WP-19** |
| Context window packing | **WP-21** |
| Sandbox | **WP-16** |

---

## 11. Open questions for decision maker

1. **Resident set (demo):** Pre-load **one** warm model and load others on demand, or pre-load **all ≤3** demo cards if they fit?  
2. **Unload policy:** On VRAM pressure, **LRU unload** automatic, or **fail load** until Admin unloads?  
3. **CPU fallback:** If GPU unfit/missing, allow **CPU `/v1`** for tiny models (demo survival), or **GPU-required** fail-closed?  
4. **Probe visibility:** Must Audience B/jury see **VRAM / GPU name** in log or monitor (must-work), or runtime-internal only?  
5. **Multi-process:** One runtime process serving all ids, or **one process per model** allowed (still one gateway `endpoint_ref` or many cards)?  
6. **Quantisation:** Demo may use **quantised** open-weight builds (GGUF/etc.) as first-class, or prefer “full” weights only in paper language?

---

## 12. Next after your decisions

**Done.** Frozen as `WP-10_FREEZE.md` rev 1.0. Next: **WP-12**.
