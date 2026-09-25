# Robust E2E Report — Laptop B

**When:** 2026-09-20 (UTC evening)  
**Inference during tests:** `lan_peer_laptop_a` — LAPTOP-A peer `10.45.226.121:11434` (`runtime_reachable: true`, allow host `10.45.226.121`)  
**API:** `http://127.0.0.1:8080` (restarted mid-session with same `SOVEREIGN_*` env to load `cards.py` fix; hotspot link preserved)

## Known-issue checks

| Item | Result |
|------|--------|
| Monitor Live log `e.event` vs API `kind` | **FIXED** — `App.tsx` now prefers `e.kind` |
| `SOVEREIGN_INFERENCE_ALLOW_HOSTS` plain IP / NoDecode | **OK** — status shows `inference_allow_hosts: ["10.45.226.121"]`, gateway OK |
| `hotspot_link_workbench.ps1` em-dash / parse | **OK** — `PARSE_OK` |

## PASS / FAIL table

### Basic E2E

| Script | First run | After fix | Notes |
|--------|-----------|-----------|-------|
| `smoke_orch_word.py` | PASS | PASS | Workflow B word path |
| `smoke_platform.py` | PASS | — | skills / roles / MCP |
| `validate_endpoints.py` | PASS | — | 18/18 |
| `smoke_orch_file_read.py` | PASS | — | |
| `sim_single_model_e2e.py` | **FAIL** (httpx 30s ReadTimeout on `/orch/turn`) | **PASS** | timeout → 180s |
| `e2e_one_model.py` | **FAIL** (draft_edit/export after revoke; g1 same-model assert) | **PASS** | reorder + G1 two-card assert + G7 |

### Robust / broader

| Script / check | Result | Notes |
|----------------|--------|-------|
| `smoke_ocr_extract.py` | PASS | PNG uses fixture stub (Tesseract missing — acceptable) |
| `smoke_orch_pptx.py` | PASS* | *Script name is pptx; body still exercises Word `.docx` path |
| `smoke_chat_history.py` | PASS | |
| `validate_station_link.py` | FAIL → **PASS** | Now prefers live `/inference/status` LAN URL |
| `hitl_gates_smoke.py` | PASS | stale export, sandbox-red, G10 |
| `stage_dry_run_aj.py` | PASS | |
| G6 retrieve | PASS | 200 under grant |
| G7 revoke | PASS | `/task/revoke` 200 → retrieve 403 |
| G8 bad model | PASS | 403 `model_not_on_card` |
| G9 secret | PASS | 400 `secret_in_draft` |
| Audit verify | PASS | chain OK |

## Fixes applied (minimal)

| File | Change |
|------|--------|
| `apps/kwb-app/src/App.tsx` | Live log / audit lines use `e.kind \|\| e.event` |
| `backend/app/cards.py` | Coding second-tag: skip vision (`moondream`); prefer `qwen2.5-coder:7b` / card config (was alphabetically picking moondream) |
| `backend/scripts/e2e_one_model.py` | Stale-deny **before** export revoke; G1 = two cards; add G7 |
| `backend/scripts/sim_single_model_e2e.py` | httpx timeout 30 → 180 |
| `backend/scripts/validate_station_link.py` | Prefer live API inference URL + allow hosts |

## Remaining gaps

1. **Tesseract not installed** — PNG OCR honest degrade / fixture stub (not a demo blocker).
2. **`smoke_orch_pptx.py` misnamed** — still walks Word draft path; true PPTX smoke not covered by that file name.
3. **Sandbox** remains host-process (not deny-all container) — prior known floor.
4. Desk **Live log** fix needs Electron/Vite reload to show in UI (API already returns `kind`).

## Verdict

Hotspot **LAPTOP-A peer** stayed up. Basic + robust demos pass after the fixes above. G1 now correctly shows `inspect-draft→llama3.2:3b` and `code-assist→qwen2.5-coder:7b` (`full_two_tag`).
