# SIH software playbook (adversarial-checked)

Strategies only. No application and no PPT file is generated here. This is a **software-edition** operating manual for the whole Smart India Hackathon path: college internal round → 6-slide idea PDF → national screening → 36-hour finale. PS-117 (MRPL workbench) is one worked example at the end, not the whole game.

Hardware exists in the same programme (same idea-PDF template; longer finale). This file does not try to win hardware.

---

## 0. How to read this file

Every claim is graded:

| Grade | Meaning | What you should do with it |
|---|---|---|
| **Official** | On the 2026 idea template (slide 7) or in MIC/AICTE College SPOC guidelines | Obey it |
| **Observed** | Visible in our extracted idea decks / digest; not proof that the team won | Steal the craft, not the status |
| **Unverified** | Alumni posts, YouTube, Scribd “rulebooks”, blogs | Useful rumour. Never treat as a scorecard |
| **Invalidated** | Contradicted by a stronger source | Do not repeat as fact |

If a blog and the official template disagree, the template wins.

---

## 1. Claim ledger (adversarial pass)

### 1.1 Invalidated or unsafe — do not repeat as fact

| Claim we (or the files) previously implied | What actually checks out | Grade |
|---|---|---|
| TechPioneers and GeoGuards both **won** SIH 2025 PS SIH25071 | Filenames in `previous_winner` say “Winner”. Public posts name **HACKMONKS06 (Datta Meghe College of Engineering, Airoli)** as the national winner for SIH25071 (Ministry of Mines / NIRM). GeoGuards’ LinkedIn post is an **internal** TMU hackathon (Sep 2025), not a national result. | **Invalidated** as winner labels. Keep the two PDFs as **same-PS idea-deck samples** only. |
| Those two PDFs are a “winner natural experiment” proving beauty is not the filter | You cannot infer “they won *because* of layout” if they are not verified winners. Opposite layouts on the same PS still exist in the files (words-first vs picture-first). That is a **layout sample**, not a win proof. | **Invalidated** as causal claim. **Observed** as two styles on one PS. |
| Code+Catalyst / Shree Anna Connect is a verified **finalist** | File is a LinkedIn 6-slide PDF. Several unrelated “Code Catalyst / CodeCatalysts” teams exist on other PS IDs. | **Invalidated** as result status. **Observed** as a content-heavy idea PDF. |
| The 17-deck folder is a **winner corpus** | Convenience sample of SIH 2025 idea PDFs/PPTX plus one old NTRO deck (TECH NATIVES, PS SIH1456, **pre-6-slide** template). Almost every title slide has a **blank Team ID**. | **Invalidated** as “winners”. **Observed** as craft sample. Blank Team ID is a corpus defect, not a winning habit. |
| `SIH2026_Official_Winning_Playbook_and_Strategy_TechDoodles.pdf` is MIC/AICTE | Filename says Official. Body is a third-party guide. It proposes a **different slide list** (Problem Understanding, Proposed Solution, …) and Gamma/Canva tooling that **conflicts** with official pointer 5 (“use provided template, do not change pointers”). | **Invalidated** as official. **Unverified** as student advice. |
| Innovation 25% / feasibility 20% / impact 20% / PPT 15% (Reskilll-style) | Contradicts the official 6-slide file, which publishes **no numeric weights**. | **Invalidated** as rubric |
| Finale round weights 20% / 30% / 50% (Scribd “Marking”) | Not MIC-stamped in anything we could fetch. Conflicts with other rumours (30/60/100 *product* staging is a different claim). | **Invalidated** as official weights |
| College nomination is 30 Software + 15 Hardware (Zaid-style blogs) | 2025 SPOC PDF: max **50 teams (45 + 5 waitlist)**; **no software/hardware quota** inside that cap. Mix is the college’s choice. | **Invalidated** |
| Software prize is ₹1 lakh (Neurosignal-style blogs) | 2025 SPOC PDF: **₹1,50,000** per PS if the organisation likes the idea. | **Invalidated** |
| Screening attention is 8/28/22/16/14/12% across the six slides | Invented heuristic from an earlier canvas. No MIC data. | **Invalidated** as numbers. Idea + Technical *feeling* important is still reasonable as **Unverified** psychology. |
| Screeners spend 2–3 minutes per PDF | Guess about tired remote readers. No official timing. | **Unverified** (heuristic only) |
| `sih.gov.in` FAQ numbers are current for 2026 | Search snippets still show **2024** (25+5 teams, 12 Sep 2024). Prefer the on-disk **2026 template** and a college-hosted **2025 SPOC PDF**. Re-check sih.gov.in before treating any date or quota as this year’s. | **Unsafe** without a fresh official PDF |
| Public GitHub “SIH Winners PPT” repos are a verified winner archive | Aadiii00 and kartik7607 are the **same tree**. Joyson stamps TechPioneers + GeoGuards as national winners and TechDoodles as MIC. Three of four 2024 “winner” decks fail `SIH_PS_Winners_2024.csv`. Aadiii README recommends **10 slides**. | **Invalidated** as winner/MIC. See §1.5. |

