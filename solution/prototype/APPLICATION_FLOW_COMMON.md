# KWB — Common application flow

**Date:** 2026-09-19  
**Status:** **LOCKED** — DM accepted common workflow (A→J); follow this only.  
**Not yet:** full desk UI implementation · PPT narrative  
**Product behaviour (DM locked):**

| ID | Decision |
|---|---|
| F1 | Anyone opens workbench; **no in-app hierarchy** |
| F2 | Assistance only; **paper approval outside**; soft copy if officer asks |
| F3 | No worker-to-worker task dependency inside KWB |
| F4 | **Common capability set** for all users; jobs differ by task |
| F5 | Design around **one common workflow**; start/end stretch by need |
| F6 | **HITL = same user** checks own DRAFT; no in-app boss Approver |
| F7 | Jury / leave-with: **Word DRAFT + audit**; **+ sandbox proof** if code/calc used |

**Freeze note (WP-05):** **FROZEN rev 2.0** (2026-09-19) — self-HITL · export leave · Admin-as-IT · paper Approver outside. Aligns F6.  

---

## Why the old 6-step spine was incomplete

It missed **must** steps that Official PS + Expected Solution + industrial HITL practice require. Adversarial fill below.

**Sources used for fill (not assumptions alone):**
- Official PS Expected Solution (scan→Word, sandbox, multimodal, WAN=0, ≥2 task types)
- Freezes WP-00/04/05/11/16/18 (behaviour contracts)
- External patterns: cite-or-abstain / validation-before-delivery (CiteGuard-RAG class); evidence-aware engineering workbench (extract → human review → export); HITL audit components (identity, gate, artefact version, decision); industrial KMS “DRAFT ≠ approved”

---

## Common workflow (filled)

Every user / every job type walks this **spine**. Optional branches only when the task needs them.

```text
A. ENTER
   A1. Open workbench (any knowledge worker — no org chart)
   A2. Session starts (who is operating) — NOT the same as document grant

B. INTENT
   B1. State task intent in plain language (or pick a common job type)
   B2. System records task type (needed later for auto model select ≥2 types)

C. INPUTS
   C1. Attach what this task needs (scan / image / files / notes) — or none if text-only
   C2. Pick template: org/KWB base / company-allowed freestyle

D. EXTRACT (only if scan/image/PDF)
   D1. OCR / vision extract → structured fields + raw text
   D2. ★ SAME-USER HITL H1: confirm / correct extract before it may feed draft or KB-as-truth
       (machine OCR ≠ truth)

E. ACCESS TO EXISTING KNOWLEDGE (when task needs org docs)
   E1. Request / activate **task grant** (what shelves this task may read) — grant ≠ session
   E2. Retrieve only under grant
   E3. ★ KNOWLEDGE VERIFIER (machine, fail-closed):
       - every material claim must bind to retrieved evidence OR be marked NOT FOUND / abstain
       - no invented citations
   E4. ★ SAME-USER HITL: review citations / gaps / contradictions (H7 path) before trusting draft prose
       (retrieve ≠ verified knowledge)

F. ASSIST / DRAFT
   F1. Plan multi-step work (agentic) under grant + Never rules
   F2. Route to model card by task type (visible; ≥2 types in demo)
   F3. Generate **DRAFT** artefact (Word .docx required path) with clear DRAFT status
   F4. Continuous **audit** events (who, what gate, model_id, grant_id, artefact version)

G. CODE / CALC BRANCH (only if task produced code or numeric verify)
   G1. Run in **sandbox** (jail ≠ GPU runtime)
   G2. Machine report = evidence only
   G3. ★ SAME-USER HITL H9: accept/reject sandbox outcome as a decision
   G4. Keep sandbox proof for jury / export pack when this branch ran

H. SELF-CHECK DRAFT (always for deliverable tasks)
   H1. ★ SAME-USER HITL H2: accept / edit / reject own DRAFT
   H2. Any material edit → prior accept stale → must self-check again
   H3. DRAFT is **not** plant record; not filed to SoR by KWB

I. LEAVE / SHARE OUTSIDE
   I1. ★ SAME-USER HITL **H3 = export leave** (soft copy **off** the box — not forward-accept)
   I2. Take: Word DRAFT + audit export; + sandbox proof if G-branch used
   I3. Higher officer / paper approval / filing = **outside KWB** (company process)
   I4. Task end → grant revokes (no leftover privileged read)

J. ALWAYS-ON PROOFS (demo / sovereign)
   J1. Monitor A **evidence pack / start–stop snapshot** (Audience A) — **not CERT**; no verbal WAN=0 without artefact
   J2. Fail-closed on: unregistered model, revoked grant, secret-in-draft, sandbox-red export leave, fake cite
```

### Must-have gates the thin spine forgot (adversarial list)

| Must | Why | If skipped |
|---|---|---|
| **Session ≠ grant** | PS confidentiality / ACL | Wrong shelves leak into draft |
| **H1 extract confirm** | Scans lie; Expected multimodal | Hallucinated findings become “facts” |
| **Knowledge verifier (cite-or-abstain)** | PS “grounds in our documents”; G6 | Fake SOP cites — jury kill |
| **Same-user review of cites/gaps** | Machine green ≠ decision | User rubber-stamps unsupported prose |
| **DRAFT status + self H2** | Human final DM; no in-app boss | Looks like auto-approved record |
| **Sandbox + H9 when code/calc** | Expected Solution coding | “It compiled in chat” is not proof |
| **Audit always** | You locked F7; industrial HITL practice | Cannot show how decision was made |
| **Export leave (H3)** | Soft copy leaves the box | Uncontrolled leak of DRAFT+secrets |
| **Grant revoke at end** | G7 | Privilege hangs after task |
| **Monitor A evidence pack** | Expected Solution sovereign proof — **not CERT** | Claim without artefact |
| **Task-type → model card** | Expected ≥2 types | Dropdown theatre |
| **Contradiction / policy conflict surface** | H7 must-work | Silent policy vs user conflict |

---

## What is **common** vs **per-task**

| Common (every user gets) | Per-task (branch / stretch) |
|---|---|
| Open · intent · DRAFT Word path · self-HITL · audit · fail-closed · no hierarchy | Extract H1 (if scan) |
| Template pick · grant request pattern · cite-or-abstain when KB used | Knowledge retrieve (if docs needed) |
| Export leave (H3) · outside paper process | Sandbox+H9 (if code/calc) |
| | Multimodal image understand (if image job) |

---

## Demo story (same common flow — one concrete walk)

**Inspection note (must-work story):**  
A1–B2 → C attach scan + template → D OCR/fixture + H1 → E grant + knowledge verifier + cite review → F DRAFT Word → H self H2 → I **export leave** (audit) → paper to officer outside.

**Coding story (same spine, G branch on):**  
… → F produce code → G sandbox + H9 → H self-check → I leave with sandbox proof + audit.

---

## Still open for later phases (not blocking this lock)

| Topic | Default from this lock | When to reopen |
|---|---|---|
| No org KB this task | **E skipped** OK — honest no cites / attach-only | If DM requires every demo to show E |
| OCR engine | Fixture extract + H1 (B2) day-1 | When thickening G4 |

**GATE_90:** A4/A5 + B1–B7 locked 2026-09-19 — see `DESIGN_BUILD_SOT.md`.

---

## Next phase (only when DM says)

**Technicality** of how A→J is implemented — then PPT narrative that matches this flow.  
No blind build / no PPT fill until that discussion starts.
