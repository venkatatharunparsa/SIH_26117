# WP-10 runtime — adversarial red-team + PS coverage

**Date:** 2026-09-18  
**Target:** `WP-10_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** §0  
**Extra DM framing:** Do **not** deep-design hardware here. Venue/org may **publish available models + capabilities + connect URL**; KWB **registers cards** and connects; team **picks proper models** and may document **how to deploy local hardware if required** — product remains the **software workbench**.  
**Against:** Official Description/Expected Solution; WP-00 planes; WP-09 one-load + Bearer; WP-24 enable≠loaded; prior “venue GPU gift” risk.

---

## 0. DM answers

| Q | Decision |
|---|---|
| **1** | Demo **pre-load 2** models (warm set) |
| **2** | **LRU auto-unload** under VRAM pressure |
| **3** | **Org: GPU-only** inference. **Demo: GPU + CPU combined** allowed |
| **4** | Show **GPU name / VRAM** to jury — **must-work** |
| **5** | **One runtime** serves all ids; access via **single API key** (OpenRouter-*shaped* local multiplex — **not** openrouter.ai) |
| **6** | **Quantised** open-weight builds first-class |
| **R0** | Shallow hardware contract: connect to **provided** local catalog/URL; pick models; optional deploy guide — **not** a GPU product WP |

---

## Verdict

| | |
|---|---|
| Missing | M1–M12 (OpenRouter cloud confusion; provided-URL SSRF; CPU org leak; probe without GPU; pre-load 2 vs third card; LRU mid-request; quant≠capability lie) |
| Overhyped | Deep CUDA design; “they will give models” as only plan; OpenRouter cloud; all models always warm |
| PS (WP-10 slice) | **Satisfied** for runtime/multi-model/offline/open-weight/workstation-or-server — see §PS |
| Confidence | **~0.88** → GO WP-12 |

---

## Attack A — “Don’t go deep into hardware” vs PS GPU server

| Attack | Fix |
|---|---|
| **A1** Skip runtime WP entirely | Keep **contract**: stage/serve/load/`/v1`/probe — no brand lock, no CUDA cookbook |
| **A2** Bet demo only on “organizers give URL” | **Unverified gift**. Design: **configurable local `base_url` + cards**. Bring own staged quantised weights for Expected Solution. Use provided catalog **when** offered |
| **A3** “Deploy guide” becomes in-app HF download | Guide = **offline docs**; operation stays air-gap (WP-00/19) |
| **A4** Workbench becomes GPU tuner | WP-00 Never — software category |

**Decision:** Runtime WP = **shallow but binding** contract. Model pick + connect URL = **card + endpoint_ref**. Hardware depth = ops guide, not freeze pages of CUDA.

---

## Attack B — “OpenRouter concept” (single key, many models)

| Attack | Fix |
|---|---|
| **B1** Use public OpenRouter / cloud multi-provider | **Never** — breaks sovereign PS |
| **B2** Single key bypasses WP-09 card/grant checks | Key authenticates **workbench↔gateway↔runtime** only; **card + grant** still required (WP-09) |
| **B3** One key = one model forever | Key is **transport auth**; `model` field selects id among served set |
| **B4** Multiplex to WAN backends behind one key | All backends must remain **local allowlisted** endpoints |

**Decision:** Adopt **local OpenRouter-shaped UX**: one local `/v1` base + one Bearer + many `model` ids. **Refuse** openrouter.ai / cloud provider mesh.

---

## Attack C — Load policy (pre-load 2, LRU)

| Attack | Fix |
|---|---|
| **C1** Third demo card never loads → auto-select proof fails | Pre-load **2**; third (if any) **on-demand** via WP-09 one-load; proof script uses the two warm ids or loads third inside timeout |
| **C2** LRU unloads model mid-completion | LRU only between requests / when admitting new load; **pin in-flight** id |
| **C3** LRU thrash on two-task proof | Pin both warm ids during proof script; LRU for additional loads |
| **C4** Pre-load 2 on tiny VRAM OOM | Fail closed at startup; shrink quant / drop to one warm + CPU path (demo only) |

---

## Attack D — Org GPU-only vs demo GPU+CPU

| Attack | Fix |
|---|---|
| **D1** Demo CPU path shipped as org default | **Scale flag**: org profile **rejects** CPU-only inference; demo profile allows hybrid |
| **D2** Jury thinks org runs on CPU | Honesty in Limits + monitors |
| **D3** No GPU at demo → still claim GPU name | Show **actual** device string (e.g. `CPU` / iGPU) — no fake NVIDIA name |

---

## Attack E — Probe must-work

| Attack | Fix |
|---|---|
| **E1** Fake VRAM numbers | Read from host probe; label `unknown` if unavailable |
| **E2** Probe phones home | Local only |
| **E3** Probe auto-picks cloud model | Advisory only |

---

## Attack F — Quantised builds

| Attack | Fix |
|---|---|
| **F1** Quant card claims 120B-full quality | Card notes quant; routing by **task_tags** not marketing size |
| **F2** Quant-only refused by “open-weight” pedantry | Quantised open-weight **is** open-weight for PS |

---

## Attack G — Provided model list + URL

| Attack | Fix |
|---|---|
| **G1** URL is `https://api.*` | WP-09 local endpoint reject |
| **G2** Capabilities JSON trusted as security | Capabilities = **routing hints** → cards; grants/HITL still bind |
| **G3** Auto-register every provided id without Admin | Admin still **enables** cards (WP-24) |

