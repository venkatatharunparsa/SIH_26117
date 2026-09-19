# Technical Deviation Investigation Note

Purpose: explains a product-quality, process, energy or operating deviation. Typical length: 4–12 pages plus data workbooks and trend charts.

## Structure

### Cover and control

Title, unit and stream, deviation number, date, revision, prepared/reviewed/approved fields, confidentiality.

### 1.0 Event summary

| Field | Value |
|---|---|
| Event | Diesel sulphur excursion |
| Unit | Diesel hydrotreating |
| First detection | 14-Sep-2026 12:10 IST |
| Specification | ≤10 ppm |
| Maximum result | 18 ppm |
| Product affected | 4,200 tonnes |
| Current status | Product quarantined |

### 2.0 Event date, time, unit and stream

First indication, confirmed time, unit, equipment or stream, campaign/batch/tank, start and end of affected period.

### 3.0 Specification and actual result

Applicable product standard, required limit, actual laboratory result, online analyser result, repeat test, sample ID, test method, measurement uncertainty.

### 4.0 Quantity and commercial impact

Volume or mass affected, product routed or quarantined, reprocessing/blending requirement, customer/shipment impact, estimated loss, regulatory impact.

### 5.0 Immediate containment

Product hold, routing change, rate reduction, severity increase, repeat sampling, equipment check, customer/dispatch notification, authority who approved containment.

### 6.0 Data sources

LIMS sample IDs, historian tags and time period, DCS alarm/event records, EAM work orders, shift log, operating procedure, crude/feed assay, online analyser record, emails or meeting minutes, previous comparable event.

### 7.0 Trend charts

Recommended figures: product sulphur vs. specification, feed sulphur, reactor temperature, hydrogen-to-oil ratio, reactor pressure, product flow, analyser vs. laboratory result, relevant alarm timeline.

Every chart should show: time zone, units, tag or source, aggregation interval, missing-data treatment.

### 8.0 Analysis and calculations

Material balance, mass of sulphur entering and leaving, weighted-average product quality, operating-severity comparison, hydrogen availability, feed-change analysis, statistical comparison with stable operation, instrument validation.

### 9.0 Root cause and contributing factors

Separate: direct cause, technical root cause, contributing causes, data or measurement issue, organisational/system cause, uncertainty.

Avoid concluding "operator error" unless the investigation identifies why the error occurred and why controls did not prevent it.

### 10.0 Corrective actions

| ID | Action | Owner | Due date | Verification |
|---|---|---|---|---|
| CA-01 | Calibrate online sulphur analyser | Instrumentation | 20-Sep-2026 | Calibration certificate |
| CA-02 | Revise operating limit for hydrogen ratio | Process | 25-Sep-2026 | Approved procedure |

### 11.0 Preventive actions

Procedure change, alarm or interlock review, training, additional sampling, equipment modification, MOC, maintenance strategy, control-loop improvement, data-quality control.

### 12.0 Approval and closeout

Typical reviewers: process engineering, operations, laboratory/quality, instrumentation, maintenance, planning/production, HSE or process safety, unit/refinery head.

### 13.0 Attachments

Raw data workbook, LIMS certificates, historian export, DCS event log, shift log, EAM history, calculation sheet, photographs, corrective-action tracker.

## Good vs. bad

Good: distinguishes laboratory from online analyser result, states affected time window, quantifies product affected, shows containment, uses time-aligned trends, identifies evidence gaps, gives owners and dates.

Bad: copies chart without tag names or units, treats one sample as proof of prolonged excursion, ignores sampling or analyser validity, gives root cause without testing alternatives, lists actions without verification.
