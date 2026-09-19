# Real vs. Mocked

## Real in the demo

- Local model inference (small models)
- Air-gap (network physically disconnected)
- OCR on scanned PDFs
- Entity resolution (rule-based tag matching)
- Corrosion rate calculation (Python)
- Word approval note generation (python-docx)
- Excel thickness chart (openpyxl)
- Source citations
- Classification badge
- Audit log
- Multi-model routing (visible in logs)
- Agentic workflow (visible in logs)
- Network monitor showing zero external calls

## Mocked or simplified

- ERP (mock JSON/CSV folder)
- EAM (mock JSON/CSV folder)
- Historian (mock CSV time series)
- LIMS (mock sample CSV)
- DMS (mock document folder)
- PTW system (mock permit records)
- MOC system (mock MOC records)
- Authentication (local users, basic RBAC)
- Permissions (role-based, not source-system ACL inheritance)
- Audit trail (application log, not enterprise SIEM)
- Model quality (small models, limited context)
- OCR accuracy (varies with scan quality)
- Template library (one or two templates)

## How to present mocked components honestly

Frame mock components as **connector placeholders**:

> "In production, this connector would be a read-only API to SAP EAM. For the demo, we use a folder of JSON files that match the same schema. The AI workbench treats both identically."

This is honest and shows architectural thinking.

## What judges care about

- Does the workflow work end-to-end?
- Is the output a real deliverable?
- Is the air-gap proof visible?
- Is the multi-model routing visible?
- Is the agentic behavior visible?
- Is the classification-aware?
- Is the output labelled as draft?
- Does the architecture scale?

## What judges do NOT expect

- Production SAP integration
- Certified defence deployment
- Perfect OCR
- Enterprise RBAC
- Penetration-tested security
- 120B parameter models
- Multi-site DR
- Full legal compliance certification

## How to talk about scale

> "The architecture is designed for organisation-level deployment. The demo runs the same architecture at 1/100th scale — one GPU, small models, mock connectors. Scaling up means adding GPUs, loading larger models, and connecting real APIs. The logic does not change."
