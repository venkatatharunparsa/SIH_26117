# ChatGPT 6-slide PNG spec — SIH26117

**DALL-E 3 path (current):** white vector body graphics. No workbench UI. See `DALLE_RULES.txt` and `PROMPT_S2.txt`–`PROMPT_S6.txt`.  
Do **not** attach `GRID_*.png` / `LAYOUT_*.png` to DALL-E (it copies the overlay).  
DALL-E native landscape is **1792×1024**. Ask for that, then paste onto the **white** official slide under the title.

**You generate PNGs. You paste onto the official template.**  
**I do not edit the PPTX.**  
**Precision rule:** quoted strings are verbatim. If a string does not fit, enlarge type. Do not paraphrase. White `#FFFFFF` only. No dark UI.

Placeholders (do not invent real values): `[TEAM_ID]` `[TEAM_NAME]` `[PRODUCT_NAME]`  
KPI locked for this render: **A** (1–5 days → 2–3 h to a DRAFT, labelled estimate). Swap only by editing the quoted KPI card.

---

## 0. Adversarial facts (read once)

1. Official canvas is **13.333 in × 7.5 in (16:9)** = **1920 × 1080 px** at 144 dpi. Source: `SIH2026-IDEA-Presentation-Format.pptx` (`prs.slide_width` 12192000 EMU).
2. SIH Official pointer 5: use **this** template; **do not change idea-detail pointers**. Recreating the SIH brain/logo in ChatGPT will look fake and can fail screening. **Keep chrome from the official file.**
3. ChatGPT Images often misspells dense tables. That is why each cell has **short quoted text**, one slide per prompt, and a **layout PNG attached**. If a word is wrong, **edit that cell only** — do not regenerate the whole slide.
4. ChatGPT landscape presets are often **1536×1024 (3:2)** or **1792×1024**, not 16:9. You must ask **1920×1080, 16:9**. If you get 1536×1024, do not stretch; regenerate or letterbox-crop back to 16:9.
5. **Slide 1 is typed in PowerPoint**, not generated, unless ChatGPT fails the other five and you still want a title PNG. Form fields are too easy to misspell (`SIH26117`).

---

## 1. Exact chrome to never paint over

Measured from the official PPTX. Coordinates at **1920×1080**.

| Lock | Inches (left, top, w, h) | Pixels | Hex / note |
|---|---|---|---|
| Slide size | 0,0, 13.333, 7.500 | 0,0, 1920,1080 | White `#FFFFFF` |
| Title chrome (slides 2–6) | 0,0, 13.333, 1.250 | 0,0, 1920,180 | Keep official title text |
| Team oval | 0.361, 0.276, 1.369, 0.883 | 52,40, 197,127 | Accent `#C0504D`. Type `[TEAM_NAME]` in PPT |
| SIH logo picture | 10.696, 0.002, 2.460, 1.162 | 1540,0, 354,167 | Official PNG. Do not redraw |
| Footer bar | 0, 6.950, 13.333, 0.550 | 0,1001, 1920,79 | `#0070C0` |
| Footer text | 5.083, 6.951, 3.504, 0.399 | 732,1001, 505,58 | `@SIH Idea submission- Template` |
| Slide number | 9.556, 6.951, 3.111, 0.399 | 1376,1001, 448,58 | 2…6 |
| Slide 1 field box | 0.362, 2.271, 6.479, 5.143 | 52,327, 933,741 | Type here |
| Slide 1 brain picture | 7.497, 1.877, 3.503, 3.747 | 1080,270, 504,540 | Do not cover |
| Slide 1 logo | same as others | 1540,0, 354,167 | Do not cover |

**Safe content rectangle (slides 2–6) — this is the only area the PNG may fill:**

| | Inches | Pixels |
|---|---|---|
| Origin | 0.333, 1.278 | **48, 184** |
| Size | 12.778, 5.611 | **1840 × 808** |
| Bottom-right | 13.111, 6.889 | **1888, 992** |

Footer starts at y=6.950 in. Logo ends at y=1.164 in. Oval ends at y=1.159 in. The box sits in the gap.

---

## 2. Grid (use these cell names in every prompt)

