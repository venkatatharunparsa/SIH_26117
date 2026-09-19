# KWB — Organisation-level technical design (COMPLETE)

**Date:** 2026-09-19  
**Status:** **ACCEPTED by DM 2026-09-19** (with runtime: org **vLLM** · demo **Ollama**).  
**Show/verify pack:** `ORG_DESIGN_SHOW_VERIFY_ADVERSARIAL.md`  
**Demo narrow:** `DEMO_TECH_STACK.md`  
**Process (DM):**  
1. Organisation tech design ← accepted  
2. **Org architecture diagrams** ← `ORG_ARCHITECTURE_DIAGRAMS.md` (**ACCEPTED 2026-09-19**)  
3. **Narrow diagrams + stack for demo** ← `DEMO_ARCHITECTURE_DIAGRAMS.md` (**ACCEPTED 2026-09-19**)  
4. **Add REAL** ← in progress (`backend/`) · then red-team implementation  

**Depends on:** Flow A→J locked · T1–T3 · accepted tech baseline · WP-00 §7 · freezes  
**Not in this file:** demo G1–G10 cut · PPT · implementation code  

---

## 1. Organisation product (one picture)

KWB at organisation scale is a **self-hosted knowledge workbench** (air-gap = strongest **posture**; SIH demoable) for every knowledge worker:

- **Same common flow A→J** for all users (no in-app hierarchy; paper Approver outside).  
- **Common capability set**; jobs differ by task.  
- Artefacts (Word must / Excel·PPT **ORG EXT**) + evidence — not chat-as-product.  
- **Assist in workbench**; **no in-app accept-for-forward**; after task complete worker **exports** output (downstream use outside picture).  
- Reads plant SoR via **connectors**; **never writes** plant systems.  
- Inference only via **gateway → local `/v1`**; weights stay on **runtime plane**.  
- Offline intake: USB → **quarantine/SHA** → Model Cards enable → vLLM (never raw Admin→GPU).  
- **Monitor A** = hash-chained **egress evidence pack** (default-deny + attempts log) — **not CERT**; audit **fail-closed**; no cloud `/v1` fallback.

```text
┌─────────────────────────────────────────────────────────────────────────┐
│  ORG NETWORK — air-gap posture (or controlled boundary + Monitor A)       │
│                                                                           │
│  Worker ──► KWB Workbench ──► Gateway ──► vLLM (GPU)                     │
│                │                 ↑ packed prompts only                    │
│                ├── ASSIST → EXPORT deliverable (Word ± evidence)          │
│                │     no in-app forward-accept  ← solution ends at export  │
│                ├── grants · H7 · secrets · audit · KB · MCP · sandbox     │
│                ├── Monitor A (egress evidence pack — not CERT)            │
│                └── read-only ──► Plant SoR                                │
│                                                                           │
│  USB ──► quarantine/SHA ──► Admin ack ──► Cards enable ──► vLLM          │
└─────────────────────────────────────────────────────────────────────────┘
  (Not in solution picture: how the exported file is used afterwards)
```

---

## 2. Three planes (org — non-negotiable)

| Plane | Org deployment | Owns | Never |
|---|---|---|---|
| **A Workbench** | App servers + desk UI + services | Flow A→J, grants, HITL self-gates, Word (Excel/PPT ORG EXT), retrieve, MCP host, audit, Monitor A | Weight files; plant write |
| **B Runtime** | Dedicated GPU hosts | Open-weight serve `/v1`; load/LRU; probe; **card-gated** load after quarantine | Task policy; grants |
| **C Sandbox** | Exec workers | Code/calc verify; reports for H9; **best-effort + isolation menu** | Inference; Docker-as-product identity |

---

## 3. Organisation module catalog (complete)

Every module maps to flow A→J and WP. Brands = accepted baseline unless marked **ORG EXT**.

### 3.1 Identity & access

| Module | Org design | Stack |
|---|---|---|
| Session | Person authenticated; **≠ grant** | SQLite→**ORG EXT:** IdP/SSO adapter (OIDC/SAML) later |
| Roles | Worker / Admin (+ Approver **outside app** for paper) | Config; no in-app boss queue |
| Task grant | Time-bounded sources/tools/ceiling; revoke on end/abort | SQLite grants; revoke-before-tool |
| Classifier | Sensitivity / expand friction | Rules first; model assist optional |

