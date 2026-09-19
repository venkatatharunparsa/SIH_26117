# Solution — Knowledge Work Bench (SIH26117)

**Product:** Knowledge Work Bench (KWB)  
**Org:** MRPL · **PS:** SIH26117 · Software · Smart Automation  
**Official PS:** `../sih_research/sovereign-ai-workbench-kb/01-problem-context/01-problem-statement.md`  
**App code:** `../backend/` (build next)

---

## Folder map

```text
solution/
  README.md                 ← you are here
  freezes/                  ← BINDING contracts only (*_FREEZE.md)
  wp/                       ← per-WP architect / red-team / verify / drafts
  connection/               ← WP-20 system picture + architecture + stack SoT
  prototype/                ← REAL/MOCK/LATER overlay + demo build plan
  design-inputs/            ← pre-freeze agendas / repo map / inventory
  ppt-paused/               ← idea PDF prompts (paused — demo first)
```

---

## Read order (before coding)

| # | Path | Why |
|---|---|---|
| 1 | `freezes/WP-00_FREEZE.md` | Product contract · Must / Never |
| 2 | `connection/WP-20_ORG_CONNECTION.md` | Connected loop |
| 3 | `connection/ARCHITECTURE_HIGH_LEVEL.md` | Diagrams |
| 4 | `connection/TECH_STACK_SOURCE_OF_TRUTH.md` | Interfaces vs brands |
| 5 | `prototype/PROTOTYPE_OVERLAY.md` | REAL / MOCK / LATER |
| 5a | `prototype/APPLICATION_FLOW_COMMON.md` | **LOCKED** common flow A→J |
| 5b | `prototype/ORG_TECH_DESIGN.md` | Organisation-complete tech design **ACCEPTED** |
| 5c | `prototype/ORG_ARCHITECTURE_DIAGRAMS.md` | **Org architecture diagrams** (discuss / accept) |
| 5d | `prototype/DEMO_TECH_STACK.md` | Demo-narrowed stack (after org diagrams) |
| 5e | `prototype/ARCHITECTURE_DIAGRAM_DISCUSSION.md` | Earlier demo-first draft — superseded for order |
| 6 | `prototype/REPO_PULL_MAP.md` | Clone → extract → compose |
| 7 | `prototype/OPENHANDS_EXTRACT.md` | OpenHands / SDK take vs refuse (workbench first) |
| 8 | `prototype/DEMO_BUILD_PLAN.md` | G1–G10 build order |
| 9 | `freezes/WP-18_FREEZE.md` | Eval / demo_ready |

Supporting detail for any WP: `wp/WP-XX/`.

---

## Binding freezes (`freezes/`)

| WP | File | Topic |
|---|---|---|
| 00 | `WP-00_FREEZE.md` | Product contract · planes · Never |
| 01 | `WP-01_FREEZE.md` | Roles · jobs · artefacts |
| 02 | `WP-02_FREEZE.md` | Plant connectors · KWB store |
| 03 | `WP-03_FREEZE.md` | Ingest OCR/VLM |
| 04 | `WP-04_FREEZE.md` | Session ≠ grant |
| 05 | `WP-05_FREEZE.md` | HITL H1–H12 |
| 06 | `WP-06_FREEZE.md` | Orchestrator (software brain) |
| 07 | `WP-07_FREEZE.md` | Specialists · skills · tools |
| 08 | `WP-08_FREEZE.md` | MCP host |
| 09 | `WP-09_FREEZE.md` | Gateway |
| 10 | `WP-10_FREEZE.md` | Runtime |
| 11 | `WP-11_FREEZE.md` | Authz-first RAG |
| 12 | `WP-12_FREEZE.md` | Output gates |
| 13 | `WP-13_FREEZE.md` | Monitors A/B |
| 14 | `WP-14_FREEZE.md` | Lineage |
| 15 | `WP-15_FREEZE.md` | Personal `.md` |
| 16 | `WP-16_FREEZE.md` | Sandbox |
| 17 | `WP-17_FREEZE.md` | Audit |
| 18 | `WP-18_FREEZE.md` | Fail-closed · G1–G10 |
| 19 | `WP-19_FREEZE.md` | USB offline |
| 21 | `WP-21_FREEZE.md` | Context packer |
| 22 | `WP-22_FREEZE.md` | Three-source claims |
| 23 | `WP-23_FREEZE.md` | Untrusted T0–T4 |
| 24 | `WP-24_FREEZE.md` | Model Cards |

**WP-20** is not a freeze file yet — open connection design lives in `connection/`.

---

## Rules

- Freezes in `freezes/` are **binding**. Do not contradict in code.  
- Stack brands: see `connection/TECH_STACK_SOURCE_OF_TRUTH.md` (still candidates until locked).  
- PPT: **paused** under `ppt-paused/`.  
- Next: build demo spine in `../backend/` per `prototype/DEMO_BUILD_PLAN.md`.

---

## Next

1. Follow `prototype/REPO_PULL_MAP.md` (vendor clones + extract).  
2. Compose app in `../backend/` (grants → gateway → G1–G10).  
3. PPT remains under `ppt-paused/`.
