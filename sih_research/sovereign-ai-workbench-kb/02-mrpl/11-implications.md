# MRPL Implications for AI Workbench Design

## Highest-value initial use cases

1. **Engineering document copilot** — Search P&IDs, PFDs, datasheets, vendor manuals, calculations, operating procedures and as-built revisions with page-level citations.

2. **Maintenance and reliability assistant** — Summarise equipment history, work orders, inspection findings, vibration data, spares, recurring failures and pending actions.

3. **Shift-handover intelligence** — Consolidate shift logs, alarms, abnormal events, permits, work orders and unit constraints into a traceable handover brief.

4. **Turnaround planning assistant** — Search historical turnaround work packs, estimate task durations, identify safety prerequisites and compare contractor progress.

5. **HSE and compliance evidence assistant** — Map procedures and operating records to OISD, statutory, environmental and internal audit requirements.

6. **Procurement and vendor-analysis assistant** — Extract technical compliance, deviations, delivery history, commercial terms and evaluation criteria while preserving bid confidentiality.

7. **Process-optimisation knowledge layer** — Link historian trends, APC constraints, lab results, operating notes and engineering recommendations.

8. **Management approval assistant** — Draft approval notes from structured project, budget, procurement and risk data, with mandatory human review.

## Suggested architecture

| Layer | Recommended design |
|---|---|
| Deployment | On-premise GPU cluster or controlled private data centre |
| Retrieval | Hybrid keyword plus vector search, with engineering-tag and equipment-identifier search |
| Document processing | OCR, table extraction, drawing metadata, revision detection and P&ID symbol/tag extraction |
| Knowledge graph | Units, equipment, tags, lines, vendors, work orders, documents, incidents and approvals |
| Model gateway | Multiple approved models selected by data classification and task |
| Access control | Integration with corporate identity, department, plant, project and document permissions |
| OT integration | Read-only historian and alarm access initially; no direct control action |
| Governance | Source citations, confidence indicators, approval status and audit trails |
| Data protection | Encryption, segmentation, DLP, redaction, retention and legal holds |
| User interface | Web workstation, control-room display mode, mobile shift mode and API for existing systems |
| Evaluation | Retrieval precision, citation accuracy, hallucination rate, permission leakage and response latency |

## Phased implementation

**Phase 1: controlled document search**

Start with approved procedures, engineering drawings, equipment manuals, HSE procedures, inspection reports and selected maintenance history. Exclude live OT control and highly restricted legal or cybersecurity data.

**Phase 2: maintenance and operations context**

Connect the document workbench to the EAM system, equipment master and selected historian tags. Make outputs advisory and require operator or engineer confirmation.

**Phase 3: engineering and HSE workflows**

Add MOC, HAZOP, RBI, incident investigations, permits, turnaround planning and compliance evidence.

**Phase 4: process and reliability analytics**

Use historical historian data, lab results and equipment data for anomaly detection, failure prediction and energy optimisation. Maintain a strict separation between analytical recommendations and control-system commands.

## What the AI should NOT do

- Approve a permit autonomously
- Determine that an area is gas-free
- Override an isolation
- Close an incident action without evidence
- Decide that an MOC is safe
- Replace a competent HAZOP team
- Infer that a control is effective because a document says it exists
- Write to DCS, SIS, PLC, EAM, ERP or permit systems
- Issue financial approval or apply a signature
- Recommend a vendor without a documented evaluation

## The core product principle

> The AI should reduce the time required to find, reconcile and explain evidence, while leaving technical judgement, safety authorisation, commercial evaluation and statutory approval with accountable personnel.

## Why on-premise or air-gapped matters at MRPL

- Confidential documents remain inside the organisation
- Prompts and outputs remain controlled
- Model inference is local
- Retrieval indexes do not leave the enclave
- Logs can remain within Indian jurisdiction
- OT and classified networks can be isolated
- Security teams can inspect software and network paths
- Access can follow existing identity and clearance rules
- The organisation controls upgrades and retention

## Discovery checklist for a real MRPL deployment

For designing the workbench, the most important discovery exercise would be a controlled inventory of:

- MRPL's document repositories
- Equipment master
- ERP/EAM objects
- Historian tags
- Approval workflows
- Identity groups
- OT/IT security zones
- Current DMS, ERP, EAM, LIMS product names
- Document templates in active use
- Classification labels in current policy
- Retention and legal-hold rules

The public record clearly supports a high-value use case around engineering knowledge, maintenance, process optimisation, HSE compliance and controlled management approvals — but it does not justify assuming unrestricted access to live control systems or all enterprise data.
