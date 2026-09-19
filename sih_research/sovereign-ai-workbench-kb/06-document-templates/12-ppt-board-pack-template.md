# PPT Board-Pack Template

The SIH problem statement requires PowerPoint as one of the deliverable formats. This template documents the structure, content sources and design conventions for board and management presentations.

## Purpose

Management presentations are used for:

- Monthly unit or refinery performance review
- Capital-expenditure approval
- Turnaround planning and progress
- Incident review to management
- Annual budget and strategy
- Project progress and gate reviews
- Audit and compliance updates

Length: 10–30 slides for a management review; 5–10 slides for a decision item.

## Standard structure

### Slide 1: Title

Organisation, unit or project, title, date, prepared by, classification marking, revision.

### Slide 2: Executive summary (the "one-slide")

Four to six bullets. What is the decision or message? What are the key numbers? What is being asked? What is the risk of not acting?

This is the most important slide. A senior manager should be able to make a decision from this slide alone if needed.

### Slide 3: Context

Why this matters now. What has changed since the last review. What triggered this update.

### Slide 4: Performance vs. plan

For performance reviews:

- Throughput vs. plan
- Yield
- Energy intensity
- Quality compliance
- Availability
- Safety (LTIFR, near misses, incidents)
- Environmental indicators

Table format with plan, actual, variance, trend arrow.

### Slide 5: Financial summary

For approval or review:

- Capital cost
- Operating cost impact
- Payback or NPV
- Budget source
- Cash-flow impact

### Slide 6: Key issues or deviations

Bulleted list of the three to five most important issues, each with:

- Issue
- Impact
- Cause or hypothesis
- Proposed action
- Owner and due date

### Slide 7: Technical or operational detail

Supporting chart or diagram relevant to the item. One message per slide.

### Slide 8: Options considered

For decision items: show alternatives in a table with cost, benefit, risk, recommendation.

### Slide 9: Risks and mitigations

Table with probability, impact, mitigation, owner.

### Slide 10: Recommendation

Clear, actionable. What is being asked? Amount, scope, route, conditions, decision date.

### Slide 11: Approvals

Prepared by, reviewed by, concurred by, approved by. Date, signature block.

### Slides 12–N: Annexures

Detail slides by exception (only if a manager asks). Technical data, charts, schedules, spreadsheets.

## Design conventions

- One message per slide
- 16:9 aspect ratio (modern standard)
- Font: Arial or Calibri, 18–24 pt body, 28–32 pt title
- Colour palette: customer standard; avoid red-green only (accessibility)
- Charts: line charts for trends, bar charts for comparisons, waterfall for variance
- Data tables: RAG status (Red / Amber / Green) for exception highlighting
- Footnotes: source for every number
- Classification marking: top-right or footer of every slide
- Revision: on title slide

## Data sources per slide

| Slide | Primary sources |
|---|---|
| Executive summary | Multiple — synthesize from below |
| Performance vs. plan | Historian, LIMS, ERP production accounting, EAM |
| Financial summary | ERP, budget, project cost reports |
| Key issues | Shift logs, incident system, EAM, HSE |
| Technical detail | Historian, drawings, inspection reports |
| Options considered | Technical evaluation, procurement, finance |
| Risks and mitigations | HSE review, project risk register, audit |
| Recommendation | Approval note, finance concurrence |

## AI generation approach

1. User selects "board pack" or "management review" template
2. System identifies the period and scope (unit, project, tender, incident)
3. System retrieves required data from authorised sources
4. System generates charts using matplotlib or plotly (rendered to image)
5. System drafts slides using python-pptx
6. Every number on every slide has a source citation in the speaker notes
7. Draft is marked "AI-generated draft — requires review"
8. Human reviewer validates numbers, message, and recommendations
9. After approval, the deck is saved to the DMS with classification marking

## Good vs. bad

Good: starts with a decision-oriented executive summary, one message per slide, every number sourced in speaker notes, options considered, risks and mitigations shown, clear recommendation, classification marking on every slide.

Bad: opens with 10 slides of background before stating the ask, no clear decision, charts without source tags, hides adverse information, no alternatives shown, no risk discussion, recommendation buried at the end, no classification marking.

## Related

- The CAPEX approval note (`06-document-templates/08-capex-approval-note.md`) is the textual counterpart
- The daily performance report (`09-daily-performance-report.md`) is the operational counterpart
