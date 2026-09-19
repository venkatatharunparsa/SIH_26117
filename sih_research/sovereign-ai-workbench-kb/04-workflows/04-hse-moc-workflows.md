# HSE and MOC Workflows

## MOC (Management of Change) review

### A. Proposal arrival

**Step 1: Receive MOC request**

The proposal may arrive through: MOC workflow system, email attachment, project document-management system, engineering change request, EAM or project-management system, or paper form converted to PDF.

The request should identify: existing condition, proposed change, reason, unit and equipment, temporary or permanent status, technical basis, expected duration, safety impact, environmental impact, training requirement, required completion date, responsible owner.

### B. Identify affected documents and systems

**Step 2: Search document management or shared drives**

The HSE officer searches for: current P&IDs, PFDs, equipment datasheets, control narratives, cause-and-effect diagrams, operating procedures, emergency procedures, inspection plans, maintenance strategies, fire-and-gas drawings, relief-system documents, previous MOCs, HAZOP studies, LOPA/SIL assessments, PSSR records.

The major problem is identifying the approved current revision, not merely finding a document with the right words.

**Step 3: Check asset and tag relationships**

The officer checks: equipment master, line list, instrument index, valve list, area and unit hierarchy, related work orders, active permits, isolation plans, inspection records.

If the change affects a valve, for example, the workbench should find: the valve on the P&ID, its datasheet, control-system tag, maintenance strategy, interlock or cause-and-effect reference, relevant HAZOP node, previous MOC.

**Step 4: Check HAZOP and action registers**

The officer searches HAZOP records for: same node, same deviation, same safeguard, similar equipment, open recommendations, previous changes, safety-critical actions.

HAZOP documents may be stored in: document-management system, shared drive, project archive, scanned PDF, or consultant deliverable.

**Step 5: Check operational and maintenance impact**

The HSE officer consults: EAM work orders, permit system, current isolation plans, shift logs, operating procedures, inspection and integrity records, training records, emergency-response plans, environmental records.

### C. Send review requests

**Step 6: Identify reviewers**

The HSE officer sends the proposal to relevant departments: process engineering, operations, mechanical, electrical, instrumentation and control, inspection, maintenance, projects, laboratory, environment, fire and emergency services, IT/OT cybersecurity (if control systems are affected), legal or regulatory affairs (where required).

The request may be sent by email with: MOC form, P&ID markup, technical datasheet, review checklist, due date, required response format.

### D. Perform risk review

**Step 7: Review technical basis**

The officer checks: why the change is needed, whether the design basis is adequate, whether operating limits change, whether hazards are introduced, whether relief capacity changes, whether control logic changes, whether materials compatibility changes, whether environmental emissions change, whether inspection or maintenance needs change.

**Step 8: Review HAZOP implications**

The team decides whether: existing HAZOP remains valid, a focused HAZOP is needed, a full HAZOP revalidation is needed, LOPA or SIL review is needed, emergency procedures must change, operator training is required.

**Step 9: Prepare checklist**

The checklist may include: process safety, mechanical integrity, electrical safety, instrumentation and SIS, fire and gas, environmental impact, operating procedure, maintenance strategy, inspection plan, training, drawings, spare parts, emergency response, regulatory approval, PSSR.

### E. Approval and closeout

**Step 10: Compile comments**

The HSE officer consolidates: department comments, open actions, action owners, due dates, risk ranking, required controls, required documents to be updated.

**Step 11: Route approval**

Likely route: change initiator → technical owner → operations → maintenance/integrity → instrumentation/electrical → HSE/process safety → unit or refinery head → project or corporate authority if capital work is involved.

**Step 12: Verify implementation**

Before startup or return to service: updated drawings are available, procedures are revised, training is complete, inspection and maintenance plans are updated, PSSR is complete, permits and isolations are closed, HAZOP actions are addressed, P&ID and equipment records are updated, MOC is formally closed.

## Time estimate

| Activity | Typical elapsed time |
|---|---|
| Register and classify proposal | 0.5–2 hours |
| Find affected documents | 2–12 hours |
| Send and track reviews | 1–5 days |
| Technical risk review | 4–16 hours |
| HAZOP or focused study | 1–5 days |
| Final approval and PSSR | 1–10 days |
| People involved | 5–15 people |

Finding and assembling evidence may be 40–70% of the effort for a complex MOC.

## AI intervention

Read-only data: MOC form, document-management repository, P&IDs, PFDs and datasheets, HAZOP/LOPA/SIL records, EAM, permit and isolation records, operating procedures, training records, previous MOCs.

Output: Affected-document list, revision and approval check, related HAZOP actions, reviewer list, draft checklist, change-impact matrix, open-action tracker, draft review pack.

Human gate: HSE and process-safety professionals decide risk acceptability; technical authorities approve design; operations authorises implementation; PSSR team confirms readiness.

## Documents produced

### Permit and work-control documents

- Hot-work permit
- Cold-work permit
- Confined-space permit
- Electrical-work permit
- Excavation permit
- Line-breaking permit
- Vehicle-entry permit
- Gas-test certificate
- Isolation certificate
- Blind-list or lockout/tagout record
- Job safety analysis
- Risk assessment
- Toolbox-talk record
- Permit closeout

### Process-safety documents

- HAZOP worksheet
- HAZID report
- LOPA assessment
- SIL assessment
- MOC proposal
- MOC review sheet
- PSSR checklist
- Operating-procedure update
- Safety-critical-equipment register
- Process-safety information file
- Emergency-response plan
- Alarm and trip review
- Relief-system review
- Process-safety audit report

### Incident and compliance documents

- Initial incident notification
- Near-miss report
- Internal investigation report
- Root-cause analysis
- Corrective-action tracker
- Environmental incident report
- OISD compliance report
- Factory or statutory report
- Fire and emergency-drill report
- Contractor-safety audit
- Training and competency record
- Environmental statement
- Consent-condition compliance statement

OISD states that major onsite incidents should be investigated by the company and that the internal investigation report should be submitted within one month.

## What is repetitive

- Checking whether permits contain all required fields
- Verifying gas-test validity and isolation status
- Comparing job scope with hazard controls
- Tracking overdue corrective actions
- Copying incident details into multiple forms
- Repeatedly extracting information from photographs, scanned permits and handwritten forms
- Preparing monthly safety statistics
- Compiling audit evidence
- Mapping procedures to statutory requirements
- Updating HAZOP and MOC action registers
- Preparing training attendance and competency reports
- Producing management presentations

## What is high-risk for AI

The HSE role has a lower tolerance for plausible but unsupported text. An AI system should not:

- Approve a permit autonomously
- Determine that an area is gas-free
- Override an isolation
- Close an incident action without evidence
- Decide that an MOC is safe
- Replace a competent HAZOP team
- Infer that a control is effective because a document says it exists

## Example: MOC review

Current task: A project proposes replacing a control valve with a different material and changing the operating range. The HSE/process-safety officer reviews the existing P&ID, datasheet, material specification, process conditions, relief and control-system implications, HAZOP actions, operating procedure, maintenance requirements, training needs, emergency-response implications and PSSR checklist.

AI-assisted task: The system identifies all affected documents, compares the old and proposed specifications, lists required reviewers, extracts similar historical MOCs and drafts a review checklist. The responsible engineer still decides whether the change is acceptable.
