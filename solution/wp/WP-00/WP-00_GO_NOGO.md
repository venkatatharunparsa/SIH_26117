# WP-00 go / no-go readiness

**Date:** 2026-09-17  
**Contract:** `WP-00_FREEZE.md` rev **1.1**  
**Question:** Is WP-00 complete enough to decide and move to WP-01?

---

## Decision

| | |
|---|---|
| **WP-00 complete as a product contract?** | **Yes** |
| **Ready to move to WP-01?** | **Yes** |
| **Confidence (product-contract completeness)** | **0.88** |
| **Confidence (prototype already proven)** | **0.00** — no code; not claimed |
| **Must reopen WP-00 before WP-01?** | **No** — residual items belong in later WPs |

---

## Why WP-00 is done

A WP-00 freeze must answer: what we are, what must work, what is org ambition, what is deferred, what is never, and what is parked. Rev 1.1 does that.

| Checkpoint | Status |
|---|---|
| Expected Solution mapped to must-work | Pass |
| Description/Background in ambition or deferred | Pass |
| Q1–Q7 closed | Pass |
| Hardware vs software / model reference | Pass |
| Assist vs decide / HITL / DRAFT | Pass |
| Offline / read-only plant / Never | Pass |
| Discussed promotions present (MCP, skills, grants, lineage, monitors, …) | Pass (1.1) |
| Stack not falsely locked | Pass |
| Red-team of freeze executed | Pass |

Nothing material from the WP-00 discussion is still **undefined at contract level**. Detail work remains — that is what WP-01+ are for.

---

## Weak-probability aspects (not blockers)

These can still hurt **later** if ignored. They do **not** require reopening WP-00 now.

| ID | Weak aspect | P(hurts later if ignored) | Why not a WP-00 blocker | Owns |
|---|---|---|---|---|
| W1 | **OCR HITL every scan** vs **low friction** | Medium | Principle stated; tension is UX design | WP-05 / WP-03 |
| W2 | **Grant revoke of copies** (chat/`.md`) hard to enforce | Medium–High | Contract admits “not complete security” | WP-04 |
| W3 | **Classifier** rules vs model undecided | Medium | Explicitly parked | WP-04 |
| W4 | **Freestyle templates** may look like plant records | Medium | Policy needed, not product identity | WP-01 / WP-05 |
| W5 | **“Models at once”** misread as many weights in VRAM | Low–Medium | Catalog + load policy is WP-10/24 | WP-10 / WP-24 |
| W6 | **Three-source citation** pulled into must-work too early | Medium | Ambition vs demo; freeze separates | WP-11 / WP-22 / prototype overlay |
| W7 | **Local MCP** still dangerous if allowlist weak | Medium | Never + offline media stated | WP-08 |
| W8 | **No MRPL template/IdP truth** yet | Medium | Marked unknown; MOCK OK | WP-01 / WP-02 |
| W9 | **Spreadsheet in Description** vs Excel deferred | Low | Jury answer exists in deferred table | Demo script later |
| W10 | **PDF when possible** soft | Low | Docx rule explicit | Already in §5 |

No additional **contract holes** found that require editing the freeze before WP-01.

---

## What “0.88” means

- **~0.12 residual** = implementation and later-WP risk (W1–W8), not “we don’t know what KWB is.”  
- If new Official PS text appears, or you reverse a Q1–Q7 answer, reopen WP-00.  
- Do **not** treat 0.88 as confidence the prototype will pass SIH — that confidence starts after build/eval.

---

## Recommendation

**Move to WP-01** (users, jobs, artefacts) under `WP-00_FREEZE.md` rev 1.1. Do not reopen WP-00 unless a W-item forces a **product identity** change (unlikely; they are design depth).
