# Slide 4 — Feasibility and Viability

**Official pointers:**  
• Analysis of feasibility  
• Potential challenges and risks  
• Strategies for overcoming these challenges  

**Narrative job:** Prove 36h honesty + mid-GPU realism + risk table.

---

## 1. On-slide paste

### Feasibility (3 facts)

1. **PS allows** smaller open-weight models when 120B-class hardware is absent.  
2. **Demo spine is built:** task routing, human checkpoints, Word DRAFT, sandbox, Monitor A, fail-closed denies (demo proof checklist).  
3. **Viability:** OSS + existing GPU; scale = more GPUs / cards behind the **same** `/v1` socket — not a rewrite.

### REAL / MOCK / LATER (36h honesty)

| Capability | REAL (demo) | MOCK | LATER |
|---|---|---|---|
| Confirm extract → Word DRAFT | ● | | |
| ≥2 task types (model cards) | ● (one model tag OK) | | Dual-load VRAM |
| Sandbox calc/code + accept result | ● | | |
| Monitor A evidence pack | ● (≠ CERT) | | Continuous A |
| Authz retrieve + citations | ● local packs | | Live EAM/DMS APIs |
| MCP host | | stub OFF | Full host |
| Excel / PPT artefacts | | | ● |
| Live plant OCR / VLM | fixture path | | ● engine |
| SSO / SIEM / USB quarantine | | | ● |
| Write DCS / SIS / EAM | **Never** | | **Never** |

### Challenges · Risk · Mitigation

| Challenge | Risk | Mitigation |
|---|---|---|
| Mid-GPU VRAM | Dual-model theatre | Sequential load; one adopted tag OK |
| LLM invents mm / rates | Bad engineering number | Schema + human checks; **math in sandbox** |
| Bad / partial scan | Invented readings | Confidence; cite-or-abstain; fail closed |
| Venue Windows jail | Missing sandbox | Process jail and/or container `--network=none` |
| “Air-gap” that pulls weights | WAN on first run | Pre-stage tags (**no pull**); unplug |
| Trust in DRAFT | Shadow “approval” | DRAFT badge; human ultimate verifier |
| Scope creep vs SIH | Org forever, no demo | **Demo proof spine first**; rest Later |

---

## 2. Full inventory

### 2.1 Why this is buildable now

- Working Electron desk + FastAPI on loopback.  
- Single-laptop demo locked; start script available.  
- Eval evidence signed (agent) + manual UI walk recorded.  
- Public/synthetic fixtures — no plant secrets required for demo.

### 2.2 Cost / resource (honest, optional Q&A)

| Resource | Notes |
|---|---|
| Software | OSS stack; no cloud LLM bill |
| Hardware | Mid-range GPU class per PS; laptop demo OK |
| People | Engineer operator + IT for runtime |
| Time to DRAFT | Estimate on slide 5 — not SLA |

### 2.3 Sustainability / future work (one line)

Add Model Cards and read-only connectors without redesigning grants/gateway; keep Never-write plant SoR.

### 2.4 Do not put

- “100% feasible with zero risk”  
- Fake 36h hour-by-hour Gantt on idea PDF (finale pitch only if asked)  

---

## 3. Speaker notes (~0:50)

“Feasibility: the problem statement itself allows smaller models on mid-range GPUs. We already run the spine — routing, human checkpoints, Word DRAFT, sandbox, evidence pack. Risks we name: VRAM, hallucination of numbers, bad scans, weight pulls. Mitigations: one model at a time, sandbox math, cite-or-abstain, no-pull policy, DRAFT badge. Excel, SSO, live OCR stay Later — never plant writes.”

---

## 4. Adversarial check

| Risk | Fix |
|---|---|
| Overclaiming REAL OCR | Fixture path REAL; engine Later |
| Claiming CERT | ≠ CERT on Monitor A row |
| Hiding Held items | REAL/MOCK/LATER table visible |
