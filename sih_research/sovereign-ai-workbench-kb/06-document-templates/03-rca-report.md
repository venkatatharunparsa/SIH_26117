# Root Cause Analysis Report

Purpose: records why a failure occurred and how recurrence will be prevented. Typical length: simple equipment RCA 5–15 pages; major failure 20–60 pages with attachments.

## Structure

### Cover

RCA number, equipment tag, unit, failure date, report revision, investigation team, approval status.

### 1.0 Executive summary

What failed, consequence, immediate restoration, root cause, main corrective action, recurrence risk.

### 2.0 Problem statement

A good statement is measurable:

> P-204A experienced three mechanical-seal failures between April and September 2026, causing 14.5 hours of reduced unit throughput and two emergency interventions.

### 3.0 Equipment details

Tag, manufacturer/model, service, design duty, operating duty, motor, seal, bearings, materials, installation date, criticality, standby arrangement.

### 4.0 Event chronology

| Time | Event | Source | Confidence |
|---|---|---|---|
| 02:14 | Vibration alarm | DCS historian | High |
| 02:16 | Pump tripped | DCS event log | High |
| 02:21 | Standby started | Shift log | Medium |
| 04:30 | Seal leakage observed | Operator statement | Medium |

### 5.0 Immediate cause

Examples: mechanical seal failed, bearing overheated, motor overload occurred, pump lost suction, impeller was damaged.

### 6.0 Technical root cause

Examples: cavitation caused by inadequate NPSH, misalignment due to pipe strain, wrong seal material for fluid service, lubrication contamination, repeated operation outside design flow range.

### 7.0 Systemic causes

Examples: inadequate preventive-maintenance task, no alarm-response procedure, spare specification not controlled, work-order closeout did not record failure mode, contractor repair not independently verified, similar-failure lessons not shared.

### 8.0 Evidence

EAM work orders, historian trends, DCS alarms, vibration reports, oil-analysis results, inspection findings, photographs, vendor report, P&ID and datasheet, spare-parts record, operator interviews, previous RCA.

### 9.0 Analysis method

State whether the team used: Five Whys, Fishbone, Fault tree, FMEA, Barrier analysis, Change analysis, Pareto of failures.

### 10.0 Corrective actions

Immediate restoration: replace failed part, align equipment, repair piping support, restore instrumentation, inspect standby equipment.

### 11.0 Preventive actions

Longer-term: change seal design, revise operating envelope, add vibration monitoring, revise PM frequency, update spare specification, modify piping, train operators, add similar-equipment check.

### 12.0 Action register

Owner, due date, priority, cost, status, verification.

### 13.0 Verification method

Examples: no repeat failure for 90 days, vibration below defined limit, successful trial run, revised PM completed, work-order coding audited, operating limit embedded in procedure, reliability KPI improved.

### 14.0 Lessons learned

What should be transferred to similar pumps, other units, turnaround scope, maintenance strategy, training, design standards.

### 15.0 Approval

Reliability engineer, maintenance manager, operations manager, mechanical engineering, process engineering, HSE (if relevant), unit/refinery head.

## Good vs. bad

Good: uses evidence and chronology, distinguishes immediate/technical/systemic causes, avoids vague "human error," includes verification, assigns action ownership, checks similar equipment.

Bad: ends at failed component, recommends "train operator" without identifying system failure, uses unsupported causal language, has no evidence table, does not verify effectiveness.
