# WP-01 Users, jobs, artefacts — FREEZE (rev 2.0)

**Date:** 2026-09-19  
**Status:** **FROZEN rev 2.0** — reopened and updated to align with **WP-05 rev 2.0** (DM accepted 2026-09-19)  
**Prior:** rev 1.1 (2026-09-17) — **superseded** for in-app Approver / dual-role DRAFT accept  
**Depends on:** WP-00; **WP-05 rev 2.0** (must not contradict)  
**Inputs:** prior WP-01 pack; WP-05_REV2_REDTEAM; Flow F1–F7; product assist→export  
**Product:** **KWB**  

**Stack:** not locked. No MRPL form numbers, SLA hours, or KB Unverified KPIs as Official.

---

## 1. One-sentence contract

KWB is used by **organisation knowledge workers** and **admins (IT)** to run **defined jobs** that consume typed **inputs** and produce typed **outputs**; the binding demo job is **inspection scan → DRAFT Word (`.docx`) note** (assist in workbench → **export leave**), not chat-as-product. **Paper / officer Approver** exists in the **organisation**, not as an in-app DRAFT-accept role.

---

## 2. Two “who” concepts (do not collapse)

| Concept | Meaning | Frozen set |
|---|---|---|
| **Role class (in-app)** | What KWB *allows* (access) | **Knowledge worker** / **Admin** (+ optional Auditor ambition) |
| **Org paper role (outside KWB)** | Company process after export | **Approver / officer** — paper / plant filing — **not** an in-app HITL actor for H2/H3 |
| **Job persona / job family** | What *work* they bring | Demo: inspection knowledge worker (+ coding/multimodal may be same human). Org: families in §5 |

**Do not collapse:** in-app Worker self-HITL ≠ org paper Approver.  
**Demo:** one human may be Worker for the walk; **do not** label dual-role “Approver” for export (WP-05).

---

## 3. Role classes and activities

### 3.1 Mandatory in-app roles

| Role | May | Must not |
|---|---|---|
| **Knowledge worker** | Start jobs; attach inputs; **self-HITL** H1/H2/H3/H7/H9 (WP-05); edit DRAFT; request/use task grants; use Admin/KWB templates or **company-allowed freestyle**; invoke **allowlisted local MCP/tools under task grant**; view **Audience B** for **own** task (card, grant, citations, own HITL state); **export leave** | Register models; unbounded MCP install; auto-file plant; treat personal `.md` as SOP; act as in-app plant Approver; break Never |
| **Admin (IT)** | **Application/platform control:** model cards add/disable (local tags only; **no pull**); local MCP/skill **allowlist**; own **org/higher templates**; offline-media intake ack; promote org skill packs (**H6**); configure Audience A monitor path; high-class grant expand UX (**H8**) | Override **Never**; write plant systems; **proxy** worker H1/H2/H3/H7/H9; enable public `/v1` or registry pull; silent un-audited break-glass |

**Skill promotion (in-app):** **Admin only** (WP-05 H6). Org paper may still require offline policy sign-off outside KWB.

### 3.2 Org paper only (not in-app KWB role)

| Role | Where | May | Must not |
|---|---|---|---|
| **Approver / officer** | **Outside KWB** (paper / company process after export) | Accept/reject for **plant / record-facing** outcomes using exported DRAFT + evidence; company filing | Exist as in-app H2/H3 clicker; be replaced by a bot inside KWB; write plant **via** KWB |

### 3.3 Optional ambition role (in-app)

| Role | May | Bucket |
|---|---|---|
| **Auditor** | Read audit / lineage / egress evidence only | Org-ambition |

### 3.4 Non-users (frozen)

| Non-user | Why |
|---|---|
| DCS / console / OT control operator (as KWB product user) | WP-00 Never OT agent |
| Autonomous approver bot (in-app or org) | Human ultimate decider |
| In-app “Approver” queue user | WP-05 — no forward-accept |
| Cloud / public AI path user | Fully offline |
| Anyone expecting KWB to **write/edit** EAM / ERP / DCS / DMS-of-record | Read-only to existing systems |

