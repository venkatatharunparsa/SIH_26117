# Slide 6 — Research and References

**Official pointer:** Research and References  
**Narrative job:** Show we studied standards, papers, ecosystem, and **named** alternatives.  
**Include:** competitor matrix with ticks **only where true**.

---

## 1. On-slide paste

### Government / org / PS

- SIH26117 Expected Solution — portal (local mid-GPU; ≥2 task types; Word path; sandbox; multimodal; egress proof)  
- MRPL profile — 15.0 MMTPA — https://www.mrpl.co.in/Content/Profile  
- OISD-STD-128 (name) — https://www.oisd.gov.in/en-in/oisd-standards-list  
- DPDP Act, 2023 (context — **not** “we are certified”)  
- CERT-In Directions 20(3)/2022 — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf  
- IndiaAI Mission — ₹10,371.92 crore · 10,000+ GPUs — PIB PRID **2012355** (07 Mar 2024)  
- NIST AI 600-1 (Jul 2024) — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf  

### Papers (ideas we use; we did not re-run)

- ReAct — arXiv:2210.03629  
- RAG — arXiv:2005.11401  
- DocLayNet (layout research) — arXiv:2206.01062 — **not** our OCR %  
- Luccioni et al. inference energy — arXiv:2311.16863 — **no fake kg saved**  

### OSS composed (patterns / libraries — not “we forked the product”)

llama.cpp · vLLM · Ollama · Tesseract/PaddleOCR (path) · python-docx · Agent Skills spec · MCP (local stub)

### Ecosystem (not our revenue)

IndiaAI compute pillar + crowded local inference tools → **gap = air-gapped industrial artefacts with human checkpoints and Word**.

### Competitor matrix (ticks only where true)

| | Air-gap proof | Task auto-select | Sandbox verify | Human check before Word | Word from fields | Calc/code in jail |
|---|---|---|---|---|---|---|
| **Knowledge Work Bench** | Y | Y | Y | Y | Y | Y |
| Cloud assistants | N | cloud | N | weak | cloud | N |
| Local inference UI + Ollama | local possible | weak | N | weak | weak | N |
| PrivateGPT / AnythingLLM-class | often local | N | N | weak | RAG/UI | N |
| Continue / OpenHands-class | local possible | coding | IDE/dev jail | N | N | partial |

**Difference line:**  
*Local inference UIs and coding agents help developers; KWB delivers **PSU inspection artefacts + citations + sovereign evidence** on the same mid-range GPU class the PS describes.*

---

## 2. Full inventory

### 2.1 Extra refs (speaker / appendix — not all on slide)

- Cisco Privacy Benchmark 2024 (48% paste) — cite on slide 5 primarily  
- agentskills.io specification  
- Model Card practice (org ML governance literature)  

### 2.2 Screening criteria reminder (tiny)

Novelty · complexity · clarity in prescribed format · feasibility · practicability · sustainability · scale of impact · UX · future work — **Official, no invented %**.

### 2.3 Research honesty line

We studied vendor extracts under `KWB/`; product code is team-built FastAPI + Electron desk. We do **not** claim to have shipped upstream clones.

---

## 3. Speaker notes (~0:30)

“We ground the design in the Expected Solution, MRPL-scale context, CERT-In logging direction as *shape*, and IndiaAI as ecosystem — not our budget. Versus cloud assistants we stay on-prem; versus a bare local model UI we add router, human checkpoints, Word, and evidence; versus coding agents we centre inspection deliverables.”

---

## 4. Adversarial check

| Risk | Fix |
|---|---|
| Every competitor cell green | Only true ticks |
| Claiming we own IndiaAI | Complement wording |
| CERT badge via link dump | Links ≠ certification |
| Too many URLs | Prefer tiny URLs / names; detail in Q&A |
