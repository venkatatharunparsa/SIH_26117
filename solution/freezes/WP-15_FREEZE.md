# WP-15 Personal `.md` harness — FREEZE

**Date:** 2026-09-18  
**Status:** **FROZEN** (rev **1.0**). Binding with WP-00 / WP-01 / WP-04 / WP-05 / WP-07 / WP-23.  
**Depends on:** those freezes (must not contradict).  
**Inputs:** `WP-15_ARCHITECT_PERSPECTIVE.md`, `WP-15_REDTEAM.md`, **DM 2026-09-18** (freeform `.md`; user-only; full H6 accept; pin/tag load; export/promote scan only; Admin hold).  
**Findings SoT:** `WP-15_REDTEAM.md`  
**Verify SoT:** `WP-15_FREEZE_VERIFY.md`  
**Product:** **KWB**

**Note:** **Not** an Official PS requirement — User/host capability. Do not claim PS mandated “self-learning.”

---

## 1. One-sentence contract

KWB’s “self-learning” is a **personal `.md` harness**: the user writes **freeform personal notes** on a **personal shelf**, loads them only when **pinned/tag-matched**, always as **T3**; **H6** promotes to org; **Admin hold** can retain on promote/export; **no** agent auto-write, **no** weight training, **no** internet-compat skills.

---

## 2. Limits

| True | False / refuse |
|---|---|
| Workflow memory in markdown | Plant weight fine-tuning |
| Freeform note must-work | Note grants tools |
| User-only authorship (must) | Agent silent writes to personal shelf |
| Pin/tag gated load | Load all personal notes every task |
| Secret heuristics on H3 + H6 promote | Continuous personal DLP must-work |
| User feature | Official PS “self-learning” clause |

---

## 3. Closed decisions (DM)

| ID | Decision |
|---|---|
| **D1** | Demo must-work = **freeform personal `.md`**; personal `SKILL.md` = ambition |
| **D2** | **User-only** create/edit on personal shelf |
| **D3** | Demo includes **full H6 promote accept** (role-correct Approver/Admin) |
| **D4** | Load personal content only if **pinned** and/or **tags ∩ job** |
| **D5** | No extra always-on secret scanner; invoke **light heuristics on H3 and on H6 promote** |
| **D6** | **Admin hold** blocks user delete when pending H6, in export package, or Admin hold flag |

---

## 4. Shelf & trust

| Rule | Must |
|---|---|
| Location | Personal area ≠ controlled SOP store |
| Artefact class | **Personal** (WP-00/01) |
| Trust | Always **T3** delimited (WP-23) |
| Tools | Freeform notes = **no** `allowed-tools` authority |
| Internet | Refuse load if skill metadata requires WAN / `compatibility: internet` |
| Grant | Personal text ≠ standing org ACL (WP-04) |

---

## 5. Lifecycle

```
User edits personal .md (pin/tags optional)
  → later task: load only if pinned ∨ tag-matched
  → pack as T3 (WP-21/23)
  → propose H6 → Approver/Admin accept → copy to org shelf (still T3)
  → secret heuristic before promote write / before H3 if exported
  → Admin hold may retain
```

---

## 6. Must / ambition / deferred / never

### Must-work

1. Personal shelf + freeform `.md` create/edit (user-only).  
2. Pin/tag load gate; T3 load.  
3. Full H6 accept demo path.  
4. Block internet-compat skills; no weight training; no auto-promote.  
5. Secret heuristics on H3 + H6 promote.  
6. Admin hold on promote/export/pending H6.  
7. PS honesty (not Official mandate).

### Org-ambition

- Personal SKILL.md packs; agent-proposed drafts with confirm; personal search; bulk H6.

### Deferred

- Cross-device sync; ML habit mining.

### Never

- Unsupervised training on plant data.  
- Auto-promote.  
- Agent unattended write to personal shelf.  
- Personal `.md` as grant/ACL.  
- WAN Skills Hub.  
- Store personal as controlled SOP.

---

## 7. Adopt / add / refuse

| | What | Why |
|---|---|---|
| **Adopt** | Agent Skills layout for ambition packs | Spec |
| **Add** | Freeform harness; pin/tag; H6 demo; hold | DM |
| **Refuse** | Fine-tune-as-learning; silent agent shelf writes |

---

## 8. Demo acceptance

1. User creates personal `.md`, pins it, runs task → note appears as T3 (not system).  
2. Unpinned/unmatched → not loaded.  
3. H6 accept moves/copies to org shelf with Approver/Admin role.  
4. Internet-compat skill refused.  
5. No model training step.  
6. Hold blocks delete while pending H6.

---

## 9. Next

**WP-18** — Fail-closed + eval suite.

---

## 10. Changelog

| Rev | Note |
|---|---|
| **1.0** | Freeze after adversarial pin/H6/hold/freeform pass |

**Confidence:** **0.88**
