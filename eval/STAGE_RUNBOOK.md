# Stage runbook — Knowledge Work Bench (one page)

**Product:** SIH26117 KWB · **Date:** 2026-09-20  
**Demo mode (LOCKED):** **Single laptop** — Ollama + one adopted chat tag + Electron workbench + FastAPI on the **same** machine.  
**Primary desk:** `apps/kwb-app` (Electron) — **do not** demo `apps/kwb-desk`.  
**Integrity:** DRAFT ≠ CERT · no in-app Approver · export leave · Monitor A ≠ CERT · Ollama = inference only (**no pull**).

**Two-laptop Model Workstation:** deferred / optional only — see `DEMO_TWO_LAPTOP_ADV_PLAN.md`. **Not required for jury demo.**

---

## 0. Start

**Preferred (one command):**

```text
pwsh -File scripts/start_demo.ps1
```

**Manual (two terminals):**

```text
# Terminal A — API
cd backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 8080
# health: http://127.0.0.1:8080/health

# Terminal B — Electron desk
cd apps/kwb-app
npm install          # first time only
npm run electron:dev
# window title: Knowledge Work Bench
```

Optional API-only evidence (no UI):  
`python backend/scripts/execute_walk.py` · `python backend/scripts/stage_dry_run_aj.py`

UI walk evidence: `eval/evidence/MANUAL_TEST_REPORT.md`

---

## 1. Inspection walk (A→J — show this)

| Step | Say / do | Prove |
|---|---|---|
| **A** Enter | Open Electron desk; session visible | Workbench open — no org chart |
| **B** Intent | Start **inspection** task | Route card + model shown (G1 floor OK) |
| **C/D** Extract + H1 | Load fixture / paste FX-EXT-01; **H1 confirm** | Extract not auto-truth |
| **E** Retrieve + H7 | Retrieve under grant; **H7 ack** cites/gaps | Cite-or-abstain; server H7 SoT |
| **F** Draft | Generate Word **DRAFT** | Banner DRAFT — not plant record |
| **H** Self-check | **H2** accept own DRAFT | Same-user HITL — no Approver button |
| **I** Leave | **Export leave** → download DRAFT / leave-pack | Soft copy off box; paper outside |
| **J** Monitor A | Start before walk / stop after | Evidence pack sha256 — **say “not CERT”** |

Skip coding branch unless time; if used: sandbox → **H9** → include sandbox proof in leave pack.

---

## 2. One fail-closed (must show)

Pick **one** live:

| Inject | Expected |
|---|---|
| Secret text → export-check | Deny (`secret_in_draft`) |
| Bad model `gpt-4o` → gateway | Deny (`gateway_deny`) |
| Revoke grant → retrieve/tool | Deny (403 / `grant_revoked`) |
| Sandbox-red then export | Deny (`sandbox_red`) — G10 |

Monitor B should show the deny in `/audit/recent` if desk poll is live.

---

## 3. Say out loud (jury honesty)

- “DRAFT soft copy — **not** certified plant record.”
- “Monitor A is an **evidence pack**, not CERT-In / WAN=0 theatre.”
- “Approver is **paper outside** — not in this app.”
- “G1 today is **floor**: two task cards, one local Ollama tag — no registry pull.”

---

## 4. If something fails

| Symptom | Action |
|---|---|
| API down | Restart uvicorn; check `:8080/health` |
| Electron blank | `npm run electron:dev` from `apps/kwb-app`; API must be up |
| H7 blocks draft | Ack cites on server first (`POST /task/h7-ack`) |
| Export blocked after edit | Re-H2 after stale (`artefact_version`) |
| Ollama missing | Inference optional for fixture walk; do not `ollama pull` mid-demo |

**Eval pack:** `eval/evidence/` · checklist: `eval/CHECKLIST.md` (`demo_ready: true`, G1 floor).

---

## 5. Two-laptop (OPTIONAL — not the demo path)

**Locked demo = single laptop.** Skip this section unless you later split GPU vs desk.

If needed later: `solution/prototype/DEMO_TWO_LAPTOP_ADV_PLAN.md` · `config/model_station.card.example.yaml` · `python backend/scripts/validate_station_link.py`.