Content box split into **12 columns × 8 rows**.

Column x (left edge, px):  
`C1=48 C2=201 C3=355 C4=508 C5=661 C6=815 C7=968 C8=1121 C9=1275 C10=1428 C11=1581 C12=1735`  
right of C12 = **1888**

Row y (top edge, px):  
`R1=184 R2=285 R3=386 R4=487 R5=588 R6=689 R7=790 R8=891`  
bottom of R8 = **992**

Cell size ≈ **153 × 101 px**.

A region `C1–C6, R1–R3` means pixel box `(48,184) → (968,487)`.

Overlay files (attach these in ChatGPT):

| File | Use |
|---|---|
| `GRID_MASTER_1920x1080.png` | Cell IDs |
| `LAYOUT_S2.png` … `LAYOUT_S6.png` | Named regions for that slide |
| `GRID_SLIDE1_1920x1080.png` / `LAYOUT_S1.png` | Only if you generate slide 1 |

Folder: `sih_research/chatgpt_slide_prompts/`

---

## 3. How you run ChatGPT (do this order)

1. Open official `SIH2026-IDEA-Presentation-Format.pptx`. Duplicate it. Delete slide 7 later.
2. Screenshot **blank slide 2** at 100% zoom (or export slide as PNG 1920×1080 from PowerPoint: File → Export → PNG, 1920 width). Repeat for slides 3–6.
3. New ChatGPT chat per slide (do not stack six slides in one image).
4. Attach **two** images: (a) blank official slide screenshot (b) `LAYOUT_Sn.png`.
5. Paste **Prompt n** below. First line of your ChatGPT message: `Create a 1920 by 1080 PNG, 16:9, high quality.`
6. Check the QA list in §5. If a cell is wrong: *“Edit only region C…R…. Replace text with exactly: …”*
7. Save as `S2.png` … `S6.png` (and `S1.png` only if needed).
8. In PowerPoint, **Insert → Pictures** on that slide. Size the picture to **12.778 in × 5.611 in**, position **Left 0.333 in, Top 1.278 in**. Send **behind** the oval/logo if it overlaps. Do **not** cover footer or logo.
9. Type `[TEAM_NAME]` in the oval. Keep official titles: IDEA TITLE → you may type `[PRODUCT_NAME]` in the title placeholder. **Do not rename** the four idea pointers; they are already in the generated content as section headers.
10. Slide 1: type the six fields in the existing text box. Wrap the long title so it never enters x ≥ 1080 px.

**Do not** set a generated full-slide PNG as the slide background if it redraws the SIH logo.

---

## 4. Visual language (all slides)

- White body `#FFFFFF`. Navy headings `#1F497D`. Body text near-black `#1A1A1A`.
- Header bars `#1F497D` with white text. Table grid `#D6DCE4`.
- Thin accent line `#0070C0` (same as footer). Risk/warn `#C0504D`. OK/yes `#548235`.
- Font: clean sans (Calibri / Arial / Segoe). Headings **bold**. No script, no 3D, no isometric city, no robots, no neural-network clipart, no SIH brain copy.
- No paragraph blocks. Cards, tables, 6 rounded boxes max for the loop.
- No extra title such as “SMART INDIA HACKATHON” inside the content box (chrome already has it).
- No “Click here”, no QR, no fake URL, no 99%, no ₹crore savings, no 38,000 GPUs.

---

## 5. QA after every PNG (fail = regenerate that cell)

- Size is 16:9. If 3:2, reject.
- Logo, oval, footer not redrawn inside the PNG (PNG is **content-only**; transparent or white outside the 1840×808 box is OK).
- Every quoted string present, spelling identical (`SIH26117`, `Tesseract`, `python-docx`, `openpyxl`, `--network=none`, `NOT FOUND`, `₹10,371.92`).
- Pointer headers present **verbatim** (see each slide).
- No second flowchart on a slide that already has one (slides 2 and 3 each have **one** loop).

---

## 6. Six prompts

Copy **one prompt per ChatGPT message**. Keep the layout PNG attached.

---

### Prompt 1 — TITLE PAGE (prefer typing; prompt only if you must)

**Better method:** In PowerPoint, in the existing left text box, type exactly:

