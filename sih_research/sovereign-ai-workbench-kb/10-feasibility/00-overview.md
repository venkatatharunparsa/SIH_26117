# Feasibility Overview

What is realistically buildable in a 36-hour hackathon with a mid-range GPU, and what the judges will expect.

## Core strategy

**Design the solution for organisation level. Implement a scaled-down version for the hackathon demo.**

Same architecture. Same components. Same data flow. Smaller models. Mock connectors.

This is not a hackathon tactic. It is the correct product strategy.

## What the judges see

1. A working demo (scanned inspection report → OCR → extraction → entity resolution → corrosion calculation → Word approval note + Excel chart)
2. The full architecture (diagram showing how the same system scales)
3. Air-gap proof (network monitor showing zero external calls)
4. Multi-model routing (logs showing different models used for different tasks)
5. Agentic behavior (logs showing the multi-step workflow)
6. Real deliverables (downloadable Word and Excel files)
7. Classification awareness (output labelled with classification and "draft" status)

## Feasibility summary

| Component | Real in 36-hour prototype | Mocked or simplified |
|---|---|---|
| Local LLM inference | Yes | Model quality and throughput limited |
| Air-gap | Yes, demonstrate with network disabled | Formal accreditation not possible |
| Document ingestion | Yes | Limited formats and OCR accuracy |
| RAG citations | Yes | Citation completeness and page accuracy need testing |
| Word output | Yes | Customer template library limited |
| Excel output | Yes | Advanced formula validation limited |
| PowerPoint output | Yes | Design quality and executive style simplified |
| EAM/ERP | Mock JSON/CSV/API | Real SAP or Oracle integration |
| Historian | CSV/time-series mock | Live PI/DCS connector |
| LIMS | Sample CSV/API mock | Real LIMS integration |
| Permissions | Basic RBAC | Full source-system ACL inheritance |
| Entity resolution | Rule-based equipment tags | Enterprise-scale ontology |
| MOC/RCA/TBE agents | One working workflow | Full approval automation |
| Audit trail | Application log | Immutable enterprise SIEM integration |
| Security | Local login, network isolation | Formal penetration testing and certification |

## What 4 people can realistically build

- Local model server
- Web interface
- PDF/DOCX/XLSX ingestion
- OCR for selected scans
- Hybrid search
- Simple metadata layer
- Citation-backed answers
- One or two agent workflows
- Word/Excel/PPT generation
- Mock refinery or PSU dataset
- Visible air-gap demonstration (disconnect the network)
- Basic user roles

## What 4 people cannot build in 36 hours

- Full ERP/EAM/DCS/LIMS integration
- Certified defence or nuclear deployment
- Complete RBAC at every source system
- Industrial-grade P&ID symbol recognition
- Perfect revision management
- Enterprise audit and SIEM integration
- Comprehensive vulnerability testing
- Safety-certified AI decision support
- Multi-site disaster recovery
- Full legal/compliance certification
