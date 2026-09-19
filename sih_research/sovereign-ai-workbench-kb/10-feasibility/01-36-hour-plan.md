# 36-Hour Build Plan

## Hours 0–4: Scope and data

- Choose one workflow: technical deviation or RCA (or the exact PS example: scanned inspection report → approval note)
- Prepare 20–50 synthetic or public documents
- Define metadata and classification
- Define expected output

## Hours 4–10: Local stack

- Install local model runtime
- Install embedding model
- Configure vector/full-text search
- Disable external network access
- Create local user authentication

## Hours 10–18: Ingestion and retrieval

- PDF/DOCX/XLSX parser
- OCR for selected scans
- Chunking and metadata
- Source citations
- Revision and document-number fields

## Hours 18–26: Workflow agent

- Input form
- Evidence retrieval
- Structured fact sheet
- Calculation function
- Draft Word output
- Excel evidence workbook

## Hours 26–32: UI and controls

- Chat/search interface
- Document view
- Source drill-down
- Classification badge
- Human-review checkbox
- Audit event display

## Hours 32–36: Testing and demo

- Deliberately insert conflicting revisions
- Test permission leakage
- Disconnect network
- Test unsupported questions
- Demonstrate draft versus approved output
- Measure response time and citation accuracy

## Recommended demo workflow

**Scanned inspection report → Word approval note**

This single workflow covers:

- Multimodal (scanned PDF + vision)
- Agentic (multi-step plan)
- Multi-model (OCR + reasoning + generation)
- RAG (historical inspection data)
- Real deliverable (Word + Excel)
- Air-gap proof (network monitor)
- Entity resolution (tag linking)
- Revision awareness
- Human approval gate

## Minimum viable demo

- Scanned PDF upload
- OCR + vision extraction
- Equipment tag matching
- Historical data retrieval
- Corrosion rate calculation
- Word approval note generation
- Excel thickness chart
- Network monitor showing zero external calls
- Classification badge on output
- Audit log showing model routing + agent steps

## Demo script structure

1. Opening statement (30 sec): "We built a scaled-down version of a production architecture."
2. Architecture diagram walkthrough (1 min)
3. Live demo (5 min): Upload → OCR → extract → match → calculate → draft → export
4. Air-gap proof (1 min): Network monitor showing zero external calls
5. Multi-model routing (30 sec): Logs showing different models used
6. Agentic behavior (30 sec): Logs showing multi-step workflow
7. Closing statement (1 min): "Ready to scale from single department to whole organisation."
