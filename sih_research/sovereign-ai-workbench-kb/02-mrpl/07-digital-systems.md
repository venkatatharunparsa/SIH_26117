# MRPL Digital Systems

MRPL does not publicly disclose a complete authoritative inventory of its current enterprise and control-system products. It is therefore safer to define the systems by function and verify product names during discovery.

| System layer | Likely function at MRPL | AI-workbench relevance |
|---|---|---|
| ERP | Finance, procurement, materials, inventory, purchase orders, vendors, projects and HR | Retrieve transactions, budgets, materials history and approval status |
| Maintenance-management / EAM | Equipment master, notifications, work orders, preventive maintenance, spare parts and backlog | Failure analysis, work-order summarisation and maintenance recommendations |
| DCS / SCADA / PLC | Real-time unit control and automation | Process context, alarms, trips and operator assistance; must remain read-only unless explicitly engineered |
| SIS and fire-and-gas systems | Safety instrumented functions and emergency detection | High-risk data; use for controlled search and compliance evidence, not autonomous control |
| Process historian | Time-series data from transmitters, control loops, analysers and equipment | Trend analysis, anomaly detection, energy optimisation and event reconstruction |
| Laboratory information systems | Samples, test results, certificates and quality release | Correlate lab results with batches, units and customer specifications |
| Document management | Controlled engineering documents, policies, procedures and records | Core retrieval and revision-control source |
| Email and calendaring | Approvals, correspondence, meetings and operational escalation | Searchable only under strict retention, privacy and legal-hold controls |
| File shares and intranet | Working documents, templates, reports and departmental files | High-value but high-risk source due to duplicates and uncontrolled versions |
| Tender and e-procurement portals | Bid documents, vendor responses, evaluations and awards | Procurement intelligence and workflow extraction |
| Cybersecurity and SOC tooling | Identity, endpoint, network and security logs | Sensitive operational-security data; restricted index |
| GIS and asset mapping | Pipelines, tanks, utilities, land and facilities | Spatial search and asset context |
| Business-intelligence systems | KPI dashboards, production, finance, energy and maintenance metrics | Cross-functional decision support |
| Access-control and contractor systems | Personnel, permits, gate access and contractor compliance | Safety and workforce analytics, subject to privacy controls |

## Typical data flow

## Where the AI workbench sits
Approved read-only connectors
↓
Identity and permission filtering
↓
Industrial search and knowledge graph
↓
Calculations, comparison and evidence extraction
↓
Draft report / Excel / PowerPoint / action list
↓
Human review and controlled publication

## Central architectural challenge: entity resolution

The workbench must understand that a document mentioning "P-204A," a work order for "Pump 204A," a vibration report, a spare-parts request and a P&ID equipment tag may all refer to the same physical asset.

This requires an industrial entity-resolution layer, not just semantic search.

## Public evidence on procurement systems

MRPL's publicly visible tender and order records show the importance of storage-tank maintenance, refinery-to-jetty pipeline work, power-system upgrades and other engineering procurement activity. This confirms e-procurement and public tender portals are part of the digital estate.

## Public evidence on process systems

MRPL's FY2024–25 chairman's speech confirms implementation of advanced process control in CDU/VDU, diesel hydrotreating, PFCC, isomerisation and FCC-related systems, plus predictive models in polypropylene, power and PFCC and prescriptive models in hydrotreating.

## Confirmed vs. inferred

| Confirmed public | Inferred (industry standard) |
|---|---|
| Advanced process control in multiple units | ERP vendor |
| Predictive models in PP, power, PFCC | EAM vendor |
| Prescriptive models in hydrotreating | Historian product |
| Innovation Centre working on AI/ML | LIMS product |
| Public tenders via e-procurement | DMS product |
| 29 patents filed, 12 granted | Specific DCS/SCADA vendor |

Product names should be confirmed during customer discovery, not assumed.
