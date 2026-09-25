# Two-laptop demo — adversarial research + red-team + completion plan

**Date:** 2026-09-20  
**Status:** **OPTIONAL / DEFERRED** — jury demo is **single laptop** (Ollama + kwb-app + FastAPI on one machine).  
**Ask (historical):** Laptop-1 model workstation · Laptop-2 workbench  

> **Do not block demo on this doc.** Use `eval/STAGE_RUNBOOK.md` single-laptop path.

---

## 0. Honest answer first

### Is Laptop-2 (workbench) completely ready?

| Layer | Ready? | Note |
|---|---|---|
| Electron desk + FastAPI HITL / export leave / G1–G10 API | **YES** (single-box proven) | Confidence ~0.88 API |
| Calling **local** Ollama on same machine | **YES** | Default today |
| Calling **remote** model on Laptop-1 over LAN | **NO until config change** | Gateway **denies non-localhost** (G8) |
| Receiving “API key + Model Card” from L1 as a product flow | **PARTIAL** | Model Cards = `config/models.yaml` today · **no** key-issuance UI yet |
| Jury demo end-to-end two-laptop | **NOT YET** | Needs link mode + rehearsal |

**Verdict:** Laptop-2 workbench **app is ready**. Laptop-2 **remote-inference wiring is not complete**. That gap is real — not optional polish.

---

## 1. Roles (correct split)

```text
┌─────────────────────────────┐         ┌──────────────────────────────┐
│ LAPTOP-1  Model Workstation │         │ LAPTOP-2  Knowledge Work Bench│
│                             │         │                              │
│ • Ollama / vLLM (GPU)       │  infer  │ • Electron desk (kwb-app)    │
│ • Adopted tags ONLY         │◄───────►│ • FastAPI :8080              │
│ • Issues Model Card YAML    │  card   │ • Grants / HITL / audit      │
│ • Optional station token    │         │ • Points llm_base_url → L1   │
│ • NO operator desk required │         │ • NO model pull              │
└─────────────────────────────┘         └──────────────────────────────┘
```

**What L1 “gives” L2 (map their words to our system):**

| They said | In KWB terms | Artifact |
|---|---|---|
| Model card | Task→card→`model_id` allowlist | `config/models.yaml` cards (+ routing) |
| API key | Station credential (optional) OR “proof of adopt” | Shared `station_token` **or** USB card file signed by date — **not** OpenAI cloud key |
| API base | Inference OpenAI-shape base | `llm_base_url` → L1 Ollama `/v1` |

**What stays on L2 only:** grants, H1/H2/H7/H9, Word DRAFT, export leave, Monitor A, sandbox, audit.  
**What stays on L1 only:** GPU/weights, `ollama serve`, adopted tags list.

---

## 2. Adversarial research (what’s good for us)

| Pattern | Pros | Cons for SIH jury |
|---|---|---|
| **A. SSH tunnel** L2→L1:11434 → L2 `127.0.0.1:11434` | Keeps G8 localhost; encrypted; no Ollama LAN bind | Needs SSH; tunnel drop mid-demo |
| **B. LAN bind** L1 `OLLAMA_HOST=0.0.0.0` + L2 allowlist peer IP | Simple jury story “workstation ↔ desk” | WiFi isolation; firewall; **Ollama has no auth** |
| **C. Everything on one laptop** | Most reliable | Abandons stated two-laptop story |
| **D. Public / cloud LiteLLM** | — | **REFUSED** (locks) |

**Recommended primary:** **Mode A (SSH tunnel)** for integrity + G8 honesty.  
**Recommended backup:** **Mode B (LAN allowlist)** if SSH awkward — only private RFC1918 peer listed in config.  
**Always:** USB offline fallback — same models.yaml + local Ollama on L2 if link dies (SIH WiFi kills demos).

---

## 3. Red-team attack table (two-laptop)