```
Problem Statement ID – SIH26117
Problem Statement Title- Sovereign On-Premise Agentic AI Workbench
using Open-Weight Multimodal LLMs for Confidential Industrial Work
Theme- Smart Automation
PS Category- Software
Team ID- [TEAM_ID]
Team Name (Registered on portal)- [TEAM_NAME]
```

Title already says `SMART INDIA HACKATHON 2026`. Oval: `[TEAM_NAME]`.  
Long title must stay **left of x=1080 px** (brain graphic).

**If you still generate S1.png:** attach `LAYOUT_S1.png`. Fill **only** pixel box `(52,327,933,741)`. Six rows F1–F6 with the six lines above. Leave brain and logo empty white. 1920×1080, 16:9.

---

### Prompt 2 — IDEA (attach `LAYOUT_S2.png` + blank slide 2)

```
Create a 1920 by 1080 PNG, aspect ratio 16:9, professional SIH idea-slide CONTENT PANEL only.

Canvas: 1920x1080. Fill ONLY the inner rectangle x=48 y=184 width=1840 height=808. Outside that rectangle: solid white. Do not draw a header, footer, SIH logo, brain graphic, oval, or slide number.

Use this 12x8 grid inside the rectangle. Column left edges px: 48,201,355,508,661,815,968,1121,1275,1428,1581,1735,1888. Row top edges px: 184,285,386,487,588,689,790,891,992.

Style: white background, navy #1F497D section bars, Calibri/Arial, no 3D, no robots, no extra text beyond the quoted strings.

REGION A — C1 to C6, R1 to R3. Section bar exactly: "Proposed Solution (Describe your Idea/Solution/Prototype)"
Then four bullets, exact text:
"• [PRODUCT_NAME]: on-prem agentic workbench. Not a chatbot. Not a new LLM."
"• Output: Word recommendation note + Excel thickness sheet + sandbox-tested code."
"• Software is OpenAI-compatible /v1 client. Org GPU holds weights."
"• Sovereign proof: WAN unplug + visible log = 0 external calls."

REGION B — C7 to C12, R1 to R3. Section bar exactly: "Detailed explanation of the proposed solution"
Draw six small rounded boxes in one row, arrows between them, labels exactly:
"1 Scan"
"2 OCR"
"3 /v1 extract"
"4 HITL JSON"
"5 Sandbox CR"
"6 Word DRAFT"
Under the boxes, two lines exactly:
"Same boxes at org scale. Mock EAM JSON now; real read-only API later. Never write DCS/SIS."
"8 GB: load one 7B-class at a time. Log two model ids. Skills on disk."

REGION C — C1 to C12, R4 to R6. Section bar exactly: "How it addresses the problem"
Table 2 columns, 5 data rows. Header cells exactly "PS requirement" and "Our mechanism".
Row1: "Claude/Codex forbidden on P&IDs" | "Nothing leaves LAN. WAN log is the demo."
Row2: "Manual 1–5 day inspection pack (estimate)" | "Cut find-and-type ~50–70%. Human still judges."
Row3: "Must not lock to one model" | "Model Cards + GET /v1/models. New GGUF = new card."
Row4: "Must act like an agent + real files" | "Tools: OCR, EAM lookup, sandbox, python-docx."
Row5: "Mid-range GPU; no 120B at venue" | "Sequential 7B Q4 on RTX 4060 8 GB (PS allows this)."

REGION D — C1 to C8, R7 to R8. Section bar exactly: "Innovation and uniqueness of the solution"
Three equal cards:
"1 vs ChatGPT / Copilot / Claude: air-gap + audit. Cisco 2024: 48% of orgs pasted non-public data into GenAI."
"2 vs Open WebUI / Ollama / PrivateGPT: we add task router + HITL JSON gate + sandbox calc + template Word."
"3 vs OpenHands / Continue: inspection-document workbench with a jail; we borrow patterns, we do not fork."

REGION E — C9 to C12, R7 to R8. Navy card, white text, exactly:
"WAN log = 0"
"That is the sovereign claim."

Do not add a seventh region. Do not invent metrics. Spell every technical token exactly: /v1, GGUF, python-docx, RTX 4060, DCS/SIS, HITL, OCR.
```

