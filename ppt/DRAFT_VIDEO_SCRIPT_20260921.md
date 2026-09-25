# DRAFT — Demo / video script (for your review)

**Status:** DRAFT only — for a **screen-recorded demo video** or live jury walk.  
**After** you finish manual testing of required workflows, ask for cuts/timing edits.  
**Date:** 2026-09-21  
**Length target:** ~4–6 minutes talk track · optional 8–10 min with dual-laptop setup shown  

**Companion:** `DRAFT_PPT_PACK_20260921.md` · `E2E_FULL_SIMULATION_GUIDE.md` · `SPEAKER_SCRIPT.md` (older 5-min idea-PDF voice)

---

## 0. Recording setup (before “Action”)

### Preferred story A — Single laptop (jury-safe)
1. API + Ollama + Electron already up (`scripts/start_demo.ps1` or manual).  
2. Monitor open · Status shows runtime reachable.  
3. Fixtures ready: `data/fixtures/README_attach_demo.md`, `scan_vessel_V101.png`.  

### Preferred story B — Two-laptop (shows LAN peer GPU)
1. Follow `E2E_FULL_SIMULATION_GUIDE.md` §1–2.  
2. Titlebar / Monitor: **LAPTOP-A peer** (not LOCAL).  
3. Optional: A’s `ollama serve` window visible for 3 seconds when model loads.  

**On-camera honesty bumper (5 sec, optional lower-third):**  
`Private LAN / on-prem Gateway · Monitor A ≠ CERT · DRAFT ≠ plant record`

---

## 1. Shot list + spoken lines

### Shot 0 — Cold open (0:00–0:25)
**Show:** Title card or desk empty state.  
**Say:**  
“Confidential industrial knowledge work — inspection notes, drawings, calculations — cannot go to cloud assistants. Today people either assemble packs by hand or paste into public tools. **Knowledge Work Bench** keeps that work on premises.”

---

### Shot 1 — Sovereign path (0:25–0:55)
**Show:** Monitor → Status / Share (host, tags, NOT CERT).  
**Say:**  
“Inference goes only through our Gateway to open-weight models. Public model ids are denied. What you see here is a **Monitor evidence pack and live status** — it is **not** a CERT-In certificate. Our demo posture is **on-prem / private LAN** — stronger NIC-off air-gap rehearsal is optional for venue.”

**If two-laptop:** point at `LAPTOP-A peer` and tags `llama3.2:3b`, `qwen2.5-coder:7b`, `moondream`.

---

### Shot 2 — Dual-model auto-select · WF1 (0:55–1:35)
**Show:** New **inspection** session → send short message → Status card/model.  
Then new **coding** session → send short message → Status shows coder tag.  
**Say:**  
“Expected Solution asks for model auto-selection across at least two task types. Inspection routes to an inspect card and chat model. Coding routes to a coder card and a second staged tag. On eight-gigabyte GPUs, loads are sequential — that latency is honest hardware, not a hang.”

---

### Shot 3 — Agentic inspection → Word · WF2 (1:35–3:20) — **main beat**
**Show:**  
1. Attach `README_attach_demo.md` (or PDF).  
2. Confirm extract (Enter).  
3. Confirm cites.  
4. Phase chips / Live log while polish runs.  
5. Self-check DRAFT → Export leave.  
6. Download `.docx` · “grant revoked”.  

**Say:**  
“This is the agentic Expected Solution walk: read an inspection note, pull key findings, ground in local knowledge with cite-or-abstain, then draft an **approval-style Word file** marked **DRAFT**. The engineer confirms each gate. Judgement stays human — there is no in-app Approver and no plant write. Export leave ends the solution path and closes the grant.”

**If phase chips visible:** “While the model works, you see mid-turn phases — packing, calling the model on the peer, drafting Word — so the workbench does not look frozen.”

---

### Shot 4 — Sandbox coding · WF3 (3:20–3:55)
**Show:** More → Sandbox calc · result · optional H9.  
**Say:**  
“Coding and calc run in a sandbox under the grant. We show verified arithmetic in the jail, with human acknowledgement. Fail-closed demos can inject a red sandbox and block export — we do not pretend the process jail is Docker network-none unless that path is on.”

---

### Shot 5 — Multimodal · WF4 (3:55–4:25)
**Show:** Attach `scan_vessel_V101.png` · source line (moondream **or** honest stub).  
**Say:**  
“For image or scan understanding: when a vision tag is staged, we call it through the Gateway. If OCR binaries are missing, we degrade to a labeled fixture stub — we never claim live OCR when it is not live.”

---

### Shot 6 — Fail-closed + close (4:25–5:10)
**Show:** Bad model deny **or** Inject secret → export deny · Verify audit.  
**Say:**  
“Sovereign claim is proven by controls and evidence: public models denied, secrets blocked on leave, grants revoked, audit chain verifiable. Happy to answer architecture questions — and to show the same walk on a single mid-range workstation as the problem statement allows.”

**End card:** Product name · SIH26117 · Team placeholders · `DRAFT ≠ CERT`

---

## 2. B-roll / cutaways (optional)

| Clip | Seconds | Note |
|------|---------|------|
| A `ollama serve` log on model load | 2–4 | Two-laptop only |
| Word open in Word Online/Desktop | 3 | DRAFT watermark / footer if present |
| Share text copy | 2 | Shows tags + peer URL |

---

## 3. Banned on video (same as PPT)

- “Chatbot app” as the product name  
- “CERT certified” / “WAN=0 proven forever” on hotspot alone  
- “AI approved this for the plant”  
- Fake URLs / fake metrics  

---

## 4. After your manual test — what to tell us

Reply with notes like:
1. Which shots felt slow / confusing  
2. Whether you want **Story A** (single laptop) or **Story B** (two-laptop) as the primary cut  
3. Any wording you want softer/stronger on air-gap  
4. Target length (3 / 5 / 8 minutes)  

Then ask for **video script modification** (and PPT sync) — we will not rebuild PPTX/video assets until you say so.
