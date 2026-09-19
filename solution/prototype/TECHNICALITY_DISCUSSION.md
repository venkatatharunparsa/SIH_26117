# KWB — Technicality discussion (phase 2)

**Date:** 2026-09-19  
**Status:** **IN DISCUSSION** — T1–T3 locked · T4 **accepted baseline** · org red-team done · demo narrow later  
**Depends on:** `APPLICATION_FLOW_COMMON.md` (**LOCKED** A→J) · `TECH_STACK_VERIFY.md` · `TECH_STACK_ORG_REDTEAM.md`  
**Rule:** Flow wins. Tech serves A→J. Org spine first; demo slice later. No PPT until DM opens that phase.

---

## Locked this session (DM)

| ID | Decision |
|---|---|
| **T1** | **One task desk** — intent + files + DRAFT + HITL + audit on one workspace; **Claude-like visual quality** (artifact-first desk, not chat-as-product) |
| **T2** | Module map **accepted** (A→J → session … audit) |
| **T3** | **No in-app hierarchy / no in-app approval chain.** Company paper approval **outside** only. HITL = **same user self-gates**. WP-05 must be reopened to match (when we edit freezes). |
| **T4** | Do **not** accept stack on assumption — **adversarial research** below; DM chooses |

---

## T1 visual shape (locked intent — layout contract)

Steal **Claude desk patterns**, not Claude cloud product:

| Claude pattern (research) | How we use it in KWB | Refuse |
|---|---|---|
| Chat left / **artifact canvas right** | Intent + progress left; **Word DRAFT / extract / sandbox report** as primary canvas | Chat transcript as the deliverable |
| Artifact versioning + download | DRAFT versions + export pack (docx + audit ± sandbox) | Publish-to-web / share links |
| Pane: files, evidence, terminal-like proof | Attachments · citations · sandbox log · audit strip | Browser-use / cloud connectors |
| Clean typography, calm density | Professional industrial desk | Purple-glow chatbot skins / Open WebUI clone |

**Product rule:** Canvas title is always the **artefact** (DRAFT note / code report), never “conversation.”

---

## T2 module map (accepted)

| Flow | Module | Demo tag |
|---|---|---|
| A | `session` | MOCK |
| B | `intent` + `task_type` | REAL |
| C | `uploads` + `templates` | REAL |
| D | `extract` + H1 self-UI | REAL (light OK) |
| E | `grants` + retrieve MOCK + `knowledge_verifier` REAL | E skip if no KB |
| F | orch + cards + gateway + `docx_draft` | REAL |
| G | `sandbox` + H9 self-UI | REAL |
| H | H2 self accept/edit/reject | REAL |
| I | H3 self-export + evidence pack | REAL |
| J | audit + Monitor A/B | REAL |

---

## T3 company vs app (locked)

```text
INSIDE KWB:  assist → self-HITL → DRAFT + evidence
OUTSIDE:     paper / officer / company filing  (not our app)
```

No Approver queue, no boss role in UI, no task handoff between workers in-app.

---

## T4 — Adversarial research + red-team (see full file)

**Full attack write-up:** `TECH_STACK_REDTEAM.md`

### Proposed BEST set (survives red-team for must-work)

| Layer | BEST |
|---|---|
| API | FastAPI (127.0.0.1) |
| UI | React + Vite · Claude-like artifact desk |
| Word | docxtpl + python-docx |
| Audit | JSONL + SHA-256 hash chain |
| Grants/session | SQLite |
| OCR | Tesseract + fixture fallback |
| Retrieve | Grant → lexical k≤5 |
| Verifier | Rule cite-or-abstain |
| Orch | Thin custom loop |
| Sandbox | Process jail must-work (+ optional Docker network=none) |
| Runtime | Deferred (Ollama \| llama.cpp when hardware) |

**DM: Lock BEST set / change row / more attack on row.**
