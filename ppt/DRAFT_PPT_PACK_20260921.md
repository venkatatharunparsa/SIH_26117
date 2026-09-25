# DRAFT — Idea PPT pack (for your review)

**Status:** DRAFT only — paste into official SIH 6-slide PPTX **after** you finish manual workflow testing.  
**Do not** treat this as final until you ask for modifications.  
**Date:** 2026-09-21  
**Evidence base:** PS robust 24/24 · E2E dual-tag · Workflow B Word · red-team 0 HIGH · `E2E_FULL_SIMULATION_GUIDE.md` · scorecard ~72%

**Product one-liner (use everywhere):**  
> **Knowledge Work Bench** is an on-prem industrial workbench that routes open-weight models by task, gates human verification, and delivers cited **DRAFT Word** plus sandbox-verified calc — with grants, audit, and a Monitor A evidence pack — on mid-range GPU hardware.

**Honest sovereign line (say this, not “air-gapped forever”):**  
> Inference stays on **private LAN / on-prem Gateway** paths to open-weight runtimes. **Monitor A** is an **evidence pack**, **not** CERT-In. Demo may use two laptops on a phone hotspot as a **LAN peer** — that is **not** the same claim as a venue NIC-off air-gap rehearsal.

---

## How this maps to the official 6 slides

| # | Official pointer | Draft file below | Primary visual |
|---|------------------|------------------|----------------|
| 1 | Title | §S1 | Logo / team (you fill) |
| 2 | Proposed Solution | §S2 | Context diagram → `prompt/DALLE_S02_CONTEXT.md` (gen **920×420** empty-top → crop **~920×200**) · topology `D01_CONTEXT_DIAGRAM.md` |
| 3 | Technical Approach | §S3 | Component diagram → `D02_COMPONENT_DIAGRAM.md` |
| 4 | Feasibility / Viability | §S4 | REAL / LATER table |
| 5 | Impact / Benefits | §S5 | One estimate + Cisco context |
| 6 | Research / References | §S6 | Matrix + refs |

Existing slide files `S01_…`–`S06_…` remain the older pack. **This DRAFT supersedes wording** where it conflicts (dual-model, Word, LAN honesty). After your manual test, ask to sync S01–S06 / build PPTX.

Integrity: `00_INTEGRITY_RULES.md` + updates in §Integrity below.

---

## Integrity (updated chips)

| Say | Don’t say |
|-----|-----------|
| On-prem / private-LAN Gateway · open-weight | “Fully air-gapped” without NIC evidence |
| Dual-task auto-select: inspect→`llama3.2:3b`, code→`qwen2.5-coder:7b` (demo staged) | “Many models” / dual 70B in VRAM |
| **DRAFT Word** soft copy · export leave | Certified plant record / in-app Approver |
| Monitor A evidence pack · **≠ CERT** | CERT-In certified |
| Human checkpoints (extract, cites, DRAFT, sandbox) | “AI approved the plant” |
| Sandbox host-process + deny guards · Docker later | Full deny-all jail if not using Docker |
| Vision/OCR: on-device vision when staged; stub labeled | “99% OCR” |

---

## S1 — Title (paste)

- **Title:** Knowledge Work Bench — Sovereign On-Premise Agentic Workbench for Confidential Industrial Knowledge Work  
- **PS:** SIH26117 · Theme: Smart Automation · Category: Software  
- **Org / Dept:** Mangalore Refinery and Petrochemicals Limited (MRPL)  
- **Team:** `[TEAM_ID]` · `[TEAM_NAME]` · `[COLLEGE]` · `[MEMBER NAMES]`  

*(No product pitch on this slide beyond the title.)*

---

## S2 — Proposed Solution (paste)

### Proposed
- **KWB** — industrial **workbench** (not a chatbot): task grants, model cards, human checkpoints, cited retrieve, **DRAFT Word**, sandbox calc/code, audit + Monitor A evidence pack.  
- Same architecture for **demo mid-range GPU** and **org GPU server** (scale cards/connectors, not rewrite).

