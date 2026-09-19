# WP-05 — Architect perspective (not frozen)

**Date:** 2026-09-18  
**Depends on:** WP-00 / WP-01 / WP-02 / WP-04 freezes (rev 1.1 / 1.0 as applicable)  
**Status:** **SUPERSEDED by `WP-05_FREEZE.md` rev 1.0.** Kept for history. Red-team: `WP-05_REDTEAM.md`.  
**Job of WP-05:** Map **where a human must act** before KWB may proceed — hard gates vs review-only vs none — so HITL is not only “approve the Word file.” Cover export, plugin install, org-skill promotion, file **write**, policy↔user contradiction, OCR verify, DRAFT accept, and grant-expand touchpoints already named in WP-04.

**Sources:** Official Background (approval notes; human owns decisions); WP-00 human–AI role + OCR→human→KB + Never; WP-01 draft/OCR/skill promotion; WP-04 export≠grant, self-approve ban; `DESIGN_REPO_MAP_v1.md` WP-05; User: HITL forever; KWB never safety/legal/financial/statutory decider.

---

## One sentence (proposed)

KWB may **draft, propose, and check**; **humans** own **gates** that change trust (OCR truth, DRAFT→record-facing, export, org skill/plugin install, high grant expand, policy contradictions). Automated sandbox/citation checks are **not** substitutes for those gates.

---

## 1. Three gate strengths (do not collapse)

| Strength | Meaning | Blocks progress? | Example |
|---|---|---|---|
| **Hard gate** | Explicit human accept / reject / correct before next step | **Yes** | OCR extract confirm; DRAFT accept for record-facing; export download; plugin install; org-skill promote |
| **Review-only** | Human should look; system may continue with **visible warning** if skipped (org policy may promote to hard) | Soft | Optional citation pack skim inside an already-granted task |
| **None (machine OK)** | No human required for that step | — | Model routing log write; sandbox run *inside* jail; retrieve under active grant |
| **Machine check ≠ HITL** | Automated pass/fail (sandbox, schema, citation presence) | May fail-closed **without** being a human gate | Sandbox fail → no “verified code” claim |

**Never confuse:** grant allow (WP-04) ≠ human gate (WP-05). A grant can open retrieve; **export** still needs HITL.

---

## 2. Who sits at which gate

| Role | Typical gates | Must not |
|---|---|---|
| **Knowledge worker** | OCR correct-vs-assumed; edit DRAFT; request grant expand; start/abort task | Self-approve **high-class** grant ceiling (WP-04); install unbounded plugins; auto-file SoR |
| **Approver** | Accept/reject **record-facing** DRAFT; deny grant expand (ambition UX); promote personal→org skill (with/or Admin) | Be replaced by a bot; bypass Never |
| **Admin** | Plugin/skill **allowlist install**; org templates; offline media intake; Audience A path; may promote org skill | Silent engineering Approver by default |
| **Dual-role demo** | One human labelled worker+Approver OK (WP-01) | Org paper still separates roles |

---

## 3. HITL map — proposed freeze table

| ID | Moment | Strength | Actor | Must-work? | Notes |
|---|---|---|---|---|---|
| **H1** | **OCR / extract verify** (correct vs assumed) | Hard | Knowledge worker | **Yes** | WP-00 spine; before company KB treat-as-truth |
| **H2** | **DRAFT Word accept/reject** (record-facing / approval-note path) | Hard | Approver (dual-role OK in demo) | **Yes** | Label: DRAFT / AI-assisted — requires human verification |
| **H3** | **Export / download** out of KWB (docx/PDF/zip) | Hard | Approver or policy-designated; worker may request | **Yes** for any off-workbench copy | WP-04 Q5; classification inherits |
| **H4** | **File write** beyond routine DRAFT workspace update (e.g. overwrite shared org template area, bulk write) | Hard | Approver and/or Admin | Principle **yes**; detail vs WP-07 | Workspace DRAFT edit by worker = **not** this gate |
| **H5** | **Local plugin / MCP install** onto allowlist | Hard | **Admin** | Ambition for full UX; **must** state Never: user self-install from WAN | Offline media only (WP-00) |
| **H6** | **Personal skill → org skill** promotion | Hard | Approver and/or Admin | Ambition for demo; **Never** auto-promote | WP-01 |
| **H7** | **Policy vs user contradiction** | Hard (choose / escalate) | Knowledge worker + Approver if unresolved | Ambition strong; must-work may MOCK one contradiction banner | Detail assembly WP-22; **gate** freezes here |
| **H8** | **High-class grant expand** (ceiling / bidder corpus) | Hard | Approver (not self for high class) | Ambition UX; principle frozen WP-04 | Not a substitute for H2/H3 |
| **H9** | **Sandbox “verified” claim** toward deliverable | Machine check + optional review | Worker sees pass/fail | Machine **must**; human review-only unless claiming safety | Never: sandbox pass ⇒ plant-safe |
| **H10** | **Routing / model card choice** | None (machine) + Audience B visible | — | Log must-work | Human may abort task; not pick model as proof |
| **H11** | **Retrieve under active grant** | None | — | Grant is WP-04 | Not HITL |
| **H12** | **Filing into plant DMS/EAM** | Hard + **outside KWB write API** | Human org process | KWB **Never** auto-files | Human may export then file elsewhere |

---

## 4. Inspection spine (must-work path)

Ordered human/machine stops for Expected Solution:

