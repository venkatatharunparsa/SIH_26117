# MRPL Sensitive Data

An on-premise AI workbench should treat MRPL information as a segmented data estate, not as one undifferentiated document repository.

| Data class | Examples | Why sensitive |
|---|---|---|
| Process and production data | Throughput, yields, temperatures, pressures, alarms, unit constraints and historian trends | Reveals operating capability, bottlenecks, vulnerabilities and commercial performance |
| Engineering drawings | P&IDs, plot plans, electrical diagrams, control narratives, fire-and-gas layouts | Can expose hazardous materials, isolation points, critical equipment and physical vulnerabilities |
| OT and cybersecurity data | DCS architecture, PLC logic, SIS configuration, network diagrams, firewall rules and credentials | Could enable disruption, unsafe manipulation or cyber intrusion |
| Inspection and integrity data | Corrosion rates, thickness readings, fitness-for-service assessments and failed equipment | Reveals asset vulnerabilities and safety-critical degradation |
| Maintenance data | Breakdown history, bad actors, work orders and backlog | Exposes reliability weaknesses and operational readiness |
| Crude and commercial data | Crude assays, purchase prices, vessel schedules, inventory and product economics | Affects trading position, margin, negotiations and market strategy |
| Vendor data | Quotations, negotiation notes, technical bids and commercial evaluations | Confidential procurement information and competition-sensitive material |
| Financial data | Budgets, forecasts, cash flows, borrowing, margins and internal management accounts | Material non-public and commercially sensitive information |
| Legal and governance data | Board notes, litigation, investigations, legal opinions and unreleased decisions | Privileged, confidential or market-sensitive |
| HSE and incident information | Accident investigations, near misses, root causes and emergency plans | Safety-sensitive and potentially legally sensitive |
| Personal data | Employee records, health data, attendance, payroll and contractor identities | Privacy, labour-law and cybersecurity obligations |
| Intellectual property | AI models, patents, process recipes, catalyst performance and pilot results | Competitive advantage and ownership-sensitive research |
| Strategic plans | Expansion, decarbonisation, SAF, petrochemical integration and retail strategy | Unreleased business strategy and investment information |

## Recommended handling principles

A suitable AI workbench should provide:

- On-premise inference and retrieval
- No external model-training use of company data
- Document-level and paragraph-level access control
- Role-based access by department, project, plant and document classification
- OT/IT network separation
- Approval-aware answers that distinguish draft from approved documents
- Full citation to source documents, revisions, page numbers and equipment tags
- Immutable audit logs
- Data-loss-prevention controls
- Redaction of personal data and credentials
- Model-output retention and review history
- Air-gapped or controlled-update options
- Separate indexes for corporate, engineering, HSE, commercial, legal and OT data
- Human approval before generated content becomes an official record

## Classification mapping

Using the unified cross-sector classification framework, MRPL data maps as follows:

| MRPL data class | Classification |
|---|---|
| Published annual report, public tenders | Public |
| Internal procedures, non-sensitive meeting notes | Internal |
| Working files, maintenance schedules, internal procurement drafts | Restricted |
| P&IDs, vendor quotes, inspection reports, incident drafts, budgets, legal opinions | Confidential |
| DCS/SIS architecture, OT network diagrams, cyber vulnerabilities | Secret |
| Highest-level strategic or national-security-relevant information | Top Secret |

## Public vs. non-public

Even a published document has non-public aspects. A published annual report is public; an internal draft of the next annual report is not. A published tender notice is public; bidder evaluations and negotiation notes are confidential.