### How it addresses the PS
| PS pain | KWB mechanism |
|---------|----------------|
| Confidential work cannot go to cloud assistants | On-prem / private-LAN Gateway · open-weight only · public model ids denied |
| Need agentic multi-step deliverables | Orch spine: attach → confirm → retrieve → polish → Word → export leave |
| Coding must be verified | Sandbox calc/code + human H9 · fail-closed on red |
| Multimodal scans | Image attach → vision model when staged · OCR framework / honest stub fallback |
| Sovereign proof | Logs + Monitor A evidence pack (**≠ CERT**) |

### Uniqueness (3 ticks only)
1. **Task→card→model** auto-select (≥2 task types) behind Gateway.  
2. **Human-gated** inspection pack → **DRAFT Word** with cites (judgement stays with engineer).  
3. **Fail-closed** grants + secret/export denies + evidence pack — not “chat with a local LLM”.

**Caption under context diagram (cropped ~920×200):** Worker exports DRAFT · Admin stages offline packs · Gateway only · Monitor A ≠ CERT · Plant read-only · Public net blocked  
**Generate from:** `prompt/DALLE_S02_CONTEXT.md` (920×420 with empty top, then crop)  

---

## S3 — Technical Approach (paste)

### Flow (one line)
`Desk → /orch/turn → Grant → Pack → Gateway → local/LAN /v1 (Ollama) → tools/sandbox → DRAFT → export leave`

### Three planes
| Plane | What |
|-------|------|
| Workbench | Grants, orch, retrieve, HITL, Word, audit, Monitor B |
| Gateway | Allowlist hosts · card model allowlist · deny public WAN models |
| Runtime | Open-weight tags (demo: llama / qwen-coder / moondream) · no pull from workbench |

### Demo stack (honest)
- Electron desk `kwb-app` · FastAPI · Ollama (single laptop **or** two-laptop LAN peer)  
- Dual-tag routing proven in eval · Word primary · optional vision on image attach  

**Component diagram:** use `D02_COMPONENT_DIAGRAM.md` (Orch decides cards).  

---

## S4 — Feasibility / Viability (paste)

| Layer | Status |
|-------|--------|
| Routing ≥2 tasks · Word walk · sandbox · Monitor A · fail-closed G7–G10 | **REAL** (eval + robust suite) |
| Two-laptop LAN peer demo | **REAL** (ops) · claim = private LAN, not air-gap |
| Excel / plant SoR write / SSO / full MCP registry | **LATER** |
| Venue NIC-off air-gap rehearsal | **OPTIONAL** stronger proof |

**Risks / mitigations**
- Mid-GPU VRAM: sequential load · smaller tags · PS allows smaller models.  
- Shadow paste: DRAFT + human gates + no cloud path.  
- Jury “air-gap?”: show Monitor/Share host = peer/local · say private LAN · offer NIC rehearsal if asked.  

---

## S5 — Impact / Benefits (paste)

- **Primary user:** inspection / integrity engineer — leaves with a **DRAFT they still own**.  
- **Social context (cite):** Cisco GenAI benchmark — large share of orgs admit pasting non-public data into GenAI (use published figure; not “our ROI”).  
- **Time (estimate, not MRPL SLA):** inspection pack assembly **days → hours to a DRAFT** (industry estimate).  
- **Org:** reduces incentive to paste confidential work into public tools; keeps evidence on premises.  

---

## S6 — Research / References (paste)

| Ref type | Examples |
|----------|----------|
| Problem | SIH26117 Expected Solution (verbatim bullets) |
| Governance | NIST AI RMF companion · IndiaAI ecosystem (ecosystem, not badge) |
| Pattern literature | ReAct / tool-using agents · RAG cite-or-abstain |
| Alternatives | Cloud assistants (blocked by policy) · bare local chat UIs (no grants/Word/evidence) |

**Difference line:** Artefacts, citations, human gates, and sovereign **evidence** on the hardware class the PS describes — not another chatbot skin.

---

## Your checklist before asking for PPT modifications

- [ ] Manual WF1 dual-model on desk  
- [ ] Manual WF2 attach → Word → export leave  
- [ ] Manual WF3 sandbox  
- [ ] Manual WF4 image source line honest  
- [ ] Manual WF5 Monitor / deny  
- [ ] Fill Team ID / names / college  
- [ ] Confirm which sovereign line you want on slides (private LAN vs stronger NIC claim)  
- [ ] Then ask: “update PPT / video from drafts”  

**Operator runbook for manual test:** `solution/prototype/E2E_FULL_SIMULATION_GUIDE.md`
