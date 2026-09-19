# WP-09 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-06 / WP-21 / WP-24 (and WP-10 as runtime peer — freeze after this)  
**Status:** **SUPERSEDED by `WP-09_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-09_REDTEAM.md`. Verify: `WP-09_FREEZE_VERIFY.md`.  
**Job of WP-09:** **LLM gateway** — the **software socket** between packer output and local runtime: schema-valid `/v1` only; **auth**, **timeout**, **size**; **Model Card** check; **fail closed**; **never** rewrite to a public/cloud `base_url`; vision as **`data:` only**. Gateway ≠ CUDA ≠ MCP bus ≠ orchestrator brain.

**Sources:** Official Description (own GPU server; nothing leaves); WP-00 §7 Valid gateway + fail-closed; User “valid requests”; WP-06 passes `model_id`+params (does not replace gateway); WP-21 PackManifest / may reject oversize; WP-24 card must be on catalog + enabled + local endpoint; prior LCD paper (`POST /v1/chat/completions`, `GET /v1/models`, Bearer) — re-confirm at freeze; repo map Continue/OpenHands client triad + offline-only proxy pattern.

---

## One sentence (proposed)

The **gateway** is the only path to the runtime: it accepts **schema-valid**, **card-checked**, **size/timeout-bounded** local `/v1` calls built by the packer, and **fails closed** on mismatch — it does **not** load weights, route jobs, or assemble prompts.

---

## 1. Ownership (locked by prior freezes)

| Actor | Role | Not owner of |
|---|---|---|
| **Orchestrator (WP-06)** | Emits intent: `model_id` + params + step need | Wire schema; CUDA; packing |
| **Packer (WP-21)** | Builds messages + PackManifest; grant/trust/size policy | Talking to GPU; rewriting endpoint |
| **Gateway (WP-09)** | Auth, schema, size ceiling, timeout, card check, forward to local `base_url` | Job routing; VRAM load; MCP |
| **Runtime (WP-10)** | Serve weights; load/unload; answer `/v1` | Product policy; plant ACL |
| **Model Card catalog (WP-24)** | Registered ids, enabled status, local endpoint ref | Live process list alone as policy |

**Forbidden:** Orchestrator or UI calling runtime with a public URL; gateway “helpfully” falling over to WAN; treating `GET /v1/models` as the card catalog; gateway as plugin/MCP bus.

---

## 2. Must schema (proposed LCD)

Brand-free OpenAI-compatible **shape** (not a product lock on one server binary):

| Surface | Must |
|---|---|
| **`POST /v1/chat/completions`** | Required for agent/chat/vision-as-message path |
| **`GET /v1/models`** | **Liveness** only — ids currently serveable; **not** full Model Card |
| **Request body** | `model` (= `model_id`), `messages` (array), optional generation params from allow-list |
| **Vision** | Image parts as **`data:` / local bytes only** — reject `http(s):` image URLs |
| **Auth** | Bearer (or equivalent local secret) between workbench↔gateway↔runtime as configured |
| **Response** | Standard completion shape; errors do not trigger cloud retry |

**Out of WP-09:** Exact OpenAI SDK version; streaming vs non-streaming product default (open Q); tool_choice LCD detail if runtime lacks tools (open Q / re-confirm).

---

## 3. Checks before forward (proposed order)

```
inbound request (from packer/orchestrator path)
  → auth present & valid — else deny
  → schema-valid /v1 chat body — else deny
  → model_id ∈ WP-24 catalog ∧ status=enabled ∧ open_weight ∧ local endpoint_ref
  → endpoint_ref is local (no public/cloud base_url rewrite) — else deny
  → size ≤ Admin/demo ceiling (messages + optional PackManifest estimate) — else deny
  → capability flags compatible with card/runtime LCD (e.g. no forbidden tool_choice) — else deny
  → apply timeout
  → forward to local runtime base_url only
  → on runtime miss / timeout / 4xx/5xx → fail closed (no WAN failover)
```

**Fail closed** means: stop or degrade safely; **log**; **never** silent substitute of another public model.

---

## 4. Auth, timeout, size (proposed)

| Knob | Demo proposal | Org |
|---|---|---|
| **Auth** | Shared local Bearer between workbench and gateway (and gateway→runtime if split) | Same + rotation / per-plane secrets |
| **Timeout** | Hard wall-clock per call (e.g. tens of seconds–few minutes — freeze number) | Admin-tunable ceiling |
| **Size** | Reject over Admin max chars/tokens; may use PackManifest `token_est` + reserve | Same + per-card window hint |
| **Oversize** | Fail closed **or** mandatory shrink already done by packer — gateway is last gate | Same |

