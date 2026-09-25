# Knowledge Work Bench — Idea PPT content pack

**Product:** Knowledge Work Bench (KWB)  
**Problem:** SIH26117 · Smart Automation · Software  
**Format:** Official SIH idea PDF — **exactly 6 slides** (title included). Pointers **must not be renamed**.  
**Date:** 2026-09-21  

### Review drafts (start here)

| File | Role |
|------|------|
| **[`prompt/`](./prompt/README.md)** | **ChatGPT + DALL·E prompt pack** — master narrative, per-slide prompts, diagram image prompts (playbook-aligned). Start here to design the official 6-slide PDF. |
| **[`DRAFT_PPT_PACK_20260921.md`](./DRAFT_PPT_PACK_20260921.md)** | PPT paste pack — dual-model, Word, private-LAN honesty |
| **[`DRAFT_VIDEO_SCRIPT_20260921.md`](./DRAFT_VIDEO_SCRIPT_20260921.md)** | Demo/video narration |
| `../solution/prototype/E2E_FULL_SIMULATION_GUIDE.md` | Manual cold-boot → WF0–WF5 before locking slides |

**Rule:** Do **not** paste into official PPTX / record final video until you finish manual workflows and request modifications.

---

## How to use this folder (legacy + diagrams)

| File | Role |
|---|---|
| `00_README.md` | Index (this file) |
| `00_NARRATIVE_ARC.md` | Story through the 6 slides + speak timing |
| `00_ADVERSARIAL_Q_AND_PLAN.md` | Hostile jury / screener questions + planned answers |
| `00_INTEGRITY_RULES.md` | Banned language, metrics grades, CERT honesty |
| `00_PLAIN_LANGUAGE.md` | **H1/H2/H3 → plain words** dictionary (use this on every slide) |
| `D01_CONTEXT_DIAGRAM.md` | **Diagram 1 — Context** (Slide 2) · image SoT = `prompt/DALLE_S02_CONTEXT.md` gen **920×420** → crop **~920×200** |
| `D02_COMPONENT_DIAGRAM.md` | **Diagram 2 — Components** (Slide 3 primary visual) |
| `S01_TITLE.md` … `S06_RESEARCH_REFERENCES.md` | Older per-slide packs — **prefer DRAFT_PPT_PACK_20260921** where they conflict |
| `SPEAKER_SCRIPT.md` | Older ~5-minute idea-PDF voice — **prefer DRAFT_VIDEO_SCRIPT** for demo video |

**Diagram plan:** Slide 2 = **who/what around KWB** (context). Slide 3 = **what’s inside** (components / three planes). Do not put both full diagrams on one slide.
---

## Official 6 pointers (do not rename)

1. Title  
2. Proposed Solution (idea / solution / prototype)  
3. Technical Approach  
4. Feasibility and Viability  
5. Impact and Benefits  
6. Research and References  

---

## Sources this pack obeys

- Official SIH 2026 idea template (6 slides + delete instructions)  
- `sih_research/judging_sources/SIH_SOFTWARE_PLAYBOOK.md`  
- Frozen solution + demo evidence (`eval/CHECKLIST.md`, `PS_ROBUST_TEST_REPORT.md`, `REDTEAM_ADV_REPORT.md`, `E2E_FULL_SIMULATION_GUIDE.md`)  

**Ignored as official:** Reskilll 10-slide decks, invented % rubrics, “winner PPT” GitHub mirrors.

---

## One-sentence product line (use everywhere)

> **Knowledge Work Bench** is an on-prem industrial workbench that routes open-weight models by task, gates human verification, and delivers cited **DRAFT Word** plus sandbox-verified calc/code — with grants, audit, and a Monitor A evidence pack — on mid-range GPU hardware.
