# Demo eval / G1–G10 checklist

**Status:** **SIGNED** (prototype agent smoke + API evidence) — 2026-09-20  
Label fixtures: **Confidential synthetic**. Monitor A ≠ CERT.  
**G1 honesty (GATE_90 A3 / WP-18 rev 1.1):** floor = single-tag adopt OK; full = ≥2 distinct `model_id`s only when staged offline — **never pull**.

| G# | Check | How | Result | Evidence |
|---|---|---|---|---|
| G1 | ≥2 task→card→model routes logged | `/task/start` inspection + coding → audit `router_select` | **PASS (floor)** — 2 task types, 2 `card_id`s (`inspect-draft`, `code-assist`), same `model_id` `llama3.2:3b` | `eval/evidence/G1_routing.json` |
| G2 | Word DRAFT + self-HITL H1/H2 | `/task/inspect-draft` → docx + same-user gates | **PASS** — DRAFT artefact; no in-app Approver | `eval/evidence/G2_draft.json` |
| G3 | Sandbox coding/calc + H9 | `/sandbox/calc` + H9 ack | **PASS** | `eval/evidence/G3_sandbox_h9.json` |
| G4 | OCR/extract path | fixture FX-EXT-01 + H1 confirm | **PASS** | `eval/evidence/G4_h1.json` |
| G5 | Monitor A start/stop artefact | `/monitor-a/start` then `/stop` → JSON sha256 | **PASS** — evidence pack, **not CERT** | `eval/evidence/G5_monitor_a.json` |
| G6 | Cite-or-abstain | `/task/retrieve` under grant | **PASS** — cites returned under grant (no fake invent) | `eval/evidence/G6_retrieve.json` |
| G7 | Revoke grant blocks tools | revoke then retrieve → deny | **PASS** — HTTP 403 | `eval/evidence/G7_revoke.json` |
| G8 | Deny public / unregistered model | gateway `gpt-4o` → deny | **PASS** — `gateway_deny` | `eval/evidence/G8_deny.json` |
| G9 | Secret in draft blocks export leave | `/task/export-check` with `api_key=…` | **PASS** — deny | `eval/evidence/G9_secret_deny.json` |
| G10 | Sandbox-red / H9 blocks export leave | coding walk + export | **PASS** — `sandbox_red` deny | `eval/evidence/G10_sandbox_red_deny.json` |

**Additional smoke (same day):**
- `backend/scripts/execute_walk.py` → all G1–G10 **PASS** (`SUMMARY.json`)
- `backend/scripts/stage_dry_run_aj.py` → inspection A→J + fail-closed G9/G7 **PASS** (`STAGE_DRY_RUN_AJ.json`)
- `backend/scripts/hitl_gates_smoke.py` → stale export deny + G10 **PASS**
- `backend/scripts/test_m1_m3_leavepack.py` / `test_m4_m7_desk_maturity.py` → **PASS**

Mandatory stage walks: **inspection + one fail-closed** — **DONE** (API). Coding covered in G3/G10.

| Field | Value |
|---|---|
| **Signer** | Prototype agent smoke (SIH26 M8–M10 pass) — DM human co-sign optional |
| **Date** | 2026-09-20 |
| **G1 mode used** | ☑ floor (single-tag adopt) ☐ full (≥2 model_ids) |
| **demo_ready** | ☑ **true** ☐ false |
| **Integrity notes** | DRAFT ≠ CERT · no in-app Approver · export leave · Ollama inference-only / no pull · Monitor A ≠ CERT |
| **Primary desk** | `apps/kwb-app` Electron — **not** `apps/kwb-desk` |
| **Blockers for PPT** | None for execute gate; PPT still **NO-GO** until team starts slide work separately (execute claimed ≥0.90 below) |

**Honest residual (does not falsify demo_ready):**
1. G1 is **floor** (one local chat tag) — do not claim multi-model tags without offline staging.
2. Electron/Vite UI operator walk **recorded** — `eval/evidence/MANUAL_TEST_REPORT.md` (A→J + G9 deny after inject fix).
