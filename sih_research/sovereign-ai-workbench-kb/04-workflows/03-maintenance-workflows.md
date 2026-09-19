# Maintenance Engineer Workflows

## Recurring pump failure investigation

Assume a crude charge pump, feed pump or product pump has failed repeatedly.

### A. Detect and classify failure

**Step 1: Receive failure notification**

The event may appear in: EAM notification, DCS equipment alarm, operator phone call, shift log, email, reliability dashboard, or breakdown report.

The maintenance engineer records or confirms: equipment tag, date and time, failure mode, running condition, consequence, standby availability, production impact, and immediate repair.

**Step 2: Search EAM first**

The engineer opens the EAM/CMMS and searches the equipment master. They review work-order history, failure codes, breakdown notifications, preventive-maintenance plans, repair descriptions, parts replaced, labour hours, contractor reports, return-to-service notes, repeat failure frequency, and similar equipment.

The engineer exports the records to Excel if the EAM search is weak.

Saved: Failure-history workbook, list of relevant work orders, preliminary failure chronology, action list.

### B. Pull operating context

**Step 3: Search historian**

The engineer selects a time window around each failure and retrieves: suction pressure, discharge pressure, flow, motor current, vibration (if connected), bearing temperature, seal pressure, pump speed, minimum-flow recycle, tank level, fluid temperature, upstream and downstream valve position, DCS trip or alarm status.

The engineer compares normal and failed periods.

**Step 4: Check DCS and alarm history**

Check: trip cause, motor overload, low-suction-pressure alarm, high-vibration trip, seal-system alarm, control-valve behaviour, standby-pump start, interlock sequence.

May request detailed event log from instrumentation or operations.

**Step 5: Search email and shared drives**

Search for vendor service reports, previous RCA files, pump datasheet, mechanical seal specification, alignment report, vibration reports, installation drawings, commissioning reports, change notices, previous turnaround documents, informal operator observations.

This is often the slowest step because file names and equipment references are inconsistent.

**Step 6: Check inspection and laboratory information**

Depending on the failure, consult: inspection reports, piping vibration observations, strainer or filter findings, fluid contamination, particle or solids data, corrosion records, pump casing thickness, shaft or impeller inspection, mechanical-seal failure analysis.

### C. Assemble failure history

**Step 7: Create a timeline**

Excel or Word timeline with: date, operating condition, failure symptom, alarm, failure mode, immediate repair, parts replaced, contractor, return-to-service date, repeated pattern, production impact.

**Step 8: Identify failure mode**

Possible hypotheses: cavitation, low NPSH, misalignment, seal failure, bearing failure, impeller damage, mechanical looseness, piping strain, operating outside design flow, electrical overload, instrument or interlock fault, contamination, poor maintenance execution, wrong spare or material.

### D. Conduct RCA

**Step 9: Convene RCA team**

Participants may include maintenance, reliability, operations, mechanical engineering, process engineering, instrumentation, inspection, HSE (where safety or release occurred), and vendor or OEM.

**Step 10: Build evidence pack**

Team reviews: EAM history, historian trends, DCS alarms, vibration data, work-order closeout, inspection findings, photographs, vendor report, operating procedure, pump datasheet, similar equipment history.

**Step 11: Conduct analysis**

Methods may include: Five Whys, Fishbone diagram, Fault-tree analysis, FMEA, Cause-and-effect timeline, Bad-actor analysis, Operating-envelope review.

**Step 12: Write RCA report**

RCA report contains: problem statement, equipment details, event chronology, immediate cause, technical root cause, systemic causes, evidence, corrective actions, preventive actions, owner and due date, verification method, residual risk.

### E. Check spare parts

**Step 13: Open ERP/materials module**

Check: material number, stock quantity, reserved quantity, reorder point, open purchase order, supplier, lead time, alternate material, compatibility, historical consumption, critical-spares status.

**Step 14: Check procurement and warehouse**

Contact stores, procurement, materials planning, vendor or OEM. Raise: material requisition, purchase requisition, technical specification, emergency procurement note, critical-spares justification.

### F. Draft repair recommendation

**Step 15: Prepare technical note**

May recommend: replace mechanical seal, correct alignment, modify piping support, change operating range, upgrade bearing, replace pump with alternate design, add vibration monitoring, revise preventive maintenance, hold a critical spare, undertake a turnaround repair.

**Step 16: Route for approval**

Likely sequence: reliability engineer drafts → maintenance engineer validates scope → operations confirms production impact → process engineer checks operating implications → procurement/materials confirms availability and cost → finance checks budget where capital or major expenditure is involved → HSE reviews risk where relevant → maintenance head or refinery head approves → EAM work order or project is created → completion evidence is attached after execution.

## Time estimate

| Activity | Typical elapsed time |
|---|---|
| EAM history search | 1–4 hours |
| Historian and alarm review | 2–6 hours |
| Email/shared-drive search | 2–8 hours |
| RCA meeting and analysis | 4–16 hours |
| Spare-parts review | 1–4 hours |
| Technical recommendation | 2–8 hours |
| Approval and work-order creation | 1–5 days |
| People involved | 4–10 people |

For a recurring failure, finding and assembling evidence may consume 40–60% of the investigation effort.

## AI intervention

Read-only data: EAM history, historian trends, DCS alarms, vibration and condition-monitoring data, vendor reports, drawings and datasheets, spare-parts inventory, email and shared-drive documents (subject to permission).

Output: Equipment timeline, similar-failure search, failure-mode classification, trend charts, evidence-backed RCA draft, spare-parts status, draft repair recommendation, Word report and Excel evidence pack.

Human gate: Reliability engineer confirms diagnosis; maintenance head approves work; operations authorises operating restrictions; procurement and finance approve expenditure.

## Documents and systems

### EAM and maintenance documents

- Maintenance notification
- Work order
- Job plan
- Preventive-maintenance schedule
- Equipment history
- Failure code
- Breakdown report
- Job safety analysis
- Permit and isolation record
- Spare-parts reservation
- Material issue record
- Contractor completion certificate
- Test and commissioning record
- Post-maintenance report

### Reliability documents

- Bad-actor list
- Pareto analysis
- RCA report
- FMEA/FMECA
- RCM study
- Criticality assessment
- Reliability block diagram
- RAM study
- Condition-monitoring report
- Vibration report
- Oil-analysis report
- Thermography report
- Defect-elimination plan
- Equipment strategy
- Reliability dashboard

### Turnaround documents

- Equipment list
- Scope book
- Job list
- Work packs
- Method statements
- Inspection and test plans
- Resource plan
- Material and spare-parts plan
- Contractor mobilisation plan
- Shutdown schedule
- Critical-path schedule
- Daily progress report
- Punch list
- Mechanical-completion certificate
- Pre-startup safety review package
- Startup readiness checklist
- Lessons-learned report

## What is slow

- Searching historical work orders
- Linking equipment failures to process conditions
- Finding the correct spare-parts specification
- Comparing vendor repair reports
- Reading vibration graphs and attaching them to work orders
- Tracking action items from RCAs
- Reconciling equipment names between EAM, drawings and historian
- Checking whether a recurring failure already occurred elsewhere in the refinery
- Preparing turnaround work packs
- Updating schedules when materials or contractors are delayed
- Converting field notes into formal closeout reports
- Obtaining signatures from operations, maintenance, inspection and HSE
