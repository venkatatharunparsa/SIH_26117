# WP-09 LLM gateway — adversarial red-team + org/demo verify split

**Date:** 2026-09-18  
**Target:** `WP-09_ARCHITECT_PERSPECTIVE.md`  
**DM intent (2026-09-18):** Gateway must **properly verify everything** on the path to the LLM server at **organisation** scale; **demo shows a small part** of the same contract (not a different, weaker product). Open Q1–Q6 answered via adversarial research (§0).  
**Against:** Official Description (own GPU server; nothing leaves) + Expected Solution (WAN=0 proof); WP-00 Valid gateway; WP-06 conductor≠gateway; WP-21 packer last policy / gateway wire reject; WP-24 card/local/fail-closed; WP-04 grant_id on privileged I/O; WP-16 timeout pattern; follow-list WP-09.

**Mode:** Attack first. Missing checks here = air-gap theatre.

---

## 0. Open questions → adversarial decisions

| Q | Options | Attack | **Decision (freeze)** |
|---|---|---|---|
| **1 Topology** | Separate process vs in-process | In-process alone invites “just call runtime” bypass; separate process alone ≠ proof if UI still bypasses | **Logical socket mandatory** in product path. **Demo:** in-process library OK **iff** no other path to runtime. **Org:** separate gateway process **must-work** (hop to GPU server) |
| **2 Timeout** | 60 vs 120 | 60 kills long local gen; unbounded hangs GPU | Default **120s** per chat call; ≤ Admin max; demo may lower for jury pacing |
| **3 Oversize** | Reject vs shrink callback | Shrink-at-gateway hides packer bugs; double-shrink races | Gateway **hard-reject** only; packer already shrinks (WP-21) |
| **4 Unserveable** | Fail now vs one load | Immediate fail flaky on cold start; infinite load = hang | **One** WP-10 load attempt (logged, inside timeout budget) then fail-closed; then WP-06 failover may pick next card |
| **5 Streaming** | Required vs not | Streaming complicates size/audit; not in Expected Solution | Demo must-work = **non-streaming**; streaming = org-ambition |
| **6 Auth** | Shared Bearer | Shared secret weak for multi-user org; fine for air-gap demo | Demo must-work: **single shared Bearer**. Org: rotation + separate workbench↔gateway and gateway↔runtime secrets (**ambition** if not day-one) |

**R0 (DM):** Org = **full verify suite** on every forward; Demo = **subset proof** of the same suite (schema deny, unknown card, oversize, no WAN) — not a stripped architecture.

---

## Verdict

| | |
|---|---|
| Missing | M1–M16 (bypass, grant_id, param allow-list, local endpoint definition, SSRF, response egress, embeddings scope, rate/retry, correlation id, org verify matrix, demo slice honesty) |
| Overhyped | Gateway = security complete; Bearer = IdP; `/v1/models` = policy; in-process = same as org hop |
| Confidence after freeze | **~0.87** → GO WP-10 |

---

## Attack A — Path integrity (“everything going to LLM server”)

| ID | Attack | Fix |
|---|---|---|
| **A1** | UI/orchestrator calls runtime `base_url` directly | Product rule: **only** gateway may open runtime socket; any other path = Never / redesign |
| **A2** | Gateway forwards then also retries public URL | Never rewrite; no second provider |
| **A3** | Card `endpoint_ref` set to `https://api.openai.com` | Reject non-local endpoint at card enable **and** at gateway forward |
| **A4** | SSRF via `http://169.254.169.254` or internal metadata as “local” | Define **local allowlist**: loopback and Admin-approved on-prem CIDRs only — never link-local cloud metadata |
| **A5** | DNS rebinding / hostname tricks | Prefer IP allowlist or resolve-and-check; refuse bare public DNS |
| **A6** | Completions leave via side channel (telemetry SDK) | Gateway process: **no WAN**; deny outbound except allowlisted runtime |

---

## Attack B — Incomplete verification before forward

| ID | Attack | Fix |
|---|---|---|
| **B1** | Schema-valid but `model` not on card | Card check after schema |
| **B2** | Card enabled but `open_weight=false` | Deny |
| **B3** | Runtime lists id; card disabled | Catalog wins — deny |
| **B4** | Params: huge `max_tokens`, jailbreak `logit_bias`, extra fields | **Param allow-list** ∩ card defaults ∩ task policy; strip unknown keys |
| **B5** | `http(s):` image URL in content | Reject vision non-`data:` / non-local |
| **B6** | Missing/invalid auth | Deny |
| **B7** | Oversize after packer estimate lie | Hard-reject using bytes and/or PackManifest `token_est` |
| **B8** | No timeout | 120s wall + cancel forward |
| **B9** | Orphaned call without `grant_id` | Require **`grant_id`** (or session-bound task id) on privileged inference; check grant **active** (WP-04) — deny if revoked |
| **B10** | Capability mismatch (tools on OCR-only card) | Deny if request features ⊄ card modalities/kind |

