# WP-01 — Architect perspective (not frozen)

> **NON-BINDING SUPERSEDED.** Historical only. Binding = freezes WP-01/05 rev 2.0: Approver=org paper only; self-HITL; export leave; Admin=IT.

**Date:** 2026-09-17  
**Depends on:** `WP-00_FREEZE.md` rev 1.1 (binding)  
**Status:** **SUPERSEDED by `WP-01_FREEZE.md`.** Kept for history.  
**Job of WP-01:** Who uses KWB, what jobs they run, what artefacts exist — must vs ambition vs never-mix.

Official PS: Background jobs + Expected Solution inspection→Word.  
Do not invent MRPL org-chart titles as facts.

---

## One sentence (proposed)

KWB is used by **organisation knowledge workers** (and approvers/admins) to run **defined jobs** that produce **typed artefacts**; the binding demo job is **inspection scan → DRAFT Word approval note**, not “anyone chats about anything.”

---

## 1. Two different “who” concepts (do not collapse)

WP-00 already froze **role classes** (access): Knowledge worker / Approver / Admin.

WP-01 adds **job personas** (work to be done). One person may hold one role class and several job types over a week.

| Concept | Answers | Example |
|---|---|---|
| **Role class** | What KWB *allows* them to do | Approver may accept/reject DRAFT |
| **Job persona** | What *work* they bring | Inspection engineer drafts approval note from a scan |

---

## 2. Primary users (my recommendation)

### 2.1 Must-work / demo spine (Expected Solution)

| Persona (generic) | Job | Artefact out |
|---|---|---|
| **Inspection knowledge worker** | Read scanned inspection report; extract findings; draft approval note | **DRAFT `.docx`** (+ PDF if possible) |
| Same or second worker | Coding task for an internal tool snippet | Code + **sandbox verified** result |
| Same | Multimodal: understand image/scan | Structured findings feeding the note |

Demo may use **one human** wearing Knowledge worker (+ Approver for HITL) to keep the venue simple. Org paper still separates Approver.

### 2.2 Org-ambition users (Official Background + Description)

Knowledge work types named or implied by the PS (not exclusive MRPL titles):

| Job family | Typical work | Typical artefacts |
|---|---|---|
| Inspection / integrity | Scans, drawings, thickness/findings → notes | Word/PDF DRAFT |
| Engineering calc / analysis | Calculations with steps (rule book) | Calc pack / later Excel (**deferred calc per WP-00**) |
| Internal tools / coding | Scripts, small tools | Code + sandbox proof |
| Document / approval / board | Approval notes, board presentations | Word; **PPT deferred** |
| Spreadsheet / data tables | Tables, trackers | **Excel deferred** |
| Correspondence / search-heavy | Ground answers in SOPs/mail | Cited DRAFT notes |
| Cross-sector same shape | PSU / defence-linked / gov office knowledge work | Same artefact classes |

**Sponsor:** MRPL. **Product shape:** not MRPL-only (WP-00).

### 2.3 Non-users (who KWB is *not* for)

| Non-user | Why |
|---|---|
| DCS / console operator controlling the plant | Never OT agent |
| Autonomous “approver bot” | Human is ultimate decider |
| Public/cloud AI user path | Fully offline |
| Someone expecting KWB to **write** EAM/ERP/DCS | Read-only to existing systems |

Contractors vs employees: **org-ambition concern** (different grants). Exact IdP mapping = later / unknown. Do not invent MRPL contractor policy.

---

## 3. Jobs (what “a task” means)

A **job** in KWB = a user-started unit of work with:

1. Intent (e.g. inspection approval note)  
2. Inputs (scan, files, optional KB grant)  
3. Skill(s) + specialist agent  
4. Model route (card)  
5. **DRAFT** artefact(s)  
6. HITL verify steps (OCR → human → KB; draft gate)  
7. Grant that **revokes** at end  

### 3.1 Must-work jobs (acceptance)

| Job id | Description | PS hook |
|---|---|---|
| `inspect-to-note` | Scan → findings → DRAFT Word approval note | Expected Solution |
| `code-sandbox` | Generate code → run/verify in sandbox | Expected Solution |
| `multimodal-understand` | Image/scan understanding (feeds or stands with above) | Expected Solution |
| `route-demo` | Show ≥2 task types → ≥2 model ids in log | Expected Solution |

### 3.2 Org-ambition jobs (examples — freeze names later)

