# Process Engineer Workflows

## A. Morning daily performance review

### Step 1: Open communications and work queue

The process engineer starts at a desktop or laptop and opens:

- Corporate email and calendar
- Intranet or document-management system
- EAM/CMMS work queue
- Daily production-report folder or dashboard
- Process historian client
- LIMS or laboratory-results portal
- ERP or production-accounting reports
- Team chat or shift-handover application

They read:

- Previous shift handover
- Overnight abnormal-event emails
- Unit trip or alarm summaries
- Pending process-engineering actions
- Laboratory exceptions
- Maintenance notifications affecting the unit
- MOC, HAZOP and project-review actions

Sensitive data involved: Throughput, crude slate, unit rates, product quality, operating constraints, equipment availability, unreleased performance information, internal email, personnel names.

### Step 2: Open the process historian

The engineer opens the historian and selects a standard tag set for the assigned unit. Typical tags:

- Feed flow, product flows
- Column pressures and temperatures
- Furnace outlet temperature
- Reactor inlet and outlet temperatures
- Hydrogen flow and purity
- Compressor suction and discharge pressure
- Recycle flow
- Valve positions
- Level and pressure-control variables
- Online analyser values
- Energy and fuel-gas consumption
- Flare flow
- Steam and cooling-water consumption

The engineer reviews last 8–24 hours, current shift, previous day, same period prior week, current campaign, and performance before/after maintenance.

Manual burden: Selecting the correct tags, correcting tag names, handling missing or bad-quality data, aligning time zones and sample intervals, choosing a representative averaging period, copying data into Excel.

### Step 3: Check DCS and alarm information

The engineer may consult the DCS directly or request data from the panel operator. DCS information includes:

- Alarm summary
- Trip history
- Interlock status
- Controller output
- Setpoints
- Bypass status
- Manual/automatic control status
- Valve position
- Equipment running status
- Cause-and-effect response

The process engineer usually does not change DCS settings independently. The engineer sends an operating recommendation to the operations supervisor or panel operator.

### Step 4: Check LIMS and laboratory reports

The engineer opens the LIMS and checks:

- Feed assay
- Intermediate-stream quality
- Product sulphur, density, flash point, distillation properties, viscosity
- Octane or cetane-related properties
- Hydrogen sulphide or nitrogen content
- Polypropylene quality
- Water and effluent results

Laboratory data is matched against online analyser results, sample time, tank or stream identity, batch or campaign, and unit operating conditions.

### Step 5: Check EAM/CMMS and maintenance status

The engineer searches the EAM for:

- Equipment under maintenance
- Open work orders
- Temporary repairs
- Bypassed equipment
- Instrument or analyser maintenance
- Pumps or compressors unavailable
- Exchanger cleaning
- Furnace or boiler issues
- Planned interventions affecting throughput

### Step 6: Attend the morning coordination meeting

Participants: operations, process engineering, production planning, laboratory, maintenance, inspection, HSE, utilities, commercial or supply-chain representatives.

Typical agenda:

1. Safety and abnormal events
2. Unit availability
3. Production versus target
4. Quality deviations
5. Maintenance constraints
6. Tank and dispatch constraints
7. Crude and feedstock changes
8. Action ownership
9. Forecast for the next 24 hours

## B. Sulphur excursion investigation

Assume a diesel or gasoline stream exceeds its sulphur specification.

### Step 1: Receive notification

Detection through LIMS result, online sulphur analyser, operations call, shift handover, product-quality dashboard, or customer complaint.

People notified: Shift engineer, process engineer, laboratory manager, production manager, HSE if unsafe, maintenance/instrumentation if analyser faulty, marketing if product released.

### Step 2: Validate the laboratory result

Open LIMS and check: sample ID, sample time, sample point, test method, analyst status, duplicate or repeat result, calibration status, previous results, product specification.

The engineer may call the laboratory to request reanalysis, retained-sample testing, sample-line verification, instrument-calibration check, and sample identity confirmation.

### Step 3: Pull historian data

Export a time window (24 hours before first bad sample, the affected batch, last stable period, comparable previous campaign). Pull:

- Feed sulphur
- Reactor temperature, pressure
- Hydrogen flow, purity
- Liquid hourly space velocity
- Recycle rate
- Quench flow
- Product flow, draw temperature
- Separator pressure
- Fractionator conditions
- Bypass-valve position
- Online-analyser values