---

## Attack C — Org full vs demo small

| ID | Attack | Fix |
|---|---|---|
| **C1** | Demo weak checks → ship that as org | Same codepath; demo **exercises subset** of deny proofs |
| **C2** | Org claims “verify everything” including plant ACL in gateway | Gateway verifies **wire + card + grant active + local endpoint** — not RAG authz (WP-11) or HITL (WP-05) |
| **C3** | Jury thinks Bearer = enterprise IAM | Limits: demo shared secret; org rotation ambition; person identity stays WP-04 |

**Org verify suite (must exist as design):** auth, schema, card, local endpoint, param allow-list, size, timeout, grant active, vision URL ban, deny logging, no WAN outbound.  
**Demo show:** at least **four** visible denies — invalid schema, unknown/disabled `model_id`, oversize, remote image URL — plus WAN=0 on model path (Expected Solution).

---

## Attack D — Runtime / load / failover interaction

| ID | Attack | Fix |
|---|---|---|
| **D1** | Unserveable → hang waiting load forever | One load attempt inside remaining timeout |
| **D2** | Load attempt bypasses card check | Load only for **already card-approved** id |
| **D3** | Gateway silently substitutes another model on 404 | Forbidden; return error; WP-06 may failover |

---

## Attack E — Scope creep / confusion

| ID | Attack | Fix |
|---|---|---|
| **E1** | Gateway becomes MCP bus | Refuse |
| **E2** | Gateway packs prompts | Refuse — WP-21 |
| **E3** | Gateway routes jobs | Refuse — WP-06 |
| **E4** | Gateway owns VRAM | Refuse — WP-10 |
| **E5** | Expose `/v1/embeddings` etc. without policy | Only **chat/completions** + **models** must-work; other surfaces deferred or same gates |
| **E6** | Streaming must-work without audit story | Streaming ambition only |

---

## 1. Missing → fill

| ID | Gap | Fill |
|---|---|---|
| **M1** | Single product path | Only gateway→runtime |
| **M2** | Local endpoint definition | Loopback + Admin on-prem allowlist; no metadata IPs |
| **M3** | Param allow-list | Strip unknown; cap max_tokens |
| **M4** | `grant_id` + active check | On every privileged forward |
| **M5** | Org vs demo verify matrix | R0 + §C |
| **M6** | Q1–Q6 decisions | §0 |
| **M7** | Correlation / request id | Logged with deny/allow (WP-17 shape) |
| **M8** | No WAN from gateway process | Air-gap |
| **M9** | One load then fail | D1 |
| **M10** | Hard-reject oversize | Q3 |
| **M11** | Non-streaming demo | Q5 |
| **M12** | Deny reason codes | schema/auth/card/size/timeout/grant/endpoint/vision/params |
| **M13** | Retry policy | No cloud retry; limited local retry ≠ rewrite |
| **M14** | Response path | Return to workbench only; no exfil webhook |
| **M15** | Card≠liveness | Already WP-24 — reaffirm |
| **M16** | Bypass test in acceptance | Must prove direct runtime call is not used |

---

## 2. Overhyped

| ID | Claim | Reality |
|---|---|---|
| **O1** | Gateway verifies “everything” | Wire + card + grant-active + local + size/time — **not** plant truth / RAG ACL / HITL |
| **O2** | Shared Bearer = org IAM | Demo only |
| **O3** | Schema-valid = safe | Still need card/grant/params/vision |
| **O4** | In-process = org hop | Org requires process hop to GPU server |
| **O5** | Timeout = sandbox 60s | Different plane — inference **120s** default |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| OpenAI-compatible `/v1` LCD as **shape** | Cloud provider brain / public base_url |
| Offline one-socket auth+timeout pattern | Helicone-cloud; HF-on-miss |
| Card check + fail-closed | Silent model substitute |
| Org full suite / demo subset | Demo-only weak gateway as product |

---

## 4. Disposition

**Applied.** → `WP-09_FREEZE.md` rev 1.0 + `WP-09_FREEZE_VERIFY.md`. Confidence **0.87**. **GO** → **WP-10**.