| ID | Attack | Severity | Mitigation |
|---|---|---|---|
| **2L-01** | Gateway blocks L1 IP → blank/fail drafts | **Critical** | Tunnel **or** `inference_allow_hosts` |
| **2L-02** | Venue WiFi client isolation | **Critical** | Ethernet/hotspot from L1 · or tunnel · or local fallback |
| **2L-03** | Ollama open on LAN, stranger burns GPU | **High** | Prefer tunnel; firewall allow only L2 IP |
| **2L-04** | Wrong/missing model tag on L1 | **High** | Pre-adopt offline; card lists only present tags |
| **2L-05** | “API key” story but no real gate | **High (honesty)** | Either implement station token **or** say “Model Card + base URL” honestly |
| **2L-06** | L2 still bound FastAPI `127.0.0.1` only (OK) | — | Desk stays on L2; do **not** expose 8080 to room |
| **2L-07** | Pull on L1 during demo | **Critical integrity** | Banner: inference-only; tags pre-staged |
| **2L-08** | Operator runs `kwb-desk` on L2 | **High** | Only `kwb-app` Electron |
| **2L-09** | Card says model X, L1 has only Y | **High** | `validate_station_link.py` preflight |
| **2L-10** | Mid-demo cable/WiFi drop | **Critical** | Local fallback profile on L2 |

---

## 4. What’s missing on Laptop-2 (complete list)

1. **Link mode** — `llm_base_url` to L1 (tunnel keeps 127.0.0.1; LAN needs allowlist) ← code gap  
2. **Model Card import path** — paste/USB `models.yaml` from L1  
3. **Station token (optional)** — if we claim “API key”  
4. **Preflight script** — ping L1 `/api/tags` + card models present  
5. **Demo runbook two-laptop** — cable order, IPs, fallback  
6. **Rehearsal** — full A→J with remote inference once  
7. **PPT slide** — architecture two boxes + honesty (no CERT)  

**Already OK on L2:** Electron desk, FastAPI HITL, grants, leave-pack, G-pack evidence (local), Monitor B on demand.

---

## 5. Completion plan (do in order)

### Phase P0 — Decide link mode (30 min)
- [ ] Choose **A tunnel** (preferred) or **B LAN**  
- [ ] Write L1 IP / SSH user on paper cheat sheet  

### Phase P1 — Model Workstation (Laptop-1)
- [ ] Install Ollama; **offline** ensure `llama3.2:3b` (or agreed tags) listed  
- [ ] **Never pull** on stage  
- [ ] Export Model Card file from template `config/model_station.card.example.yaml`  
- [ ] Mode A: enable SSH; leave Ollama on localhost  
- [ ] Mode B: `OLLAMA_HOST=0.0.0.0:11434`; firewall allow **only L2**  

### Phase P2 — Workbench (Laptop-2) wiring
- [ ] Install repo + `npm i` + Python deps (pre-venue)  
- [ ] Import Model Card → `config/models.yaml`  
- [ ] Set `llm_base_url` (127.0.0.1 if tunnel; `http://L1_IP:11434` if LAN)  
- [ ] If LAN: set `inference_allow_hosts: ["L1_IP"]`  
- [ ] Run `python backend/scripts/validate_station_link.py`  
- [ ] Run API + `npm run electron:dev`  
- [ ] Smoke: Start → H1 → retrieve → draft → H2 → export leave  

### Phase P3 — Fail-closed demo beats
- [ ] G8: bad model still denies  
- [ ] Unplug link → show local fallback **or** clear deny (no hang)  

### Phase P4 — Jury day
- [ ] Two-laptop STAGE addendum in `eval/STAGE_RUNBOOK.md`  
- [ ] PPT architecture slide  
- [ ] Backup: single-laptop mode recorded  

---

## 6. Confidence (two-laptop story)

| Axis | Now | After P0–P3 |
|---|---|---|
| L2 workbench app | **0.88** | 0.88 |
| L2↔L1 inference link | **0.25** | **0.85** (if rehearsed) |
| “API key + card” honesty | **0.40** | **0.80** with card file + optional token |
| Jury two-laptop demo | **0.35** | **0.82** |

---

## 7. Refuse

- Cloud API keys / LiteLLM cloud  
- Public WAN Ollama  
- Claiming CERT  
- Pulling models on stage  
- Putting FastAPI Approver on either laptop  

---

## 8. Next engineering (this repo)

1. Gateway allowlist for **explicit** private peers (LAN mode)  
2. Example Model Card from station  
3. `validate_station_link.py` preflight  
4. Two-laptop section in stage runbook  

Tunnel mode needs **zero** gateway change if L2 uses `127.0.0.1:11434`.
