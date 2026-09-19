# WP-00 freeze red-team audit (rev 1.1)

**Date:** 2026-09-17  
**Target:** `WP-00_FREEZE.md` rev 1.0 → **1.1**  
**Result:** Freeze updated. Q1–Q7 unchanged. See freeze **§17 Changelog**.

## Verdict

Rev 1.0 was a valid product spine and correctly captured your closed questions. It was **not** complete as the single source of truth for everything agreed in the org-design discussion. Rev 1.1 closes those gaps without changing must-work acceptance or Never fundamentals.

## Coverage check (discussion → freeze 1.1)

| Topic | In 1.1? |
|---|---|
| Software ≠ weights; model reference; hardware adopt | Yes |
| Must / ambition / deferred / never | Yes |
| Assist = draft + HITL; human ultimate decider | Yes |
| Templates admin + freestyle | Yes |
| docx must; PDF when possible | Yes (+ PDF fail rule) |
| Fully offline; no internet | Yes (+ offline media path) |
| Read-only existing systems | Yes (+ workspace vs plant write) |
| Three-level citation | Yes (+ NOT FOUND) |
| Calc org-only; Excel/PPT deferred | Yes |
| Local MCP; skill library; role skills | Yes (scoped load) |
| OCR → human → KB | Yes |
| Classifier placeholder | Yes |
| Task grants + revoke | **Added** |
| Specialist agents | **Added** |
| Lineage (not graph DB) | **Added** |
| Personal `.md` harness | **Added** |
| Operator + sovereign monitors | **Added** |
| Gateway valid requests / data-to-pass | **Added** |
| Artefact classes | **Added** |
| Fail closed must-work | **Added** |

## No change required to application direction

Still the same application: offline org knowledge workbench, draft artefacts, HITL, pluggable models/plugins/skills, read-only plant connectors. Red-team **filled omissions**, did not reverse the product.
