# Organisation design — SHOW · VERIFY · ADVERSARIAL RESEARCH

> **Note (2026-09-19):** Residuals scrubbed post **GATE_90_REDTEAM** — dual-story / overclaim language aligned to freezes WP-01/05 rev 2.0 (self-HITL; export leave; Approver = org paper only; Monitor A ≠ CERT).

**Date:** 2026-09-19  
**Status:** **ORG DESIGN ACCEPTED 2026-09-19** · runtime org **vLLM** · demo **Ollama**  
**Full catalog:** `ORG_TECH_DESIGN.md`  
**DM next:** architecture diagrams · then build add · then red-team on demo stack.

---

# PART A — SHOW (what we designed)

## A1. One sentence

Offline **Knowledge Work Bench** for every knowledge worker: common flow **A→J**, self-HITL, Word (and later Excel/PPT) DRAFTs grounded in org knowledge under **task grants**, inference only via **gateway → local `/v1`**, plant systems **read-only**, paper approval **outside** the app.

## A2. Picture

```text
  Workers ──► Workbench cluster ──► Gateway process ──► GPU Runtime (/v1)
                  │
                  ├── KWB Store (DRAFTs, extracts)
                  ├── Grants + Audit DB
                  ├── KB index (authz-first, not SoR)
                  ├── MCP host (allowlisted, local)
                  └── Sandbox workers (≠ GPU)

  Admin USB ──► stage weights / cards / skills / MCP packs
  Plant SoR ··· read-only connectors ···► Workbench
  Soft copy export ──► paper / officer OUTSIDE KWB
```

## A3. Three planes (hard)

| Plane | Org job |
|---|---|
| **Workbench** | Desk, grants, orch, retrieve, Word, HITL, MCP host, audit |
| **Runtime** | Weights + `/v1` serve only |
| **Sandbox** | Code/calc verify only — never wraps GPU |

## A4. Module map (complete list)

| # | Area | What org gets |
|---|---|---|
| 1 | Session ≠ grant | SSO later; grants time-bound + revoke |
| 2 | Task desk | Claude-like artefact canvas; Admin console; Monitor B |
| 3 | Ingest | PDF text → OCR; H1 self-verify; versioned extract |
| 4 | Knowledge | Read-only connectors; FTS then hybrid; cite-or-abstain; three-source |
| 5 | Orch | Thin loop + specialists + skills shelves + packer + cards router |
| 6 | Artefacts | Word now; Excel/PPT/calc when promoted; self H2/H3 |
| 7 | Gateway + runtime | Separate gateway process; multi-model farm; brand deferred |
| 8 | Sandbox | Best-effort default + org isolation menu |
| 9 | MCP | Full local lifecycle; USB packs; egress deny |
| 10 | Audit / lineage / monitors | SQLite→Postgres; JSONL+hash export; 180d-shaped; Monitor A evidence pack (not CERT) |
| 11 | USB offline | Stage + reviewed ack; quarantine ambition |

## A5. Stack BOM (org)

Python 3.11/3.12 · FastAPI workbench + **separate** gateway · Claude-like desk · SQLite→Postgres · JSONL+hash audit · docxtpl/python-docx · pdfplumber/pypdf→Tesseract · grant→FTS→cite-or-abstain · thin orch · best-effort+menu sandbox · local MCP · `/v1` runtime deferred · regex first  

**Never:** cloud brain · plant write · Open WebUI-as-product · E2B · in-app boss approval queue  

## A6. Flow A→J ownership

A session · B intent/cards · C upload/template · D extract+H1 · E grant+retrieve+verifier · H7 cite review · F pack→gateway→DRAFT · G sandbox+H9 · H self H2 · I export leave (H3) off box; paper Approver outside · J audit+Monitor A/B continuous  

---

# PART B — VERIFY (against our SoT)

| Check | Result | Note |
|---|---|---|
| Matches locked flow A→J + F1–F7 | **PASS** | Self-HITL; no in-app hierarchy |
| Matches WP-00 planes + Never | **PASS** | Workbench ≠ runtime ≠ sandbox; no plant write; offline |
| Matches WP-00 §7 org-ambition coverage | **PASS with EXT** | Excel/PPT/connectors/MCP/skills/specialists present as modules |
| Matches WP-04 session≠grant | **PASS** | Explicit |
| Matches WP-05 HITL moments | **PASS** — WP-05 FROZEN 2.0 self-HITL | Design uses self-HITL; Approver = org paper only; export leave (H3) |
| Matches WP-09 org separate gateway | **PASS** | Called out for org |
| Matches WP-11 authz-first + k=5 demo / org hybrid | **PASS** | Lexical first; hybrid ORG EXT |
| Matches WP-16 sandbox honesty | **PASS** | Best-effort + menu; not CERT claim |
| Matches WP-17 audit | **PASS** | Store + export + fail-closed |
| License trap PyMuPDF AGPL | **PASS avoided** | pdfplumber/pypdf preferred |
| Demo narrow consistency | **PASS** | Demo is slice of same spine (`DEMO_TECH_STACK.md`) |
| Overclaim air-gap = certification | **PASS avoided** | Honesty language |

