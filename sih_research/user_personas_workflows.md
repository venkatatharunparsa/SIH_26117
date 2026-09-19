Perfect—now I can reconstruct the **real user personas, their core workflows, and exactly how they’ll use your application** by reading between the lines of the problem statement and cross-referencing with verified PSU/refinery/defence workflow documentation.

I’ll structure this as:

1. Real end-user personas (who will actually use this)
2. Their core workflows today (step-by-step, with pain points)
3. How they will use your AI workbench in practice (day-to-day usage patterns)
4. What the problem statement *really* expects (adversarial reading)
5. Implications for your design and demo

***

## 1. Real end-user personas (actual humans, not “the organization”)

From MRPL’s structure and similar PSUs, the primary users are **knowledge workers in technical and secretariat roles**, not “IT” or “AI teams”. They are:

### Persona A: Process / Mechanical / Inspection Engineer (Refinery/Plant)

- Works in: Process Engineering, Mechanical, Inspection, Reliability departments  
- Typical profile: B.Tech/M.Tech in Chemical/Mechanical/Instrumentation, 3–20 years experience  
- Daily work:
  - Reviews **inspection reports** (thickness measurements, corrosion rates, NDT findings)  
  - Performs **engineering calculations** (line sizing, relief valve sizing, pump hydraulics, thickness per ASME, etc.)  
  - Prepares **technical justification notes** for modifications, deviations, repairs  
  - Reads and interprets **P&IDs, isometrics, vendor drawings**, often scanned or photographed  
