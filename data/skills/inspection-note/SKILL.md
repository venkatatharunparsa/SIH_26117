---
name: inspection-note
description: >
  Rules for drafting offline inspection recommendation notes (Word DRAFT).
task_families: [inspection]
license: MIT
---

# Inspection note skill

## Must

- Decision / recommendation first
- Asset ID and location when present in extract
- Findings grounded in Confirm extract only
- Citations from retrieve — cite-or-abstain (NOT FOUND if empty)
- Label every deliverable **DRAFT — not a plant record**

## Must not

- Invent thickness, codes, or corrosion rates
- Claim CERT, Approver, or in-app forward-accept
- Strip adverse evidence

## Agent steps

- ingest | Ingest the scan, PDF, or note | OCR, PDF text, or vision into an extract
- confirm_extract | Confirm the extract | Operator checks facts before anything is drafted (H1)
- retrieve | Retrieve local SOP cites | Grant-scoped knowledge base only
- review_cites | Review citations | Cite what was retrieved, or abstain (H7)
- draft_word | Draft the Word note | Pack → Gateway polish → .docx DRAFT
- self_check | Self-check the draft | Stale-artefact gate before leave (H2)
- export | Export a leave pack | Soft copy for an Approver outside the app

## Word path

Confirm extract → Review citations → LLM polish via Gateway → Word `.docx` → Self-check → Export leave.
