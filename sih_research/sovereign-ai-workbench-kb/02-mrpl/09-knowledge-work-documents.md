# MRPL Knowledge Work and Documents

MRPL's knowledge work is highly document-intensive and approval-driven. The most useful AI-workbench design is not simply a chatbot; it is a controlled evidence system connecting documents, assets, equipment tags, work orders, approvals and operating context.

## Corporate and governance documents

- Board notes and agenda papers
- Board and committee minutes
- Approval notes and delegated-authority files
- Investment proposals and capital-expenditure cases
- Annual reports and sustainability reports
- Stock-exchange disclosures
- Shareholder correspondence
- Company-secretarial registers and statutory filings
- Internal audit reports
- Vigilance and investigation records
- Legal opinions and litigation files
- Corporate policies and procedures
- Senior-management correspondence

## Engineering and process documents

- Process design basis
- Design criteria and engineering calculations
- PFDs and P&IDs
- Heat and material balances
- Equipment datasheets
- Line lists and valve lists
- Cause-and-effect diagrams
- Control narratives
- Instrument index and I/O lists
- Electrical single-line diagrams
- Cable schedules and load lists
- Piping isometrics
- Plot plans and general-arrangement drawings
- Hazardous-area classification drawings
- Relief-system calculations
- Fire-and-gas layouts
- Utility summaries
- Operating envelopes
- Catalyst and chemical-management records
- Management-of-change files
- HAZOP, HAZID, SIL and LOPA studies
- Commissioning and startup dossiers
- As-built drawings and vendor manuals

## Operations documents

- Shift logbooks
- Daily production reports
- Unit operating instructions
- Startup and shutdown procedures
- Emergency operating procedures
- Abnormal-situation reports
- Production-loss reports
- Tank and inventory statements
- Crude receipt and assay reports
- Product blending sheets
- Operating-window exception reports
- Control-room alarm and trip summaries
- Permit-to-work records
- Isolation and de-isolation certificates
- Line-up sheets
- Shift handover notes
- Flare and emission event records
- Product release and quarantine records

## Maintenance and reliability documents

- Maintenance work orders
- Preventive-maintenance schedules
- Corrective-maintenance notifications
- Breakdown reports
- Equipment history cards
- Failure-analysis reports
- Root-cause-analysis reports
- Vibration and condition-monitoring reports
- Lubrication records
- Spare-parts lists
- Equipment criticality assessments
- Reliability-centred-maintenance studies
- Inspection test plans
- Turnaround work packs
- Shutdown schedules
- Job safety analyses
- Contractor work-completion certificates
- Post-maintenance test records

## Inspection and integrity documents

- RBI assessments
- Corrosion-loop records
- Thickness-measurement reports
- Ultrasonic testing reports
- Radiography and magnetic-particle testing reports
- Dye-penetrant testing reports
- Weld maps and weld histories
- Pressure-test records
- Relief-valve test certificates
- Pressure-vessel inspection reports
- Tank-floor and tank-shell inspection reports
- Fitness-for-service assessments
- Statutory inspection certificates
- Coating and lining inspection reports
- Piping integrity assessments
- Cathodic-protection records

## HSE and regulatory documents

- Permit-to-work files
- Hot-work and confined-space permits
- HSE inspection reports
- Behaviour-based safety observations
- Near-miss reports
- Incident and accident investigation reports
- Emergency-response plans
- Mock-drill records
- Fire-system inspection reports
- Process-safety management records
- HAZOP and MOC records
- Environmental-monitoring data
- Consent-to-operate compliance reports
- OISD compliance reports
- Factory and boiler statutory filings
- Hazardous-waste returns
- Water-consumption and effluent reports
- Greenhouse-gas and sustainability data
- Contractor-safety audits

## Laboratory and quality documents

- Crude assay reports
- Feed and product laboratory results
- Sulphur, density, viscosity and flash-point analyses
- Octane and cetane-related quality data
- Bitumen penetration and softening-point reports
- Polypropylene melt-flow and grade-quality reports
- Para-xylene and benzene purity results
- Water and wastewater analyses
- Calibration certificates
- Sampling plans
- Certificates of analysis
- Product-release approvals
- Customer complaint investigations
- Laboratory quality-system records

## Commercial, procurement and finance documents

- Purchase requisitions
- Material requisitions
- Technical specifications
- Enquiry documents
- Tender notices
- Pre-bid clarifications
- Technical bid evaluations
- Commercial bid evaluations
- Comparative statements
- Vendor quotations
- Negotiation records
- Purchase orders
- Rate contracts
- Service contracts
- EPC and LSTK contracts
- Performance guarantees
- Bank guarantees
- Inspection-release notes
- Goods-receipt records
- Invoice approvals
- Budget files
- Cost-centre reports
- Financial statements
- Inventory valuation
- Tax records
- Treasury and borrowing documents
- Insurance claims
- Customer contracts and credit files

## Document families by classification

| Family | Sensitivity | Primary users |
|---|---|---|
| Corporate and governance | Confidential | Board, company secretary, senior management |
| Engineering and process | Confidential/Restricted | Process, projects, operations |
| Operations | Restricted | Operations, shift engineers |
| Maintenance | Restricted | Maintenance, reliability |
| Inspection | Confidential/Restricted | Inspection, integrity |
| HSE and regulatory | Confidential | HSE, process safety |
| Laboratory | Restricted | Laboratory, quality, process |
| Commercial/procurement | Confidential | Procurement, finance |
| Financial | Confidential | Finance, management |

## Entity resolution requirement

Documents do not share a common identifier for the same physical asset. The AI workbench must link:

- "P-204A" on a P&ID
- "Pump 204A" in a work order
- "204A" in a vibration report
- A historian tag such as discharge pressure
- A spare-parts record
- A failure-analysis report
- A maintenance notification

This is not semantic search. It is industrial entity resolution.
