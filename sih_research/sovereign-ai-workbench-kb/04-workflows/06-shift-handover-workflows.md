# Shift Handover Workflows

## A. Shift start

**Step 1: Receive verbal and written handover**

The incoming shift engineer receives: verbal handover from outgoing engineer, shift logbook, handover note, control-room event list, open permits, isolation list, equipment status, tank status, unit constraints, abnormal conditions, contractor activity list.

The handover may be: electronic logbook, Word or Excel file, EAM notification list, paper logbook, email, or shift-management application.

Structured shift handover improves situation awareness and completeness compared with an unstructured logbook, according to refinery handover research.

**Step 2: Check systems**

The engineer checks:

- DCS overview screens
- Alarm summary
- Historian current trends
- EAM open work orders
- Permit-to-work system or permit register
- Isolation/LOTO system
- Tank and inventory dashboard
- LIMS quality results
- Email and shift communication channel
- Fire-and-gas system, where authorised
- Utility status

**Step 3: Confirm priorities**

The incoming engineer confirms: units on normal operation, units on startup or shutdown, equipment unavailable, safety-critical permits, simultaneous operations, product-quality risks, tank or pipeline movements, maintenance constraints, any emergency or regulatory watch item.

## B. Compressor-trip abnormal event

**Step 4: Receive alarm**

The DCS or SIS generates: compressor trip alarm, low suction pressure, high vibration, high discharge temperature, motor overload, seal-system failure, fire-and-gas alarm.

The panel operator and shift engineer coordinate immediate response under the approved emergency or abnormal operating procedure.

**Step 5: Consult approved procedure**

The engineer retrieves: emergency operating procedure, cause-and-effect diagram, compressor operating manual, unit operating instructions, restart checklist, previous trip report, equipment availability.

The procedure should come from the controlled document repository, not an unverified shared-drive copy.

**Step 6: Check DCS and historian**

The engineer reviews: alarm sequence, trip cause, pressures and temperatures, flow decay, valve positions, standby equipment start, interlock response, recycle flow, process response before and after trip.

The historian is used for event reconstruction; DCS is used for current state and alarm information.

**Step 7: Check operations and maintenance status**

The engineer checks: EAM work orders, active permits, isolation status, maintenance work on the compressor, standby-compressor availability, spare equipment, process-unit constraints, tank and product routing.

**Step 8: Decide immediate response**

The shift engineer may decide, within approved procedures, to: stabilise the unit at reduced rate, start standby equipment, divert feed or product, reduce throughput, isolate equipment, notify maintenance and instrumentation, initiate controlled shutdown, escalate to the operations manager and HSE.

The AI should not make or execute these decisions. It may retrieve procedures and provide a read-only context panel.

**Step 9: Log the event**

The operator or shift engineer records: time of trip, initial alarm, actions taken, equipment state, process response, personnel notified, permit or isolation actions, production impact, safety or environmental consequence, current status.

The record may be entered in: electronic logbook, DCS event log, EAM notification, incident system, email, or paper logbook.

**Step 10: Prepare abnormal-situation report**

The report includes: event description, timeline, operating conditions, alarm sequence, immediate cause (if known), actions, impact, equipment condition, required investigation, follow-up owner.

**Step 11: Shift end**

The engineer prepares the handover by combining: DCS status, historian trends, open permits, isolation list, EAM work orders, tank status, product quality, abnormal event status, pending decisions, next-shift instructions.

The handover is sent to: incoming shift engineer, operations supervisor, unit head, maintenance, process engineering, HSE (where relevant).

## Time estimate

| Activity | Typical elapsed time |
|---|---|
| Routine handover preparation | 0.5–2 hours per shift |
| Abnormal event reconstruction | 1–4 hours |
| Immediate response | Minutes to hours |
| Formal incident/abnormal report | 2–8 hours |
| People involved | 3–12 people |

Manual copying and formatting may consume 30–60% of routine handover preparation.

## AI intervention

Read-only data: DCS alarm and event history, historian, electronic logbook, permit and isolation records, EAM, operating procedures, LIMS, tank and inventory systems.

Output: Shift summary, event timeline, open-action list, procedure retrieval, draft abnormal-event report, next-shift handover note.

Human gate: Shift engineer validates the summary; operations supervisor accepts the handover; authorised operator controls the plant; HSE or incident team determines formal classification.

## Documents created

- Shift log
- Handover note
- Daily production report
- Unit operating log
- Alarm and trip report
- Abnormal situation report
- Deviation report
- Permit-to-work request or clearance
- Isolation certificate
- Line-up sheet
- Tank movement report
- Product-quality deviation note
- Equipment-status report
- Operations notification to maintenance
- Incident or near-miss report

## What is manual

- Writing or typing shift logs
- Reconstructing events from DCS alarms
- Copying production figures into reports
- Checking multiple permit records
- Confirming isolation status across paper and digital records
- Creating daily production summaries
- Compiling outstanding work and abnormal conditions
- Sending repetitive email updates
- Searching operating procedures during abnormal events
- Preparing management reports from shift notes

## What is time-critical

- Loss of containment
- High pressure or temperature
- Compressor, furnace or pump trip
- Fire-and-gas alarm
- Power or utility failure
- Loss of cooling water or instrument air
- Product-quality excursion
- Flare event
- Tank overfill risk
- Permit or isolation conflict
- Restart after maintenance

## Example

Current task: During a compressor trip, the shift engineer must decide whether the unit can remain stable, what equipment is available, what operating procedure applies and whether a shutdown is required. The engineer may consult DCS alarm sequence, emergency operating procedure, cause-and-effect diagram, equipment status, shift log, current permits, operating envelope, maintenance status and previous trip reports.

AI-assisted task: A read-only assistant displays the event timeline, retrieves the relevant approved procedure, lists active permits and isolations, identifies similar historical trips and prepares a handover message. It must not issue control commands or replace the authorised operator.

## Good vs. bad handover

Good: current and time-stamped, focuses on what the next shift must know, lists live permits and isolations, separates confirmed facts from assumptions, identifies unresolved risks, uses equipment tags and work-order numbers.

Bad: long narrative with no priorities, omits equipment unavailable, fails to list active permits, uses informal names instead of tags, copies yesterday's handover without updating status.