### 1.2 Official — lead with these

Sources: on-disk `SIH2026-IDEA-Presentation-Format.pptx` (7 slides; slide 7 is instructions to delete before upload) and SIH 2025 College SPOC guidelines (MIC/AICTE text as hosted by DRIEMS: `https://www.driems.ac.in/wp-content/uploads/2025/09/SIH2025-Guidelines-College-SPOC.pdf`).

| Rule | Detail | Grade |
|---|---|---|
| Idea file | Maximum **six slides including title**. **PDF only** (no PPT, Word, or other). | Official |
| Headings (do not rename) | 1 Title · 2 Idea (solution, how it addresses, uniqueness) · 3 Technical Approach (stack + flowchart/images/prototype) · 4 Feasibility and Viability · 5 Impact and Benefits · 6 Research and References | Official |
| Density | Points / diagrams / infographics / pictures — **not paragraphs**. Precise and easy to understand. | Official |
| Template lock | Use the provided template; **do not change the idea-detail pointers**. | Official |
| Novelty | Idea should be unique and novel; must **not** have been presented in a previous event/programme. | Official |
| Path | Students cannot self-register. College **internal hackathon** → SPOC nominates → team leader completes idea (title, description, **PDF**). | Official |
| Nomination cap (2025 text) | Max **50** teams per institute (**45 shortlisted + 5 waitlisted**). | Official (2025 SPOC PDF; confirm 2026 PDF) |
| Team | **6** students including leader; **same college**; **≥1 female**; software: **majority should have strong programming skills**. Optional ≤2 mentors. | Official |
| PS load | One team may submit against **maximum 2** problem statements. A PS can **freeze at 500** ideas. | Official (2025 SPOC PDF) |
| Screening criteria (no %) | Novelty, complexity, **clarity and details in the prescribed format**, feasibility, practicability, sustainability, scale of impact, user experience, potential for future work. | Official |
| Finale shortlist | **4–5 teams per PS** *may* be selected; **the PS-creating organisation is not obligated to declare a winner**. | Official |
| Software finale duration | ~**36 hours** continuous build is the standard software edition (hardware is longer). | Official process / consistent SPOC + rulebook language. Confirm the year you enter. |
| Prize / IP (2025 text) | **₹1,50,000** if the organisation likes the idea. IP typically split with the PS owner or by mutual agreement. | Official (2025) |

### 1.3 Observed in our files — craft, not trophies

Extracted in `past_hackathon_patterns/_digest.txt`. Treat named teams as **sample decks**.

**Patterns that make a software PDF scannable**

