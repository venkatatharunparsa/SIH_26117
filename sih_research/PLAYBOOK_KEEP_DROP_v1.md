# Playbook keep / drop / approve — SIH26117

**Date:** 2026-09-16  
**Source:** `C:\Users\THARUN PARSA\Downloads\SIH_SOFTWARE_PLAYBOOK.md`  
**Stored copy:** `sih_research/judging_sources/SIH_SOFTWARE_PLAYBOOK.md`  
**Checked against:** official SIH 2026 Guidelines extract; SIH 2025 SPOC PDF (DRIEMS host, fetched); our `DESIGN_ORG_PROTOTYPE_v1.md`.

This is **not** an MIC document. It is a graded operating manual. We treat it the same way it treats itself: Official / Observed / Unverified / Invalidated.

---

## Verdict

**Use it for the official 6-slide portal PDF craft.**  
**Do not use it as a scoresheet, winner list, or college-round campaign.**  
**Do not let §7 (PS-117 example) override our locked spine** where they disagree.

---

## Verified this session

| Playbook claim | Check | Grade now |
|---|---|---|
| 6 slides, PDF only, do not rename pointers | Matches SIH2026 idea-format rumours **and** our earlier intake; official PPTX still **not** in this workspace | **Approve as operating rule** until the 2026 PPTX is in-hand |
| Nine screening criteria, no % | Matches SIH 2026 Guidelines p.20 (our extract) | **Official** |
| Team 6, same college, ≥1 female | Matches 2026 Guidelines | **Official** |
| Students cannot self-register; SPOC nominates | 2025 SPOC PDF (DRIEMS fetch) | **Official process** (2025 text). We still **do not design for college jury**. Portal still needs this path. |
| Max 50 teams (45+5), no SW/HW quota | 2025 SPOC PDF | **Official 2025.** Confirm 2026 PDF before quoting. |
| 4–5 teams per PS *may* be selected; org not obligated to pick a winner | 2025 SPOC PDF | **Official 2025** |
| Prize ₹1,50,000 if org likes the idea | 2025 SPOC PDF p.18 | **Official 2025.** Do not put rupees on our idea PDF. |
| 500 ideas freeze / 2 PS per team | 2025 SPOC PDF | **Official 2025.** Confirm 2026. |
| Numeric slide weights, 20/30/50, Reskilll 10-slide, GitHub “Winner” stamps | Playbook already **Invalidated**; we agree | **Drop** |
| 2026 dates, 2026 quota, 2026 prize | Playbook says re-check sih.gov.in | **Do not print as 2026 fact** |

---

## Take (approve for our PDF + prototype)

| Playbook item | How we use it |
|---|---|
| Stay inside official template; delete instruction slide | Portal PDF only |
| Points / diagrams, not paragraphs | Rewrite our slide bullets shorter |
| **Named product** on slide 2 | Working name: **Sovereign Workbench** (you can rename) |
| One **core-loop** flowchart, not logo salad | User → OCR → route → HITL → Word / sandbox code |
| Layer / tech / **purpose** table | Gateway, OCR, `/v1` 7B, docker jail, python-docx |
| Slide 4: **36h real vs mocked** columns | Copy our REAL/MOCK table, compressed |
| Challenge \| risk \| mitigation | 8 GB sequential; OCR; tool-calling; Docker on Windows |
| One **sourced** KPI, labelled estimate | Inspection assemble 1–5 days → **target hours for a DRAFT** (`06-document-templates` / KB: **industry estimate, not MRPL SLA**) |
| Competitor ticks **only where true** | vs ChatGPT/Copilot/Claude **and** Open WebUI/Ollama/PrivateGPT |
| PSU screener edge: air-gap, citations, HITL, no hallucinated numbers | Already our novelty |
| Finale: one PS loop, not five modules; leave 36h delta | Portal-level prototype = that loop |
| Do not show E2B / cloud sandbox | Already rejected |
| Do not invent plant KPIs / production SAP | Already rejected |
| Fill **Team ID** | When you send it; blank ID is a known fail in their sample |
| Screening PDF must stand alone (video may never be clicked) | No fake URL |