### 3.2 Desk & interaction (T1)

| Module | Org design | Stack |
|---|---|---|
| Task desk UI | Claude-like: intent + files + **DRAFT canvas** + HITL + audit | React+Vite preferred; static assets; 127.0.0.1 / internal TLS |
| Admin console | Cards, MCP allowlist, templates, USB intake ack, Audience A | Same UI shell, Admin routes |
| Monitor B | Own-task: card, grant, cites, HITL, allow/deny | Read audit/grant APIs |

### 3.3 Ingest & extract (D)

| Module | Org design | Stack |
|---|---|---|
| Intake allowlist | PDF/PNG/JPEG/WebP/TIFF/txt; fail-closed else | MIME sniff |
| PDF text path | Selectable text extract + trust label | **pdfplumber / pypdf** (no AGPL unless licensed) |
| OCR | Scans / empty pages | Tesseract; **ORG EXT:** PaddleOCR / VLM cards |
| Normalize | Extract artefact versioned | Internal schema |
| H1 | Same-user confirm/correct | Hard gate |

### 3.4 Knowledge (E)

| Module | Org design | Stack |
|---|---|---|
| Connectors | Read-only DMS/EAM/file shares; pluggable | **ORG EXT:** connector pack (Onyx-shape ACL intent) |
| Index | Not SoR; rebuildable | FTS5/BM25 + **ORG EXT:** hybrid dense when corpus demands |
| Authz-first retrieve | Grant filter **before** rank | Mandatory |
| Rerank | Deterministic ID/heading/clause boosts | No vector required at start |
| Verifier | Cite-or-abstain; NOT FOUND | Deterministic |
| Three-source claims | File / user / policy + H7 | WP-22 |

### 3.5 Orchestration & specialists (B/F)

| Module | Org design | Stack |
|---|---|---|
| Thin orch | Explicit state A→J; no safety autonomy | Custom Python loop |
| Task types | Approved job catalog + freestyle under policy | Config |
| Router | Task type → Model Card | Cards YAML/DB |
| Specialists | Separate agents per family (inspect, code, multimodal, …) | Packages under orch; no shared super-context |
| Skills | Org / plugin / personal shelves; progressive load | On-disk `SKILL.md`; H6 promote outside auto |
| Packer | Minimize context to grant | WP-21 |

### 3.6 Generation & artefacts (F/H/I)

| Module | Org design | Stack |
|---|---|---|
| Word | Company templates → DRAFT | docxtpl + python-docx |
| PDF out | Best-effort from docx | LibreOffice headless optional |
| Excel / PPT / calc-steps | Org Description artefacts | **ORG EXT:** openpyxl / PPT lib when promoted |
| Self H2 / H3 | Same user accept/edit/export | No in-app Approver chain |
| Evidence pack | docx + audit export (+ sandbox if used) | Manifest hashes |

### 3.7 Gateway & runtime (F/J)

| Module | Org design | Stack |
|---|---|---|
| Gateway | **Separate process** (org must); schema/card/grant/loopback checks | FastAPI gateway service; httpx to runtime |
| Model Cards | Add/disable/remove without redesign | Catalog service |
| Runtime farm | Multi-model `/v1`; GPU-only org; LRU | **Org brand: vLLM** (OpenAI-compatible server). Workbench still uses LocalModelClient only. |
| LocalModelClient | Workbench depends on contract only | Same client → demo Ollama **or** org vLLM |

### 3.8 Sandbox (G)

| Module | Org design | Stack |
|---|---|---|
| Default path | Best-effort isolation (timeout, cwd, secrets, Job Objects) | Python workers |
| Org menu | Podman/Docker `--network=none`; Linux nsjail/bubblewrap; ambition gVisor/Firecracker | Admin-selected profile |
| Calc-in-sandbox | Required capability | Same plane |
| H9 | Same-user decision on report | Evidence ≠ approval |

### 3.9 MCP & tools (org lifecycle)

| Module | Org design | Stack |
|---|---|---|
| Host | stdio / 127.0.0.1; grant ∩ allowlist; egress deny | MCP Python SDK |
| Admin H5 | Allowlist / disable / remove | Admin console |
| Packs | Offline USB only | WP-19 |
| Demo stub | One FastMCP MOCK | After spine |

