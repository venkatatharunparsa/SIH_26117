# Procurement Workflows

## Technical Bid Evaluation (TBE) for a compressor overhaul

### A. Tender and bid receipt

**Step 1: Tender preparation**

Before bids arrive, the procurement officer receives: purchase requisition, scope of work, compressor datasheet, inspection findings, maintenance history, technical specifications, qualification criteria, commercial terms, approved budget, delegation approval.

The tender is uploaded to MRPL e-procurement portal, Government e-procurement portal, or approved PSU tendering system.

**Step 2: Bid submission**

Bidders may submit: technical bid, commercial bid, qualification documents, method statement, manpower plan, tools and equipment list, similar-work certificates, OEM authorisation, quality plan, HSE plan, delivery schedule, deviations, price schedule, tax details, bank guarantees.

**Step 3: Store and control documents**

The system or tender cell records: bidder name, submission date, bid version, envelope type, technical documents, commercial documents, clarifications, addenda, opening record, bid-security details.

Documents may also be downloaded to a controlled tender folder for evaluation.

Sensitive data: competitor prices, bidder strategy, internal estimate, evaluation comments, technical deviations, negotiation position, unreleased procurement decision.

### B. Technical evaluation

**Step 4: Open technical package**

The procurement officer and user department open the technical submissions after the technical-bid opening event.

The technical evaluator checks: eligibility, similar experience, OEM capability, personnel qualifications, tools and facilities, methodology, shutdown duration, quality assurance, HSE plan, warranty, spare and consumable scope, inspection and testing, schedule, compliance with each technical clause.

**Step 5: Extract compliance matrix**

The evaluator creates an Excel matrix with rows for: tender clause, required specification, Bidder A response, Bidder B response, Bidder C response, compliance status, deviation, clarification required, evaluator comment, final recommendation.

The evaluator may manually copy from hundreds of pages.

**Step 6: Check technical deviations**

The evaluator identifies: exceptions to scope, substituted materials, different overhaul methodology, excluded tests, reduced warranty, longer shutdown period, unapproved subcontractors, missing OEM support, non-compliant personnel, alternative spare parts, commercial terms embedded in technical documents.

Each deviation is classified as: acceptable, clarifiable, conditionally acceptable, major deviation, disqualifying.

**Step 7: Issue technical queries**

The procurement officer or user department prepares a clarification letter containing: bidder reference, clause number, question, required supporting document, due date, statement that the clarification does not change the bid unless permitted by tender conditions.

The query is sent through: e-procurement portal, controlled email, or tender clarification workflow.

Responses are uploaded and attached to the evaluation file.

**Step 8: Revise technical matrix**

The evaluator updates: compliance status, deviations, clarification response, final technical qualification, conditions of acceptance.

The technical team may prepare a signed or digitally approved technical bid evaluation.

### C. Commercial and recommendation stage

**Step 9: Prepare comparative statement**

After technical qualification, the commercial team or authorised officers prepare: basic price, taxes, freight, duties, labour, consumables, optional scope, warranty, escalation, delivery impact, total evaluated cost, life-cycle cost.

The comparison is usually in Excel or an ERP/e-procurement module and may be transferred into a tender committee note.

**Step 10: Prepare recommendation note**

The note typically contains: requirement, background, scope, tender history, bidders, technical qualification, commercial comparison, negotiation details, price reasonableness, budget, recommendation, delegation of authority, integrity-pact or vigilance considerations, attachments.

**Step 11: Approval chain**

Typical route: user department prepares technical evaluation → procurement checks tender compliance → finance reviews commercial and budget aspects → legal reviews contractual issues where required → tender committee reviews → competent authority approves → purchase order or contract is issued → bid securities and performance guarantees are tracked → contract execution is monitored.

## Time estimate

| Activity | Typical elapsed time |
|---|---|
| Download, classify and distribute bids | 2–8 hours |
| Technical compliance extraction | 1–3 days |
| Clarifications and response cycle | 2–10 days |
| Comparative statement | 4–16 hours |
| Recommendation note | 4–16 hours |
| Approval and award | 2–10 days |
| People involved | 5–12 people |

Finding, extracting and formatting can account for 60–80% of the technical-evaluation effort for large submissions.

## AI intervention

Read-only data: tender specification, bid documents, clarifications, vendor master, past performance, approved budget, historical prices, technical evaluation templates.

Output: Clause-level compliance matrix, missing-document list, deviation register, contradiction detector, technical-query draft, comparative-statement draft, recommendation-note draft.

Human gate: Technical evaluator confirms compliance; procurement confirms fairness and tender rules; finance confirms financial aspects; tender committee and competent authority approve award.

Bidder workspaces must be strictly segregated. The model should not expose Bidder A's price or technical response while processing Bidder B's documents.

## Documents handled

### Technical documents

- Purchase requisition
- Material requisition
- Scope of work
- Technical specification
- Datasheets
- Drawings
- Quality-assurance plan
- Inspection and test plan
- Vendor qualification criteria
- Technical deviation statement
- Technical bid evaluation
- Clarification register
- Site-visit record
- Vendor drawing review
- Factory-acceptance-test documents

### Commercial and contractual documents

- Notice inviting tender
- Tender conditions
- Bid forms
- Commercial bid
- Comparative statement
- Price-negotiation record
- Tender committee note
- Purchase order
- Contract agreement
- Bank guarantee
- Performance guarantee
- Insurance certificate
- Tax documents
- Delivery schedule
- Amendment or change order
- Claim and dispute correspondence
- Completion certificate
- Liquidated-damages calculation

## What is document-heavy

- Reading large tender submissions
- Checking every clause against bidder responses
- Comparing technical deviations
- Extracting data from tables and scanned annexures
- Preparing comparative statements
- Cross-checking price, tax, freight, warranty and delivery terms
- Ensuring that all mandatory certificates are present
- Tracking bidder clarifications
- Reusing past tender language without copying obsolete requirements
- Preparing approval notes
- Maintaining an audit trail for every decision

## What is confidential

- Vendor prices
- Negotiation positions
- Technical deviations
- Bidder ranking
- Internal estimates
- Approved budget
- Reservation prices
- Evaluation committee comments
- Vendor performance concerns
- Unreleased tender strategy
- Legal and contractual advice
- Commercial terms
- Proprietary vendor designs
- Integrity-pact or vigilance-sensitive information

## Example

Current task: Evaluate six bids for a compressor overhaul. The procurement officer and technical team may spend one or more working days opening hundreds of pages, extracting qualifications, manpower, tools, methodology and deviations, checking previous experience, comparing warranty and delivery, preparing a compliance matrix, sending technical queries, revising the comparative statement after replies, and preparing the approval note.

AI-assisted task: The system extracts each bidder's response into a structured matrix, flags missing documents and deviations, identifies contradictory claims and generates a draft technical-query list. A human evaluator verifies every material finding.

## Good vs. bad TBE

Good: evaluates only disclosed criteria, uses clause-level references, records every deviation, separates clarification from negotiation, preserves bidder confidentiality, explains disqualification clearly, allows audit reconstruction.

Bad: uses vague "technically suitable," introduces criteria after bid opening, mixes technical and price information improperly, omits bidder clarifications, treats silence as compliance, gives an unexplained recommendation.