---

## Drop / do not approve

| Playbook or §7 line | Why |
|---|---|
| College-internal **tactics** (quota politics, 15-page SPOC report) | You said skip college rounds. Process still exists; we don’t spend design on it. |
| GitHub “winner” decks as proof | Playbook invalidated them; we don’t copy RockVision numbers |
| 10-slide / Figma-instead-of-template | Conflicts with official pointer 5 |
| Invented % attention per slide | Playbook invalidated |
| python-pptx as 36h artefact | Our lock: PPT is **LATER**. Word + Excel only |
| Flow “ask → retrieve → DMS” as the demo | Our spine is **scan → OCR → fact sheet → Word**. DMS is MOCK |
| Comparison ticks for PPT if we don’t ship PPT | Would be a MiTra-style fake tick |
| Prototype URL on the PDF before it loads | Don’t put Vercel theatre |
| “Ask two AIs” uniqueness method | Playbook: Unverified. Uniqueness = **PS constraint**, which we already have |
| 30/60/100 finale staging as a rule | Unverified; we only keep “leave a visible 36h increment” |
| ₹1.5 lakh / 500-cap / Nov dates on **our** slides | Year-mix risk |

---

## §7 PS-117 example vs our locked design

| Playbook §7 | Us | Decision |
|---|---|---|
| Inspection → Word + corrosion Excel + deny-all sandbox | Same | **Keep** |
| Uniqueness: air-gap, citation, HITL, classification | Same | **Keep** |
| OCR + open-weight + docx/xlsx + Docker no-net | Same | **Keep** |
| python-pptx in the tech table | LATER | **Drop from PDF tech table** |
| 36h real includes network monitor at zero | Same | **Keep** |
| Mock historian/EAM/LIMS JSON | Same | **Keep** |
| DPDP / CERT-In / SMLDI one line each | OK on slide 5 **one line**, not a policy dump | **Keep thin** |
| Matrix vs ChatGPT, Copilot, Claude only | Add **Open WebUI / Ollama / PrivateGPT** or we look like we never heard of local chat | **Approve with extra rows** |
| Flow through DMS | Mock later | **Drop from 36h flowchart** |

---

## What goes onto the official PDF (accepted craft)

Working title: **Sovereign Workbench** · PS **SIH26117** · Software

**Slide 2 uniqueness (3 ticks only):** on-prem / no WAN · every number cited or `NOT FOUND` · HITL before Word is a record · (sandbox-verified code as the second PS loop)

**Slide 3 loop:** ingest scan → CPU OCR → gateway `vision_extract` → HITL JSON → sandbox CR → gateway `draft_note` → `.docx` · parallel: `code_sandbox` + pytest in Docker `--network=none` · runtime = RTX 4060 8 GB sequential 7B.

**Slide 4 36h real:** OCR, two model ids, Word, Excel CR, sandbox tests, WAN unplug + log. **Mocked:** EAM JSON. **Not claimed:** SAP, 14B, PPT, two models in VRAM.

**Slide 5:** Primary = inspection engineer. KPI = KB 1–5 days → target hours **for a draft** (estimate). Shadow-AI stop. No crore savings.

**Slide 6:** OISD-STD-128 (name only) · API 510-class fields · OpenAI-compat local serving. Matrix: air-gap / citations / sandbox / HITL / Word|Excel — ticks true for us, false for ChatGPT and for Open WebUI.

---

## Still waiting (cannot finish the upload file)

1. Official `SIH2026-IDEA-Presentation-Format.pptx`  
2. Team ID + registered team name  
3. 2026 SPOC PDF if you want 2026 caps/dates on anything public  

Playbook stored. Idea **content** updated to playbook rules. The portal PDF is still not a generated `.pdf` until the official template is here.
