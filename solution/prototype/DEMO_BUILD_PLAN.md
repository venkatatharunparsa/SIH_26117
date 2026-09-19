# Knowledge Work Bench — demo build plan

**Status:** Active — **D1–D6 ACCEPTED**; **add REAL in progress**  
**Overlay:** `PROTOTYPE_OVERLAY.md`  
**Diagrams:** `DEMO_ARCHITECTURE_DIAGRAMS.md`  
**Freezes:** `../freezes/`  
**Code root:** `../../backend/`  

## Week-zero spine (do in order)

| # | Module | Status |
|---|---|---|
| 1 | FastAPI app entry + health | **REAL** |
| 2 | Grant engine (create / revoke / ceiling) | **REAL** (`grants.py`) |
| 3 | Model Cards YAML + gateway client (local `/v1` only) | **REAL** (`cards.py` + `gateway.py`) |
| 4 | Task router → log `model_id` (G1) | **REAL** (`/task/start`) |
| 5 | Inspect path → python-docx DRAFT (G2) | **REAL** (`word_draft.py`) |
| 6 | Sandbox runner (G3) | **REAL** (`sandbox.py` + grant check) |
| 7 | Monitor A snapshot helper (G5) | **REAL** (`monitor_a.py`) |
| 8 | `eval/` checklist template | **REAL** (`eval/CHECKLIST.md`) |
| 9 | Retrieve cite-or-abstain (G6) | **REAL** light (`retrieve.py`) |
| 10 | Secrets export gate (G9) | **REAL** (`secrets.py`) |
| 11 | REAL red-team fixes | **DONE** — see `REAL_REDTEAM.md` (v0.3.0) |

## Still to thicken

- Desk UI · H1 extract/OCR · full docx secret scan · confirm Ollama model tags with DM  

## Never in code

- Public `base_url` / HF download in UI  
- Write outside KWB store into plant SoR  
- In-app accept-for-forward  
- Waive G-goldens  
- `ollama pull` / any registry download from workbench or demo box  
- Adopting model tags that are not already in the local Ollama store  

## Commands (when scaffold ready)

```text
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8080
```
