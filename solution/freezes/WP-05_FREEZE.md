# WP-05 HITL map — FREEZE (rev 2.0)

**Date:** 2026-09-19  
**Status:** **FROZEN rev 2.0** — DM accepted 2026-09-19 (self-HITL · export leave · Admin-as-IT · stale kept)  
**Prior:** rev 1.1 (2026-09-18) — **superseded** for in-app Approver on H2/H3  
**Depends on:** WP-00 / WP-02 / WP-04; Flow A→J F1–F7; org/demo diagrams (assist→export)  
**Next freeze follow-up:** none for Approver path — GATE_90 A1–A5 closed; build desk per `DESIGN_BUILD_SOT.md`  
**Red-team:** `../wp/WP-05/WP-05_REV2_REDTEAM.md` (GO 0.91)  
**Product:** **KWB**  
**Stack:** not locked.

---

## 1. One-sentence contract

KWB **assists** in the workbench: it may draft, propose, and machine-check. **The operating knowledge worker** owns every **in-app decision gate** (self-HITL). Accepts bind to an **artefact version** — after any **material change**, prior accept is **stale** and the **same user** must explicitly check again. **Export leave** is a same-user gate. **Plant / officer / paper approval** is **outside** KWB. Grants (WP-04) open access; HITL gates trust. HITL **helps**; it is **not** complete security.

---

## 2. Limits (anti overclaim)

| True | False / refuse |
|---|---|
| Hard gates = explicit same-user accept/reject/correct + audit | Chat “LGTM” / thumbs-up = gate pass |
| Re-check after **material** content change | Click on every UI refresh or keystroke |
| Sandbox / citation / schema = **evidence** | Machine green = human **decision** |
| DRAFT self-check ≠ plant approval | In-app boss / forward-accept queue |
| Export leave reduces uncontrolled soft copies | Export erases residue (WP-04) or = CERT |
| Paper Approver may exist **outside** KWB | Approver role **inside** KWB for H2/H3 |
| Still need air-gap, grants, Never, audit, sandbox | HITL replaces those |

---

## 3. Gate strengths (do not collapse)

| Strength | Meaning |
|---|---|
| **Hard gate** | Explicit human accept / reject / correct **blocks** next privileged step |
| **Review-only** | Warning if skipped; **forbidden** for H1 / H2 / H3 / H7 / H9 |
| **None** | Machine OK (routing log, retrieve under grant, sandbox *run*) |
| **Machine check ≠ HITL** | May fail-closed without being a human decision |

**Grant ≠ gate:** WP-04 allowlists I/O; WP-05 decides trust / export-leave / own-work outcomes.

---

## 4. Closed decisions

### 4.1 Still binding from DM 2026-09-18 (mechanism)

| ID | Decision |
|---|---|
| **D1 Re-check** | After every **material change**, prior accept is **void**; **same user** must explicitly pass the gate again |
| **D2 H1** | **Hard-block** until extract confirm/correct |
| **D3 H7** | Contradiction / cite-gap gate = **must-work** (MOCK OK until WP-22) |
| **D4 Editorial** | User may edit DRAFT; edit = material → **H2 stale**; re-H2 before export leave |
| **D5 Decisions** | **Always human** (same user in-app) owns decisions incl. sandbox/code |
| **D6 Export** | In-place preview ≠ leave. **H3** on **download/export** of docx/PDF/zip **off** KWB |

### 4.2 New / overriding (DM 2026-09-19 — product boundary)

| ID | Decision |
|---|---|
| **D7 Self-HITL** | In-app HITL actors for H1/H2/H3/H7/H9 = **same operating user** (F6). **No** in-app Approver / boss queue / accept-for-forward |
| **D8 Assist→export** | Solution ends when deliverable is **exported** from the workbench. How company uses the file afterwards = **out of solution** |
| **D9 Paper outside** | Officer / paper approval / plant filing = **outside KWB** (H12). Not drawn as in-app HITL |
| **D10 Admin gates** | H4/H5/H6/H8 = **Admin** |
| **D11 Admin = IT platform** | Admin has **application/IT control** (cards, allowlists, USB stage, org templates, monitor config). **Not** content HITL for workers. **Cannot** break Never, write plant, proxy H1/H2/H3/H7/H9, enable public `/v1` or pull. Sparse assignment + audit. |

---

## 4.3 Adversarial verify (2026-09-19)

See `../wp/WP-05/WP-05_REV2_REDTEAM.md`.  
**Verdict:** **GO — direction right** with Admin fence + no SoD overclaim.  
**DM answers 1–4:** accepted under that verify.

## 5. Stale accept & material change (core mechanism)

### 5.1 Binding

Each hard-gate accept records: `person_id`, `role_class` (worker|admin), `gate_id`, `artefact_id`, `artefact_version` (content fingerprint), timestamp.

### 5.2 Material change (invalidates accept)