- Named product on slide 2 (TransitMind, Sehat Sathi, MiTra, FloatChat, MAITRI, Shree Anna Connect).
- Layer / technology / purpose table (Code+Catalyst).
- Competitor matrix with real alternatives (Code+Catalyst vs ONDC/eNAM/DeHaat; MiTra vs Indian college chatbots).
- Org-specific constraint named in plain words (Niyati: **Maximo**, IBL, ranked induction list, 40+ trainsets; Runtime Terror: **NSG** cameras / node graph).
- Honest risk column (Sehat Sathi: OCR, lab-range variability, medical sensitivity).
- Prototype or live URL on the PDF (Code+Catalyst vercel-style link; AttenAI demo URL in the same sample set).

**Patterns that hurt meaning (still in the files)**

- Paragraph walls (COMET / FloatChat — high character count vs official “no paragraphs”).
- Broken slide order (Automation Guys: feasibility on slide 5, impact on 6, “End…..”, no references).
- Leftover chrome: “TITLE PAGE”, “IDEA TITLE”, “Your Team Name”, blank **Team ID** (most of the sample).
- Logo / library salad without one loop (Automation Guys lists Flask **and** Django **and** FastAPI).
- Invented global metrics (TechTrek: “billions worldwide”, 10x–50x reach).
- Comparison table with every cell winning and no evidence (MiTra).
- TECH NATIVES: old template, wrong year for 2026, cloud speech APIs as the product.

**TechPioneers vs GeoGuards (SIH25071 samples)**

Both PDFs are **image-only** (0 extractable text in the digest). Layout contrast is from rendered slides, not OCR:

- TechPioneers: words + architecture + competitor ticks; product name **RockVision AI** visible on the renders.
- GeoGuards: mine drawing + flow + charts; thin references.

Do **not** quote their 70–90% / $2–5M figures as validated metrics; they were read from pictures in an earlier pass and are not in `_digest.txt`. Steal arrangement, not numbers.

### 1.4 Unverified — list as tactics, never as rules

| Rumour | Where it comes from | How to use it |
|---|---|---|
| Three live finale evals (Day 1 / mid / Day 2 end) | Scribd “SIH 2025 Grand Finale Rulebook”; Rushabh Bhalgat SIH 2024 write-up | Plan as if you will be seen **three times**. Confirm on arrival. |
| Show ~30% / ~60% / 100% across those rounds | YouTube “SIH Finale Roadmap 2025” winner story | Leave a **visible 36-hour delta**. Same speaker claimed “SI policy: only 50% built before finals” — **no official PDF says that**. |
| Mentor suggestions become next-round criteria | Rushabh and other alumni | Write every mentor ask in a shared note; show it done next round. |
| Prototype video 2–3 minutes, URL on the PPT | LinkedIn (Team Invariants-style advice) | Video is extra. Screening may never click. The six slides must stand alone. |
| Skip the official template / use Figma only | LinkedIn finale-looking advice | **Conflicts with Official pointer 5.** Design **inside** the white rectangle of the official file. |
| “Judges spend very little time per slide” | TechDoodles third-party PDF | Reasonable anxiety. Not a measured MIC statistic. |
| Grand finale pitch decks expand to **8–15 slides** | JoysonBeera README “Key Takeaways” | Plausible for a **live nodal-centre pitch**, not for the portal idea PDF. Screening stays **6 slides**. Unverified as a rule. |

### 1.5 GitHub “winner PPT” repos — checked, mostly the same pile

These four public repos were harvested. They are **student mirrors**, not MIC. Several files are already on disk under `past_hackathon_patterns` and `previous_winner`. Filename “Winner” in a GitHub tree is the same trap as a Downloads folder.

