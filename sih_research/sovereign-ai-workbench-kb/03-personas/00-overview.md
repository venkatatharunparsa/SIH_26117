# Personas Overview

Eight personas use the AI workbench at MRPL-type organisations. Each has a distinct daily workflow, document set, pain points, and trust requirements.

## Persona summary

| # | Persona | Core pain | Primary output | AI willingness |
|---|---|---|---|---|
| 1 | Process engineer | Assembling unit performance data from historian, LIMS, DCS, shift logs | Excel workbook, Word technical note | High if traceable |
| 2 | Inspection engineer | Processing scanned reports, matching historical readings | Word recommendation, Excel thickness chart | High for extraction; cautious for safety |
| 3 | Maintenance engineer | Scattered failure history across EAM, email, shared drives | Word RCA, Excel timeline | High if it saves time |
| 4 | HSE officer | Chasing documents across systems for MOC/HAZOP/permit | Word checklist, action register | Moderate; cautious for safety decisions |
| 5 | Procurement officer | Building compliance matrices from hundreds of pages | Excel matrix, Word recommendation | High for extraction; cautious on confidentiality |
| 6 | Shift engineer | Manually copying from five systems into handover note | Word handover, event timeline | High during routine; cautious in emergencies |
| 7 | Finance officer | Reconciling ERP, EAM, procurement and invoices | Excel variance, Word/PPT report | High for reconciliation |
| 8 | Senior manager | Reviewing long approval notes and annexures | Word decision brief, risk list | High if concise and source-backed |

## Common patterns

All eight personas share:

- Fragmented information across ERP, EAM, historian, DCS, LIMS, email, shared drives, portals and paper
- Entity-resolution failures (P-204A = Pump 204A = 204A)
- Version confusion (which P&ID is current?)
- Manual copying between systems
- Formatting Word, Excel and PowerPoint outputs
- Approval bottlenecks
- Weak audit reconstruction

## Common trust requirements

- Source citations to document, page, revision, equipment tag
- Clear uncertainty ("not found," "conflicting sources")
- Revision awareness ("Rev C — superseded by Rev D")
- Read-only default (no writes to DCS, SIS, EAM, ERP)
- Human approval gates
- Permission-preserving retrieval
- Complete audit trail
- Reproducible calculations
- Industrial vocabulary and tag awareness
- Offline operation
- Fast responses
- Useful exports

## Risk-level guardrails

| Risk level | Example | AI role |
|---|---|---|
| Low | Find a procedure or previous report | Direct answer with citation |
| Medium | Draft a daily report or comparison | Draft with review |
| High | Interpret equipment degradation or process deviation | Advisory analysis with engineer approval |
| Critical | Permit approval, isolation, DCS action, emergency decision | No autonomous action; human-controlled workflow only |
