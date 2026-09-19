# UI adversarial research — Claude Code desk for KWB

**Date:** 2026-09-19  
**Problem ID:** SIH26117  
**Trigger:** User rejection of current web/marketing desk (“worst UI”; “we have KWB **application** not web application”)  
**Verdict:** Build **Electron + Vite React** desktop shell (`apps/kwb-app/`). FastAPI stays. Hero Next desk (`apps/kwb-desk/`) = **rejected / legacy**.

---

## 1. What Claude Code does well for agent desks

Sources studied (adversarial, not marketing copy):

- Anthropic Agent View docs / blog (`claude agents`, session list + peek + attach)
- Claude Code interface write-ups (conversation stream, tool transparency, status)
- Independent UX teardown: *how-claude-code-works* ch.14 (observable autonomy, Ink/React terminal)

### Patterns that transfer to KWB

| Pattern | Claude Code | KWB mapping |
|---|---|---|
| **Observable autonomy** | Tool calls stream live; user can interrupt early | Every FastAPI action = a **tool block** in the transcript (start, h1, retrieve, draft, h2, export, sandbox, monitor-a) |
| **Session stream as primary surface** | Chronological messages + tool results, not a wizard | Center column = task session stream; no multi-step marketing wizard |
| **Session list** | Agent view: rows for running / waiting / done | Left rail: tasks/sessions; new task = new stream |
| **Composer at bottom** | Input for next turn / findings | Bottom composer: findings, retrieve query, slash-ish actions |
| **Status / debug panel** | Compact status, permissions, cost, transcript mode | Right **Monitor B**: grant, card, model, artefact version, denies, audit |
| **Developer chrome** | Terminal-adjacent, dense, monospace for technical | Dark/neutral high-contrast desk — not SaaS hero |
| **Glass box tools** | Tool name + params + result inline | Collapsible tool cards with request/response JSON snippets |
| **Honesty of state** | Permission pauses; clear waiting | DRAFT badge, not CERT; export leave; no Approver role |

### What we deliberately do **not** copy

- Full Ink TUI / alternate-screen terminal (we need Word download + Monitor B density → Chromium window is fine)
- Open WebUI chat clone aesthetics
- DeerFlow / OpenHands Canvas fork
- Purple glow / marketing landing

---

## 2. Why hero-Next web failed user test

`apps/kwb-desk/` shipped as Next.js App Router with:

- Syne / steel-green **marketing fonts**
- **Hero billboard** (“Start inspection walk”)
- Multi-step **wizard** (`step-rail` + stage panels)
- Browser URL mental model (`localhost:3000`)

User feedback (strong): this reads as a **web/SaaS product**, not a **Knowledge Work Bench application**. Jury and operators expect a desk like Claude Code / Cursor: open the window → already in the workbench → stream of actions.

Failure modes:

1. **Wrong first second** — brand/CTA splash instead of session workspace  
2. **Wrong information architecture** — wizard steps hide the audit trail; Claude Code puts the trail in the center  
3. **Wrong packaging signal** — “open Chrome to :3000” ≠ desktop application  
4. **Visual language** — expressive marketing type fights dense technical work  

---

## 3. Why Electron (or Tauri) for “application”

| Option | Pros | Cons for this demo |
|---|---|---|
| **Browser Next only** | Fast iterate | Failed user test; still “web app” |
| **Electron** | Native window title, desktop chrome, offline jury box, same React skills, wraps Vite/Next easily | Heavier binary (~Chromium); packaging Later |
| **Tauri** | Smaller binary, Rust shell | Extra toolchain on jury Windows; slower SIH iterate |

**Choice: Electron** for SIH demo velocity and “double-click later” packaging path. Tauri remains a Later alternate if binary size becomes a gate.

Desktop shell responsibilities:

- Window title: **Knowledge Work Bench**
- Load UI in `BrowserWindow` (Vite renderer in dev)
- Talk to FastAPI at `127.0.0.1:8080` (CORS already allows Vite origins)
- Do **not** rewrite API; do **not** embed inference in Electron

---

## 4. Verdict + build choice

| Decision | Choice |
|---|---|
| Primary UI | **`apps/kwb-app/`** — Electron + Vite + React (desktop) |
| Layout | Left sessions · Center stream + composer · Right Monitor B |
| Aesthetic | Dark/neutral developer tool; JetBrains Mono / IBM Plex Sans — **no Syne hero** |
| Backend | **FastAPI unchanged** |
| `apps/kwb-desk/` | **Rejected / legacy** — keep for reference; do not demo as primary |
| Static `desk/` | Still legacy fallback |
| Packaging | `electron:dev` now; installers **Later** |

**Confidence:** ~0.88 design / build direction (user signal was unambiguous; Claude Code patterns map cleanly to grant/tool/audit desk).

---

## 5. Refuse list (honoured)

- More Syne hero landing pages  
- Open WebUI chat clone  
- DeerFlow / OpenHands Canvas fork  
- Ignoring FastAPI / rewriting API into Electron  
