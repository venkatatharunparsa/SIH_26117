# WP-01 — Adversarial red-team + source verification

> **NON-BINDING SUPERSEDED.** Historical only. Binding = freezes WP-01/05 rev 2.0: Approver=org paper only; self-HITL; export leave; Admin=IT.

**Date:** 2026-09-17  
**Target:** `WP-01_ARCHITECT_PERSPECTIVE.md` (not yet frozen)  
**Against:** `WP-00_FREEZE.md` rev 1.1 + Official PS (`01-problem-statement.md`)  
**Status:** Findings consumed. **WP-01 frozen** in `WP-01_FREEZE.md` (all fills accepted; A4 = ambition).

Grades: **Official** = PS text. **WP-00** = frozen contract. **Proposed** = architect recommendation. **KB/Unverified** = research notes, not binding. **Invalidated** = contradicts Official or WP-00.

---

## Verdict

| Question | Answer |
|---|---|
| Aligns with WP-00? | **Mostly yes** — no hard contradiction found |
| Roles complete for a freeze? | **Almost** — three WP-00 roles present; a few **secondary** actors missing |
| Docs/artefacts complete? | **Strong on outputs**; **weak on inputs** and a few must-work evidence docs |
| Ready to freeze without user answers? | **No** — open Qs in §8 of the perspective still block a clean freeze |
| Confidence WP-01 draft is usable | **0.82** as a debate base; **~0.70** as freeze-ready until gaps + your answers |

**Bottom line:** Keep the spine (inspection → DRAFT docx; role vs job split; three artefact classes; deferred Excel/PPT/calc). **Fill gaps below** before or inside `WP-01_FREEZE.md`. Do not import KB time KPIs or invented MRPL titles as Official.

---

## 1. WP-00 alignment matrix

| WP-00 rule | WP-01 draft | Align? |
|---|---|---|
| Artefact not chat | One-sentence + formats | Yes |
| Role classes Worker / Approver / Admin | §1, §5 | Yes |
| Artefact classes plant / generated / personal | §4.1 | Yes |
| Must-work docx; PDF when possible | §2.1, §4.2 | Yes |
| Excel / PPT / calc deferred | §2.2, §4.2, §3.2 | Yes |
| Human ultimate; DRAFT; no auto record | §4.4 | Yes |
| Read-only plant systems | §4.1, non-users | Yes |
| Offline / no cloud user path | Non-users | Yes |
| Task = grant + skills + HITL + revoke | §3 job definition | Yes |
| Templates Admin + freestyle if allowed | §4.3 | Yes |
| Never promote deferred to must-work | §6 | Yes |
| Specialist agents / skills by role | Mentioned; not fully tabulated | Soft — OK for WP-01, detail WP-07 |
| Monitors Audience A/B | **Missing as user/consumer** | Gap G4 |
| OCR → human → KB | Inside job steps | Yes |
| Personal `.md` not plant truth | §4.1 | Yes |

**No Invalidated conflict with WP-00.** Soft gaps only.

---

## 2. Claim-by-claim source verification

### § One sentence

| Claim | Grade | True? | Note |
|---|---|---|---|
| Users = org knowledge workers + approvers/admins | **WP-00** + **Proposed** | Yes | Roles from WP-00 |
| Binding demo = inspection scan → DRAFT Word | **Official** Expected Solution + **WP-00** DRAFT | Yes | PS says Word file; WP-00 adds DRAFT/HITL |
| Not “anyone chats about anything” | **WP-00** + **Official** deliverables | Yes | |

### §1 Role vs job persona

| Claim | Grade | True? | Note |
|---|---|---|---|
| Role class = access; job persona = work type | **Proposed** | Yes | Sound design; not in PS wording |
| WP-00 froze three roles | **WP-00** §10 | Yes | |

### §2.1 Demo users

| Claim | Grade | True? | Note |
|---|---|---|---|
| Inspection worker → scan → approval note docx | **Official** Expected Solution | Yes | |
| Coding → sandbox verified | **Official** Expected Solution | Yes | |
| Multimodal image/scan | **Official** Expected Solution | Yes | |
| One human may wear worker+approver in demo | **Proposed** | Allowed by WP-00 “small deployment” | Must not erase Approver in **org** paper |
| “Inspection knowledge worker” title | **Proposed** generic | Yes | Not an MRPL HR title — keep generic |

### §2.2 Org job families

| Claim | Grade | True? | Note |
|---|---|---|---|
| Approval notes, board presentations, engineering calculations, code, review scans/drawings/inspection | **Official** Background | Yes | |
| PPT / Word / Excel / calc steps as outputs | **Official** Description | Yes | Buckets must follow WP-00 deferred |
| Spreadsheet work | **Official** Description tools | Yes | Deferred as Excel artefact |
| Internal document search / correspondence | **Official** Description | Yes | |
| PSU / defence / gov offices | **Official** Background | Yes | |
| MRPL sponsor, not only shape | **Official** org + **WP-00** | Yes | |
| “Thickness/findings” wording | **KB/Unverified** colour | Soft | Drop or mark Unverified in freeze — not Official PS |
| Exact hours (2 days typing, etc.) | **KB/Unverified** | **Do not freeze** | Not Official |