| Material | Examples |
|---|---|
| **Yes** | OCR/extract text or region corrections; **new extract run**; findings fields; DRAFT body/tables/substantive fields; code artefact source; export package membership/bytes; agent/tool rewrite of any of the above |
| **No** | Monitor refresh; routing/egress log append; grant TTL; UI layout; unread citation skim; in-place PDF **preview** without download |

Edits may be **batched** into a new `artefact_version` (debounce) so the user is not gated per keystroke (**A1**).

### 5.3 Effects when stale

- Own-work “accepted DRAFT” flag cleared.  
- **H3 export leave denied** until upstream gates fresh (H1 if extract-based; H2 for note; H9 for code package).  
- Desk shows **needs re-check** (same user) — **not** an Approver queue.

---

## 6. HITL map (rev 2.0)

| ID | Moment | Strength | Actor (in-app) | Must-work? |
|---|---|---|---|---|
| **H1** | OCR / extract verify | Hard | **Same user** (knowledge worker) | **Yes** — hard-block (D2) |
| **H2** | Own DRAFT self-check accept/edit/reject | Hard | **Same user** | **Yes** — re-required after editorial (D4). **Not** plant approval |
| **H3** | **Export leave** (docx/PDF/zip off KWB) | Hard | **Same user** | **Yes** — blocked if H1/H2/H9 stale |
| **H4** | Write to **org** shelves (templates, shared skills) | Hard | **Admin** | Principle **yes** |
| **H4b** | Task workspace DRAFT **edit** | None as edit | Same user | Edit free; **triggers H2 stale** |
| **H5** | Local plugin/MCP **install** to allowlist | Hard | **Admin** | Ambition UX; Never WAN self-install |
| **H6** | Personal skill → org skill | Hard | **Admin** | Ambition UX; Never auto |
| **H7** | Cite / gap / policy contradiction review | Hard | **Same user**; unresolved → **outside** escalate (paper/officer) | **Yes** (MOCK OK) |
| **H8** | High-class grant expand | Hard | **Admin** (in-app); org policy may also require **outside** paper | Ambition UX |
| **H9** | Accept/reject **sandbox / code outcome** as decision | Hard | **Same user** | **Yes** — machine pass ≠ decision (D5) |
| **H10** | Model routing | None + visible log | — | Log must-work |
| **H11** | Retrieve under active grant | None | — | WP-04 |
| **H12** | File into plant / officer paper approval | **Outside KWB** | Human org process | KWB **Never** auto-files; **no in-app Approver** |

**Role-correct accept (M9 rev 2):** Hard-gate accept counts only if actor matches gate (H1/H2/H3/H7/H9 = operating worker; H4/H5/H6/H8 = Admin). Wrong-role click = **invalid** (audit denied).  
**Admin ≠ worker HITL:** Admin **must not** pass H1/H2/H3/H7/H9 for another user.  
**Removed:** in-app Approver role for H2/H3; dual-role “label as Approver” demo for export.

### Admin-as-IT scope (D11)

| Admin may | Admin must not |
|---|---|
| Cards, MCP/skill allowlist, org templates, USB intake ack, Audience A config, H8 expand UX | Override Never; plant write; proxy worker HITL; public `/v1`; registry pull; silent un-audited break-glass |

---

## 7. Inspection spine (must-work)

1. Attach scan (user-attached grant).  
2. Extract → **H1** (hard-block). New extract version ⇒ H1 + downstream H2/H3 stale.  
3. Optional KB under grant + after **fresh** H1.  
4. Cite-or-abstain + **H7** when cites/gaps shown.  
5. Generate **DRAFT** `.docx` (DRAFT badge).  
6. User may edit (**H4b**) → **H2 stale**.  
7. **H2** same-user self-check (fresh version).  
8. **H3** export leave if taking soft copy off the box.  
9. Plant / officer paper = **outside** (**H12**).  
10. Material change after H2 → stale → re-H2 (and re-H3 if new export).

Label: **DRAFT / AI-assisted — own-work verification required — not a plant record**.

---

## 8. Code / sandbox spine (must-work)

1. Generate code under grant.  
2. Sandbox **run** = machine check (may fail-closed).  
3. **H9** same-user accept/reject of outcome.  
4. Export of code package = **H3**.  
5. Material code edit after H9 → stale → re-H9.  
6. Sandbox-red / rejected H9 ⇒ **export leave denied** (G10-shaped).

**Never:** sandbox pass ⇒ plant-safe / statutory / FFS decision.

---

## 9. Weak spots (must not bypass)

