# E2E one-model results — 2026-09-20

**Mode:** Single laptop · one chat model `llama3.2:3b` · G1 floor  
**API:** `127.0.0.1:8080` · **Ollama:** `127.0.0.1:11434`

| Suite | Result | Evidence |
|---|---|---|
| Station / model preflight | **PASS** | local tags include `llama3.2:3b` |
| Endpoint matrix | **PASS 18/18** | `eval/evidence/ENDPOINT_VALIDATE.json` |
| E2E inspection + fail-closed + coding | **PASS** | `eval/evidence/E2E_ONE_MODEL.json` |
| G1–G10 execute walk | **PASS** | `eval/evidence/SUMMARY.json` |
| HITL stale + G10 | **PASS** | console OK |
| Stage A→J + G9/G7 | **PASS** | `eval/evidence/STAGE_DRY_RUN_AJ.json` |

### E2E path covered
Start (inspection) → H1 → retrieve → H7 → DRAFT → H2 → export leave → downloads → draft-edit → stale export **deny** → G8 **403** → G9 **400** → start coding (same model, other card) → sandbox → H9 → Monitor A start/stop.

### Not covered by this API suite
Human click-through of Electron UI (operator should still run `eval/STAGE_RUNBOOK.md` once in the window).

**Verdict:** Backend end-to-end with one model is **READY**.
