# Document Templates Overview

Every generated document should carry: document number, revision, date, unit/department, equipment/project/tender reference, prepared/reviewed/approved fields, source list, approval status, controlled-copy marking.

## Common formatting conventions

- A4 portrait for reports; A3 landscape for large tables, P&ID extracts and bid matrices
- Arial or Calibri, 10–11 pt body, 14–16 pt title, 11–12 pt headings
- Margins: 25 mm left, 20 mm right, 20 mm top and bottom
- Header: organisation, unit/department, title, document number, revision, page number
- Footer: classification, controlled/uncontrolled status, issue date, `Page X of Y`
- Tables: `Table 1`, `Table 2`; Figures: `Figure 1`, `Figure 2`
- Decimal sections: `1.0`, `1.1`, `1.2`; actions: `A-01`, `A-02`
- SI units with basis: `°C`, `barg`, `mm`, `kg/h`, `MMTPA`
- Dates: `15-Sep-2026 14:30 IST`
- Revision: Rev. 0 first issue; Rev. 1 or Rev. A later
- Signatures: name, designation, signature or digital approval, date, comments

## Eleven document types documented

1. Inspection recommendation note
2. Technical deviation investigation note
3. Root Cause Analysis report
4. MOC review checklist
5. Technical Bid Evaluation report
6. Shift handover note
7. Monthly maintenance cost variance report
8. Capital-expenditure approval note
9. Daily unit performance report
10. Incident investigation report
11. PPT board-pack / management presentation

## AI generation pipeline

1. User selects document type
2. System applies controlled template (department, numbering, revision, header/footer, approval matrix, classification, required annexures)
3. AI retrieves evidence from authorised sources
4. System builds structured fact sheet (identity, dates, sources, values, units, missing data, conflicts, approval status, confidence)
5. Calculations shown with formula, inputs, units, source, assumptions, validation warnings
6. Draft generated with label "AI-generated draft — technical review required"
7. Document checks: missing sections, placeholders, conflicting numbers, wrong revision, missing citations, open actions without owners, dates in past, approval gaps, unapproved standards, inconsistent tags
8. Human review
9. Approve and publish: final revision, signature record, save to DMS, create linked actions, lock approved version

## Data fields needed for reliable generation

| Field | Examples |
|---|---|
| Organisation | MRPL, unit, department |
| Asset/entity | Equipment tag, tender number, project number, case number |
| Location | Unit, area, plant, site |
| Time | Date, start/end, time zone, reporting period |
| Status | Running, shutdown, open, closed, approved, draft |
| Source | System, document number, revision, page, tag, sample ID |
| Numeric value | Value, unit, basis, quality flag |
| Responsibility | Owner, reviewer, approver |
| Action | Description, due date, priority, verification |
| Confidentiality | Public, internal, restricted, confidential, secret |
| Version | Revision, effective date, superseded date |
| Decision | Requested, recommended, approved, rejected, conditional |
| Evidence confidence | Confirmed, inferred, conflicting, missing |

## Good vs. bad AI-generated documents

Good: uses organisation template, does not invent missing data, clearly marks assumptions, cites original sources, shows revisions, preserves units/time zones, correct approval chain, separates facts from interpretation, includes unresolved questions, generates editable Word/Excel/PPT, preserves data and formula lineage, respects permissions. Board packs start with a decision-oriented executive summary and cite every number in speaker notes.

Bad: invents technical values, mixes current and obsolete drawings, omits revision, produces charts without source tags, converts "not found" into confident statement, hides adverse evidence, recommends a vendor without evaluation, omits HSE/legal concurrence, creates approval-ready document without human review, copies confidential bidder info across workspaces, generates final-looking report with no draft status.