**Verify confidence on paper:** ~**0.82** for “design coherent with freezes + flow.”  
**Not verified:** runtime brand, multi-node load, connector ACL fidelity, handwritten/drawing quality — those need later proof, not design fiction.

---

# PART C — ADVERSARIAL RESEARCH (external pressure on this org design)

Sources consulted (patterns, not products to fork): on-prem RAG blueprints; air-gapped RAG supply-chain notes; sovereign on-prem LLM control/data/governance planes; MCP gateway/registry patterns; HITL workbench patterns.

## C1. Attacks that **support** our design (keep)

| Attack theme from industry | Our design response | Verdict |
|---|---|---|
| Cloud RAG fails regulated offline | Air-gap + USB stage + no public `/v1` | **Keep** |
| ACL after retrieve = leak | Authz-**first** grant filter | **Keep** |
| Chat UI becomes the product | Artefact desk + DRAFT Word | **Keep** |
| Inference mixed with policy | Three planes + separate gateway | **Keep** |
| Fake citations | Deterministic cite-or-abstain | **Keep** |
| Tool sprawl / MCP chaos | Allowlist + grant ∩ allowlist + USB only | **Keep** |
| Overclaim sandbox | Best-effort language + isolation menu | **Keep** |

## C2. Attacks that **expose gaps** (org must plan — not silent)

| # | Adversarial finding | Gap in current org design? | Suggested add (design-level, not build yet) |
|---|---|---|---|
| **R1** | Air-gap **supply chain** is the hard problem (signed bundles, offline wheels/images, no HF phone-home) | USB stage exists; **signed artifact registry / offline package mirror** thin | Add **ORG EXT:** signed offline registry (Harbor-class) + “no egress” install verify |
| **R2** | Sovereign programs use **control / data / governance** planes (registry, eval, change approval) | We have cards + audit; weak on **eval harness + model change governance** | Add **ORG EXT:** offline golden-eval; card change = Admin + audit reason |
| **R3** | Embedding swap = full re-index cost inside gap | We defer hybrid — good; if hybrid added, need **embed model pin + backfill plan** | Document pin rule when hybrid promoted |
| **R4** | Enterprise MCP often wants **gateway/registry** not only host | We have host; may need **MCP registry** at scale | ORG EXT later — not fork cloud MCP OAuth |
| **R5** | Multi-user orch needs durable jobs / queues | Thin loop OK start; **no** Celery/Temporal named | ORG EXT: job queue when concurrency proven |
| **R6** | Connector ACL drift / schema drift | Connectors named; **no** drift/reindex ops story | Add connector **version + reindex job** in Admin |
| **R7** | Dual-run cloud fallback common in industry | We **refuse** — correct for MRPL Never | Keep refuse; do not add “shadow OpenAI” |
| **R8** | K8s GPU farms common for org | We allow farm behind `/v1`; **not** locking K8s | Keep brand-agnostic runtime farm |
| **R9** | HITL “Approver queue” in many products | We put Approver **outside** — intentional | Confirm you still want this vs industry default |
| **R10** | Observability (latency, refusal, drift) | Monitor A/B thin vs full SRE stack | ORG EXT: Prometheus-class later; not demo |

## C3. Fatal alternatives research says “use X” — we still **refuse**

| Industry pull | Why we refuse for KWB |
|---|---|
| Open WebUI / chat+RAG portal as core | Wrong product job |
| DeerFlow / agent OS as product | Coding/research harness ≠ inspection workbench |
| Cloud MCP SaaS OAuth mesh | Breaks air-gap |
| Vector DB as plant SoR | Index ≠ SoR |
| Auto plant write / ticket file | WP-00 Never |

## C4. Adversarial score on org design

| Question | Score | Meaning |
|---|---|---|
| Coherent with SIH/MRPL SoT? | **0.82** | Strong |
| Survivable as org spine without redesign? | **0.78** | Strong if R1–R6 EXT accepted as backlog |
| Complete vs mature sovereign platform? | **0.55** | Missing supply-chain registry, eval governance, SRE depth — **honest** |
| Safe to present to you for perspective? | **Yes** | Gaps listed, not hidden |

---

# PART D — What I need from you

Share your perspective on:

1. Does **PART A** match the organisation you want?  
2. Any module **wrong / missing / too heavy**?  
3. Especially **R9**: Approver outside app — still correct?  
4. Which **R1–R6** gaps must enter org design **now** vs stay backlog?

I will **not** treat org design as accepted until you reply.
