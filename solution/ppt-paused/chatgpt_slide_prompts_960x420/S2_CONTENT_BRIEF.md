# Slide 2 (Idea) — adversarial content brief + layout

> **PPT paused** — language scrubbed post **GATE_90_REDTEAM**; do not claim CERT. Monitor A = evidence pack / start-stop — not CERT.

**Rev 3.0** · Date 2026-09-18  
**Why:** Generated S2 failed selection eye-path (jargon, flat 11-box loop, weak uniqueness chips, addresses ate the diagram).  
**SoT:** Official SIH Idea pointers (do not rename) · Expected Solution · WP-00/WP-20 · playbook KEEP.

---

## Official constraints (cannot break)

Slide 2 **must** still contain these four pointers (template lock):

1. Proposed Solution  
2. Detailed explanation of the proposed solution  
3. How it addresses the problem  
4. Innovation and uniqueness of the solution  

We **keep header 4** but replace chip theatre with **Must-work proof + Never** (that *is* uniqueness for a PSU screener).

---

## Why the previous S2 loses

| Attack | What the image did wrong | Fix |
|---|---|---|
| Jargon wall | Session≠grant, Orch+Card, H1/H9, Authz | Plain English first; jargon only if needed |
| Unreadable loop | 11 tiny boxes = cannot redraw in 10s | **Two clear spines** + shared gateway |
| Addresses dominates | 5-row table squeezed the story | **3 rows max**, thin strip |
| Fake uniqueness | AIR-GAP / TRUTH / INTEGRATION stickers | **Expected Solution checklist + Never** |
| Screener question fail | “Is this ChatGPT with a skin?” unclear | One-line product + Word artefact + Monitor A evidence pack |

---

## What a screener must answer from Slide 2 alone

1. **What is it?** Offline workbench → DRAFT Word + verified code (not chat).  
2. **How does it work?** Two jobs share grant → gateway → local models; human approves.  
3. **Does it match Expected Solution?** Three tight PS→mechanism rows.  
4. **Why not Claude / Open WebUI?** Must-work proof + Never line.

---

## New layout @ 960×420 (Rev 3)

```
+------------- C1–C5 --------------+-------------- C6–C12 ---------------+
| R1–R4  PROPOSED (wider+taller)   | R1–R4  DETAILED (taller diagram)    |
| 5 short bullets                  | TWO spines + shared gateway         |
+----------------------------------+-------------------------------------+
| R5     ADDRESSES — thin 3-row table only                               |
+------------------------------------------------------------------------+
| R6     UNIQUENESS — Must-work proof strip + Never (not slogan chips)   |
+------------------------------------------------------------------------+
```

| Region | Cells | Height intent |
|---|---|---|
| A Proposed | C1–C5, R1–R4 | More horizontal + more vertical |
| B Detailed | C6–C12, R1–R4 | More vertical for diagram |
| C Addresses | C1–C12, R5 | **Shrunk** (one row of cells) |
| D Uniqueness | C1–C12, R6 | Proof / Never (selection content) |

---

## Content lock (paste source for PROMPT_S2)

### A — Proposed (5 bullets, plain)

1. **Knowledge Work Bench** — offline workbench for confidential industrial knowledge work (MRPL-class). **Not a chatbot. Not a new LLM.**  
2. **What user gets:** scanned inspection → **DRAFT Word (.docx)** approval note; coding task → **run + verify** in a sealed sandbox.  
3. **How models work:** pluggable open-weight models on a **separate GPU runtime**; workbench talks only through a **local gateway** (`/v1`).  
4. **Control:** every job needs a **task grant**; **human** is final approver; software only drafts and checks.  
5. **Safety line:** outputs stay in **KWB store**; **never write** plant systems; demo shows **Monitor A evidence pack** (start-stop snapshot — **not CERT**).

### B — Detailed (diagram — readable)

**Shared spine (top):**  
`Person → Task grant → Workbench brain → Local gateway → On-prem model`

**Job 1 — Inspection (middle):**  
`Scan/photo → On-device read (OCR/vision) → Human checks extract → Template Word DRAFT → Human approve → Audit`

**Job 2 — Code (bottom):**  
`Code task → Auto-pick model → Sandbox (no network) → Pass/fail evidence → Human decide`

**Callouts (3 lines max):**  
- Gateway is the **only** path to models. Sandbox **never** wraps the GPU.  
- Auto-select ≥2 task types → **G1 floor: single-tag adopt OK**; full = **two model ids** when 2nd chat staged offline (load one model at a time on mid-GPU).  
- Missing cite / bad grant / audit fail → **stop** (fail-closed).

### C — Addresses (3 rows only)

| Expected Solution | Knowledge Work Bench |
|---|---|
| Mid-GPU local; smaller model OK | Separate runtime; smaller/quant models OK |
| ≥2 task types auto-selected | G1 floor single-tag OK; full ≥2 model ids if staged |
| Scan→Word + sandbox code + zero external calls | Word DRAFT path + sealed sandbox + Monitor A evidence pack (not CERT) |

### D — Uniqueness (keep official title; better body)

**Left — Must-work proof (what jury can see):**  
Word DRAFT · G1 floor/full model ids · sandbox verify · multimodal scan · Monitor A pack  

**Right — Never (why PSU-safe):**  
No cloud LLM · no write to DCS/EAM/ERP · no auto statutory/safety decision · Excel/PPT = later not claimed now  

**One bottom line:**  
*vs Claude/Copilot: cannot take P&IDs. vs Open WebUI: chat+RAG is not grant→Word→sandbox→Monitor A evidence pack.*

---

## Info still useful from you (optional)

| Ask | If blank we keep |
|---|---|
| Prefer bottom title text exactly “Innovation and uniqueness of the solution”? | **Yes** (official) |
| Any team tagline under product name? | None |
| Confirm Excel/PPT stay LATER on this slide? | **Yes** |

---

## Disposition

`PROMPT_S2.txt` rewritten to Rev 3.0 from this brief. Regenerate Slide 2 PNG only first; judge eye-path before regenerating S3–S6.