### §2.3 Non-users

| Claim | Grade | True? | Note |
|---|---|---|---|
| Not OT/DCS console product | **WP-00** Never | Yes | |
| Not approver bot | **WP-00** human decider | Yes | |
| Not cloud path | **WP-00** offline | Yes | |
| Not EAM/ERP writer | **WP-00** read-only | Yes | |
| Contractors = ambition concern | **Proposed** + prior Mem0/KB | Soft | OK as ambition open point; no Official contractor rule |

### §3 Jobs

| Claim | Grade | True? | Note |
|---|---|---|---|
| Job = intent+inputs+skills+route+DRAFT+HITL+revoke | **WP-00** composition | Yes | |
| `inspect-to-note` / `code-sandbox` / multimodal / route-demo | **Official** Expected Solution | Yes | `route-demo` is meta — keep as acceptance job |
| Ambition job ids | **Proposed** | Yes | Examples only until freeze |
| `rulebook-calc` deferred | **WP-00** Q5 | Yes | |

### §4 Artefacts

| Claim | Grade | True? | Note |
|---|---|---|---|
| Three classes | **WP-00** §5.1 | Yes | |
| docx must; PDF when possible | **WP-00** Q1 | Yes | |
| Structured findings as must-work internal | **Proposed** (supports Official path) | Yes | Needed for HITL/OCR gate — freeze as must-work **internal** artefact |
| DRAFT label | **Proposed** + WP-00 HITL spirit | Yes | Recommend freeze |
| Freestyle if company allows | **WP-00** Q6 | Yes | |
| Acceptance does not write DMS | **WP-00** | Yes | |

### §5 Role ↔ job map

| Claim | Grade | True? | Note |
|---|---|---|---|
| Worker cannot register models / unbounded MCP | **WP-00** Admin owns those | Yes | |
| Admin should not be sole engineering approver | **Proposed** SoD | Soft | Prefer in org paper; demo may combine |

### §6 Never for WP-01

| Claim | Grade | True? | Note |
|---|---|---|---|
| No invented MRPL SLAs/forms | Correct method | Yes | |
| No Excel/PPT/calc → must-work | **WP-00** | Yes | |

---

## 3. Attacks (where WP-01 is weak)

### A1 — Roles incomplete for full KWB host

**Attack.** WP-00 has plugin host, skill promotion, monitors, offline media. WP-01 only lists three roles’ *typical jobs*. Who is the **day-to-day consumer of Audience B monitors**? Who **promotes personal skill → org**?

**Finding.** Not a fourth RBAC role required. Missing **activities** on existing roles + one optional **read-only auditor** (ambition).

**Fill before freeze:**

| Actor | Activity (add to role map) |
|---|---|
| Admin | Promote org skills (HITL); offline media allowlist; view sovereign monitor config |
| Approver | Promote personal→org skill (or shared with Admin — **decide**) |
| Knowledge worker | Consume operator monitor for own task (card, grant, citations) |
| Auditor (optional ambition) | Read audit/lineage only — park if you reject |

### A2 — Docs incomplete: inputs vs outputs

**Attack.** PS path starts with a **scanned inspection report**. WP-01 catalogues outputs well; **input artefact types** are thin.

**Fill:**

| Input type | Class | Notes |
|---|---|---|
| User-attached scan/photo/PDF | User-attached (grant low friction) | Official multimodal + Expected Solution |
| Handwritten note image | User-attached | **Official** Description |
| Engineering drawing image/PDF | User-attached or plant-controlled if from DMS | **Official** Background/Description |
| Plant SOP/manual/correspondence chunk | Plant-controlled read | **Official** KB connector |
| Sandbox test project / script | Workbench workspace | Coding path |

### A3 — Missing must-work **evidence** artefacts

**Attack.** Expected Solution requires **model auto-select proof** and **sandbox verified** and **zero external calls**. Those are artefacts/logs, not only Office files.

**Fill as must-work artefacts (not Office):**

| Artefact | Why |
|---|---|
| Routing log (≥2 task types, ≥2 model ids) | Official Expected Solution |
| Sandbox pass/fail report | Official Expected Solution |
| Offline / egress evidence (log or visible monitor capture) | Official Expected Solution |
| OCR extract sheet (pre-human-verify) | WP-00 OCR pipeline |
| Citation pack / `NOT FOUND` list (ambition for full three-source; minimal citations on demo note if KB used) | WP-00 ambition; don’t over-require for bare Expected Solution |

### A4 — Drawing review under-specified

**Attack.** Official Background: “review of scanned drawings and inspection reports.” Draft folds drawings into inspection family only.

**Fill:** Either explicit job `drawing-review` (ambition or under multimodal) **or** freeze line: drawing review ⊆ `multimodal-understand` + optional note path.

### A5 — Sensitive corpus jobs missing

