# Lived Experience

What the user who wrote the problem statement is actually saying, reading between the lines.

## The combined problem statement

> We are a refinery. We have 2,500 employees and 5,000 workers. We run 24/7. We generate thousands of documents every month — P&IDs, inspection reports, work orders, shift logs, HAZOP studies, MOC forms, tender evaluations, approval notes, board notes.
>
> Our engineers, inspectors, maintenance personnel, HSE officers, procurement officers, finance staff, and managers spend 30–70% of their time finding and assembling evidence, not doing actual engineering, actual analysis, actual decision-making.
>
> A process engineer spends 4 hours assembling data from historian, LIMS, DCS, EAM, and email to explain a sulphur excursion. An inspection engineer spends 2 days typing thickness readings from a scanned PDF. A maintenance engineer spends 3 days searching for failure history. An HSE officer spends a week chasing documents for an MOC review. A procurement officer spends 10 days building a compliance matrix. A shift engineer spends 2 hours per shift copying data into a handover note.
>
> We cannot use cloud AI. Our P&IDs reveal process vulnerabilities. Our inspection reports reveal equipment weaknesses. Our vendor quotes reveal negotiation positions. Our incident reports reveal liability. Our board notes reveal strategy. If an engineer pastes a P&ID into ChatGPT, we lose control of that data.
>
> But our people are already using cloud AI anyway. Quietly. On personal phones. Pasting snippets. Because they need help. Because the internal search is slow. Because the public AI tool is convenient. This is the shadow AI problem. We can't ban it. We need to replace it with something better.
>
> We need an AI workbench that runs on our own GPU server. Air-gapped. Supports multiple models. Acts like an agent. Handles scanned PDFs, handwritten notes, drawings, photos. Produces real deliverables. Grounds itself in our documents with citations. Proves it is air-gapped.
>
> But we don't want a chatbot. We want a system that reduces the time required to find, reconcile, and explain evidence, while leaving technical judgement, safety authorisation, commercial evaluation, and statutory approval with accountable personnel.
>
> We want an industrial evidence and document workbench. Not an autonomous refinery operator. Its core promise: find the right evidence, reconcile it, calculate transparently, draft the required output, and preserve the approval trail.
>
> This is not just our problem. Every PSU, every defence unit, every government department, every bank, every regulator has the same problem. Their most valuable data cannot go to cloud AI. They need a sovereign, air-gapped AI workbench. We are the beachhead. But the market is national.

## What the solution is NOT

- Not a chatbot
- Not an autonomous refinery operator
- Not a model invention
- Not a generic RAG system
- Not a cloud service in disguise
- Not a system that makes safety, legal, financial or statutory decisions

## What the solution IS

- An industrial evidence and document workbench
- Permission-aware retrieval
- Revision-aware document control
- Industrial entity resolution
- Agentic multi-step workflows
- Real deliverable generation
- Air-gapped by design
- Cross-sector applicable
- Human-in-the-loop for all critical decisions

## What the user will judge you on

| What they care about | What they will look for |
|---|---|
| Can it read my scanned documents? | Upload a scanned report. Show OCR + vision. |
| Can it find the right equipment? | Show entity resolution: P-204A on P&ID = Pump 204A in EAM. |
| Can it find the right revision? | Show "Rev C — superseded by Rev D" warning. |
| Can it calculate? | Show corrosion rate with formula, inputs, units. |
| Can it produce a real deliverable? | Generate Word approval note + Excel chart. |
| Can it ground itself in my documents? | Show RAG with source, page, revision, tag. |
| Can it handle multiple models? | Show routing: coding task uses one model, summary uses another. |
| Is it actually air-gapped? | Network monitor showing zero external calls. |
| Does it understand my domain? | Refinery terminology. Equipment tags, P&IDs, HAZOP, MOC. |
| Does it respect permissions? | Role-based access visible. |
| Does it preserve the approval trail? | Audit log visible. |
| Does it distinguish draft from approved? | Output labelled "AI-generated draft — requires engineer approval." |
| Does it handle my documents? | Real formats: scanned PDFs, Excel, Word, PPT. |
| Does it save time? | Show workflow that takes 2 days today and 2 hours with AI. |
| Does it solve a real problem? | One workflow end-to-end: scanned inspection report → approval note. |

## The one workflow that proves everything

The problem statement gives the exact demo:

> "reading a scanned inspection report, pulling out key findings and drafting an approval note as a Word file"

This single workflow covers:

- Multimodal (scanned PDF + vision)
- Agentic (multi-step plan)
- Multi-model (OCR + reasoning + generation)
- RAG (historical inspection data)
- Real deliverable (Word + Excel)
- Air-gap proof (network monitor)
- Entity resolution (tag linking)
- Revision awareness
- Human approval gate
- Audit trail

## The strategic framing

> We are not building a hackathon prototype. We are building the first deployable sovereign AI workbench for Indian sensitive-data organisations. We designed the full production architecture — for refineries, PSUs, defence units, and government offices. And we built a scaled-down working proof on a single GPU. Same architecture. Same components. Same data flow. Just smaller models and mock connectors.

## The closing statement

> This is not a chatbot. This is an industrial evidence and document workbench. It reduces the time required to find, reconcile, and explain evidence, while leaving technical judgement, safety authorisation, commercial evaluation, and statutory approval with accountable personnel. It runs entirely on-premise. Nothing leaves the premises. And it is ready to scale from a single department to an entire organisation.
