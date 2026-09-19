# AI Document Generation Pipeline

This document specifies how the workbench generates each document type with evidence lineage and human approval.

## Step 1: Select document type

The user chooses: inspection recommendation, deviation note, RCA, MOC, TBE, shift handover, cost variance, CAPEX approval note, daily performance report, or incident report.

## Step 2: Select controlled template

The system applies: department template, document-numbering rules, revision format, header/footer, approval matrix, confidentiality classification, required annexures.

Templates are loaded from the customer's existing document repository. The AI must not invent a visual style.

## Step 3: Retrieve evidence

The AI searches only authorised sources:

- ERP
- EAM
- Historian
- DCS event data
- LIMS
- DMS
- Procurement portal
- HSE/MOC system
- Email and shared drives (permission-filtered)
- OCR repository

All retrieval respects the classification-aware policy engine.

## Step 4: Build structured fact sheet

Before writing prose, the system produces: equipment/unit/project identity, dates and time zone, source records, numeric values, units, missing data, conflicts, approval status, evidence confidence.

This fact sheet is shown to the user for validation before drafting.

## Step 5: Run calculations

Calculations show formula, inputs, units, source, assumptions, result, and validation warning. Calculations run in a sandbox (Python/R) rather than via the language model, to ensure reproducibility.

## Step 6: Generate draft

Output is labelled:

> AI-generated draft — technical review required.

Draft includes source citations to document, page, revision, equipment tag.

## Step 7: Run document checks

The system checks: missing mandatory sections, unresolved placeholders, conflicting numbers, wrong revision, missing source citations, open actions without owners, dates in the past, approval gaps, unapproved standards, inconsistent equipment tags.

## Step 8: Human review

The responsible professional reviews: facts, calculations, interpretation, risk, action owners, confidentiality, distribution list.

## Step 9: Approve and publish

Only then: assign final revision, apply digital signature or approval record, save to the document repository, create linked actions in EAM/HSE/procurement, lock approved version.

## Data fields required

| Common field | Examples |
|---|---|
| Organisation | MRPL, unit, department |
| Asset/entity | Equipment tag, tender number, project number, case number |
| Location | Unit, area, plant, site |
| Time | Date, start/end, time zone, reporting period |
| Status | Running, shutdown, open, closed, approved, draft |
| Source | System, document number, revision, page, tag, sample ID |
| Numeric value | Value, unit, basis and quality flag |
| Responsibility | Owner, reviewer, approver |
| Action | Description, due date, priority, verification |
| Confidentiality | Public, internal, restricted, confidential, secret |
| Version | Revision, effective date, superseded date |
| Decision | Requested, recommended, approved, rejected, conditional |
| Evidence confidence | Confirmed, inferred, conflicting, missing |

## Priority templates for first product version

1. Daily unit-performance report
2. Shift handover note
3. Inspection recommendation note
4. RCA report
5. Technical deviation investigation note
6. MOC review pack
7. Technical bid evaluation matrix
8. Capital-expenditure approval note
9. Monthly maintenance-cost variance report
10. Incident investigation report

## The core capability

The highest-value initial capability is not merely document generation. It is **evidence-backed document generation**:

- Every number links to its source
- Every chart is reproducible
- Every action has an owner and date
- Every approval is explicit
- Every draft is distinguishable from an approved record
- Every confidential document remains within the authorised security boundary
