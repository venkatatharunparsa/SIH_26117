# UI stack adversarial research — SIH26117 KWB application

**Date:** 2026-09-19  
**Question:** Jury expects a **Knowledge Work Bench application**, not a website / Postman console. Which UI shell wins for offline SIH demo + industrial assist→export self-HITL?  
**Constraint:** FastAPI spine stays. No DeerFlow / OpenHands Canvas fork. Electron packaging = Later, not day-1.

---

## 1. Comparison matrix

| Option | Pros | Cons | Kill for SIH? |
|---|---|---|---|
| **Static HTML desk** (`desk/index.html` current) | Fastest; already wired to API; Desk UX v2 visual language landed | Reads as a **website / API console**; one giant file; weak “application” perception for industrial jury | **Soft kill** for “application” framing — keep as **legacy fallback** only |
| **Next.js App Router (local)** | Real app shell: routes, layouts, components, TypeScript; desktop-*feel* at localhost; matches user ask; easy dual-run with FastAPI | Still browser-hosted (not `.exe`) | **OK** if framed as **local workbench application** on jury laptop |
| **Vite + React SPA** | Lighter tooling; same React port | User explicitly asked **Next.js**; weaker App Router / “product app” signal | Secondary — only if Next blocked |
| **Electron + Next** | True desktop window; strongest “application” claim | Heavy; offline packaging, signing, GPU/Ollama path friction | Ambition — **Later**, not day-1 |
| **Tauri + web UI** | Light native shell; good offline-first pattern (2025–26 local AI apps) | Rust toolchain on demo box; extra CI surface | Maybe later after Next MVP |

---

## 2. External pattern scan (2025–2026)

What serious **local / offline AI workbenches** do:

| Pattern | Signal | Source class |
|---|---|---|
| Next (or React) UI + **separate local API / sidecar** | UI ≠ inference host; typed client to loopback | Cognia-style: Next static/export + Rust/Node sidecars; Forge: Next inside Tauri |
| **Desktop shell later** (Tauri/Electron) wrapping same UI | Day-1 browser localhost → wrap when packaging matters | Atlas, Pern, Forge |
| **Workbench ≠ chat dashboard** | Side rail + stage + monitors; jobs/approvals visible | Industrial Canvas (Cognite): storyboard / evidence workspace, not Open WebUI clone |
| **Explicit tool / gate approvals** | Human sees deny codes; no silent agent | Forge approval-gated tools; our H1/H2/H7/H9 |
| Offline-first UI components | Model/API status badges, fail-closed banners, queues | React offline-local-AI pattern libs (status + fallback surfaces) |

**What NOT to use for KWB:**

| Anti-pattern | Why it kills jury story |
|---|---|
| Generic purple shadcn “AI SaaS” dashboard | Looks like every AI template; not plant assist |
| Chat-only Open WebUI / AnythingLLM clone | Chat ≠ assist→export leave with Word + audit |
| Infinite agent canvas fork (OpenHands Canvas / DeerFlow) | Agent OS, not our A→J self-HITL contract |
| Multi-stat marketing hero clutter | Desk UX rules: brand + one CTA + walk |
| Claiming CERT / plant Approver in chrome | Honesty bar already forbids |

**Best UI metaphor for us:** industrial **guided walk workbench** (step rail + stage + Monitor B), closer to Cognite Industrial Canvas *narrative* (evidence + gates) than to Claude chat — but keep **Claude-like clarity** (one primary action per step), not a floating node graph day-1.

---

## 3. Verdict (binding for this pass)

| Decision | Choice |
|---|---|
| **Demo application UI** | **Next.js 15 App Router + TypeScript + Tailwind** at `apps/kwb-desk/` |
| **API** | **FastAPI** `127.0.0.1:8080` unchanged |
| **Visual language** | Port Desk UX v2: **Syne / DM Sans / IBM Plex Mono**, steel-green (`#0a5c45` / `#1e3344`) — **not** default purple AI slop |
| **Components** | Custom layout matching `DESK_IA` + existing desk — **no** stock shadcn theme; if any primitive is borrowed later, restyle hard to brand |
| **Routes** | `/` hero start · `/walk/[taskId]` guided workbench (step via state / `?step=`) |
| **Static `desk/`** | **Legacy fallback** served from FastAPI `/desk/` |
| **Electron / Tauri** | **Later** — optional wrapper after Next walk is solid |
| **Refuse** | DeerFlow/OH Canvas fork · deleting FastAPI · day-1 Electron packaging |

**Execute framing:** Next.js on localhost **is** the KWB **application** UI for SIH (operator opens app URL, not a marketing site). Packaging to `.exe` is polish, not the architecture proof.

---

## 4. Component approach (port plan)

| Surface | Implementation |
|---|---|
| Honesty bar | Sticky strip — Confidential synthetic · no CERT · export leave |
| Hero | Brand-first Knowledge Work Bench · one primary CTA · coding secondary |
| Walk shell | Step rail · stage panels · Monitor B (grant/card/denies/audit poll) |
| API client | `NEXT_PUBLIC_KWB_API=http://127.0.0.1:8080` |
| Fail-closed | G8/G9 injects + revoke — same as desk v2 |
| Leave-with | Download DRAFT + leave-pack via API URLs |

---

## 5. Run shape (demo)

```text
Terminal A:  uvicorn app.main:app --host 127.0.0.1 --port 8080
Terminal B:  cd apps/kwb-desk && npm run dev   → http://127.0.0.1:3000
```

CORS: FastAPI allows `3000` + `5173`. Static `/desk/` remains fallback if Next is down.

---

## 6. Score impact (honest)

| Axis | Note |
|---|---|
| “Application” perception | ↑ vs HTML console |
| Execute G1–G10 | Unchanged — still API + eval; UI is presentation |
| Day-1 risk | Scaffold + port only; no Electron |
| PPT | Still gated on execute ≥0.90 + signed eval |
