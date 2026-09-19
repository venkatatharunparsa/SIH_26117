# Finance Workflows

## Monthly maintenance cost variance

### A. Gather actuals

**Step 1: Open ERP**

The finance officer opens the ERP financial and controlling modules and extracts: maintenance actuals, cost-centre postings, purchase orders, goods receipts, invoices, commitments, accruals, capital and operating expenditure, contractor costs, material issues, service-entry sheets.

The data is usually exported to Excel.

**Step 2: Retrieve approved budget**

The officer opens: annual budget, revised estimate, monthly phasing, cost-centre budget, turnaround budget, project budget, forecast.

The officer checks: original budget, approved revisions, current forecast, actual-to-date, remaining commitment.

**Step 3: Review maintenance records**

The finance officer or maintenance cost analyst checks EAM for: work orders, equipment and unit, planned versus unplanned maintenance, turnaround work, contractor hours, material consumption, emergency repairs, work-order completion, capitalisation status.

This is often done by downloading an EAM report or asking maintenance to provide an extract.

**Step 4: Reconcile procurement and invoices**

The officer matches: purchase order, goods receipt, service-entry sheet, invoice, work order, cost centre, asset or project code.

Exceptions include: invoice without receipt, receipt without invoice, open purchase order, wrong cost centre, accrual not reversed, capital item posted to operating expense, duplicate invoice, contract variation not reflected in budget.

### B. Explain variance

**Step 5: Calculate variance**

The officer calculates:
Variance = Actual − Budget


and may calculate:
Variance percentage = ((Actual − Budget) / Budget) × 100


Additional analysis may separate: volume variance, rate variance, timing variance, scope variance, emergency-work variance, foreign-exchange variance, turnaround variance, material-price variance.

**Step 6: Request explanations**

The finance officer sends email or workflow requests to: maintenance manager, reliability engineer, inspection, procurement, projects, materials, unit head.

Typical questions:

- Why was actual expenditure above plan?
- Was the work unplanned?
- Was a major equipment failure involved?
- Is the cost capitalisable?
- Is an accrual required?
- Is the purchase order still valid?
- Will the expense recur next month?
- Does the forecast need revision?

The responses may arrive as: email paragraphs, Excel sheets, Word notes, work-order comments, meeting minutes.

**Step 7: Prepare report**

The report may be created as: Excel variance workbook, Word commentary, PowerPoint management pack, ERP dashboard, monthly management-information report.

It generally contains: budget, actual, variance, top cost drivers, unit and cost-centre breakdown, open commitments, forecast, explanations, corrective actions.

**Step 8: Review and approve**

A likely route: finance analyst prepares → finance manager checks arithmetic and accounting treatment → maintenance head validates operational explanation → budget or planning function reviews forecast → CFO/finance head reviews → senior management receives the report → board or audit committee receives selected financial information.

## Time estimate

| Activity | Typical elapsed time |
|---|---|
| ERP extraction | 1–4 hours |
| PO, invoice and receipt reconciliation | 2–8 hours |
| EAM/work-order review | 2–8 hours |
| Explanations from departments | 1–5 days elapsed |
| Report formatting | 2–6 hours |
| Review | 2–8 hours |
| People involved | 5–15 people |

The work is often more delay-driven than analysis-driven: data can be extracted quickly, but explanations and confirmations arrive asynchronously.

## AI intervention

Read-only data: ERP actuals and budgets, purchase orders, goods receipts, invoices, EAM work orders, cost-centre hierarchy, project and asset data, prior variance reports, email explanations (subject to retention and access rules).

Output: Reconciled variance workbook, top-driver analysis, missing-explanation list, draft commentary, forecast-impact summary, Word/PPT management report.

Human gate: Finance verifies numbers; maintenance validates operational explanations; finance head approves the report.

## Documents handled

- Annual budget
- Revised estimate
- Cost-centre report
- Capital-expenditure proposal
- Investment approval note
- Project cost report
- Purchase order
- Goods-receipt note
- Invoice
- Vendor reconciliation
- Inventory statement
- Crude and product valuation
- Financial statement
- Audit schedule
- Tax return
- Bank and treasury document
- Board financial note
- Management information report
- Delegation-of-authority approval
- Contract variation
- Insurance claim

## What is document-heavy

- Matching invoices with purchase orders and receipts
- Extracting cost data from ERP
- Reconciling inventory and production numbers
- Explaining budget variances
- Consolidating departmental forecasts
- Reviewing capital-project claims
- Preparing audit evidence
- Reformatting data into management presentations
- Checking approval limits
- Tracking unresolved audit observations

## Example

Current task: Prepare a monthly refinery maintenance-cost variance report. The finance officer may need actuals by cost centre, purchase orders and invoices, work-order data, planned maintenance budget, turnaround expenditure, material issues, contractor bills, accruals and commitments, and explanations from maintenance managers. This often involves repeated Excel exports, email follow-up and manual commentary.

AI-assisted task: The workbench retrieves the approved budget, actual ERP postings, open commitments and maintenance work orders, identifies the largest variances, drafts explanations from supporting records and produces an Excel workbook and management slide.

## Good vs. bad variance report

Good: states the budget version, reconciles ERP/EAM and procurement data, explains material variances, separates timing from overspend, includes commitments and forecast, preserves source transaction references.

Bad: shows unexplained "miscellaneous" variance, mixes capex and opex, uses actuals without accruals, counts open purchase orders as actual spend, provides percentages without absolute values, includes commentary not supported by transactions.