---

### Prompt 3 — TECHNICAL APPROACH (attach `LAYOUT_S3.png` + blank slide 3)

Keep official pointer titles inside the content (the template textbox is replaced by this PNG).

```
Create a 1920 by 1080 PNG, 16:9, SIH content panel only. Fill only x=48 y=184 w=1840 h=808. Outside: white. No logo, footer, oval, or extra titles.

Grid: columns 48,201,355,508,661,815,968,1121,1275,1428,1581,1735,1888. Rows 184,285,386,487,588,689,790,891,992.
Navy #1F497D bars, Calibri/Arial, no clipart robots.

REGION A — C1 to C12, R1 to R4. Section bar exactly: "Technologies to be used (e.g. programming languages, frameworks, hardware)"
Table 3 columns, 6 data rows. Headers exactly: "Layer" | "Tech" | "Purpose"
Row1: "Workbench (Laptop B)" | "Python 3 + FastAPI" | "Task route, HITL, audit. RTX 3050 not used for LLM."
Row2: "Runtime (Laptop A)" | "OpenAI-compat POST /v1/chat/completions + GET /v1/models (llama.cpp or Ollama or vLLM)" | "One 7B-class Q4 on RTX 4060 8 GB."
Row3: "OCR" | "Tesseract and/or PaddleOCR on CPU" | "Scan/photo to text. Fail closed if unusable."
Row4: "Agent skills" | "On-disk SKILL.md (agentskills.io)" | "inspect-extract, inspect-calc, inspect-draft, code-sandbox, sovereign-policy."
Row5: "Calc / code jail" | "Docker Desktop WSL2: docker run --network=none" | "CR formula + pytest. Never wrap the GPU."
Row6: "Files + KB" | "python-docx, openpyxl, JSON folder" | "Word+Excel from approved fields. JSON schema = future EAM."

REGION B — C1 to C8, R5 to R8. Section bar exactly: "Methodology and process for implementation (Flow Charts/Images/ working prototype)"
One horizontal flowchart, 8 boxes, exact labels in order:
"Upload scan"
"CPU OCR"
"vision_extract /v1"
"JSON fact sheet"
"HITL approve"
"CR in jail"
"draft_note /v1"
".docx DRAFT"
Second thin row of 3 boxes:
"code_sandbox"
"pytest in Docker"
"pass/fail"
One caption exactly: "CR = (t_prev - t_curr) / delta_t. LLM does not invent millimetres. Missing = NOT FOUND."

REGION C — C9 to C12, R5 to R8. Yellow-tinted card. Title exactly: "8 GB routing rule"
Body exact lines:
"Multiple roles in one system."
"Auto-pick by task, not by VRAM."
"On 8 GB load one model at a time."
"Log must show two distinct model ids."
"Venue GPU: change base_url only."
"Fallback if Docker blocked: WSL jail (weaker; say so)."

No second architecture. No logo salad. Spell FastAPI, Tesseract, PaddleOCR, python-docx, openpyxl, GGUF exactly.
```

---

### Prompt 4 — FEASIBILITY AND VIABILITY (attach `LAYOUT_S4.png` + blank slide 4)