- Pain points:
  - Spending hours extracting key findings from long inspection PDFs  
  - Manually copying data into Excel for calculations  
  - Drafting repetitive approval notes from old templates  
  - Cross-checking against SOPs and standards manually [datacalculus](https://datacalculus.com/en/blog/oil-and-gas/inspection-engineer/inspection-engineer-refinery-unit-inspection-in-oil-and-gas)

### Persona B: Operations / Maintenance Engineer / Shift In-charge

- Works in: Operations, Maintenance Planning, Turnaround/Shut-down teams  
- Typical profile: Diploma/B.Tech, strong field experience  
- Daily work:
  - Raises **file notes** for operational changes, temporary deviations, repair approvals  
  - Coordinates with inspection and engineering for **shutdown planning**  
  - Reviews **field inspection photos**, handwritten logs, operator rounds data  
- Pain points:
  - Turning field observations + inspection findings into formal approval notes  
  - Compiling data from multiple sources (inspection reports, past files, emails)  
  - Time pressure during shutdowns and incidents [datacalculus](https://datacalculus.com/en/blog/oil-and-gas/inspection-engineer/inspection-engineer-refinery-unit-inspection-in-oil-and-gas)

### Persona C: Projects / Contracts / Procurement Executive

- Works in: Projects, Contracts, Procurement, Vendor Management  
- Typical profile: Engineering + MBA or CA/CS, handles tenders and contracts  
- Daily work:
  - Prepares **comparison reports**, **file notes**, **bid evaluation summaries**  
  - Reviews **vendor documents**, technical offers, correspondence  
  - Drafts **board notes** for high-value approvals  
- Pain points:
  - Manually compiling comparison tables from vendor PDFs and Excel  
  - Drafting standardized but precise file notes and board presentations  
  - Ensuring consistency with past decisions and policies [elsai](https://www.elsai.ai/blog/how-elsai-governs-defence-procurement-workflows-for-psus-rfq-to-po)

### Persona D: Board Secretariat / Corporate Strategy / Finance

- Works in: Corporate Office, Board Secretariat, Strategy, Finance  
- Typical profile: CA, CS, MBA, or senior engineers in corporate roles  
- Daily work:
  - Prepares **board presentations**, **confidential strategy notes**, **policy drafts**  
  - Consolidates inputs from multiple departments into **board notes**  
  - Handles **sensitive business strategies**, financials, unreleased plans  
- Pain points:
  - Summarizing long technical inputs into concise board-ready language  
  - Ensuring alignment with past board decisions and policies  
  - No safe AI tool to help draft or summarize confidential material [ongcindia](https://ongcindia.com/web/eng/about-ongc/subsidiaries/mrpl)

### Persona E: Internal Tools / Automation Developer (small team)

- Works in: IT, Digitalization, or a small “automation cell” within engineering  
- Typical profile: B.Tech/M.Tech in CSE/IT, knows Python/Excel/VBA  
- Daily work:
  - Builds **small internal tools**: scripts to parse reports, Excel macros, data cleaners  
  - Automates repetitive data extraction and calculations  
  - Supports engineers with ad-hoc coding tasks  
- Pain points:
  - No safe environment to prototype code that touches confidential data  
  - Engineers paste code/data into public LLMs, creating risk  
  - Spending time on boilerplate code instead of real logic [github](https://github.com/Suketu-ADT/sovereign-workbench)

These are the **actual humans** who will sit in front of your workbench.

***

## 2. Their core workflows today (before AI)

Let’s map 3 representative workflows that your system must improve.

### Workflow 1: Inspection report → Approval note (core refinery use case)

**Trigger:** An inspection agency submits a scanned PDF report (e.g., thickness survey, corrosion mapping, NDT findings).

**Current manual flow:**

1. Engineer downloads the scanned PDF from email/DMS.  
2. Opens it in a PDF viewer, manually:
   - Highlights key findings (e.g., “Line X: 30% wall loss”, “Vessel Y: pitting depth 4 mm”)  
   - Notes critical equipment IDs, line numbers, locations  
3. Opens relevant **SOP / standard** (ASME, OISD, internal manual) from shared drive or physical copy.  
4. Manually checks:
   - Is the observed condition within acceptable limits?  
   - Does it require immediate repair, monitoring, or replacement?  
5. Opens Excel and:
   - Enters key numbers (thickness, design thickness, corrosion rate)  
   - Runs calculations (remaining life, MAWP, required thickness)  
6. Opens Word and:
   - Copies an old approval note template  
   - Edits it: inserts equipment details, findings, calculations summary, recommendation  
   - References the SOP clause manually  
7. Saves the note, prints or uploads to the file system, then:
   - Sends for review to senior engineer / department head  
   - Incorporates comments, re-circulates  
8. Final note is signed (physically or digitally) and filed.

**Pain points:**

- 60–80% of the work is **mechanical**: extracting data, copying templates, formatting.  
- High risk of **transcription errors** and missed clauses.  
- Takes **hours to days**, especially if multiple reports arrive together (e.g., during shutdown).  
- Under time pressure, engineers may **paste text into public AI** to get a quick draft. [datacalculus](https://datacalculus.com/en/blog/oil-and-gas/inspection-engineer/inspection-engineer-refinery-unit-inspection-in-oil-and-gas)

### Workflow 2: Engineering calculation + justification for a modification

**Trigger:** Need to modify a line size, install a bypass, change a set pressure, etc.

**Current manual flow:**

1. Engineer gathers:
   - Process data (flow rates, pressures, temperatures) from PFD/P&ID or DCS logs  
   - Equipment datasheets, vendor manuals  
2. Performs calculations:
   - In Excel, Mathcad, or even on paper  
   - May write small scripts (Python/MATLAB) if comfortable  
3. Prepares a **calculation sheet**:
   - Shows assumptions, formulas, inputs, outputs, code references  
4. Drafts a **technical justification note**:
   - Why the change is needed  
   - What standards are satisfied  
   - Risk assessment (if any)  
5. Routes for review/approval similar to Workflow 1.

**Pain points:**

- Re-deriving standard calculations repeatedly.  
- Formatting calculation sheets to match internal standards.  
- Ensuring all assumptions and references are clearly documented. [whatispiping](https://whatispiping.com/process-engineering-deliverables/)

### Workflow 3: Board note / presentation from multiple department inputs

**Trigger:** Management wants a board note on a project, investment, or policy.

**Current manual flow:**

1. Secretariat sends a circular to departments: “Send your inputs by Friday.”  
2. Each department sends:
   - Long technical notes, Excel sheets, sometimes scanned annexures  
3. Secretariat staff:
   - Reads through all inputs  
   - Summarizes into a concise note (often 5–15 pages)  
   - Prepares a PPT for board discussion  
4. Multiple review cycles with senior management.

**Pain points:**

- Huge effort in **summarization and consolidation**.  
- Maintaining consistency in tone, format, and references.  
- Handling **confidential** financials, strategies, and projections that cannot go to cloud AI. [ongcindia](https://ongcindia.com/web/eng/about-ongc/subsidiaries/mrpl)

***

## 3. How they will actually use your AI workbench (target usage patterns)

Your application is not for “AI researchers”; it’s for these engineers and executives as a **daily productivity tool**. Here’s how they’ll use it in practice.

### Usage pattern 1: “Drop a report, get an approval note draft”

**User:** Inspection / Process Engineer  
**Goal:** Turn a scanned inspection report into a draft approval note + calculation summary.

**How they’ll use the workbench:**

1. Opens the workbench UI in their browser (on internal network).  
2. Uploads:
   - Scanned inspection report PDF (may include photos, handwritten notes)  
   - Optionally selects relevant SOP/standard from a dropdown (or lets the system auto-detect).  
3. Types a natural-language instruction, e.g.:

   > “Read this inspection report, extract key findings for lines L-1234 and L-5678, check against SOP MRPL-INS-07, compute remaining life and required thickness, and draft an approval note in Word format.”

4. The system:
   - Runs OCR + vision on the scanned PDF  
   - Extracts findings (thickness values, corrosion rates, anomalies)  
   - Retrieves relevant SOP clauses from the local knowledge base  
   - Performs calculations with steps shown  
   - Generates a `.docx` approval note with:
     - Background  
     - Key findings (tabulated)  
     - Reference to SOP clauses  
     - Calculation summary  
     - Recommendation  
5. Engineer:
   - Reviews the draft  
   - Makes minor edits (adds context, adjusts tone)  
   - Sends for review/approval via existing file system.

**Efficiency gain:**

- From **2–3 hours** of manual work to **15–20 minutes** of review + edit.  
- Reduces transcription errors and ensures SOP references are correct. [datacalculus](https://datacalculus.com/en/blog/oil-and-gas/inspection-engineer/inspection-engineer-refinery-unit-inspection-in-oil-and-gas)

### Usage pattern 2: “Help me do this calculation and show steps”

**User:** Process/Mechanical Engineer  
**Goal:** Perform a standard engineering calculation with traceable steps and generate a calculation sheet.

**How they’ll use the workbench:**

1. Opens the workbench, selects a “Calculation Assistant” mode (or just chats).  
2. Provides inputs in natural language or via a small form:

   > “Calculate required thickness for a 24-inch carbon steel line, design pressure 40 kg/cm², design temperature 350°C, corrosion allowance 3 mm, as per ASME B31.3. Show all steps and generate a calculation sheet in Word.”

3. The system:
   - Identifies this as a **calculation task** → routes to a model good at structured reasoning + code.  
   - Runs a sandboxed Python script to compute thickness using the correct formula.  
   - Generates a formatted calculation sheet with:
     - Input data  
     - Formulas (with code references)  
     - step-by-step computation  
     - Final result and checks  
4. Engineer:
   - Reviews the calculation  
   - May ask follow-ups: “What if corrosion allowance is 2 mm?”  
   - Downloads the calculation sheet and attaches it to the file.

**Efficiency gain:**

- Eliminates manual formula lookup and Excel sheet setup.  
- Ensures consistent formatting and clear documentation for audits. [whatispiping](https://whatispiping.com/process-engineering-deliverables/)

### Usage pattern 3: “Draft a board note from these inputs”

**User:** Board Secretariat / Corporate Strategy  
**Goal:** Summarize multiple department inputs into a board-ready note + PPT.

**How they’ll use the workbench:**

1. Uploads:
   - Multiple PDFs/Word docs from departments (technical notes, financial projections, scanned annexures).  
2. Gives instruction:

   > “Summarize these inputs into a 10-page board note with sections: Background, Proposal, Financial Implications, Risks, Recommendations. Also create a 10-slide PPT summary. Use our standard board note template.”

3. The system:
   - Summarizes each input document  
   - Extracts key numbers (CAPEX, OPEX, IRR, timelines)  
   - Drafts the board note in the organization’s template  
   - Generates a PPT with:
     - Problem statement  
     - Options considered  
     - Financial summary  
     - Risk matrix  
     - Recommendation  
4. Secretariat staff:
   - Reviews and edits  
   - Circulates for internal review.

**Efficiency gain:**

- Cuts consolidation time from **days** to **hours**.  
- Ensures consistent structure and language across board notes. [ongcindia](https://ongcindia.com/web/eng/about-ongc/subsidiaries/mrpl)

### Usage pattern 4: “Write and test a script to parse these reports”

**User:** Internal tools developer / automation-savvy engineer  
**Goal:** Generate and test code that parses inspection reports or extracts data from Excel.

**How they’ll use the workbench:**

1. Uploads:
   - A few sample inspection PDFs or Excel files  
2. Asks:

   > “Write a Python script that parses these inspection PDFs, extracts line number, thickness, and corrosion rate, and writes them to a CSV. Run it in a sandbox and show me the output.”

3. The system:
   - Routes to a **code-specialized model**  
   - Generates Python code using OCR + PDF parsing libraries  
   - Executes it in a sandboxed environment  
   - Shows the resulting CSV and any errors  
4. Developer:
   - Reviews the code  
   - Asks for modifications: “Also add a column for remaining life”  
   - Downloads the final script to integrate into internal tools.

**Efficiency gain:**

- Safe environment to prototype code on **confidential data** without leaking to cloud.  
- Faster iteration on internal automation scripts. [github](https://github.com/Suketu-ADT/sovereign-workbench)

***

## 4. Adversarial reading: what the problem statement *really* expects

Reading between the lines of the SIH statement plus PSU/defence context:

### Expectation 1: This must feel like “Claude/Codex but inside our firewall”

They are not asking for a “chatbot with RAG”. They want:

- A **general-purpose reasoning assistant** that can:
  - Understand long, messy, scanned documents  
  - Do structured calculations  
  - Write and run code  
  - Draft real documents (Word, PPT, Excel)  
- With an experience quality close to **Claude/Codex**, because that’s what their people are already tempted to use.  
- If your demo feels like a toy (only text Q&A, no agents, no files), it will fail the “useful in real work” test. [github](https://github.com/Suketu-ADT/sovereign-workbench)

### Expectation 2: Prove sovereignty technically, not just verbally

The statement explicitly says:

> “show, through logs or a visible network monitor, that no external calls are made at any point. That’s the actual proof of the sovereign claim, not just a statement of it.”

This means judges will look for:

- A **network monitor view** or log panel showing:
  - All model inference calls are to `localhost` or internal IPs  
  - All RAG queries hit a local vector DB  
  - Zero outbound HTTP calls during task execution  
- Ideally, a demo with the **network cable unplugged** and the system still working.  

If your architecture has any hidden external dependency (e.g., calling a cloud embedding API, auto-updating models from Hugging Face at runtime), that breaks the core promise. [github](https://github.com/Suketu-ADT/sovereign-workbench)

### Expectation 3: Multi-model routing must be real, not fake

The statement says:

> “The backend should not be locked to one model. It needs to support multiple open weight models at once and automatically pick the right one for a given task…”

They want to see:

- At least **two distinct models** in action:
  - e.g., one for coding/math, one for document summarization/drafting  
- A **router** that:
  - Inspects the task (coding vs summarization vs vision)  
  - Chooses the appropriate model  
  - Can be extended later with new models without redesign  

A hard-coded “if coding then model A else model B” is acceptable for SIH if it’s **architecturally extensible** and you can explain how new models would be added. [github](https://github.com/Suketu-ADT/sovereign-workbench)

### Expectation 4: Agentic behavior = multi-step planning + tool use + iteration

The phrase:

> “Plan out multi step work, call local tools such as file read and write, code execution in a sandbox, spreadsheet work, internal document search, and iterate on a task instead of answering once and stopping.”

This is a clear signal they want:

- An **agent loop** that:
  - Breaks tasks into sub-steps  
  - Calls tools (file I/O, code execution, RAG, document generation)  
  - Checks outputs and retries if needed  
- Not a single-turn “ask → answer” chatbot.  

Your demo should visibly show **multiple steps** (e.g., OCR → extract → retrieve SOP → calculate → draft Word file). [github](https://github.com/Suketu-ADT/sovereign-workbench)

### Expectation 5: Multimodal is non-negotiable (scanned docs, drawings, photos)

The statement explicitly lists:

> “scanned PDFs, handwritten notes, engineering drawings, photographs, read through on device OCR and vision models.”

This means:

- If your system only handles clean digital text, it **does not meet the requirement**.  
- You must demonstrate at least one flow with:
  - A **scanned, possibly noisy PDF** (ideally with some handwritten annotations)  
  - Or an image of a drawing/photo that the system interprets.  

Judges will treat this as a core differentiator from simple local chatbots. [github](https://github.com/Suketu-ADT/sovereign-workbench)

### Expectation 6: Real deliverables, not just chat messages

The statement stresses:

> “Output should be real deliverables, approval notes, PPT/Word/Excel files, working code, calculations with steps shown, not just chat replies.”

So:

- Your demo must produce **downloadable files**:
  - `.docx` approval note  
  - `.xlsx` calculation sheet or data extract  
  - `.pptx` summary (optional but strong)  
  - `.py` or `.ipynb` code file  
- The chat can explain, but the **value** is in the generated files. [github](https://github.com/Suketu-ADT/sovereign-workbench)

***

## 5. Implications for your design and demo strategy

Given all this, your **target user journey** for SIH should look like:

### Primary demo scenario (must-have)

**Scenario:** Inspection report → Approval note + calculation

1. Upload a **scanned inspection report PDF** (realistic, with some noise).  
2. System:
   - OCRs and extracts key findings  
   - Retrieves relevant SOP clauses from local knowledge base  
   - Performs a calculation (e.g., remaining life, required thickness)  
   - Generates a **Word approval note** with:
     - Findings table  
     - SOP references  
     - Calculation summary  
     - Recommendation  
3. Show:
   - The generated `.docx` file  
   - Logs proving all calls were local (no external network traffic).  

This single flow demonstrates:

- Multimodal (scanned PDF)  
- Local RAG (SOPs)  
- Agentic multi-step planning  
- Real deliverable (Word file)  
- Sovereignty (logs/network monitor) [datacalculus](https://datacalculus.com/en/blog/oil-and-gas/inspection-engineer/inspection-engineer-refinery-unit-inspection-in-oil-and-gas)

### Secondary demo scenario (strongly recommended)

**Scenario:** Coding task in sandbox

1. Ask: “Write and run a script to parse these inspection PDFs and output a CSV.”  
2. System:
   - Routes to a code-specialized model  
   - Generates and executes code in a sandbox  
   - Shows the CSV output  
3. Download the script as a `.py` file.

This shows:

- Multi-model routing (code vs document tasks)  
- Safe code execution  
- Real deliverable (script + CSV) [github](https://github.com/Suketu-ADT/sovereign-workbench)

### Optional but impressive

- A **board note + PPT** generation flow from multiple inputs.  
- A **P&ID/drawing understanding** demo (even if limited, e.g., extracting text labels, identifying equipment tags).  

***

## 6. Design implications (what to prioritize)

From a user-requirement perspective:

1. **UX must be simple for non-AI users**  
   - Engineers should not need to select models or configure pipelines.  
   - They should just: upload files + type a natural-language instruction.  

2. **File generation is core, not optional**  
   - Invest in high-quality templates for:
     - Approval notes (`.docx`)  
     - Calculation sheets (`.docx`/`.xlsx`)  
     - PPT summaries (`.pptx`)  
   - Ensure these match typical PSU formats (headings, clause references, tables).  

3. **Local knowledge base must be easy to populate**  
   - Provide a simple interface to:
     - Upload SOPs, manuals, past notes  
     - Tag them by department/type  
   - Ensure retrieval is fast and relevant.  

4. **Logs and sovereignty proof must be visible**  
   - Build a “System Status” panel showing:
     - Model endpoints (all local IPs)  
     - RAG queries (local DB)  
     - Network activity (ideally zero external).  

5. **Agent loop must be robust enough for demo**  
   - Handle at least one end-to-end flow without manual intervention.  
   - Include error handling (e.g., if OCR fails, retry or report clearly).
