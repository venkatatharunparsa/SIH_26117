# WP-09 LLM gateway — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-04 / WP-06 / WP-21 / WP-24.  
**Depends on:** those freezes (must not contradict). WP-10 is the runtime peer (next).  
**Inputs:** `WP-09_ARCHITECT_PERSPECTIVE.md`, `WP-09_REDTEAM.md`, **DM 2026-09-18** (org full verify on path to LLM server; demo shows small part of same contract; Q1–Q6 via adversarial).  
**Findings SoT:** `WP-09_REDTEAM.md`  
**Verify SoT:** `WP-09_FREEZE_VERIFY.md`  
**Product:** **KWB**

**Stack / proxy brand:** not locked.

---

## 1. One-sentence contract

The **gateway** is the **only** product path to the LLM **runtime**: it **verifies** auth, schema, **Model Card**, **local** endpoint, **param allow-list**, size, timeout, **active `grant_id`**, and vision locality before forward — **fails closed** with deny codes — and **never** rewrites to a public/cloud `base_url`. **Organisation** runs the **full verify suite** on every call; **demo** proves a **small visible subset** of the same suite.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Gateway verifies **wire + card + grant-active + local + size/time** | Gateway = plant ACL / HITL / RAG authz / safety decider |
| Org = full suite every forward | Demo = different weaker architecture |
| Demo shows subset of denies | Demo may skip card check |
| Gateway ≠ CUDA ≠ MCP ≠ packer ≠ orchestrator | Gateway “owns” the product brain |
| `/v1/models` = liveness | `/v1/models` = Model Card |
| Shared Bearer OK for air-gap demo | Bearer = enterprise IdP |

---

## 3. Closed decisions (DM + adversarial Q1–Q6)

| ID | Decision |
|---|---|
| **D0** | **Org:** full verify suite every forward. **Demo:** same architecture; **show small subset** of deny proofs (not a stripped gateway) |
| **D1** | **Logical socket mandatory**. Demo may be **in-process** iff **no bypass** to runtime. **Org:** **separate gateway process** must-work (workbench → gateway → GPU server) |
| **D2** | Timeout default **120s** per chat call (≤ Admin max); demo may lower for pacing |
| **D3** | Oversize → gateway **hard-reject** only (packer shrinks first — WP-21) |
| **D4** | Unserveable enabled card → **one** WP-10 load attempt (logged, inside timeout) then fail-closed; WP-06 may failover next card |
| **D5** | Demo must-work = **non-streaming**; streaming = org-ambition |
| **D6** | Demo auth = **single shared Bearer**; org rotation / dual-plane secrets = ambition |
| **D7** | Privileged forward requires **active `grant_id`** (WP-04) |
| **D8** | Param **allow-list**; strip unknown keys; reject non-local vision URLs |

---

## 4. Ownership

| Actor | Does | Does not |
|---|---|---|
| **Orchestrator (WP-06)** | Pass `model_id` + params + step | Bypass gateway; wire schema |
| **Packer (WP-21)** | Messages + PackManifest | Talk to GPU; rewrite endpoint |
| **Gateway (WP-09)** | Verify + forward local `/v1` | Route jobs; pack; MCP; VRAM |
| **Runtime (WP-10)** | Serve / load weights | Product policy |
| **Cards (WP-24)** | Policy catalog | Replace liveness list |

**Never:** any workbench component opens the runtime socket except through the gateway.

---

## 5. Must schema (LCD shape — brand-free)

| Surface | Must-work |
|---|---|
| `POST /v1/chat/completions` | Yes |
| `GET /v1/models` | Liveness only |
| Body | `model` (= card `model_id`), `messages`, optional allow-listed params |
| Vision | **`data:` / local bytes only** — reject `http(s):` image URLs |
| Other `/v1/*` | Deferred; if enabled later → same gates |

---

## 6. Org verify suite (every forward)

Ordered checks (deny + log reason code on fail):