**Contractors vs employees:** org-ambition **grant-class concern** (stricter grants). Exact IdP policy = later — not invented here.

---

## 4. Demo vs org users

| Scale | Primary user | Rule |
|---|---|---|
| **Must-work demo** | **Inspection knowledge worker** | Coding + multimodal may be the **same human**. **Self-HITL** only in-app. **No** Worker+Approver dual-role label for DRAFT/export. |
| **Org paper** | Inspection-first spine; equal **product shape** for other Official Background families | **Approver kept on paper outside KWB**. Cross-sector same artefact rules. MRPL = sponsor. |

---

## 5. Jobs

### 5.1 What a job is

A job = intent + inputs + skill(s)/specialist + model card route + **DRAFT/evidence outputs** + **self-HITL** (OCR→human→KB where applicable; H2 self-check; H3 export leave) + **task grant that revokes** at end.

### 5.2 Must-work jobs (acceptance)

| Job id | What the user does | Required **outputs** (see §7) |
|---|---|---|
| `inspect-to-note` | Scanned inspection report → findings → DRAFT note → self-check → **export leave** | DRAFT `.docx` (+ PDF if possible); OCR/extract; findings; **citations only if KB grant active** |
| `code-sandbox` | Generate internal-tool code → sandbox → **H9** | Code artefact + **sandbox pass/fail report** |
| `multimodal-understand` | Image or scan understanding (standalone or feeds inspect-to-note) | Structured understanding / findings fields |

**Routing proof:** ≥2 **task types** → routing log with **task→card→model_id**. Prefer ≥2 distinct `model_id`s when a second chat model is **staged offline** (no pull). Until then: ≥2 task→card routes may share one adopted local tag — **must be labelled honest** in eval/PPT (see GATE_90 A3).

### 5.3 Org-ambition jobs

| Job id / family | Bucket | Notes |
|---|---|---|
| `drawing-review` | **Ambition** | Scanned engineering drawings |
| `doc-search-cite` | Ambition | Internal search + citation DRAFT |
| `correspondence-ground` | Ambition | Past correspondence / SOP |
| `sensitive-corpus-work` | Ambition | Stricter grants (WP-04) |
| `spreadsheet-assist` | **Deferred** | Excel |
| `board-deck` | **Deferred** | PPT |
| `rulebook-calc` | **Deferred** | Calc-with-steps |

Jobs load **role- and task-scoped skills**. Not every skill on every job.

---

## 6. Artefact classes

| Class | Who creates | KWB may | Must not |
|---|---|---|---|
| **Plant-controlled** | Org systems outside KWB | **Read** under grant | Write/edit system of record |
| **Workbench-generated** | KWB job | Create/update in **KWB workspace**; **export leave** | Auto-become plant record |
| **Personal** | User (`.md`, personal skills) | Personal shelf | Treat as SOP without **Admin** promotion (H6) |
| **Ephemeral / UI** | Chat session | Interaction only | Plant-controlled; official deliverable |

**Chat transcript:** never plant-controlled — **not** the product deliverable.

---

## 7. Inputs and outputs (explicit)

### 7.1 Input types (must name)

| Input | Typical class | Used by |
|---|---|---|
| Scanned inspection report (PDF/image) | User-attached | `inspect-to-note`, multimodal |
| Photograph / image | User-attached | Multimodal |
| Handwritten note (image) | User-attached | Multimodal / inspect |
| Engineering drawing (scan/PDF) | User-attached or plant read | `drawing-review` (ambition) |
| Plant SOP / manual / correspondence | Plant-controlled **read** | Search/cite; KB after extract verify |
| User requirements / edits | User claim | DRAFT revise |
| Code task prompt + optional files | User-attached / workspace | `code-sandbox` |

### 7.2 Must-work **outputs** (acceptance artefacts)

