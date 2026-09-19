# Operations and Shift Engineer

## Role

The operations or shift engineer is responsible for safe and stable real-time operation. Compared with the process engineer, this role is more time-critical and closer to the plant.

## Typical shift

### Shift start

- Receive handover from the outgoing team
- Review unit status
- Check abnormal conditions
- Review equipment in or out of service
- Confirm permits and isolations
- Review tank levels and product movements
- Check alarms, trips and bypasses
- Review operating targets and constraints
- Confirm manpower and contractor activity

A structured shift handover is valuable because refinery handover quality affects situation awareness.

### During the shift

- Monitor the control room and field
- Adjust operating conditions within approved limits
- Coordinate with panel and field operators
- Issue or verify work permits
- Confirm process isolations
- Respond to alarms and abnormal situations
- Coordinate with maintenance and HSE
- Monitor product quality and tank movements
- Record events and operating changes
- Escalate deviations
- Prepare the outgoing handover

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

**Current task:** During a compressor trip, the shift engineer must decide whether the unit can remain stable, what equipment is available, what operating procedure applies and whether a shutdown is required. The engineer may consult DCS alarm sequence, emergency operating procedure, cause-and-effect diagram, equipment status, shift log, current permits, operating envelope, maintenance status and previous trip reports.

**AI-assisted task:** A read-only assistant displays the event timeline, retrieves the relevant approved procedure, lists active permits and isolations, identifies similar historical trips and prepares a handover message. It must not issue control commands or replace the authorised operator.

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

**Read-only data:**

- DCS alarm and event history
- Historian
- Electronic logbook
- Permit and isolation records
- EAM
- Operating procedures
- LIMS
- Tank and inventory systems

**Output:**

- Shift summary
- Event timeline
- Open-action list
- Procedure retrieval
- Draft abnormal-event report
- Next-shift handover note

**Human gate:**

- Shift engineer validates the summary
- Operations supervisor accepts the handover
- Authorised operator controls the plant
- HSE or incident team determines formal classification

## Persona table

| Attribute | Typical profile |
|---|---|
| Technical comfort | Moderate; comfortable with DCS and operational systems, less interested in complex office software |
| Primary device | Control-room workstation; rugged tablet or radio/mobile in field |
| Location | Control room, field, permit station and unit area |
| Shift pattern | Rotating 24/7 shifts |
| AI willingness | High during routine information retrieval; cautious during live abnormal events |
| Main concern | Slow response, unreliable information, screen overload and unsafe recommendations |
| Best interface | Fast search, event timeline, approved procedure retrieval and voice-friendly interaction |