**Attack.** Official confidential classes include financials, vendor negotiations, strategy. No job family for “people who draft from those corpora.”

**Fill (ambition):** job family **sensitive document knowledge work** (generic) — same artefact classes, **stricter grant/classifier** (WP-04). Do not invent “Finance Officer” as Official MRPL title.

### A6 — Self-approve vs Approver

**Attack.** §4.4 “Approver (or allowed worker policy)” + demo one person = Approver role becomes optional.

**Fill:** Freeze: **Org paper** requires Approver distinct. **Demo** may combine worker+approver on one account **labelled as dual-role**, not “Approver deleted.”

### A7 — KB lived-experience bleed

**Attack.** Thickness matching, 2-day typing, named workflows from `12-user-perspective` feel Official.

**Fill:** Freeze uses **only** Official PS work types + WP-00. KB examples stay in research folder, marked Unverified.

### A8 — `route-demo` is not a user job

**Attack.** Jury confusion: is routing a persona?

**Fill:** Freeze as **acceptance criterion / system job**, demonstrated via at least two user jobs (e.g. inspect-to-note + code-sandbox), not a separate human persona.

### A9 — Chat UI artefact silence

**Attack.** WP-00 allows chat as UI. WP-01 never says chat transcript is **not** retained as plant-controlled.

**Fill:** Chat transcript = workbench-generated or ephemeral; **never** plant-controlled; not the deliverable.

---

## 4. Required roles checklist

| Role / actor | In draft? | Required in WP-01 freeze? | Source |
|---|---|---|---|
| Knowledge worker | Yes | **Yes** | WP-00 |
| Approver | Yes | **Yes** | WP-00 |
| Admin | Yes | **Yes** | WP-00 |
| Inspection demo persona | Yes | **Yes** (primary demo) | Official Expected Solution |
| Coding persona (may = same human) | Yes | **Yes** | Official |
| Job families (Background) | Yes | **Yes** (ambition list) | Official Background |
| Skill promoter activity | No | **Yes** (on Approver and/or Admin) | WP-00 skill shelves |
| Monitor consumer activity | No | **Yes** (on worker + Admin) | WP-00 monitors |
| Auditor read-only | No | Optional ambition | Org audit |
| Plugin developer outside org | No | Out of scope | Never internet marketplace |
| OT operator | Non-user | **Yes** as non-user | WP-00 |

---

## 5. Required docs / artefacts checklist

| Doc / artefact | In draft? | Must / ambition / deferred | Source |
|---|---|---|---|
| DRAFT approval note `.docx` | Yes | **Must** | Official + WP-00 |
| PDF sibling | Yes | Must when possible | WP-00 |
| Sandbox-verified code + report | Partial (code yes; report thin) | **Must** — make report explicit | Official |
| Routing / model-id log | Via route-demo only | **Must** — name as artefact | Official |
| Offline/egress proof | No | **Must** — name as artefact | Official |
| OCR extract + human verify mark | Implied | **Must** internal | WP-00 |
| Structured findings fields | Yes | **Must** internal | Proposed supporting Official |
| Citation / NOT FOUND pack | Thin | Ambition (full three-source) | WP-00 |
| Excel / PPT / calc pack | Deferred | Deferred | WP-00 |
| Personal `.md` / skills | Yes | Ambition | WP-00 |
| Audit / lineage records | Yes | Ambition | WP-00 |
| Input: scan / photo / drawing / handwriting | Thin | **Must** name inputs | Official |
| Plant-controlled SOP/mail (read) | Class only | Ambition connector | Official Description |
| Chat transcript | No | Explicit **non-deliverable** | WP-00 |

---

## 6. What is *not* missing (do not add)

- MRPL form numbers, SLA hours, employee counts as Official  
- Excel/PPT/calc as must-work  
- IdP/SSO design  
- EAM API schemas  
- Fourth mandatory RBAC role named “Plugin User” (Admin allowlist is enough)  
- Graph database  

---

## 7. Recommended freeze contents (after your perspective)

1. Role classes (unchanged from WP-00) + **activity matrix** including skill promote + monitor consume.  
2. Primary demo persona = inspection knowledge worker; coding/multimodal may be same human.  
3. Must-work jobs = inspect-to-note, code-sandbox, multimodal (feeds or stands alone); routing proved **by those jobs**.  
4. Ambition job families from Official Background only (+ generic sensitive-corpus family).  
5. Non-users list.  
6. Artefact classes + **input types** + must-work evidence artefacts (routing log, sandbox report, egress proof).  
7. Format buckets identical to WP-00.  
8. DRAFT labelling; dual-role demo rule.  
9. Explicit: no KB Unverified KPIs in freeze.

---

## 8. Still need from you (blocks freeze quality)

Same as perspective §8, plus:

7. **Skill promotion:** Approver, Admin, or either?  
8. **Auditor role:** in or out of WP-01?  
9. **Drawing review:** separate ambition job or folded into multimodal?

---

## 9. Next

You answer open questions (perspective §8 + §8 above) → we write `WP-01_FREEZE.md` incorporating these fills → then WP-02.