```
Create a 1920 by 1080 PNG, 16:9, content panel only at x=48 y=184 w=1840 h=808. White outside. No chrome.

Grid columns 48,201,355,508,661,815,968,1121,1275,1428,1581,1735,1888. Rows 184,285,386,487,588,689,790,891,992.

REGION A — C1 to C12, R1 to R2. Section bar exactly: "Analysis of the feasibility of the idea"
Three equal cards:
"PS allows smaller models if 120B hardware is absent. 8 GB Q4 7B (~4.5–5.5 GB class) is that case."
"P1 / 36h is one loop, not SAP. Portal allows public sample PDFs/P&IDs."
"Viability: OSS + existing GPU. Scale = more GPUs behind the same /v1 socket. HITL stays forever."

REGION B — C1 to C12, R3 to R5. Section bar exactly: "36h honesty: REAL / MOCK / LATER"
Table 4 columns. Headers: "Item" | "REAL (P1)" | "MOCK" | "LATER (P2–P3)"
Row1: "OCR to HITL JSON to Word" | "Y" | "" | ""
Row2: "Excel CR in sandbox + pytest --network=none" | "Y" | "" | ""
Row3: "Two task types, two model ids" | "Y sequential" | "" | "Dual-load VRAM"
Row4: "WAN off + host log" | "Y" | "" | "Certified air-gap"
Row5: "EAM / SAP / historian" | "" | "JSON same schema" | "Read-only API"
Row6: "PPT, 14B, SSO, SIEM" | "" | "" | "Y"
Row7: "DCS / SIS write" | "NEVER" | "NEVER" | "NEVER"

REGION C — C1 to C12, R6 to R8. Section bar exactly: "Potential challenges and risks" on left third conceptually but the table spans full width with three columns. Second line of the bar may also show "Strategies for overcoming these challenges".
Table headers exactly: "Challenge" | "Risk" | "Mitigation"
Row1: "8 GB VRAM" | "Fake dual-load" | "Unload/load. Log two ids."
Row2: "7B JSON / tools" | "Bad mm or bad CR" | "Schema + HITL. Math only in sandbox."
Row3: "Bad scan" | "Invented readings" | "Confidence. NOT FOUND. Fail closed."
Row4: "Docker blocked at venue" | "No jail" | "Docker first. WSL fallback disclosed."
Row5: "App-only air-gap" | "Model pull on WAN" | "Pre-stage GGUF. Unplug. Host log."

Do not write highly scalable. Do not claim certified air-gap in P1.
```

---

### Prompt 5 — IMPACT AND BENEFITS (attach `LAYOUT_S5.png` + blank slide 5)

```
Create a 1920 by 1080 PNG, 16:9, content panel only x=48 y=184 w=1840 h=808. White outside. No chrome.

Grid columns 48,201,355,508,661,815,968,1121,1275,1428,1581,1735,1888. Rows 184,285,386,487,588,689,790,891,992.

REGION A — C1 to C7, R1 to R4. Section bar exactly: "Potential impact on the target audience"
Table 2 columns. Headers: "Who" | "What changes"
Row1: "Primary: inspection / integrity engineer" | "Draft Word + Excel from a scan. They approve."
Row2: "Secondary: process, HSE, maintenance, IT security" | "Same workbench. More skills later."
Row3: "Org context (not our MAU): MRPL 15.0 MMTPA; 2,530 staff (31 Mar 2025)" | "Stop shadow paste of P&IDs. Reuse mid-range GPU."
Row4: "Replication" | "Other PSU / defence-linked plants. Same /v1 socket. New templates."

REGION B — C8 to C12, R1 to R4. Navy KPI card, white text, exact lines:
"KPI (estimate, not an MRPL SLA)"
"Today: 1–5 days elapsed"
"Target: 2–3 hours to a DRAFT"
"Judgement stays human."
"We do not auto-approve FFS or shutdown."

REGION C — C1 to C4, R5 to R8. Section title "Social"
"Reduce shadow AI on confidential drawings."
"Cisco 2024 (n=2600, 12 countries): 48% of orgs admitted pasting non-public data into GenAI; 27% banned GenAI for a time."
"Cyberhaven Q2 2024: 73.8% of workplace ChatGPT accounts were non-corporate."
"Not an MRPL survey."

REGION D — C5 to C8, R5 to R8. Section title "Economic"
"Cut find-and-type time, not headcount."
"Reuse the 8 GB card. No crore savings claimed."
"IndiaAI rupees are national compute, not our P&L (see slide 6)."

REGION E — C9 to C12, R5 to R8. Section title "Environmental + policy"
"No extra training run."
"Do not claim greener than cloud (on-prem can use more energy)."
"Claim: no cloud round-trip of P&IDs; reuse hardware already bought."
"DPDP-shaped: no external processor. CERT-In-shaped: 180-day on-prem logs. Not a legal opinion."

Do not write 2530 users of our app. Do not print prize money.
```

---

### Prompt 6 — RESEARCH AND REFERENCES (attach `LAYOUT_S6.png` + blank slide 6)

