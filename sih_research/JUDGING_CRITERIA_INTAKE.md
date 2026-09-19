# SIH26117 — Judging Criteria Intake (Third-Party + Primary Validation)

**Role:** Principal Solutions Architect / Research Engineer  
**Date:** 2026-09-16  
**Sources used:** User third-party judging research + primary PDF extraction  
**Local copies:** `sih_research/judging_sources/`

---

## A. What we accept from the third-party research

### ACCEPT as HIGH (now primary-verified)

| Claim | Verdict | Primary evidence |
|---|---|---|
| SIH 2026 idea-eval criteria = novelty, complexity, clarity/details, feasibility, practicability, sustainability, scale of impact, UX, future progression | **ACCEPT** | Official `SIH 2026 Guidelines.pdf` p.20 (downloaded from sih.gov.in) — exact wording matched |
| Ideas evaluated by experts after submission | **ACCEPT** | Same page |
| Solutions must be **new** / not present in prior event/program | **ACCEPT** | Official SIH 2026 Guidelines p.24 |
| Team = 6 members, ≥1 female, same college | **ACCEPT for 2026** | Official SIH 2026 Guidelines p.11 |
| Exact national 2026 numerical weights (20/25/25/20/10 etc.) | **REJECT as national fact** | Not in official 2026 PDF |
| Universal 2026 three-round 20/30/50 weights | **REJECT as 2026 fact**; **ACCEPT as historical MIC pattern** | Confirmed in official `Evaluation_Guidelines_for_sih2024.pdf` (MIC) — Round1 20%, Round2 30%, Round3 50% — label as **prior-edition finale model**, not verified 2026 national sheet |
| NMIET / college local rubrics = national SIH 2026 | **REJECT** | Institution-specific |
| “Judges primarily reward advanced AI” | **REJECT** | Criteria list has no “use AI” axis; PS asks open-weight multimodal for a reason, but novelty ≠ model brand |
| “Working prototype alone wins” | **REJECT** | Historical MIC Round3 also scores relevance, UX, impact, future plan, presentation |

### ACCEPT as practical inference (MED–HIGH)

| Inference | Why it works for us |
|---|---|
| Presentation/demo quality matters | Mentor duties + historical Round1/3 emphasize presentation; PS demands visible egress proof |
| Finale emphasizes working prototype | Official mentor responsibilities explicitly say convert idea → working prototype |
| Post-finale development expected | Guidelines: selected ideas supported further; more effort after finale required |
| Preparation rubric / judge Q-list from third-party | Useful as **prep**, not as official marksheet |

### Soften / correct third-party wording

| Third-party line | Our correction |
|---|---|
| Confidence 0.88 on criterion list | Raise to **~0.95** — we extracted the official PDF ourselves |
| Working prototype mandatory for Software (DTU notice) | Treat as **strong institutional guidance**; official 2026 PDF stresses prototype via mentor duties / finale, not a separate “mandatory for software” sentence in the pages we extracted — still build as if mandatory |

---

## B. Criterion → SIH26117 strategy map (what works for us)

| Official criterion | How we score it (evidence to show) | Risk if we ignore |
|---|---|---|
| **Novelty** | Gap = knowledge-work air-gapped workbench vs process AI (MRPL already has APC/predictive) vs chat RAG (Open WebUI) vs infra (GDC). Differentiator = **policy engine + entity resolution + Office templates + HITL + egress proof** — not “we use LLMs” | Judge: “this is just PrivateGPT” |
| **Complexity** | Hard parts: offline multimodal OCR, multi-model routing, sealed tools, zero-egress, entity/revision, classification routing. Show architecture diagram + what is hard vs mocked | Over-stack without necessity **or** hide hardness |
| **Clarity / prescribed format** | Explicit: users (inspection eng), root cause (assemble evidence), workflow (12-step → demo spine), architecture, real vs mock, risks, impact | Vague “AI platform” slides |
| **Feasibility** | Mid-range GPU + small models (PS allows); synthetic Confidential fixtures; mock connectors same schema; 36h plan | Depend on real SAP/DCS access |
| **Practicability** | Fits inspection → recommendation note workflow; draft badge; human approval; shift/day users; air-gap = org policy fit | Developer-only chat demo |
| **Sustainability** | Model registry (swap models), offline update story, ownership inside IT/OT enclave, CERT-In log retention design, post-SIH pilot path to MRPL Innovation Centre | One-shot hackathon toy |
| **Scale of impact** | Beachhead MRPL inspection; expand oil/gas → power → defence → gov (ontology swap). Quantify **time-to-assemble** as illustrative, not fake millions | “Helps all of India” with no channel |
| **UX** | Short flow: upload → OCR confidence → fact sheet → calc → draft Word → approve. Draft vs approved; citations; uncertainty; no over-trust | Pretty UI, unclear trust |
| **Future progression** | Phase1 doc search → Phase2 EAM/historian read-only → Phase3 MOC/HSE → Phase4 analytics; discovery checklist; no “add blockchain” | Generic future scope |