---

## 1. Missing → fill

| ID | Fill |
|---|---|
| **M1** | Shallow hardware contract + connect-URL model |
| **M2** | Local OpenRouter-shape; refuse cloud OpenRouter |
| **M3** | Pre-load 2; on-demand rest; pin in-flight |
| **M4** | LRU between admissions |
| **M5** | Org GPU-only vs demo hybrid profiles |
| **M6** | Probe GPU name/VRAM must-work (honest) |
| **M7** | Single runtime + single API key + multi `model` |
| **M8** | Quant first-class |
| **M9** | One-load (WP-09) still applies |
| **M10** | Enable ≠ loaded |
| **M11** | Jail ≠ GPU |
| **M12** | PS coverage ledger |

---

## PS satisfaction (WP-10 + upstream — what is covered)

| PS requirement | Status | Where |
|---|---|---|
| Category **Software** workbench | **Satisfied** | WP-00; WP-10 shallow runtime |
| Air-gap / nothing leaves | **Satisfied** (contract) | WP-00/09/10 Never WAN |
| Own GPU **server** (org) | **Satisfied** (design) | WP-10 org GPU-only + endpoint |
| Not locked to one model; multi open-weight **at once** | **Satisfied** (honest) | Catalog multi-id; resident ≤ capacity; LRU |
| Auto-pick by task | **Satisfied** (other WP) | WP-06/24 — runtime only serves |
| Add models without redesign | **Satisfied** | Stage + card + same `/v1` |
| Workstation **or** server; mid-range; smaller if no 120B | **Satisfied** | WP-10 demo; quant OK |
| On-device OCR/vision models | **Satisfied** (path) | WP-03/24 kinds; runtime serves VLM/OCR ids |
| WAN=0 proof | **Partial → WP-13** | Runtime no WAN; visible proof WP-13 |
| Agentic plan/tools/iterate | **Other WPs** | WP-06/07 |
| Sandbox code verify | **Other** | WP-16 |
| Word approval note E2E | **Other** | WP-01/05 |
| Local KB grounding | **Other** | WP-11 |
| PPT/Excel/calc | **Ambition / deferred** | WP-00 |

**WP-10 does not claim** the whole PS is done — only the **runtime / multi-model serve** slice. Overall PS demo still needs remaining WPs (12→20) + prototype.

---

## 2. Overhyped

| Claim | Reality |
|---|---|
| Deep hardware WP | Shallow contract |
| OpenRouter product | Local multiplex shape only |
| Pre-load 2 = all catalog warm | Only two; others on demand |
| Provided URL always safe | Still local + Admin enable |
| Quant = full quality | Disclose on card |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| Single local `/v1` + single key + many models | openrouter.ai / cloud mesh |
| Quantised open-weight | HF-in-operation |
| LRU + pre-load 2 | All-enabled always in VRAM |
| Connect to provided local catalog | Betting solely on venue gift |
| Honest GPU/VRAM display | Fake probe |

---

## 4. Disposition

**Applied.** → `WP-10_FREEZE.md` + `WP-10_FREEZE_VERIFY.md`. Confidence **0.88**. **GO** → **WP-12**.