```
Create a 1920 by 1080 PNG, 16:9, content panel only x=48 y=184 w=1840 h=808. White outside. No chrome. Tiny but readable sans-serif.

Grid columns 48,201,355,508,661,815,968,1121,1275,1428,1581,1735,1888. Rows 184,285,386,487,588,689,790,891,992.

REGION A — C1 to C6, R1 to R5. Section bar exactly: "Details / Links of the reference and research work"
Left list, exact bullets (URLs on the same line, no Click Here):
"• SIH26117 Expected Solution: Word path, sandbox, OCR, zero-egress."
"• MRPL 15.0 MMTPA — mrpl.co.in/Content/Profile"
"• OISD-STD-128 Inspection of Unfired Pressure Vessels — oisd.gov.in (name only)."
"• CERT-In Direction 20(3)/2022 — 180-day ICT logs."
"• DPDP Act 2023 (not a universal air-gap law)."
"• IndiaAI Mission Cabinet 07 Mar 2024, Rs.10,371.92 crore, 10,000+ GPUs — PIB PRID 2012355."
"• NIST AI 600-1 Generative AI Profile (Jul 2024)."
"• Yao et al. ReAct 2022 arXiv:2210.03629"
"• Schick et al. Toolformer 2023 arXiv:2302.04761"
"• Lewis et al. RAG 2020 arXiv:2005.11401"
"• Pfitzmann et al. DocLayNet KDD 2022 arXiv:2206.01062 (layout, not our OCR %)."
"• llama.cpp, vLLM, Tesseract, agentskills.io — compose, do not fork."
"• NASSCOM: India AI ~USD 8 bn (2025) ecosystem, not our TAM."

REGION B — C7 to C12, R1 to R5. Title exactly: "You vs existing (ticks only if true)"
Table. Headers: "System" | "Air-gap proof" | "Sandbox tests" | "HITL before Word" | "Word/Excel fields"
Row1: "[PRODUCT_NAME]" | "Y WAN log" | "Y" | "Y" | "Y"
Row2: "ChatGPT / Copilot / Claude" | "N" | "N" | "weak" | "cloud"
Row3: "Open WebUI + Ollama" | "possible local" | "N" | "weak" | "chat"
Row4: "OpenHands / Continue" | "local possible" | "Y coding" | "N" | "N"

REGION C — C1 to C12, R6 to R8. One navy bar, white text, exact:
"Difference: others give chat, infra, or coding agents. We give PSU inspection artefacts + cited numbers + visible sovereign proof on mid-range GPU."
Second line exact: "SIH 2026 screening: nine named criteria, no published percentage weights."

Do not tick PPT. Do not write 99% OCR. Spell crore as Rs.10,371.92 crore. Spell arXiv ids exactly.
```

---

## 7. PowerPoint placement (after PNGs exist)

For slides 2–6, select the generated PNG:

| Property | Value |
|---|---|
| Horizontal position | **0.33 in** from top-left of slide |
| Vertical position | **1.28 in** |
| Width | **12.78 in** |
| Height | **5.61 in** |
| Lock aspect ratio | On (16:9 content) |
| Z-order | Behind oval + logo; above white body |

Then type `[TEAM_NAME]` in the oval. Replace title `IDEA TITLE` with `[PRODUCT_NAME]` on slide 2 only. Leave `TECHNICAL APPROACH` etc. as official titles.

Export **PDF**. Delete slide 7.

---

## 8. If ChatGPT still ruins tables

Do not widen the prompt. Do this instead:

1. Generate **layout only** (colored empty regions, no table text).
2. In PowerPoint, put **native tables** on top of that PNG (text will be selectable and spelled correctly).
3. Keep the PNG for the flowchart boxes only (slides 2B and 3B).

That hybrid is more precise than a single raster of 80 words. It still uses your ChatGPT image plan.

---

## 9. What I still need from you (does not block generating)

1. Confirm you will **type slide 1** in the official text box (recommended).  
2. Confirm KPI A stays, or send the B caption to swap in Prompt 5 region B.  
3. Real `[PRODUCT_NAME]` when you have it — until then ChatGPT must print the bracket string.

Do not send a second PS. Do not ask ChatGPT to “make it look like a winner PPT.” Attach the layout PNG every time.
