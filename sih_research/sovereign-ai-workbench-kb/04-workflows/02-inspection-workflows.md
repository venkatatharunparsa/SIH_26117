# Inspection Engineer Workflows

## A. Scanned inspection report processing

### Step 1: Contractor performs inspection

The contractor may perform ultrasonic thickness measurement, radiography, magnetic-particle testing, dye-penetrant testing, visual inspection, hardness testing, positive material identification, weld inspection, tank-floor scanning, or tube inspection.

Contractor may record readings on paper forms, handheld inspection software, Excel, PDF templates, photographs, or annotated drawings.

Final package may arrive as: searchable PDF, scanned image-only PDF, Excel workbook, email attachment, physical file, shared-folder upload, or EAM attachment.

### Step 2: Receipt by inspection department

The inspection engineer or inspection coordinator receives the report by email, contractor portal, EAM inspection notification, shared drive, turnaround document-control system, or physical document-control register.

The package is assigned: equipment tag, inspection date, contractor name, work order or inspection number, report revision, area or unit, reviewer.

Document controller saves the PDF in a structured folder such as:

Unit / Equipment Tag / Inspection Type / Year / Contractor / Revision

### Step 3: Identify format

The engineer checks whether the report contains machine-readable tables, image-only pages, marked-up drawings, handwritten values, multiple equipment tags, separate readings by shell/head/nozzle/pipe circuit, or units in millimetres or inches.

### Step 4: Extract values

Possible current practices: copy-paste from Excel, manual typing from PDF, OCR extraction, contractor-uploaded structured file, manual transcription from paper, direct import from handheld equipment.

Even where OCR exists, the inspection engineer usually validates critical values manually.

**Sensitive data:** Minimum thickness, corrosion rate, remaining life, defect location, weld quality, unsafe equipment condition, temporary repair status.

### Step 5: Match readings to equipment and location

The engineer matches equipment tag, line number, circuit number, inspection point, drawing coordinate, orientation, weld number, nozzle number, grid location, date, and previous measurement point.

Sources consulted: P&ID, isometric, equipment datasheet, inspection drawing, line list, EAM equipment master, previous inspection report, RBI or inspection-management system.

This is a major source of error. A reading can be numerically correct but associated with the wrong equipment or wrong measurement location.

### Step 6: Select comparison readings

The engineer chooses:

- Current thickness (t2)
- Previous thickness (t1)
- Current inspection date (d2)
- Previous inspection date (d1)
- Nominal thickness
- Minimum required thickness

Long-term corrosion rate:
CR_LT = (t_previous − t_current) / (d_current − d_previous)


Short-term rate:

CR_ST = (t_previous − t_current) / Δt




The engineer checks: same location, instrument uncertainty, physical plausibility, damage-mechanism change, process-condition change, local pit or general thinning, whether the rate should be conservatively adjusted.

### Step 7: Update RBI or integrity record

The engineer updates: current thickness, corrosion rate, remaining life, probability-of-failure input, consequence category, risk ranking, inspection interval, next inspection method, integrity operating window, recommendation status.

This may occur in RBI software, inspection-management module, EAM, Excel template, or controlled integrity database.

### Step 8: Decide whether FFS is required

An FFS assessment may be triggered by thickness below or near minimum allowable, crack-like indication, localised pitting, bulging or deformation, leak or through-wall defect, damaged nozzle, creep or high-temperature damage, fire or overpressure exposure, unusual NDT result, or inability to meet original design assumptions.

### Step 9: Gather FFS inputs

Retrieve: design pressure and temperature, operating pressure and temperature, material grade, weld efficiency, corrosion allowance, original design code, geometry, defect dimensions, inspection uncertainty, stress analysis, transient history, fluid service, future operating period, repair or mitigation options.

Data may be distributed across: equipment datasheet, mechanical design file, P&ID, vendor drawing, inspection report, historian, EAM, process engineer's note, contractor NDT package.

### Step 10: Perform or commission assessment

The engineer may perform calculations in a spreadsheet or approved engineering software. A specialist or third party may be involved for complex defects.

Outputs may include remaining-life estimate, allowable pressure, temporary operating restriction, repair or replacement requirement, inspection frequency, FFS conclusion, and engineering-critical assessment.

### Step 11: Draft recommendation note

Contains: equipment identification, defect description, inspection evidence, calculation basis, applicable standard or code, current risk, proposed action, operating restrictions, repair deadline, monitoring requirement, required approvals, attachments.

### Step 12: Review and approval

Likely route: inspector or contractor provides data → inspection engineer validates readings → integrity/corrosion engineer performs assessment → mechanical engineering reviews calculation → process engineering confirms operating conditions → operations confirms feasibility of restrictions → HSE/process safety reviews risk → inspection head or engineering head signs → refinery head approves continued operation, repair or shutdown → EAM, RBI or action tracker records the decision.

## Time estimate

| Activity | Typical elapsed time |
|---|---|
| Receive, register and classify report | 0.5–2 hours |
| Read and extract data | 2–8 hours |
| Match tags and historical points | 2–8 hours |
| Corrosion calculation and RBI update | 2–8 hours |
| FFS assessment | 1–5 days |
| Recommendation and approval | 1–5 working days |
| People involved | 3–8 people |

A large scanned or inconsistent report can make finding and assembling 50–70% of total effort.

## B. Corrosion-rate calculation and RBI update

### Workflow steps

1. Select comparison readings (current, previous, dates, nominal, minimum required)
2. Calculate long-term or short-term corrosion rate
3. Check same location, instrument uncertainty, physical plausibility, damage-mechanism change, process conditions, local pit vs. general thinning
4. Update RBI: current thickness, corrosion rate, remaining life, probability of failure, consequence category, risk ranking, inspection interval, next method, integrity operating window, recommendation status
5. Record in RBI software, inspection-management module, EAM, Excel template, or controlled integrity database

## C. Fitness-for-service assessment

### Workflow steps

1. FFS triggered by thickness below minimum, crack-like indication, localised pitting, bulging, leak, damaged nozzle, creep, fire damage, unusual NDT result
2. Gather FFS inputs (design conditions, material, weld efficiency, corrosion allowance, design code, geometry, defect dimensions, stress analysis)
3. Perform or commission assessment (spreadsheet or approved software; specialist may be involved)
4. Produce remaining-life estimate, allowable pressure, temporary restriction, repair requirement, inspection frequency, FFS conclusion, engineering-critical assessment
5. Draft recommendation note
6. Route for approval

## AI intervention for inspection workflows

**Read-only data:** Inspection PDFs, OCR/image content, equipment master, P&IDs and isometrics, previous reports, RBI data, design datasheets, historian operating conditions, EAM work orders.

**Output:** Structured inspection table, confidence score for each extracted value, tag and location matching suggestions, thickness trend, corrosion-rate calculation, missing-data list, draft RBI update, draft recommendation note, Excel thickness chart.

**Human gate:** Inspection engineer validates every critical reading; integrity engineer approves corrosion rate and remaining life; authorised engineer approves FFS; operations and HSE approve operating restrictions.