| ID | Bypass | Contract |
|---|---|---|
| W1 | Word-only HITL | Full H-map enforced |
| W2 | Export before fresh H2 | H3 checks upstream freshness |
| W3 | Copy `.md` to org shelf | Only H6 (Admin) |
| W4 | Sandbox green as approval | H9 required |
| W5 | In-app forward-accept / boss queue | **Forbidden** (D7) |
| W6 | Auto-resolve contradiction to user | H7 surface; escalate **outside** if needed |
| W7 | Grant expand = export right | Separate |
| W8 | Chat LGTM | Explicit control + audit |
| W9 | Keep using old accept after edit | Stale mechanism (§5) |
| W10 | Agent silent rewrite after accept | Tool/agent edit = material change |
| W11 | Treat H2 as plant approval | H2 = own-work only; plant = H12 outside |

---

## 10. Must / ambition / deferred / never

### Must-work

1. Gate vocabulary (§3).  
2. Stale accept + material-change (§5).  
3. H1 hard-block; H2 self-check; H3 export leave; H7 MOCK; H9 human decision.  
4. Self-HITL only in-app (D7).  
5. Human owns decisions (same user).  
6. Audit: accept / reject / stale / re-check (WP-17 shape).  
7. KWB never safety/FFS/statutory/legal/commercial **decider**.  
8. Assist→export product boundary (D8).

### Org-ambition (outside or Admin — not in-app Approver)

- Paper / officer approval workflows (**outside**).  
- H5/H6/H8 full Admin UX.  
- Rich H7 resolver (WP-22).  

### Deferred

- Legal e-sign / wet signature.  
- Replacing plant DMS approval workflows.  
- In-app multi-user approval queues.

### Never

- Auto-promote DRAFT → plant record.  
- **In-app Approver / accept-for-forward.**  
- Auto-file SoR.  
- Skip H1 then treat OCR as verified plant truth.  
- Use stale accept for export.  
- Machine/sandbox/model as decision-maker.  
- WAN plugin self-install.  
- Human instruction overrides Never (WP-00).  
- Per-keystroke gate spam (use version batching).

---

## 11. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Interrupt/resume **pattern** at hard gates | Checkpoint until human acts |
| **Adopt** | Confirm-before-export **behaviour** | H3 export leave |
| **Adopt** | Approval binds to **revision** | D1/D4 |
| **Add** | Self-HITL actor map; stale-accept; H9; H7 must-work; D7–D10 | KWB 2026-09-19 |
| **Refuse** | In-app Approver queue; chat Approver; ISO/e-sign cosplay; LangGraph-as-product |

---

## 12. Boundary vs later WPs

| Topic | WP-05 | Later |
|---|---|---|
| Contradiction resolution rules | Gate H7 exists | **WP-22** |
| OCR engines / scan path | H1 required | **WP-03** |
| Untrusted OCR/MCP text | Before trust | **WP-23** |
| Plugin host install | H5 Admin | **WP-08** |
| Tool write details | H4 / H4b | **WP-07** |
| Audit retention | Events required | **WP-17** |
| Desk UI for gates | State required | Demo desk / **WP-13** |

---

## 13. Demo acceptance (aligned A→J)

1. Extract → cannot treat as truth / clean DRAFT path without **H1**.  
2. **H2** self-check → edit body → **stale** → **H3 export denied** until re-H2.  
3. Re-H2 → **H3** export leave succeeds.  
4. Sandbox green without **H9** ≠ accepted code decision; sandbox-red blocks export.  
5. H7 MOCK when cites/gaps/contradiction.  
6. **No** in-app Approver step on the walk.  
7. Leave-with: Word DRAFT + audit (+ sandbox proof if used).

---

## 14. Explicitly not locked

Exact debounce ms, fingerprint algorithm brand, desk wireframes, which Admin UX ships in SIH demo vs ambition.

---

## 15. Traceability

| Source | Where absorbed |
|---|---|
| DM 2026-09-18 D1–D6 | §4.1, §5, §6 (mechanisms kept; actors updated) |
| Flow F1–F7 / F6 self-HITL | §4.2 D7–D9, §6, §13 |
| Product assist→export | §1, D8, H3 |
| Org/demo diagrams 2026-09-19 | §2, §10 Never |

---

## 16. DM discuss checklist (rev 2.0)

| # | Item | Status |
|---|---|---|
| 1 | Self-HITL for H1/H2/H3/H7/H9 | **Yes** — red-team PASS with plant-SoD honesty label |
| 2 | H3 = export leave; paper Approver outside | **Yes** — PASS |
| 3 | Admin = IT application control (D11 fence) | **Yes** — PASS with must-not list |
| 4 | Stale / version re-check | **Yes** — red-team PASS keep |
| 5 | Mark **FROZEN rev 2.0**? | **ACCEPTED / FROZEN 2026-09-19** |
| 6 | Next: reopen **WP-01** (Approver = org paper only) | **Next** |

---

## 17. Changelog

| Rev | Note |
|---|---|
| **1.0** | Initial freeze — Approver on H2/H3 |
| **1.1** | M9 role-correct; re-OCR stale |
| **2.0** | **FROZEN** DM accept 2026-09-19: self-HITL; export leave; paper Approver outside; Admin-as-IT (D11); stale kept; red-team GO |