| Repo | What is actually in it | Verdict |
|---|---|---|
| [Aadiii00/SIH-Winners-PPt-and-Sources](https://github.com/Aadiii00/SIH-Winners-PPt-and-Sources) | README + PDFs at **repo root** (no `Winners-PPTs/` folder the README advertises). Includes GeoGuards, Tech Pioneers, TechDoodles, four 2024 PDFs, a 2023 deck, and “Easy vs Difficult Problem Statements.” Upsells a paid “SIH Winners Vault.” README teaches a **10-slide** outline. | **Invalidated** as official. Same 10-slide conflict as Reskilll. Craft sample only. |
| [kartik7607/SIH-PPT-AND-RESOURCES-](https://github.com/kartik7607/SIH-PPT-AND-RESOURCES-) | **Clone of Aadiii00**: README blob SHA `9b6810cc…` is identical; same file names and sizes. | Not a second source. |
| [JoysonBeera/sih-winning-presentations](https://github.com/JoysonBeera/sih-winning-presentations) | Best organised (year/domain folders + `manifest.json`). README claims “verified winning presentations.” Manifest still stamps TechPioneers **and** GeoGuards as “National Winner,” and TechDoodles as “Official Master Guide” under MIC. Most 2025 rows are more honest: “Internal Hackathon Winner / Selected for Nationals.” README misstates the six pointers as Title / Problem Understanding / Proposed Solution / Feasibility / Impact / Future Scope. | Useful **file index**. **Invalidated** as a winner oracle and as an official heading list. |
| [mohitjoping/SIH-ppt-references](https://github.com/mohitjoping/SIH-ppt-references) | README last promised updates until **18 Sep 2024**. Contains 2024 idea-format PPTX files, `SIH ppt (applications added).pptx` (TECH NATIVES / SIH1456 — already in our extract), a 2022 PDF, and `Hacking Bad_01.pdf`. | Historical templates. Not 2026 MIC. Not a winner list. |

**2024 PDFs in Aadiii/Joyson vs our official-ish winner CSV** (`SIH_PS_Winners_2024.csv`):

| GitHub label | PS | CSV actual TEAM NAME / status | Grade |
|---|---|---|---|
| Team AKY / GreenSort AI = National Winner | SIH1592 | **TrashCam** (Kirti Rathi) = Winner | **Invalidated** |
| Team Techbyte = National Winner | SIH1587 | **Team Codiee** and **Escape Character** = Joint Winner | **Invalidated** |
| Team Innovators = National Winner | SIH1605 | **SHILEDAR** = Winner; Team Boka = consolation | **Invalidated** |
| Cannon Crew = National Winner | SIH1686 | **Canon Crew** (Nikhil Guru Venkatesh, KMIT) = Winner | **Likely the same team** (spelling). Deck is still an idea PDF, not proof the *slides* won. |

**Where our `previous_winner` filenames came from:** Aadiii00, kartik7607, and JoysonBeera all host the identical GeoGuards / TechPioneers PDFs with `Winner` in the name. That is a **replication chain**, not three independent confirmations.

**What you can still take from the repos**

- 2025 software idea PDFs in Joyson’s `SIH_2025/` are the same convenience sample we already digested. Steal tables and flows; ignore award stamps.
- Joyson’s split is useful: **screening = 6-slide official PDF**; a longer deck, if any, is a **finale live pitch**, not the portal file.
- mohitjoping’s `SIH2024_IDEA_Presentation_Format*.pptx` shows the 6-slide idea format already existed in 2024. Do not use 2024 chrome for a 2026 upload; use the 2026 template on disk.
- Aadiii00’s 10-slide “Recommended SIH PPT Structure” is **student folklore**. Do not build the idea PDF that way.

---

## 2. The software path (where you can lose)

```
Internal college hackathon
        → SPOC nomination (quota)
                → National idea PDF (6 slides)
                        → Expert screen (qualitative criteria)
                                → Software finale (~36h, usually 3 evals)
```

| Stage | Who decides | What they actually look at | How software teams die here | Grade |
|---|---|---|---|---|
| Internal college hackathon | Your SPOC / faculty jury | Talk + maybe a mock demo; they fill a **quota** | Cannot explain the PS; missing female member; late file; pretty idea with no loop | Official process |
| National idea PDF | Ministry / PSU / industry screener, often remote | **The 6-slide PDF only.** A prototype URL only if it is **on a slide** and they click | Generic chatbot; wall of text; no 36h honesty; no difference vs ChatGPT; wrong template | Official format |
| Finale round 1 (typical) | Nodal jury + PS mentors | Did you understand the PS; is a path to a working slice real | Showing “finished product” with nothing left for 36 hours | Unverified staging; Official that a working prototype is the point |
| Finale round 2 (typical) | Same jury | Progress since round 1; mentor notes implemented | Ignoring mentor feedback; git chaos; demo broken | Unverified as rubric; Observed in alumni stories |
| Finale round 3 (typical) | Same jury | Working core loop, pitch, Q&A, deployability | Feature pile; crash on stage; cannot answer “how is this different” | Unverified as weights |

**Software vs hardware (do not mix tactics)**

- Same 6-slide idea PDF.
- Software finale is a **digital product in ~36 hours**. Hardware is a longer on-site prototype (often cited as 72+ hours). This playbook is software.

**Deadlines and caps change by year.** 2025 SPOC text used 30 Sep 2025 and a 500-idea freeze. Confirm 2026 dates on sih.gov.in / the year-specific SPOC PDF before you treat any date as locked.

---

## 3. Official 6 slides — do / don’t / filler (any software PS)

Stay inside the official template. Delete slide 7 (instructions) before upload.

| Slide | Official pointer | Do this | Do not do this | Filler you can reuse |
|---|---|---|---|---|
| 1 Title | PS ID, title, theme, Software/Hardware, Team ID, registered team name | Fill **every** field including Team ID. Wrap the PS title so it never hits the SIH brain graphic. | Leave Team ID blank (most of our sample did). Extra college collage. Wrong year. | Exact portal strings. Category = Software. |
| 2 Idea | Solution · how it addresses · uniqueness | Replace “IDEA TITLE” with a **product name**. Three blocks. Optional small screenshot or URL box. | Opening paragraph. Feature dump that is a second product. “Powered by AI/ML/Blockchain/IoT” with no how. | One sentence + ~5 bullets + 3 uniqueness bullets + prototype URL |
| 3 Technical | Technologies · methodology (flowcharts / images / working prototype) | One flowchart of the **core loop**. Side table: layer, tool, **purpose**. Show the output artefact (dashboard, Word, Excel, ranked list, QR). | Logo salad. Two frontends “just in case.” Flask+Django+FastAPI on one slide. | User → ingest → process → artefact → human check |
| 4 Feasibility | Feasibility · challenges/risks · mitigations | Three columns. One line: **demoable in 36h vs mocked**. | Only “open source so cheap.” Decorative art over text. Adjectives (“highly scalable”) with no countermeasure. | Challenge \| High/Med/Low \| mitigation |
| 5 Impact | Target audience · benefits (social, economic, environmental) | Primary / secondary audience. One **sourced** KPI. | SDG laundry list. Duplicate of Idea. “Billions of users.” | Who \| what changes \| number + source |
| 6 References | Details / links of reference and research | Gov/PS-org docs + 1–2 papers + **you vs existing tools** + live link. | Scribd as a source, “Click Here” with no URL, skipping the slide, “End…..” | You vs 3 real alternatives; ticks only where true |

**Official uniqueness test (screening):** if two public AIs both invent the same app for the PS, that overlap is what half the field will submit. Your uniqueness is usually a **constraint from the PS owner’s world** (air-gap, Maximo, offline, on-device, explainable list, sandbox), not “we also use an LLM.” (The “ask two AIs” method is **Unverified** Invariants-style advice; the uniqueness requirement is **Official**.)

---

## 4. How to show data on a software PDF

Official rule: not paragraphs. Observed craft that fits that rule:

| Pattern | Where it belongs | Steal this (sample decks) | Do not steal this |
|---|---|---|---|
| 2-column: words left, picture right | Idea, Technical | Pipeline or operator screen on the right | A screenshot that is not your product |
| 3-column table: Layer / Tech / Purpose | Technical | Code+Catalyst — each library has a job | Logo wall with React+Angular+Django+Streamlit |
| Challenge \| risk \| mitigation | Feasibility | High/Med/Low + one countermeasure | Feasibility as adjectives |
| Audience \| benefit \| number | Impact | Primary user, secondary user, one KPI | “Billions worldwide” (TechTrek) |
| You vs existing tools | References (or uniqueness on Idea) | Ticks only where you truly differ | Every cell green with no evidence (MiTra) |
| Operator output | Technical or Idea | Niyati ranked induction list; Runtime Terror node graph | Decorative pie with fake slices |

### Metrics that survive Q&A

A metric without a source is a dare to the jury. Winners (and non-winners) in the wild use bold numbers; that does **not** make invented percentages safe.

| Shape | Honest example from samples or KB | Honesty test | If you cannot pass |
|---|---|---|---|
| Time: before → after, same unit | KB: scanned inspection 1–5 days → target hours (industry estimate, not a plant SLA) | Who timed it? | Write “target, from workflow study,” not “we achieve” |
| Count of people / assets | Niyati: 40+ trainsets (org-scale, not your users) | Is the count from the PS org or a census? | Use the org’s published number only |
| Accuracy / latency | AttenAI-style 99% / 30s claims in the sample | Measured on what set? 36h demo or a paper? | “Baseline in literature; we will measure on *this* camera set” |
| Money | Market-size rupees on millet / mine decks | Market size ≠ your revenue | Drop rupees; keep time and safety |
| Phase plan | Niyati: CSV then API; Code+Catalyst 6 months / 1 year / 3 years | Does phase 0 fit 36 hours? | Label mock connectors vs live APIs |

Prefer **one sourced number** over five round ones.

### Eye path (heuristic, not a stopwatch)

**Unverified.** A remote screener still has to answer, in order: Who is this and which PS? What is the product? Can I redraw the flow? Can they demo a slice in 36 hours? Who benefits? Why is this not ChatGPT? If the portal file has no working URL, they never see a video.

---

## 5. Selector edges by organisation type

Strategy, not a scored rubric. Screening criteria are qualitative (**Official**). These edges are how software teams look **specific** instead of generic.

| Selector type | What they fear | Edge you can show on the PDF |
|---|---|---|
| Ministry / PSU (data-sensitive) | Cloud leak, hallucinated numbers, no audit trail | On-prem / air-gap / citations / human accept / classification |
| Ops org (metro, mine, plant) | Toy dashboard; cannot talk to Maximo / EAM / historian | Name **their** system; explainable output; override button |
| Public service (education, health, agri) | English-only, needs 4G, not for the real user | Offline, language, low-end device, named scheme (eNAM, ICMR, Khelo) |
| Defence / LEA / NTRO-like | Generic CV demo, no domain method | Hybrid method (not one YOLO); research citations; no cloud dependency |
| Any software screener | This is ChatGPT with a UI | Comparison matrix + one constraint AIs would not invent |

Showing data works when it is a **table or flowchart** the screener can redraw. It does not work as a paragraph of market size. Code+Catalyst’s comparison table does more work than a dartboard of buzzwords (COMET). That is **Observed** craft, not a trophy.

---

## 6. Software finale (after you are shortlisted)

**Official:** you must produce a working prototype; travel to a nodal centre; software edition is a short continuous build.

**Unverified but consistent enough to plan against:** three evaluations; mentors from the PS organisation; mentor notes reappear as questions.

### Build

- Roles for six people: tech lead, frontend/demo, backend/integration, research/citations, QA/demo owner, pitch. **≥1 female is Official at formation** — do not discover this at SPOC.
- MVP is **one loop that matches the PS**, not five modules at 40%.
- Git + one deploy target rehearsed at home. Local demo **video on a phone** if venue Wi-Fi dies.
- Progress staging (~30 / ~60 / full loop) is **Unverified**. The surviving idea: do not arrive with a frozen 100% demo and nothing to show for 36 hours.

### Pitch and Q&A

- Open with the beneficiary, then demo, then architecture. Slides after the demo.
- Write mentor suggestions in a shared note; the next round should show they were done.
- Prepare: why this PS, what exists, assumptions, scale, what you would do with a month, how it is maintained.
- “I don’t know yet” beats a fake accuracy. Sehat Sathi-style medical-sensitivity / not-a-diagnosis caution is **Observed** honesty, not a guarantee.

### What the 36 hours are for

Jury at a nodal centre can tell pre-built theatre from work done on site. You do **not** need an official “50% rule” to leave a visible increment. You do need a core loop that still runs if a library install fails.

---

## 7. Worked example — PS-117 (one software PS)

Use this only if you stay on the MRPL / air-gapped workbench problem. Same six-slide rules as every other software PS. Numbers below are from `sovereign-ai-workbench-kb`, which labels inspection times as **industry-based estimates, not MRPL benchmarks**.

| Slide | What to put (you write it) |
|---|---|
| 1 | Exact SIH title, **Software**, theme as on the portal, **Team ID filled** |
| 2 | Named product. Scanned inspection → Word recommendation note + corrosion Excel, executed in a **deny-all sandbox**. Uniqueness: air-gap, citation on every number, human gate before a document becomes a record, classification (Restricted / Confidential) |
| 3 | Flow: ask → retrieve authorised files → draft/code → sandbox → engineer accept → DMS. Table: OCR, open-weight LLM, python-docx / openpyxl / python-pptx, Docker or Podman **no network**. Output artefact: Word + Excel, not a chatbot bubble |
| 4 | **36h real:** OCR + one Excel path + citations + human accept + network monitor at zero. **Mocked:** historian / EAM / LIMS connectors as schema-matched JSON/CSV (`10-feasibility/04-real-vs-mocked.md`). Risks: hallucination, OCR, classification leak. Mitigations: citations, sandbox, human accept |
| 5 | Inspection / process / HSE / procurement / finance. Time from KB: scanned inspection **1–5 days → target 2–3 hours** (estimate). Stops shadow ChatGPT on P&IDs. Align DPDP / CERT-In / SMLDI in one line each, not a policy dump |
| 6 | OISD / API / IndiaAI. Matrix vs ChatGPT, Copilot, Claude, cloud RAG — ticks **only** for air-gap, citations, sandbox, HITL, Word/Excel/PPT |

Do not invent plant KPIs. Do not claim production SAP. Do not show a cloud sandbox (E2B) as the 36-hour demo.

---

## 8. Non-negotiables for a software idea PDF

1. Official 6-slide template, pointers unchanged  
2. PDF upload  
3. Team ID filled  
4. Named product  
5. One flowchart, not a logo wall  
6. 36-hour honesty (real vs mocked)  
7. Risk \| mitigation table  
8. One sourced metric  
9. Competitor ticks only where true  
10. Prototype URL if you have one that actually loads  

---

## 9. Sources

### Official / primary (prefer these)

- On-disk idea template: `past_hackathon_patterns` extract of `SIH2026-IDEA-Presentation-Format.pptx` (also originally under Downloads). Slide 7 instructions quoted in `past_hackathon_patterns/_digest.txt`.
- SIH 2025 College SPOC guidelines (MIC/AICTE text, college-hosted copy): https://www.driems.ac.in/wp-content/uploads/2025/09/SIH2025-Guidelines-College-SPOC.pdf  
  Confirm the **2026** SPOC PDF on sih.gov.in before using 2025 dates, 50-team cap, 500-idea freeze, or ₹1,50,000 as this year’s numbers.
- Process overview: https://www.sih.gov.in/ — FAQ snippets were still showing **2024** quotas when checked; do not copy FAQ dates blindly.
- Contact on the 2025 SPOC PDF: sih.gov.in · sih@aicte-india.org / hackathon@aicte-india.org

### Corpus (observed craft)

- Digest of extracted decks: `past_hackathon_patterns/_digest.txt`
- Idea decks under `past_hackathon_patterns/_extract/` (SIH 2025 software PDFs/PPTX + TechDoodles third-party PDF + TECH NATIVES old template)
- Same-PS image PDFs: `C:\Users\HP\Downloads\previous_winner\`  
  `SIH2025_SIH25071_Rockfall_Prediction_Team_TechPioneers_Winner.pdf`  
  `SIH2025_SIH25071_Rockfall_Prediction_System_Team_GeoGuards_Winner.pdf`  
  **Filename “Winner” is not a verified national result.**

### 2024 winner CSV (edition mix, not slide advice)

- `past_hackathon_patterns/SIH_PS_Winners_2024.csv`
- Row counts in that file: **221** lines containing `,Software,` · **92** containing `,Hardware,` · **128** containing `Joint Winner`
- Use this only to remember that software is the larger edition and that **joint winners happen**. It does **not** tell you how to lay out a 2026 PDF. It does **not** validate SIH25071 2025 filenames.
- It **does** falsify three of four “2024 National Winner” decks in the GitHub mirrors (AKY / Techbyte / Innovators). SIH1686 CSV winner is **Canon Crew**, close to GitHub’s Cannon Crew.

### Unverified (labelled in the ledger)

- Rushabh Bhalgat, “My Smart India Hackathon 2024 Journey”: https://rushabhbhalgat.github.io/articles/smart-india-hackathon-2024-journey-guide.html
- YouTube: “SIH Finale Roadmap 2025 Travel | Rounds | Strategy | My SIH Winning Story”
- LinkedIn posts claiming HACKMONKS06 won SIH25071 (used only to **invalidate** the TechPioneers/GeoGuards winner filenames; not an MIC results PDF)
- Scribd “grand finale rulebook” / marking sheets — not treated as MIC
- Reskilll / Neurosignal / Zaid / TechDoodles — student or commercial guides; contradict the official template where noted
- GitHub mirrors (not MIC; see §1.5): [Aadiii00/SIH-Winners-PPt-and-Sources](https://github.com/Aadiii00/SIH-Winners-PPt-and-Sources) (kartik7607 is the same tree), [JoysonBeera/sih-winning-presentations](https://github.com/JoysonBeera/sih-winning-presentations), [mohitjoping/SIH-ppt-references](https://github.com/mohitjoping/SIH-ppt-references)

### PS-117 numbers

- `sovereign-ai-workbench-kb/04-workflows/00-overview.md` (inspection 1–5 days; AI target 2–3 hours; estimates, not MRPL SLAs)
- `sovereign-ai-workbench-kb/04-workflows/10-coding-sandbox-workflow.md` (deny-all sandbox; SIH asks for a coding task in a sandbox)
- `sovereign-ai-workbench-kb/10-feasibility/01-36-hour-plan.md`
- `sovereign-ai-workbench-kb/10-feasibility/04-real-vs-mocked.md`

---

## 10. What this file is not

- Not a PPT and not a Figma file  
- Not a workbench implementation plan  
- Not an MIC scoresheet  
- Not a claim that any deck in `past_hackathon_patterns` won SIH 2025  
- Not a claim that GitHub folders named “winning presentations” are MIC results  

If you only remember four things: **obey the six slides**, **name a product that fits the PS owner’s constraint**, **show one loop you can demo in 36 hours**, **do not trust a filename that says Winner**.
