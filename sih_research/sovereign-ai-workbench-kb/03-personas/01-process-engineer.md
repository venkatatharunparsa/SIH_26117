# Process Engineer

## Role

The process engineer is the technical owner of one or more process units. In an MRPL-type refinery, that could include CDU/VDU, hydrocracking, diesel hydrotreating, PFCC, delayed coking, hydrogen, sulphur recovery, polypropylene or utilities.

The role sits between operations, planning, laboratory, maintenance, projects and management. The engineer converts plant data into decisions about throughput, yield, energy, quality, catalyst performance, constraints, operating limits, unit stability, process safety and commercial value.

## Typical day

### Start of day

- Production and throughput against plan
- Unit feed rate and product rates
- Product quality results
- Energy consumption and fuel losses
- Flare events
- Major alarms, trips and process deviations
- Equipment outages and bypasses
- Catalyst or chemical consumption
- Tank inventory and blending constraints
- Work permits and maintenance activities affecting the unit
- Unresolved shift-handover issues

May attend a morning production or operations meeting involving operations, planning, laboratory, maintenance, inspection and HSE.

### During the day

- Trending unit variables from the process historian
- Comparing actual performance with design or operating targets
- Investigating yield, quality or energy deviations
- Reviewing laboratory results against online analysers
- Advising operations on feed-rate, temperature, pressure, recycle or severity changes
- Checking hydraulic, furnace, compressor, hydrogen or heat-exchanger constraints
- Preparing operating recommendations
- Reviewing temporary operating instructions or deviations
- Supporting incident or abnormal-event investigation
- Attending HAZOP, MOC, PSSR or project-review meetings
- Evaluating catalyst performance and fouling
- Preparing daily, weekly and monthly technical reports
- Supporting crude selection and refinery planning

## Data used

| Source | Typical information |
|---|---|
| Historian | Flow, pressure, temperature, level, composition, valve position, compressor performance |
| DCS | Real-time control variables, alarms, interlocks, trips, controller output |
| Laboratory system | Sulphur, density, viscosity, distillation, octane, product quality, feed assays |
| ERP / production accounting | Material movements, production quantities, inventory, consumption, losses |
| Planning and scheduling | Crude slate, unit targets, product demand, tank constraints, shipment schedules |
| EAM / maintenance system | Equipment status, work orders, breakdowns, bypasses, planned outages |
| Engineering documents | PFDs, P&IDs, design basis, datasheets, operating manuals, vendor guarantees |
| HSE systems | MOC, HAZOP actions, incident reports, operating limits, permit information |
| Email and shared drives | Informal decisions, vendor advice, previous analyses, meeting actions |

## Calculations

- Material and component balances
- Heat balances
- Yield reconciliation
- Distillation cut-point calculations
- Furnace-duty calculations
- Heat-exchanger performance and fouling calculations
- Hydraulic calculations
- Pressure-drop calculations
- Compressor and pump performance calculations
- Hydrogen balance and consumption analysis
- Catalyst activity and deactivation analysis
- Octane, sulphur or other product-quality calculations
- Energy-intensity calculations
- Flare and relief-load checks
- Utility consumption analysis
- Debottlenecking studies
- Crude-blending studies
- Economic comparisons of alternative operating modes
- Simulation studies
- Statistical analysis of historian and laboratory data
- Operating-window and constraint analysis

## Documents created or reviewed

### Daily and routine

- Daily production report
- Unit performance report
- Shift-handover review
- Operating instruction
- Abnormal operating note
- Product-quality deviation note
- Energy report
- Yield-reconciliation sheet
- Catalyst-performance report
- Technical-service note
- Weekly and monthly unit review

### Engineering and approval

- Process design basis
- PFD and P&ID review comments
- Operating envelope
- Process datasheet
- Technical query response
- MOC technical evaluation
- HAZOP action response
- Cause-and-effect review
- Relief-system review
- Process calculations
- Project design review note
- Pre-startup safety review input
- Commissioning and performance-test report
- Investment or debottlenecking proposal

## What takes the most time

The highest manual burden is not the calculation itself. It is assembling reliable input data.

- Finding the latest P&ID or operating procedure
- Reconciling historian values with laboratory results
- Correcting bad tags, missing samples or inconsistent timestamps
- Copying data from several systems into Excel
- Cleaning equipment and stream names
- Reconstructing what happened during a trip from alarms, logs and emails
- Comparing current operating performance with old reports
- Formatting management presentations
- Finding the design basis behind a current operating limit
- Tracking action items from HAZOP, MOC and technical meetings
- Repeating calculations for slightly different feed or operating scenarios

## AI opportunities

- Produce a morning unit-performance summary from historian, laboratory, DCS and shift-log data
- Identify the five largest deviations from target
- Explain which operating variables changed before a quality excursion
- Compare current conditions with design limits and previous successful campaigns
- Draft a technical note with charts and source references
- Reconcile laboratory and online-analyser results
- Extract all operating limits from approved manuals and P&IDs
- Generate a first-pass MOC technical review
- Prepare an Excel material balance from selected historian periods
- Produce a PowerPoint unit-review deck automatically

## Example

**Current task:** A diesel hydrotreating engineer investigates a sulphur excursion. Several hours spent downloading reactor and feed data, finding laboratory results, checking hydrogen purity, reviewing catalyst-cycle history, searching shift logs and maintenance records, preparing charts and a deviation report.

**AI-assisted task:** The engineer asks:

> "Explain the increase in diesel sulphur from 12:00 on 14 September. Compare feed sulphur, reactor temperature, hydrogen-to-oil ratio, reactor pressure, analyser status, laboratory results, recent work orders and the approved operating envelope. Produce an Excel trend workbook and a one-page technical note with citations."

The system returns evidence, not an unsupported conclusion. The engineer approves the diagnosis.

## Persona table

| Attribute | Typical profile |
|---|---|
| Technical comfort | High; comfortable with Excel, historian trends, process simulation and technical documents |
| Primary device | Desktop or laptop with multiple monitors |
| Location | Engineering office, control room, laboratory or field unit |
| Shift pattern | Usually day shift; may support night incidents and shutdowns |
| AI willingness | High if the output is traceable and technically defensible |
| Main concern | Incorrect recommendations, bad data and inability to verify sources |
| Best interface | Conversational search plus trend charts, calculations, source citations and export to Excel/Word/PPT |
