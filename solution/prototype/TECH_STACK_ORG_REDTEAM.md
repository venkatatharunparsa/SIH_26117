# Tech stack — ACCEPTED baseline + organisation red-team

**Date:** 2026-09-19  
**Process (DM locked 2026-09-19):**  
1. Design **organisation complete** → `ORG_TECH_DESIGN.md`  
2. **Narrow** to demo  
3. **Add** demo REAL pieces  
4. **Red-team + adversarial research** on narrowed stack  

**Earlier “enough for org?” probe:** kept for history in this file; **authoritative org design** is `ORG_TECH_DESIGN.md`.

---

## 1. Accepted baseline (working — not eternal brand lock)

```text
Python 3.11 or 3.12 (pinned)
FastAPI + Uvicorn @ 127.0.0.1 (blocking OCR/docx/subprocess in threads)
UI: Claude-like task desk — React+Vite preferred; layout locked, toolkit reopenable
docxtpl + python-docx (+ LibreOffice PDF optional later)
PDF / OCR (split locked 2026-09-20): **demo** = OCR *framework* (pypdf text + Tesseract/pytesseract + honest fixture stub); **org SoT** = OCR *model* (vision/neural OCR) — framework optional fallback later; H1 always; no AGPL PyMuPDF unless licensed
Audit: SQLite transactional events + JSONL export + hash chain + manifest
State: SQLite sessions / grants / metadata (revoke before every tool)
Retrieve: grant-filter → FTS5/BM25 → deterministic boosts → k≤5
Verifier: deterministic cite-or-abstain
Orch: thin custom Python loop
Exec: best-effort isolation + Job Objects when available + optional Docker/Podman --network=none
Gateway: httpx → loopback OpenAI-compatible /v1 only
Runtime: deferred brand; LocalModelClient contract; test Ollama + llama.cpp
MCP: FastMCP local MOCK after spine
Presidio: optional; regex/rules first
```

**Security language (accepted):** never claim CERT / malware / kernel isolation for local exec layer.

---

## 2. Org red-team question

> With **only** this baseline, can MRPL-scale **organisation** KWB (WP-00 §7) be built without a forced redesign?

Answer format: **ENOUGH** | **ENOUGH + add module** | **GAP (must extend stack)** | **OUTSIDE stack (process/policy)** | **DEFERRED artefact**

---

## 3. Org capability matrix (adversarial)

| Org need (WP-00 / freezes) | Baseline enough? | Attack / gap | What org must **add** (not demo yet) |
|---|---|---|---|
| Offline workbench software | **ENOUGH** | — | USB stage ops (WP-19) |
| Multi model / task route / cards | **ENOUGH** | Runtime brand open | Org GPU server; separate gateway **process** (WP-09 org) |
| Agentic iterate + workspace files | **ENOUGH** | Thin orch scales if state machine explicit | Durable job store; queues if multi-user |
| Word DRAFT + templates | **ENOUGH** | Template governance | Org template shelf + Admin UX |
| Excel / PPT / calc-with-steps | **DEFERRED artefact** | Not in baseline libs | openpyxl / PPT eng **when promoted** |
| Sandbox code + calc | **ENOUGH for demo honesty** | Best-effort ≠ hostile multi-tenant | Org: stronger isolation menu (Podman/gVisor/Firecracker **ambition**) |
| OCR + vision multimodal | **ENOUGH demo skeleton; GAP quality for org** | Framework (Tesseract) weak on handwriting/drawings | **Org SoT: OCR model** (vision/neural); keep framework as optional fallback; VLM cards on org GPU |
| KB connector + three-level cites | **ENOUGH spine** | FTS5 alone fails at **large** corpus / semantic paraphrase | Org: hybrid retrieve + connector adapters (read-only EAM/DMS schemas); **not** Chroma-as-SoR |
| Cite-or-abstain | **ENOUGH** | Must stay deterministic at org | Scale tests; contradiction UI (WP-22) |
| Grants + revoke + classifier | **ENOUGH spine** | SQLite single-node | Org IdP/SSO; multi-node grant service; classifier policy engine |
| Self-HITL (F6) vs org Approver roles | **ENOUGH for product story** | Freeze WP-05 still names Approver | Org paper: Approver **outside app** OR optional dual-role admin tools — **do not** rebuild hierarchy into desk |
| Local MCP lifecycle | **ENOUGH after add** | One FastMCP MOCK ≠ full lifecycle | Admin allowlist UI; pack intake; many local servers (WP-08 org) |
| Skills org/personal/plugin | **ENOUGH + add module** | Not in baseline packages | On-disk skill shelves + progressive load (files, not new DB brand) |
| Specialist agents | **ENOUGH + add module** | Thin orch must dispatch | Specialist packages; no shared super-context |
| Audit CERT-In-shaped retention | **ENOUGH spine** | Jury-day retention ≠ 180d | Retention jobs; export; clock runbook (WP-17 org) |
| Hash-chain | **ENOUGH** | WP-17 marked hash-chain ambition historically; we elevated it | Keep; signed checkpoints org-ambition |
| Monitors A/B | **ENOUGH + add module** | Snapshot ≠ continuous | Continuous WAN evidence ambition; B operator page |
| Lineage versions↔tasks | **ENOUGH + add module** | Not automatic from SQLite alone | Lineage manifests (WP-14); engine undecided — files/SQL OK |
| Read-only plant connectors | **GAP until adapters** | Baseline has MOCK packs only | Pluggable **read** connectors; never write |
| Multi-user concurrent org | **GAP risk** | One Uvicorn + SQLite OK small site | Connection pool; WAL; eventually Postgres **if** multi-node; sticky gateway |
| HA / multi-site | **GAP** | Not in baseline | Out of SIH; org architecture later |
| Streaming tokens | **DEFERRED** | WP-09 streaming = org-ambition | Add SSE when needed; contract already `/v1` |
| Separate gateway process | **GAP for org must** | Demo may in-process | Org: gateway as **own process** (WP-09 D1) |
| GPU-only org inference | **OUTSIDE / runtime plane** | Workbench OK | Org runtime plane (WP-10) |
| SSO / plant IdP | **GAP** | MOCK users only | Integrate IdP later; session≠grant stays |
| Drawing review / handwritten | **GAP quality** | Framework OCR insufficient | **OCR model** + VLM cards + specialised skills |
| Secret/PII at org scale | **ENOUGH + harden** | Regex incomplete | Policy packs; optional Presidio; DLP ambition |
| Air-gap claim honesty | **ENOUGH** | Overclaim kills trust | Keep best-effort language |