### 3.10 Audit, lineage, monitors (J)

| Module | Org design | Stack |
|---|---|---|
| Audit store | Transactional events | SQLite → **ORG EXT:** Postgres if multi-node |
| Export | JSONL + hash chain + manifest | Jury / compliance pack |
| Retention | 180d-shaped org policy | Jobs + Admin |
| Lineage | Versions ↔ tasks ↔ drafts | Manifests (WP-14); engine files/SQL |
| Monitor A | Default-deny intent + **attempts log** → hash-chained **egress evidence pack** | Snapshots → pack; **not CERT** |
| Fail-closed | Audit write fail blocks privileged I/O; **no cloud `/v1` fallback** | WP-17 |

### 3.11 Offline intake (Admin)

| Module | Org design | Stack |
|---|---|---|
| USB | Weights, cards, MCP, skills | Staging dirs + reviewed ack |
| Quarantine / SHA manifest | Org-ambition hardening | WP-19 |

---

## 4. Organisation stack bill of materials

| Layer | Org choice |
|---|---|
| Language | Python 3.11 **or** 3.12 pinned |
| Workbench API | FastAPI + Uvicorn (internal bind) |
| Gateway | FastAPI **separate process** |
| UI | Claude-like desk (React+Vite preferred) |
| State / grants / audit ops | SQLite (small site) → Postgres (multi-node ORG EXT) |
| Audit evidence | JSONL export + SHA-256 chain + manifest |
| Word | docxtpl + python-docx |
| PDF in | pdfplumber/pypdf → OCR |
| OCR | Tesseract + pluggable stronger engines |
| Retrieve | Grant → FTS5/BM25 → deterministic rerank → hybrid ORG EXT |
| Verifier | Deterministic cite-or-abstain |
| Orch | Thin custom + specialists |
| Sandbox | Best-effort + org isolation menu |
| MCP | Local host + FastMCP for owned servers |
| Runtime | **Org: vLLM** · **Demo: Ollama** (same `/v1` LocalModelClient) |
| Secrets | Regex/rules; Presidio optional |
| Never | Cloud LLM, public `/v1`, plant write, Open WebUI-as-product, E2B |

---

## 5. Organisation deployment shapes

| Shape | When | Notes |
|---|---|---|
| **Single site mid** | Typical PSU start | Workbench + gateway + 1–N GPU nodes; SQLite or one Postgres |
| **Hardened** | Higher assurance | Separate gateway host; Podman sandboxes; signed audit checkpoints |
| **Multi-site** | Later | Replicated cards/policies; site-local runtime; no WAN brain |

All shapes keep **same software spine** and flow A→J.

---

## 6. What org design deliberately excludes

| Exclude | Why |
|---|---|
| In-app approval hierarchy | F6 / T3 — paper outside |
| Plant write APIs | WP-00 Never |
| Cloud / HF-in-UI | Offline Never |
| Agent OS fork as product | Wrong job |
| CERT badge theatre | Honesty |

---

## 7. Traceability to flow A→J (org)

| Flow | Org modules |
|---|---|
| A Enter | Session (+ SSO ORG EXT) |
| B Intent | Task type + cards router |
| C Inputs | Uploads + templates |
| D Extract | PDF/OCR + H1 |
| E Knowledge | Connectors + grant retrieve + verifier |
| F Assist | Orch + specialists + gateway + DRAFT |
| G Code | Sandbox menu + H9 |
| H Self-check | H2 |
| I Leave | **Export** deliverable (+ evidence). **No** in-app accept-for-forward. **Not** in-scope: how company uses file afterwards |
| J Proofs | Audit + **Monitor A evidence pack** (not CERT) + Monitor B + fail-closed (**continuous**) |

---

## 8. Next process gates (DM)

| Gate | Action |
|---|---|
| **G-ORG** | DM accepts this organisation design (or edits rows) |
| **G-NARROW** | Cut REAL/MOCK/LATER for SIH demo on **same** spine |
| **G-ADD** | Implement/add demo REAL modules |
| **G-RT** | Red-team + adversarial research on **narrowed** stack |

**Stop here until G-ORG.** No demo narrow, no build, no PPT in this step.
