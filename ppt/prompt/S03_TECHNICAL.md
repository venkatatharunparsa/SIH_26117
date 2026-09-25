# Slide 3 — Technical Approach — image generation prompt (960×420)

**Status: LOCKED / FIXED 2026-09-21** — do not change unless user reopens.  
**Mem0:** Slide 3 Technical Approach locked.  
**SoT:** this file · `../D02_COMPONENT_DIAGRAM.md`

Copy everything below the line into the image model.

---

```
Create one flat presentation content panel. Exact size: 960 × 420 pixels. White #FFFFFF. No 3D, no neon, no purple, no robots, no SIH chrome, no watermarks. No logo salad.

This is SIH Slide 3 — Technical Approach for Knowledge Work Bench (KWB).
Do NOT copy Slide 2 organisation story (People / Workbench / Inference / Safety lanes). This slide must look TECHNICAL: components, gateway path, workflow steps.

VERTICAL LAYOUT:
- Row 1 (~115 px): LEFT Technologies table · RIGHT Hard controls (NOT “system planes”)
- Row 2 (~175 px): Technical architecture diagram — detailed component flow (main visual)
- Row 3 (~130 px): Workflow diagram — assist→export + coding branch (NOT a vague “methodology” strip)

════════════════════════════════
ROW 1 LEFT — title ONE LINE: Technologies to be used
Table: Layer | Tech | Purpose — exactly 6 rows:
Desk | Electron + Vite + React (kwb-app) | Operator UI: sessions, files, checkpoints
Workbench API | Python FastAPI /orch/turn | Grants, orchestrator, retrieve, audit, Word draft
Skills + tools | On-disk SKILL.md + local tools | Step proposals; file R/W; cite-or-abstain
Gateway | OpenAI-shape proxy → local /v1 only | Card + grant check; ONLY path to models
Runtime | Ollama /v1 (demo) · vLLM (org) | Open-weight serve on GPU; sequential load OK
Sandbox + files | Process jail + python-docx | Verify calc/code ≠ GPU; DRAFT Word leave pack

ROW 1 RIGHT — title ONE LINE: Hard controls (fail-closed)
Replace any “System planes” block with this checklist card (5 lines):
• Desk never calls model URL directly — only Gateway
• Packed prompts only after grant + Model Card allow
• Public / unregistered model IDs → DENY
• Sandbox verifies calc/code — never wraps GPU runtime
• Monitor A = egress evidence pack ≠ CERT · never write DCS/EAM/ERP
Footer: Excel/PPT = later · Word DRAFT = must-work deliverable

════════════════════════════════
ROW 2 — title ONE LINE: Technical architecture
Draw a DETAILED technical component diagram (swimlanes). This must NOT look like Slide 2’s four org boxes.

LANE DESK (top thin):
Task desk (Electron) · Task monitor · Admin console

LANE WORKBENCH (main — show internal boxes + arrows):
Session ≠ Grant → Task type / Model Card router → Orchestrator
From Orchestrator branches:
→ Ingest / upload → Confirm extract
→ Authz retrieve → Cite-or-abstain → Review citations → Context packer
→ Word DRAFT → Secrets check → Self-check DRAFT → Export leave → Store
→ Skills / specialists / MCP allowlist
→ Sandbox control API
→ Audit (fail-closed) · Monitor A evidence pack ≠ CERT

LANE GATEWAY (must be visually central choke-point):
ONLY model path ← Context packer
Gateway checks: card · schema · grant · loopback
label on arrow into Gateway: packed prompts ONLY
Gateway → local /v1 · fail-closed if down · no cloud fallback

LANE RUNTIME:
Offline stage (quarantine · SHA · Admin ack) → Model Cards enable → Runtime /v1 (GPU weights)

LANE SANDBOX (separate from Runtime):
Calc / code workers · network deny · ≠ GPU · Accept sandbox result

Boundary notes (small):
Plant systems ←‥ read-only connectors ‥ Workbench
Public internet: BLOCKED (red) from Workbench · Gateway · Runtime

════════════════════════════════
ROW 3 — title ONE LINE: Workflow diagram
Draw a proper WORKFLOW (two spines), not a methodology paragraph:

SPINE A — Inspection leave (primary):
Attach scan/note → Confirm extract → Retrieve SOP → Review cite / NOT FOUND → Pack → Gateway → Runtime → Word DRAFT → Secrets check → Self-check DRAFT → Export leave → Store

SPINE B — Coding / calc:
Coding task → Card auto-route → Sandbox run + verify → Accept sandbox result → (may block Export leave if fail)

Callout under workflows EXACT:
Mid-GPU loads one model at a time · ≥2 task types when two cards staged · Export leave ends the path · Approver outside app

Style: #E8EEF5 fills, #1F497D borders/titles, #0070C0 arrows, #C0504D BLOCKED. Dense readable labels. No INSERT. No size callouts in the image.
```