1. **Auth** valid (Bearer or configured local secret).  
2. **Schema** valid chat body.  
3. **`grant_id` present** and grant **active** (revoked/expired → deny).  
4. **`model` ∈ catalog** ∧ **enabled** ∧ **open_weight** ∧ card version known.  
5. **Endpoint local** — card `endpoint_ref` ∈ allowlist (loopback and/or Admin on-prem CIDRs); **not** public internet; **not** cloud metadata ranges.  
6. **Param allow-list** — unknown keys stripped or reject; `max_tokens` capped.  
7. **Capability fit** — request features ⊆ card kind/modalities (e.g. no tools on OCR-only if disallowed).  
8. **Size** — bytes and/or PackManifest `token_est` ≤ ceiling (hard-reject).  
9. **Vision locality** — no remote image URLs.  
10. **Timeout** — start wall clock (default 120s).  
11. **Forward** only to resolved local runtime URL.  
12. On miss/4xx/5xx/timeout: **fail closed** (optional **one** load attempt for that card id — D4); **no** WAN failover; **no** silent model substitute.  
13. **Response** returns only to workbench caller — no egress webhooks.

**Deny reason codes (minimum):** `auth` | `schema` | `grant` | `card` | `endpoint` | `params` | `capability` | `size` | `vision` | `timeout` | `runtime` | `unserveable`.

**Correlation:** each call gets a `request_id` logged with allow/deny (WP-17 consumes).

---

## 7. Demo slice (small part of same suite)

Same gateway codepath. Jury-visible must prove at least:

| Proof | Required |
|---|---|
| Invalid schema → deny | Yes |
| Unknown or disabled `model_id` → deny | Yes |
| Oversize → deny | Yes |
| Remote image URL → deny | Yes |
| Model path WAN=0 (log or monitor) | Yes (Expected Solution) |
| PackManifest UI | No (log only — WP-21) |
| Streaming | No |
| Separate process on one laptop | Optional if in-process with **no bypass** |

Org deploy still uses **full suite** even when demo only *showed* four denies.

---

## 8. Local endpoint rule

| Allowed | Forbidden |
|---|---|
| `127.0.0.1` / `localhost` runtime | Public DNS / cloud LLM hosts |
| Admin-approved **on-prem** CIDR/hostname list | Link-local cloud metadata (`169.254.169.254` etc.) |
| Card `endpoint_ref` only | Gateway rewriting to a different host “for convenience” |

---

## 9. Never

- Cloud / public `base_url` rewrite or failover.  
- HF / internet pull on miss.  
- Remote vision URLs.  
- Skip card check because runtime listed the id.  
- Silent model substitution.  
- Bypass gateway to runtime in product path.  
- Gateway as MCP bus, packer, orchestrator, or CUDA.  
- Treat gateway logs as plant SoR.  
- Decide safety / HITL / plant outcomes.

---

## 10. Must / ambition / deferred / never

### Must-work

1. Only-path gateway; org full verify suite (§6).  
2. Demo subset proofs (§7).  
3. Schema + card + local endpoint + auth + size + timeout + grant-active + param allow-list + vision ban.  
4. Fail closed; deny codes + `request_id`.  
5. Non-streaming chat; `GET /v1/models` liveness.  
6. One load attempt then fail (D4).  
7. Demo shared Bearer (D6).

### Org-ambition

- Streaming; dual-plane secret rotation; mTLS; multi-runtime pool; Admin gateway debugger; per-role rate limits.

### Deferred

- Certified mesh; WAN enterprise API gateways; embeddings product surface.

### Never

- See §9.

---

## 11. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | OpenAI-compatible `/v1` **shape**; offline one-socket pattern | Interchangeable local runtimes |
| **Add** | Org/demo verify matrix; grant_id; param allow-list; local CIDR rule; deny codes; one-load | DM / red-team |
| **Refuse** | Cloud brain; LiteLLM public providers; Helicone-cloud; HF-on-miss |

---

## 12. Demo acceptance

1. Happy path: pack → gateway → local runtime → completion; `request_id` logged.  
2. Four denies visible (§7).  
3. Disabled card id denied even if somehow live on runtime.  
4. No public host in forwarded URL.  
5. Attempted bypass (direct runtime) not part of product path / fails review.  
6. Revoked `grant_id` → deny.

---

## 13. Next

**WP-10** — Runtime (GPU + weights; serve ids; load policy).

---

## 14. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze after adversarial org-full / demo-slice + Q1–Q6 decisions |

**Confidence:** **0.87**
