# Industrial Workbench — Gap Analysis & Design Reality Check

**Date:** 2026-09-21  
**Sources:** PS SIH26117 (MRPL), Mem0 product definition, `sih_research/`, `solution/prototype/*`, web patterns (PlantPulse, ArgusAI, ADORE/AgentDoc-style plan→HITL→evidence), current `kwb-app` + FastAPI.  
**Honesty rule:** Private LAN / hotspot ≠ air-gap. Fixed HITL spine ≠ free Cursor planner. Word DRAFT ≠ plant record.

---

## 1. What the problem statement actually asks

Industries named in background: **refineries, PSUs, defence-linked manufacturing, government offices**.

Core loop judges can redraw: **scan → extract → cite from local SOP → HITL → Word approval note DRAFT → soft export**, plus **coding in sandbox**, **≥2 model routes**, **visible no-public-LLM posture**.

Not asked: in-app Approver, DCS/SIS write, CERT stamp, ChatGPT clone, generic “agent OS”.

---

## 2. What we designed (docs) vs what exists

| Industrial capability | Designed | Built | Jury-visible? |
|---|---|---|---|
| Inspection → Word DRAFT | Yes | Yes | Yes if demoed |
| Self-HITL H1/H7/H2/H9 | Yes | Yes | Partial (asks in stream) |
| Task→card model auto-select | Yes | Yes (when 2 tags on station) | Chrome model pill |
| Cite-or-abstain / local KB | Yes | Yes | Weak unless Monitor open |
| Sandbox calc + deny-red | Yes | Yes | More menu / coding mode |
| Monitor / audit theatre | Yes | Yes | Must open Monitor |
| Files + folder workspace | Org desk design | **Now** | Files rail |
| Visible **agent plan** | Implied by “plan multi-step” | **Now (fixed spine UI)** | Agent plan strip |
| Free LLM planner / replan | PS wording | **No** (honest fixed phases) | Labelled as fixed spine |
| Excel first-class | PS tools list | **No** | Don’t claim |
| Entity resolution (P-204A) | Batch research | **No** | Later |
| True air-gap NIC proof | Expected Solution | **No** (LAN peer / loopback) | Say aloud |
| Plant connectors EAM/DMS | Org EXT | Mock only | Don’t claim live |

---

## 3. Why it can feel “not agentic”

Backend **is** multi-step: attach → confirm extract → retrieve → confirm cites → Word → self-check → export. That **is** agentic industrial workflow.

What was missing for *feel*:
1. No visible plan (Cursor-like todo / AgentDoc plan review).
2. No collapsible file tree → desk felt like chat only.
3. Phase chips only inside tool blocks — easy to miss.
4. No free tool-chooser loop — by design (policy spine), but must be **named** so jury doesn’t think we failed.

**Fix direction (done / next):** show **Agent plan** mapped to `orchPhase`; expand/collapse files; keep honesty caption “fixed industrial HITL spine”.

---

## 4. Industrial (not Cursor-clone) feature bets

From web + Mem0 + PS — **keep / add / never**:

### Keep (differentiates vs Claude Code / Cursor)
- Evidence → **cite or abstain** → Word **DRAFT** watermark / leave pack  
- Grant + revoke fail-closed tools  
- Card registry deny `gpt-4o`  
- Monitor posture: private LAN · not CERT  
- Inspection / coding **task cards**, not “pick Claude-3.5”

### Add next (high jury ROI, still industrial)
1. **Plan Review** pause: show next 3 steps before first tool (HITL on plan)  
2. **Evidence panel**: extract bullets + cite chips beside chat (not only Monitor)  
3. **Contradiction / NOT FOUND** surface when SOP missing  
4. **Tag-aware retrieve** (V-101) — light entity hint  
5. **Parallel sessions** already exist — demo multitasking explicitly  
6. Optional **Excel thickness table** as *secondary* artefact (not Word substitute)

### Never
- Write to DCS/EAM/ERP  
- In-app Approver hierarchy  
- Claim CERT / air-gap without NIC evidence  
- Replace Word Expected Solution with PPT-only theatre  

---

## 5. Effective workbench workflows (industry-shaped)

### WF-A — Integrity inspection note (demo Must)
Operator opens `fixtures/scans` → attach field PDF/image → Confirm extract → Confirm cites → Word DRAFT → H2 → leave pack. Approver is **outside**.

### WF-B — Coding assist (demo Must)
Agent mode coding → route `qwen2.5-coder` when staged → sandbox calc → H9 observe.

### WF-C — Board / gov note (same spine, different template)
Same HITL; swap template/SOP family later — **architecture already supports** via skills/roles.

### WF-D — Defence / PSU correspondence (boundary story)
Same gateway deny + audit; classify content in leave pack metadata — not built UI.

---

## 6. Testing bar (raised)

| Suite | Purpose |
|---|---|
| `outsider_complex_e2e.py` | Noisy PNG + multipage PDF |
| `outsider_multitask_e2e.py` | Field PDF+image inspection **and** coding grant in parallel |
| `redteam_adversarial.py` | Fail-closed |
| Manual | Files tree collapse, Agent plan advances, Attach → ask |

---

## 7. Verdict

We **did** design for industrial workflows. The gap is not “we only built a chatbot” — it is **surfacing the industrial agent spine** and **not overclaiming** Cursor parity or air-gap. Next demos should narrate: *“This is a governed inspection agent, not a coding IDE clone.”*
