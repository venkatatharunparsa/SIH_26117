# Sensitive Data Inventory

## MRPL-specific data classes

| Data class | Examples | Why sensitive |
|---|---|---|
| Process and production | Throughput, yields, temperatures, pressures, alarms, historian trends | Reveals operating capability, bottlenecks, commercial performance |
| Engineering drawings | P&IDs, plot plans, electrical diagrams, control narratives, F&G layouts | Exposes hazardous materials, isolation points, vulnerabilities |
| OT and cybersecurity | DCS architecture, PLC logic, SIS configuration, network diagrams, firewall rules | Could enable disruption or cyber intrusion |
| Inspection and integrity | Corrosion rates, thickness readings, FFS assessments, failed equipment | Reveals asset vulnerabilities |
| Maintenance data | Breakdown history, bad actors, work orders, backlog | Exposes reliability weaknesses |
| Crude and commercial | Crude assays, purchase prices, vessel schedules, inventory, product economics | Affects trading position and margin |
| Vendor data | Quotations, negotiation notes, technical bids, commercial evaluations | Competition-sensitive procurement |
| Financial data | Budgets, forecasts, cash flows, borrowing, margins, management accounts | Material non-public information |
| Legal and governance | Board notes, litigation, investigations, legal opinions, unreleased decisions | Privileged, market-sensitive |
| HSE and incident | Accident investigations, near misses, root causes, emergency plans | Safety and legally sensitive |
| Personal data | Employee records, health data, attendance, payroll, contractor identities | Privacy and labour-law obligations |
| Intellectual property | AI models, patents, process recipes, catalyst performance, pilot results | Competitive advantage |
| Strategic plans | Expansion, decarbonisation, SAF, petrochemical integration, retail strategy | Unreleased strategy |

## Cross-sector sensitive data archetypes

| Archetype | Sensitive data | Sectors |
|---|---|---|
| Industrial process | Process data, P&IDs, OT architecture, inspection, incident reports | Refinery, power, heavy industry, fertilizers |
| Classified defence | Drawings, test data, military requirements, classified correspondence | Defence PSUs, DRDO, private defence |
| Government files | Cabinet notes, policy drafts, personal data, investigation files | Ministries, state, district |
| Regulated finance | KYC, account data, credit models, fraud investigations | Banking, insurance |
| Legal privilege | Pleadings, judgments, opinions, evidence, case diaries | Courts, legal cells, investigators |
| Regulated submissions | Safety analyses, licensee data, non-compliance records | AERB, CEA, PNGRB, CPCB, OISD, RBI, SEBI, IRDAI, TRAI |
| Public infrastructure | Grid topology, protection settings, train-control config, port security | Power, railways, ports |
| Critical research | Clinical trial data, patents, formulations, propulsion, sensor data | Pharma, space, DRDO |

## Universal sensitive categories

Regardless of sector, these are always sensitive:

- Personal data (identity, health, payroll, contractor)
- Vendor and negotiation data
- Incident and investigation files
- Legal opinions and privilege
- Board and cabinet material
- Cyber and OT architecture
- Unreleased strategy and budgets
- Source code and configuration
- Trade secrets and process recipes
- Security arrangements
