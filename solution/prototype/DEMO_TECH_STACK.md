# KWB — Demo tech stack (NARROWED)

**Date:** 2026-09-19  
**Status:** **ACCEPTED with org design 2026-09-19** · runtime demo **Ollama** · org **vLLM**  
**Parent:** `ORG_TECH_DESIGN.md`  
**Done bar:** G1–G10 (`WP-18`) · Flow A→J · self-HITL (F6)  
**Next:** add REAL **in progress** (`backend/`) · red-team implementation · PPT later  

---

## 1. Narrow rule

| Keep from org | Drop / MOCK for demo |
|---|---|
| Three planes · A→J · cite-or-abstain · Word DRAFT · grants · gateway `/v1` · best-effort sandbox · SQLite audit+JSONL export · Claude-like desk | SSO · live plant connectors · Postgres · hybrid vector · separate gateway host · Excel/PPT · full MCP lifecycle · continuous WAN · multi-site · org Approver-in-app |

**Same architecture as org. Demo is a slice — not a different product.**

---

## 2. Demo deployment shape (one machine OK)

```text
┌──────────────────────────────────────────────────────────┐
│  Jury workstation / single server (offline)                │
│                                                            │
│  [KWB Electron desk] ──► [Workbench API :8080]             │
│  (apps/kwb-app)         FastAPI · grants · audit           │
│  Claude Code-like       │                                  │
│  session stream         ┌──────────┼──────────┐            │
│         │               ▼          ▼          ▼            │
│         │          grants/audit  sandbox   gateway client  │
│         │          SQLite+JSONL  (best-effort)  │          │
│         │               │          │            ▼          │
│         │               │          │     local /v1 runtime │
│         │               │          │     (Ollama / llama)  │
│         └───────────────┴──────────┴── artefacts + eval/ ──│
│                                                            │
│  REJECTED/legacy: apps/kwb-desk (Syne hero Next) · /desk/  │
└──────────────────────────────────────────────────────────┘
```

- Gateway may be **in-process module** for demo iff **no bypass** to runtime (WP-09 demo allow).  
- Runtime = **separate process** still (weights not in workbench).  
- Docker **optional**; must pass **without** Docker Desktop.

---

## 3. Demo BOM (locked candidates for this slice)

| Layer | Demo pick | Tag | G# |
|---|---|---|---|
| Python | **3.11 or 3.12** pinned | REAL | — |
| Workbench API | **FastAPI + Uvicorn** `127.0.0.1:8080` | REAL | — |
| UI | **Electron + Vite React** desktop app (`apps/kwb-app/`) — Claude Code-like session stream; FastAPI remains API. `apps/kwb-desk/` Syne hero Next = **REJECTED/legacy**. Static `desk/` = legacy fallback | REAL | — |
| Session | Local user id | MOCK | — |
| Grants | SQLite; revoke-before-tool | REAL | G7 |
| Cards + router | ≤3 cards; task→card→model_id; G1 floor = dual card / one tag OK | REAL | G1, G8 |
| Gateway client | httpx → loopback `/v1` only; deny public URL | REAL | G8 |
| Runtime | **Ollama** = **inference only** · `/v1` · **127.0.0.1** · adopt **local pre-staged tags only** · **NEVER pull** · G1 full only if 2nd chat tag staged offline | REAL | G1 |
| Org runtime (not demo box) | **vLLM** on org GPU farm — same LocalModelClient contract | ORG | — |
| PDF / OCR | pdfplumber/pypdf → Tesseract; **fixture fallback** | REAL (light) | G4 |
| H1 / H2 / export leave / H9 | Same-user gates; `artefact_version` stale; H9+G10 on export; docx body secrets scan | REAL | G2,G3,G9,G10 |
| Retrieve | Local SOP packs + grant filter + FTS5/BM25 k≤5 | MOCK data / REAL logic | G6 |
| Verifier | Deterministic cite-or-abstain / NOT FOUND | REAL | G6 |
| Word | docxtpl + python-docx · DRAFT badge | REAL | G2 |
| Packer | Minimal PackManifest | REAL | — |
| Secret gate | Regex deny before unmasked/export | REAL | G9 |
| Sandbox | Best-effort isolation + timeout + calc-in-jail; optional Docker `network=none` | REAL | G3,G10 |
| Audit | SQLite events + JSONL export + hash chain + manifest | REAL | all |
| Monitor A | Host start/stop snapshot on **workbench + Ollama**; evidence artefact (not CERT) | REAL | G5 |
| Monitor B | Thin: recent audit + card/grant | REAL (thin) | — |
| MCP | Skip until after G1–G5; then one FastMCP MOCK | MOCK / LATER-first | — |
| USB | Pre-staged weights; show path once | MOCK | — |
| Excel / PPT / live DMS / SSO / Postgres / hybrid RAG / lineage UI | — | **LATER** | — |
| Cloud / plant write / Open WebUI product | — | **NEVER** | — |

---

## 4. Demo modules ON vs OFF (from org catalog)

| Org module | Demo |
|---|---|
| Task desk | **ON** |
| Admin console (full) | **THIN** — cards edit + USB note enough |
| SSO / IdP | **OFF** (MOCK user) |
| Plant connectors | **OFF** — file packs only |
| Hybrid / vector retrieve | **OFF** |
| Specialists (many) | **THIN** — inspect + code paths enough for G1≥2 |
| Skills shelves full | **OFF** / minimal |
| Excel/PPT/calc-artefact | **OFF** |
| Separate gateway host | **OFF** — in-process gateway module OK |
| Sandbox org menu (gVisor…) | **OFF** — best-effort only |
| Full MCP lifecycle | **OFF** |
| Continuous WAN monitor | **OFF** — snapshot pair |
| Postgres / multi-node | **OFF** |

---

## 5. Demo walks (must prove)

| Walk | Flow | Goldens |
|---|---|---|
| Inspection note | A→D→E(optional)→F→H→I + J | G2, G4, G1, G6, G5… |
| Coding + calc | …→G→H9→I | G3, G10 |
| Fail-closed injects | revoke / bad model / secret or sandbox-red or NOT FOUND | G7, G8, +one |

Jury leave-with: **Word DRAFT + audit export** (+ **sandbox proof** if G used).

---

## 6. Explicit non-claims (jury language)

- Not CERT-In certified  
- Not plant SoR  
- Not hostile-code kernel sandbox  
- Not in-app officer approval  
- Runtime brand interchangeable  

---

## 7. Gate

**DM:** Accept demo stack narrow (already) + **demo diagrams D1–D6**?  
→ Next: add REAL · red-team demo · PPT later.