| Job id | Description | Bucket |
|---|---|---|
| `doc-search-cite` | Internal search + three-level citation DRAFT | Ambition |
| `spreadsheet-assist` | Excel-oriented work | Deferred (Excel) |
| `board-deck` | PPT / board pack | Deferred (PPT) |
| `rulebook-calc` | Calc with steps per rule book | Deferred (org-only calc) |
| `correspondence-ground` | Ground in past mail/SOP | Ambition |

Jobs load **role-appropriate skills** (WP-00). Not every job for every role.

---

## 4. Artefacts

### 4.1 Classes (from WP-00 — flesh out)

| Class | Who creates | KWB may | Must not |
|---|---|---|---|
| **Plant-controlled** | Org DMS/process (outside KWB) | **Read** under grant | Write/edit system of record |
| **Workbench-generated** | KWB task | Create/update in **KWB workspace** as DRAFT | Auto-become plant record |
| **Personal** | User (`.md`, personal skills) | Store in personal shelf | Treat as SOP without HITL promotion |

### 4.2 Formats — must / ambition / deferred (align WP-00)

| Format | Bucket | Notes |
|---|---|---|
| **Word `.docx` DRAFT** | **Must-work** | Inspection approval note path |
| **PDF** | Must-work *when possible* | Same content; failure OK if docx OK |
| **Verified code + sandbox report** | **Must-work** | Pass/fail visible |
| **Structured findings JSON/fields** | Must-work (internal) | Feeds Word; HITL after OCR |
| Excel | Deferred | Org-ambition |
| PPT | Deferred | Org-ambition |
| Calc-with-steps pack | Deferred | Org-only per WP-00 |
| Personal `.md` / skill files | Ambition | Harness; not plant truth |
| Audit/lineage records | Ambition | Who did what (WP-17/14) |

### 4.3 Template binding per job

| Job | Template source |
|---|---|
| `inspect-to-note` | Admin org template if present; else KWB base approval-note template; freestyle only if company policy allows |
| Coding | No Office template; sandbox output format is the artefact |
| Deferred Excel/PPT | Admin templates when those jobs are promoted |

### 4.4 Labelling (org need — propose for freeze)

Every workbench-generated Office-like file carries a visible **DRAFT / AI-assisted — requires human verification** mark until a human Approver (or allowed worker policy) accepts it. Acceptance does **not** write into plant DMS via KWB.

---

## 5. Mapping roles ↔ jobs (proposed)

| Role class | Typical jobs | Cannot |
|---|---|---|
| Knowledge worker | inspect-to-note, code-sandbox, multimodal, search-cite; use org or allowed freestyle templates | Install unbounded MCP; register models; silent record file |
| Approver | Accept/reject DRAFT; deny grants | Bypass Never; write plant systems |
| Admin | Model cards, local MCP allowlist, org templates, offline media ops | Be the only “approver” of engineering content by default (separation of duties preferred) |

Small demo: one person may hold worker + approver. Org paper keeps them distinct.

---

## 6. What WP-01 must never do

- Invent named MRPL SOPs, form numbers, or SLA hours as Official.  
- Make chat the primary artefact.  
- Promote Excel/PPT/calc into must-work (contradicts WP-00).  
- Mix personal `.md` into plant-controlled storage.  
- Define IdP/SSO (later).  
- Define EAM connector APIs (WP-02).

---

## 7. Adversarial flags (for when we freeze)

| Risk | Mitigation in freeze |
|---|---|
| “Everyone is a user” → no demo focus | Primary demo persona = inspection knowledge worker |
| Freestyle templates look like approved plant forms | Label DRAFT; freestyle only if company-allowed |
| Contractor pastes secrets | Grant/classifier later; note non-employee as ambition concern |
| Board PPT steals the spine | PPT stays deferred |
| Too many job ids | Freeze a short must list; ambition list as examples |

---

## 8. Open questions for your perspective

1. **Primary org paper user:** inspection-first, or equal weight across Background job families?  
2. **Demo HITL:** same person as worker+approver, or force two roles even in demo?  
3. **Freestyle templates:** allowed for must-work inspection note, or inspection note **must** use Admin/KWB base template only?  
4. **Contractors:** in scope for org paper as a distinct grant class, or out of WP-01?  
5. **Personal `.md`:** in WP-01 freeze as artefact class only, or also name “daily harness jobs”?  
6. Any job family from your MRPL/org view to **add** or **exclude**?

---

## 9. Next after you answer

Adversarial pass on combined perspectives → `WP-01_FREEZE.md` → then WP-02.