---

## 4. Org red-team verdict

### Is the accepted stack enough for **organisation**?

**Yes as the workbench spine — No as a complete org deployment by itself.**

| Layer | Org verdict |
|---|---|
| Planes (workbench / runtime / sandbox) | **Enough** — do not redesign |
| API + desk + Word + grants + verifier + audit spine | **Enough** — grow modules on same spine |
| Retrieve | **Enough to start**; **must extend** for large KB (hybrid + connectors) without replacing cite-or-abstain |
| Exec isolation | **Enough for honesty**; **must offer stronger menu** for hostile/org multi-user code |
| Runtime / GPU / separate gateway | **Required org additions** — still same `/v1` client |
| Excel/PPT/calc artefacts, SSO, live DMS, HA | **Not missing from “wrong stack”** — **deferred / ambition modules** on purpose |
| Hierarchy / in-app Approver engine | **Must not add** — contradicts F6/T3; company process outside |

### Fatal redesign risks (attacks that would force throwaway)

| Attack | Result |
|---|---|
| Replace desk with Open WebUI / DeerFlow fork | **Fatal** — wrong product |
| Make vector DB the SoR | **Fatal** — plant truth theatre |
| Require Docker Desktop / E2B | **Fatal** — de-Docker / WAN |
| Put Approver workflow engine in-app as core | **Fatal** — contradicts locked flow |
| Bind workbench to one runtime brand | **Fatal** — model-agnostic break |

**None of those are implied by the accepted baseline.** → Baseline is **org-survivable**.

### Must-add list for **organisation** (later; not demo narrow yet)

1. Separate **gateway process** + org GPU `/v1` farm  
2. Read-only **connector pack** (DMS/EAM schemas)  
3. Retrieve scale: hybrid + deterministic rerank (keep authz-first)  
4. Stronger **sandbox menu** (Podman/nsjail/gVisor options)  
5. Full **MCP + skills** shelves Admin lifecycle  
6. **Specialists** under thin orch  
7. Audit **retention / export** (180d-shaped)  
8. Lineage manifests  
9. Excel/PPT/calc when Description promoted  
10. SSO/IdP adapter  
11. Optional Postgres if multi-node proven necessary  
12. **OCR model** (vision/neural) for production ingest — demo stays on Tesseract/pypdf framework  

---

## 4b. OCR decision (DM 2026-09-20) — demo vs org

| Scale | Path | Honest label |
|---|---|---|
| **Now / demo (day-1)** | **OCR framework** already wired: **Tesseract (`pytesseract`) + pypdf** (+ fixture stub if Tesseract missing) | Live framework OCR when binary present; stub ≠ live OCR |
| **Organisation (target / SoT)** | **OCR model** (vision / neural OCR) for production-oriented org design | Do **not** ship model in demo; combine later with framework as **optional fallback** |

---

## 5. Demo narrowing (explicitly **later**)

When DM says narrow for SIH:

- Keep same spine  
- MOCK: connectors, SSO, multi-MCP, hybrid retrieve, continuous WAN  
- REAL: A→J path, G1–G10, Word, self-HITL, lexical+verifier, best-effort sandbox, audit export  

Do **not** narrow in this document yet.

---

## Runtime lock (DM 2026-09-19)

| Scale | Server | Workbench |
|---|---|---|
| **Demo** | **Ollama** (`/v1`) | LocalModelClient → `llm_base_url` |
| **Organisation** | **vLLM** (`/v1`) | Same client; point `base_url` at gateway→vLLM |

No workbench redesign when switching. llama.cpp remains optional spare, not default.

| Question | Answer |
|---|---|
| Accept verified stack as baseline? | **Yes — accepted** |
| Enough for organisation architecture? | **Yes for spine; extend for scale/connectors/isolation/gateway** |
| Enough alone to “finish org KWB”? | **No** — list §4 must-adds |
| Force new stack later? | **Unlikely** if we refuse fatal attacks above |
| Next | DM: confirm org verdict · then either deepen org must-add design **or** start **demo narrow** |

Say **org verdict OK** or dispute any GAP row.