---

## C. Judge-prep implications for OUR locks (adversarial)

### Keep (aligned with judging + PS)

1. Industrial evidence workbench framing (novelty + practicability).  
2. Demo spine = inspection → Word (+ Excel) + sandbox coding + egress monitor (PS expected solution = Round3 functionality).  
3. Honest real vs mocked connectors (feasibility + clarity).  
4. Risk-tiered air-gap as strongest posture (practicability across sectors).  
5. HITL / never write DCS (UX trust + sustainability/regulatory).  
6. Org-scale architecture / scaled demo (future progression + sustainability).

### Change / emphasize for judges

| Change | Why |
|---|---|
| Lead with **competitor gap table** (novelty) | Official novelty axis; our prior “nothing exists” claim was wrong — rewrite is now judge-safe |
| Make **real vs mock** a dedicated slide/section | Feasibility + historical Round2 integration honesty |
| Show **post-SIH 6–12 month pilot plan** (sih.gov projectImplementation culture) | Future progression + sustainability |
| Quantify one KPI carefully: “inspection assemble 1–3 days → target <2 hours for draft” labelled **illustrative** | Impact without overclaim |
| Prep answers to third-party’s 15 judge questions | Practical; not official marks |
| Do **not** optimize for unofficial 20/25/25/20/10 | Avoid wrong target |

### Historical MIC 20/30/50 — how to use without lying

Use only as **rehearsal bias** if finale resembles prior years:

- Round1-like: story, novelty, approach, timeline  
- Round2-like: prototype progress, usability, integration  
- Round3-like (largest historical weight): **live demo relevance + performance + UX + impact + future plan**

→ Our build priority stays: **one rock-solid E2E demo path** over many shallow features. That matches both PS and historical Round3 emphasis.

---

## D. Judge Q&A pack (SIH26117-specific answers)

| Judge question | Our answer spine |
|---|---|
| Primary user + evidence? | Inspection engineer; PS expected solution; MRPL document-intensive ops (chairman/public KB) |
| Today’s process failure? | Scanned NDT → manual Excel → note; 40–80% time assembling (illustrative) |
| Existing solutions studied? | Ollama/Open WebUI/PrivateGPT; GDC/Azure Local; ArgusAI/Onsite/Elixara; MRPL process AI |
| Genuine novelty? | Classification policy engine + industrial entity/revision + template Office deliverables + sealed HITL + demonstrable zero egress — integrated for Indian sensitive orgs |
| Hardest part? | Offline OCR+entity+calc lineage under air-gap; not the chat UI |
| Data/APIs/hardware? | Local GPU; open-weight models; synthetic Confidential corpus; mock EAM/historian JSON |
| Real vs mocked? | Real: inference, OCR, calc, Word/Excel, routing logs, egress monitor. Mock: ERP/EAM/LIMS connectors |
| Bad input / missing data? | OCR confidence scores; draft badge; refuse autonomous FFS; human gate |
| Measurable improvement? | Time-to-first-draft + citation completeness + zero egress events (demo metrics) |
| Deploy/maintain after SIH? | On-prem enclave; model registry; offline updates; MRPL IT/OT ownership path |
| Cost? | Prototype: 1 mid GPU workstation; pilot: 48–80GB class; production: multi-GPU later |
| Next pilot who authorizes? | MRPL Innovation Centre / Inspection + IT — discovery checklist in KB |
| Privacy/security? | Air-gap; classification routing; CERT-In-oriented logs; no external telemetry |
| Why this tech? | PS mandates open-weight multimodal + local tools; cloud GenAI forbidden by confidentiality |
| Failure modes? | Hallucinated thickness without sandbox; wrong revision; permission leak — mitigated by calc sandbox, revision warnings, ACL |

---

## E. Decision for discussion

1. **Adopt** official 9 criteria as our idea-submission and jury narrative spine.  
2. **Reject** any unofficial national weighting as planning truth.  
3. **Use** MIC 20/30/50 only as rehearsal bias toward live demo excellence.  
4. **Upgrade** novelty slide to honest competitor matrix (already corrected in Synthesis v1).  
5. **Add** explicit sustainability + future-progression milestones to design lock (not just architecture boxes).  
6. **Still no stack lock / no build** until you approve design conversation items.

**Overall confidence:** Criterion list **0.95** (primary PDF). Continuity with MIC finale themes **0.75**. Exact 2026 finale weights **0.15** (unknown). Third-party research quality: **strong and usable after corrections above**.
