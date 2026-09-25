# SIH26 Session Handoff (Mem0 mirror)

**Mem0 user_id:** `cursor-local`  
**Search first in new chat:** `SIH26 SESSION BOOTSTRAP` · also `SIH26 BUILD AUDIT BOARD`

## Role
Assistant = Principal Solutions Architect + Principal Harness Engineer + Principal Research Engineer.  
User = decision maker. **Never lie. Use Mem0 for decisions / done / next / drift.**

## Project
SIH26117 — Sovereign On-Premise Agentic AI Workbench (MRPL).  
Workspace: `C:\Users\THARUN PARSA\Documents\SIH26`

## Phase (updated 2026-09-20)
Build + eval + desk are **in progress / largely execute-ready** (GATE_90 claim execute ~0.90).  
This handoff previously said “no build” — **that line is obsolete**. Prefer Mem0 `BUILD AUDIT BOARD` over stale paragraphs.

## Binding MVP (Expected Solution — official PS)
1. Mid-GPU / small models OK  
2. Multi-model auto-select ≥2 tasks  
3. Inspection scan → **Word** approval note (agentic)  
4. Sandbox coding verified  
5. Multimodal OCR/vision  
6. Visible zero-egress proof  

## Honest status vs contract (2026-09-20)

| Contract item | Status | Honesty note |
|---|---|---|
| ≥2 task auto-select | **Partial / floor** | Live demo often **one** adopted tag `llama3.2:3b` (G1 honesty) |
| Scan → **Word** note | **Drift risk** | Working path drafts **PPTX**; Word path may still exist — do not claim PS Word if desk shows PPTX only |
| Sandbox coding | **Present** | Eval / HITL gates; rehearse live |
| Multimodal OCR | **Partial** | Framework (pypdf + Tesseract); **Tesseract not installed** → PNG fixture stub; **OCR model = org later** |
| Zero-egress monitor | **Present** | Monitor A ≠ CERT — label correctly |
| Orch spine | **Real** | `/orch/turn` · Pack → Gateway · 10-msg context |
| Primary UI | **kwb-app Electron** | `kwb-desk` = legacy refuse |

## Demo topology (hardware FACT)
- Runtime: RTX **4060 8 GB** (Laptop A)  
- Workbench: RTX **3050 6 GB** (Laptop B, UI; GPU unused for LLM)  
- Sequential 7B-class only; both Windows; Docker `--network=none` for **code** only.

## Multimodal / OCR (DM 2026-09-20 evening)
- **Target for demo claim:** multimodal/vision **model** via Gateway (same `/v1` contract)  
- **Interim still wired:** pypdf + Tesseract framework / stub — do not claim vision model until a local multimodal tag is adopted and routed  
- **Org:** may still keep framework as fallback under vision/OCR-model path

## Mem0 discipline (user 2026-09-20)
Long-context: decisions · working patterns · audit of done · remaining · next · outputs · logs · summaries.  
Update after every meaningful block of work. Discuss drift vs PS before claiming PPT/demo lines.

## DM locked 2026-09-20 evening
1. **Word** = inspection Expected Solution deliverable (PPTX secondary/org-ext)  
2. **Multimodal/vision model** for scan/image understanding (via Gateway, not side-door)  
3. **Second local language model** for real ≥2-task auto-select  

## Model call design (invariant — do not break)
**Not** Workbench → LLM direct.  
**Yes:** Desk → Orch → Pack → **Gateway** (grant · card · schema · loopback) → local `/v1` only (Ollama demo / vLLM org). Fail-closed if `/v1` down. No cloud fallback.

## Simulation phases
- **P0 DONE 2026-09-20:** single-model sim PASS → `eval/evidence/SINGLE_MODEL_SIM.json` · `backend/scripts/sim_single_model_e2e.py`
- **P1 next:** offline-stage 2nd chat model (no venue pull)
- **P2–P3:** two-laptop via reverse proxy — `solution/prototype/TWO_LAPTOP_REVERSE_PROXY_SIM.md` (A=Ollama server, B=workbench+proxy to 127.0.0.1:11434)

## Key docs
- `sih_research/sovereign-ai-workbench-kb/01-problem-context/01-problem-statement.md`
- `solution/prototype/GATE_90_DISCUSS.md`
- `solution/prototype/ORG_ARCHITECTURE_DIAGRAMS.md`
- `eval/STAGE_RUNBOOK.md` · `eval/CHECKLIST.md`
- `apps/kwb-app/` · `backend/app/orchestrator.py`