| Output | Format / form | Job | Rule |
|---|---|---|---|
| **DRAFT note** | **`.docx`** (required) | `inspect-to-note` | Label: **DRAFT / AI-assisted — own-work verification — not a plant record** |
| **PDF sibling** | PDF when possible | `inspect-to-note` | PDF failure does not fail must-work if docx OK |
| **Extract sheet** | Structured fields + flags | inspect / multimodal | **H1** before KB-as-truth |
| **Findings fields** | Structured | inspect / multimodal | Feeds Word |
| **Sandbox report** | Pass/fail + logs | `code-sandbox` | Evidence only until **H9** |
| **Code artefact** | Source in KWB workspace | `code-sandbox` | Not plant write |
| **Export pack** | docx ± audit ± sandbox proof ± Monitor A artefact | Leave path | **H3** same-user export leave |
| **Routing log** | Task type → card → **model_id** | System proof | ≥2 task types; model_id honesty per §5.2 |
| **Offline / egress evidence** | Monitor A snapshot pack | System proof | **Not CERT** |

### 7.3 Org-ambition / deferred **outputs**

| Output | Bucket |
|---|---|
| Full three-level citation pack | Ambition |
| Drawing-review DRAFT | Ambition |
| Personal `.md` / skills | Ambition |
| Rich audit / lineage UI | Ambition |
| Excel / PPT / calc-with-steps | Deferred |

### 7.4 Templates → outputs

| Job | Template rule | Output |
|---|---|---|
| `inspect-to-note` | Prefer **Admin org** template; else **KWB base**; freestyle if company allows | DRAFT docx (+ PDF if possible) |
| `code-sandbox` | No Office template | Code + sandbox report |

**Worker H2 self-check** and **H3 export** do **not** write into plant DMS/EAM. Plant acceptance = **org paper Approver outside** (§3.2).

---

## 8. Format buckets (unchanged from WP-00)

| Format | Bucket |
|---|---|
| Word `.docx` DRAFT | **Must-work** |
| PDF (when possible) | Must-work companion |
| Verified code + sandbox report | **Must-work** |
| Excel / PPT / calc-with-steps | Deferred |

---

## 9. Never (WP-01-specific)

- Invent MRPL SOP ids, form numbers, or SLA hours as Official.  
- Make chat the primary artefact.  
- Promote Excel / PPT / calc into must-work.  
- Mix personal `.md` into plant-controlled storage.  
- **Revive in-app Approver** for H2/H3 / forward-accept.  
- Delete Approver from **org paper** (outside process still valid).  
- Let Admin proxy worker HITL or break Never.  
- Import Unverified KB KPIs into this contract.  
- Define IdP/SSO or EAM write APIs here.  
- Claim Monitor A / self-HITL = CERT or plant four-eyes.

---

## 10. Closed decisions (this freeze)

| Topic | Decision |
|---|---|
| In-app roles | **Worker + Admin (IT)** |
| Approver | **Org paper only** (outside KWB) |
| Skill promotion in-app | **Admin** (H6) |
| Demo dual-role Worker+Approver | **Removed** — self-HITL only |
| Align WP-05 rev 2.0 | **Mandatory** |
| Org emphasis | **Inspection-first** spine |
| Routing | Real must-work jobs; G1 honesty if one model tag |
| Outputs | §7.2 including export pack |

---

## 11. Explicitly not locked here

Exact permission bits, IdP, contractor policy text, template binaries, OCR engine, Office library brands, lineage engine, second offline chat model tag.

---

## 12. Next

Continue GATE_90: **GO build** desk + goldens (`DESIGN_BUILD_SOT.md`). PPT after execute ≥0.90. (A1–A5 · B1–B7 locked.)

---

## 13. Changelog

| Rev | Note |
|---|---|
| **1.0 / 1.1** | In-app Approver; dual-role demo; skill promote Approver and/or Admin |
| **2.0** | **FROZEN** 2026-09-19: Approver = org paper only; in-app Worker + Admin-as-IT; self-HITL; export leave; no dual-role Approver; align WP-05 2.0; DRAFT label + G1 honesty note |