Data is usually copied into an Excel workbook.

### Step 4: Review DCS events

Retrieve alarm history, interlock events, controller output, manual interventions, valve travel, instrument bad-quality flags, equipment trips, control-loop oscillations, bypass status, setpoint changes.

If a trip was involved, create a minute-by-minute sequence.

### Step 5: Review maintenance and instrument records

Search EAM for sulphur-analyser work orders, hydrogen-flow-meter calibration, control-valve maintenance, reactor-temperature instrument issues, recent shutdown or restart work, leak or bypass work, catalyst-related work, exchanger or furnace maintenance.

### Step 6: Compare with laboratory and online data

Spreadsheet with: sample time, LIMS sulphur result, online analyser result, historian-average sulphur, feed properties, reactor conditions, product flow, operating target, specification limit.

Check: analyser bias, sample representativeness, feed change coincidence, reactor severity, hydrogen availability, product mixing or routing, equipment or control problem.

### Step 7: Perform calculations

- Time-weighted average sulphur
- Batch or tank sulphur concentration
- Mass of off-spec product
- Material balance
- Hydrogen-to-oil ratio
- Reactor severity comparison
- Residence-time or space-velocity comparison
- Sulphur-load calculation
- Product reprocessing or blending requirement
- Economic loss
- Compliance margin
- Statistical comparison with stable operation

### Step 8: Conduct a technical review

Discuss findings with operations, laboratory, instrumentation, maintenance, planning, quality control, HSE and unit or refinery manager.

Possible conclusions: genuine process degradation, feed-quality change, inadequate operating severity, hydrogen constraint, catalyst deactivation, analyser fault, sampling error, routing or blending error, equipment malfunction, or multiple contributing causes.

### Step 9: Prepare the deviation investigation note

Word or controlled form containing: event summary, date and time, unit and stream, product specification, actual result, quantity affected, immediate containment, data sources, trend charts, analysis, root cause or suspected causes, contributing factors, corrective actions, preventive actions, responsible persons, due dates, follow-up verification, attachments.

### Step 10: Review and approve

Likely route: process engineer → laboratory validates → operations confirms chronology → instrumentation or maintenance confirms → process or production manager reviews → quality or HSE reviews compliance → refinery or unit head approves → corrective actions entered into EAM, HSE or action trackers.

## C. Monthly unit-performance report

### Step 1: Collect data

Retrieve monthly crude or feed throughput, product yields, product quality, energy intensity, fuel and loss, steam/power/hydrogen/cooling-water consumption, unit availability, unplanned shutdowns, catalyst performance, flare volumes, environmental indicators, maintenance downtime, laboratory exceptions, previous-month and budget targets.

### Step 2: Export and normalise

Export data into Excel and manually rename tags, convert units, align time intervals, remove bad-quality values, reconcile mass and volume bases, check production-accounting totals, add comments for missing data, align actuals with budget and plan.

### Step 3: Calculate KPIs

Throughput vs. plan, yield variance, energy variance, product-quality compliance, availability, reliability, fuel and loss, hydrogen consumption, catalyst consumption, unplanned downtime, economic impact.

### Step 4: Create charts and narrative

Monthly trend charts, plan-versus-actual bars, unit-performance tables, Pareto chart of losses, quality trend, energy trend, event timeline, action tracker.

### Step 5: Review

Process engineer prepares → unit head reviews → operations validates production → laboratory validates quality → planning validates throughput and economics → maintenance validates downtime → refinery management reviews → final report stored.

## Time estimate

| Activity | Typical elapsed time |
|---|---|
| Finding and exporting data | 2–6 hours |
| Cleaning and reconciling data | 2–6 hours |
| Actual engineering analysis | 2–5 hours |
| Chart and document preparation | 2–5 hours |
| Review and corrections | 1–4 hours |
| Total | 1–3 working days |

## AI intervention for process engineer workflows

Read-only data: Historian, DCS events, LIMS, EAM, shift logs, production reports, operating procedures, design basis.

Output: Daily unit brief, event timeline, calculations with source references, Excel trend workbook, Word technical note, PowerPoint unit-review deck.

Human gate: Process engineer validates; unit head and data owners approve.
