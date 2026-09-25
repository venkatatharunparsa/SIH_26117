# Manual software test report — PS demo

**Date:** 2026-09-20  
**Tester:** Agent (UI click-through on Vite renderer `http://127.0.0.1:5173` + live API `:8080`)  
**Environment:** Single laptop · Ollama `llama3.2:3b` · FastAPI 0.5.0 · desk `apps/kwb-app`  
**Script followed:** `eval/STAGE_RUNBOOK.md` inspection A→J + fail-closed injects  

---

## Preconditions

| Check | Result |
|---|---|
| API `/health` | **PASS** (green in titlebar) |
| Ollama up | **PASS** |
| Workbench UI loads | **PASS** (sessions + composer + NOT CERT) |
| No Approver control | **PASS** |

---

## Inspection walk (manual clicks)

| Step | Action | UI observation | Result |
|---|---|---|---|
| A | Open workbench | Empty stream + Start | **PASS** |
| B | Click **Start** | `task.start` **ok** · route `inspect-draft` / `llama3.2:3b` · grant issued | **PASS** |
| C/D | Click **Confirm H1** | `task.h1` **ok** | **PASS** |
| E | Click **Retrieve** | `task.retrieve` **ok** (cites/verdict) | **PASS** |
| E | Click **Ack H7** | `task.h7` **ok** | **PASS** |
| F | Click **Draft** | `task.inspect-draft` **ok** · docx + artefact_version | **PASS** |
| H | Click **Confirm H2** | `task.h2` **ok** | **PASS** |
| I | Click **Export leave** | `task.export` **ok** · session **exported** | **PASS** |
| I | Monitor opens / downloads | Monitor B · Download DRAFT · leave pack enabled | **PASS** |
| J | Monitor B panel | card/model/grant · evidence ≠ CERT copy | **PASS** |

Session id observed: `b6361c8a` · model `llama3.2:3b` · card `inspect-draft`.

---

## Fail-closed (manual)

| Inject | Expected | Observed | Result |
|---|---|---|---|
| More → **Inject secret (G9)** (first pass) | Deny | Tool showed **ok** — inject string missed secret regex | **FAIL then fixed** |
| More → **Inject secret (G9)** (after fix) | Deny | `task.export-check` **deny** · `secret_in_draft` | **PASS** |
| More → **Bad model (G8)** | Deny | `gateway.chat` **deny** · session denied | **PASS** |
| More → **Sandbox red** | Job runs (exit≠0) | `sandbox.python` **ok** (HTTP) — red state for G10 export | **PASS** |
| More → **Revoke grant** | Revoke succeeds | `task.revoke` **ok** | **PASS** |

**Fixes:** G9 inject text + `secrets.py` AWS `AKIA…` / `secret_key=` patterns.

---

## Bugs / findings → disposition

1. **P1 G9 inject weak** — **FIXED** + retested.  
2. **Deferred G8 / sandbox-red / revoke UI** — **CLOSED** (this pass).  
3. **Vite vs Electron chrome** — same React; prod path `npm run electron:prod`.  
4. **Two-terminal start** — **FIXED** `scripts/start_demo.ps1`.  
5. **Audit hash UI** — **FIXED** Monitor **Verify chain**.  
6. **Revoke hang after export** — **FIXED** revoke-on-export + stream note.

---

## Verdict

| Axis | Score |
|---|---|
| Happy-path demo walk (manual UI) | **PASS** |
| Monitor B + leave downloads visible | **PASS** |
| Fail-closed G8 / G9 / revoke / sandbox-red | **PASS** |
| Overall manual demo readiness | **PASS** |