1. Attach scan (grant: user-attached) — low friction (WP-04).  
2. OCR/vision extract → **H1 hard gate** (worker confirms).  
3. Optional KB/policy retrieve only if grant — not required for bare demo.  
4. Generate findings + **DRAFT `.docx`** (+ PDF if possible).  
5. Worker may edit DRAFT content (workspace write — not H4).  
6. **H2 hard gate** — Approver (or labelled dual-role) accept/reject as record-facing DRAFT.  
7. **H3** if downloading/exporting off the workbench.  
8. Plant filing = human outside KWB (**H12**).

Fail-closed: skip H1 → must not treat extract as plant truth / must not silently KB-index as verified.

---

## 5. Weak spots (adversarial — design so they cannot bypass)

| Weak spot | Bypass if… | Contract direction |
|---|---|---|
| **W1** | HITL = only Word button | Plugins, `.md`, export, OCR skip still leak |
| **W2** | Worker exports before H2 | Export **H3** independent of draft accept |
| **W3** | Personal `.md` promoted by copy-paste to org shelf | Only **H6** path promotes; raw copy ≠ org skill |
| **W4** | “Sandbox passed” used as approval | H9 ≠ H2; never safety decision |
| **W5** | Dual-role demo hides Approver forever | Org paper keeps Approver; demo labelled |
| **W6** | Contradiction auto-resolved to user claim | H7 must surface; default prefer **policy/file** or escalate — detail WP-22 |
| **W7** | Grant expand treated as export permission | WP-04 + H3 separate |
| **W8** | Chat “LGTM” without gate UI | Hard gates need **explicit** accept control + audit event (WP-17) |

---

## 6. What is *not* a human gate

- Creating/updating files **inside** the task’s KWB workspace DRAFT area (worker editing).  
- Running sandbox tests.  
- Writing routing / egress / grant logs.  
- Retrieve/MCP **use** already allowed by active grant (still audited).  
- Showing Audience A/B monitors.

---

## 7. Must / ambition / deferred / never (proposed)

### Must-work

1. Gate strength vocabulary: hard / review-only / none / machine-check.  
2. **H1** OCR verify on inspection spine.  
3. **H2** DRAFT accept/reject with visible DRAFT label.  
4. **H3** export/download hard gate when leaving KWB.  
5. Explicit: HITL ≠ Word-only (W1).  
6. KWB never decides safety/FFS/statutory/legal/commercial outcomes.  
7. Dual-role demo allowed if labelled; org keeps Approver.  
8. Machine checks may fail-closed without being HITL.

### Org-ambition

- Full Approver queue UX (multi-user).  
- H5 plugin install wizard; H6 skill promotion UI.  
- H7 contradiction resolver UI (with WP-22).  
- H8 grant-expand Approver UX (WP-04).  
- Review-only→hard promotions per company policy pack.

### Deferred

- Wet-signature / legal e-sign integration.  
- Plant DMS approval workflow replacement.  
- Automatic escalation SLAs / paging.

### Never

- Auto-promote DRAFT → plant **record**.  
- Auto-promote personal → org skill.  
- Auto-file SoR.  
- Skip H1 then treat OCR as verified plant truth.  
- Human instruction inside KWB overrides Never (WP-00).  
- Sandbox or model “approval” as statutory/safety decision.  
- WAN self-install of plugins as HITL “yes.”  
- Skill restrictions alone as security (repo map refuse).

---

## 8. Adopt / add / refuse (patterns only)

| | |
|---|---|
| **Adopt** | LangGraph-style **interrupt / resume** *pattern* (checkpoint at hard gate) |
| **Adopt** | Hermes-like: approve before **sensitive** file ops (*behaviour*) |
| **Adopt** | GBrain/Atlas: agent **proposes**, human **promotes** to shared/canonical |
| **Add** | Full gate table H1–H12; weak-spot list; export≠draft≠grant; OCR before KB |
| **Refuse** | DeerFlow-style “skill restrictions = security”; auto-merge to plant SOP; chatbot thumbs-up as Approver |

---

## 9. Boundary vs later WPs

| Topic | WP-05 | Later |
|---|---|---|
| Contradiction *policy content* | Gate exists (H7) | **WP-22** resolution rules |
| OCR engines / fail-closed scan | H1 required | **WP-03** path |
| Untrusted OCR text | Gate before trust | **WP-23** |
| Plugin host mechanics | H5 gate | **WP-08** |
| Tool write semantics | H4 principle | **WP-07** |
| Audit of accept/reject | Event required | **WP-17** |
| HITL queue on monitor | State visible | **WP-13** |

---

## 10. Open questions for decision maker

1. **H3 Export:** must Approver always click export, or may Knowledge worker export **after** H2 accept under same dual-role demo?  
2. **H1 skip:** fail-closed only for KB-index, or also block DRAFT generation until OCR confirmed? (Recommend: **block treating as verified**; allow DRAFT only with banner “OCR unverified” **or** hard-block — pick one.)  
3. **H7 Contradiction:** must-work shows a MOCK banner, or ambition-only until WP-22?  
4. **H4 File write:** is worker DRAFT edit clearly **out** of H4 (recommended), with H4 only for org-shelf / template-store writes?  
5. **Sandbox path:** any hard Approver gate on code deliverable, or machine pass + worker ack enough for must-work?  
6. **PDF export:** same H3 as docx, or PDF generation alone without download = no H3?

---

## 11. Next after your decisions

**Done.** Frozen as `WP-05_FREEZE.md` rev 1.0. Next: **WP-03**.