Gateway may reject packs that packer mis-estimated (WP-21). Packer remains policy owner of *what* enters; gateway owns *wire safety*.

---

## 5. Card check (implements WP-24)

| Rule | Must |
|---|---|
| `model` in request | Equals a **registered** `model_id` |
| Status | **enabled** — disabled/removed → deny |
| Endpoint | Card’s `base_url` / `endpoint_ref` is **local** only |
| Unserveable | Not loaded / runtime 404 → **fail closed** (WP-10 load policy may retry load — open Q), **no** cloud rewrite |
| Liveness list | `GET /v1/models` may show fewer ids than catalog — catalog remains source of **policy** |

---

## 6. Never list (gateway)

- Rewrite / failover to public or cloud `base_url`.  
- Hugging Face / internet pull on miss.  
- Accept remote image URLs in messages.  
- Skip card check because “runtime listed it.”  
- Act as MCP/plugin bus.  
- Load/unload VRAM (that is WP-10).  
- Assemble or widen prompts (that is WP-21).  
- Decide plant safety / HITL outcomes.  
- Treat gateway logs as plant SoR.

---

## 7. Demo vs org

| | Demo | Org |
|---|---|---|
| Topology | Workbench + runtime often same box; gateway still a **logical** socket | Workbench → gateway hop → org GPU server |
| Cards | ≥2 registered; invoke only enabled local ids | Many cards; same checks |
| Proof | Invalid schema / unknown id / oversize → **visible deny**; WAN=0 on model path | Same + ops metrics |
| Streaming | Optional | Ambition |
| Multi-runtime | Single local endpoint OK | Multiple local refs via cards — still no WAN |

---

## 8. Must / ambition / deferred / never (proposed)

### Must-work

1. Only schema-valid local `/v1` chat (+ models liveness).  
2. Auth + timeout + size gates.  
3. Card check: registered, enabled, local endpoint.  
4. Fail closed — no cloud rewrite, no remote vision URLs.  
5. Orchestrator/packer cannot bypass gateway to talk CUDA/runtime “raw” in product path.  
6. Gateway ≠ MCP; gateway ≠ CUDA.  
7. Log deny reasons (schema / auth / card / size / timeout) for Audience B / audit feed (WP-17 detail later).

### Org-ambition

- Streaming; multi-endpoint local pool; Admin gateway debugger; finer capability matrices per card.

### Deferred

- Certified mTLS mesh; WAN-aware enterprise API gateways; provider failover products.

### Never

- Cloud brain / public `base_url`.  
- LiteLLM-style public provider list as product brain.  
- Silent model substitution.  
- Gateway-as-orchestrator or gateway-as-packer.

---

## 9. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Continue/OpenHands *client* triad pattern; llama.cpp/Ollama/vLLM/SGLang `/v1` as **runtime LCD** | Software socket, interchangeable servers |
| **Adopt** | Offline-only “one socket + auth + timeout” *idea* from LiteLLM/Envoy AI Gateway/Portkey — **only if** empty provider list / no WAN | Pattern, not product lock |
| **Add** | Schema validation; card check; size/timeout; `data:` vision only; fail-closed deny log | WP-00 / User / air-gap |
| **Refuse** | Cloud failover; Helicone-cloud; HF-on-miss; gateway owns routing or packing |

Stack / binary brand **not** locked.

---

## 10. Boundaries (do not steal)

| Topic | Owner |
|---|---|
| Job → specialist → card choice | **WP-06** |
| Messages, delimiters, PackManifest | **WP-21** |
| Catalog add/remove, open-weight | **WP-24** |
| Load/unload, VRAM, hardware probe | **WP-10** |
| MCP / plugins | **WP-08** |
| Full audit field set | **WP-17** |
| Output gates before download | **WP-12** |

---

## 11. Open questions for decision maker

1. **Topology (demo):** Is the gateway a **separate process** (even on one box), or an **in-process library** inside the workbench — as long as the **logical** socket + checks exist?  
2. **Timeout (must-work):** Freeze a single hard default (propose **60s** or **120s** per chat call), Admin-raisable later — pick **60** or **120**?  
3. **Oversize:** Gateway **hard-reject** only, or allow **one** mandatory shrink callback to packer before reject?  
4. **Unserveable id (card enabled, weights not loaded):** **Fail immediately**, or **one** WP-10 load attempt then fail?  
5. **Streaming:** Must-work demo = **non-streaming only**, or streaming required for Audience B “live” feel?  
6. **Auth secret:** Demo = **single shared Bearer** file/env on the air-gapped host; org adds rotation later — accept for must-work?

---

## 12. Next after your decisions

**Done.** Frozen as `WP-09_FREEZE.md` rev 1.0. Next: **WP-10**.
