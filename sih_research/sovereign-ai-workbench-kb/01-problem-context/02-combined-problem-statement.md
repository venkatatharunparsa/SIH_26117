# Combined Problem Statement

## What the user is actually saying

The person who wrote this problem statement is a senior MRPL engineer or manager who has watched their team struggle for years. They are not asking for a chatbot. They are asking for an industrial evidence and document workbench.

Here is the combined problem statement, synthesised from all research — written as if the user is speaking directly.

## The combined statement

> We are a refinery. We have 2,500 employees and 5,000 workers. We run 24/7. We generate thousands of documents every month — P&IDs, inspection reports, work orders, shift logs, HAZOP studies, MOC forms, tender evaluations, approval notes, board notes.
>
> Our engineers, inspectors, maintenance personnel, HSE officers, procurement officers, finance staff, and managers spend 30–70% of their time finding and assembling evidence, not doing actual engineering, actual analysis, actual decision-making.
>
> A process engineer spends 4 hours assembling data from historian, LIMS, DCS, EAM, and email to explain a sulphur excursion. An inspection engineer spends 2 days typing thickness readings from a scanned PDF and matching them to equipment tags. A maintenance engineer spends 3 days searching for failure history across EAM, email, and shared drives. An HSE officer spends a week chasing documents for an MOC review. A procurement officer spends 10 days building a compliance matrix from 6 bids. A shift engineer spends 2 hours per shift copying data from five systems into a handover note.
>
> We cannot use cloud AI. Our P&IDs reveal process vulnerabilities. Our inspection reports reveal equipment weaknesses. Our vendor quotes reveal negotiation positions. Our incident reports reveal liability. Our board notes reveal strategy. If an engineer pastes a P&ID into ChatGPT, we lose control of that data. We don't know where it goes, how long it's retained, who can access it, or whether it's used for training.
>
> But our people are already using cloud AI anyway. Quietly. On personal phones. Pasting snippets. Because they need help. Because the internal search is slow. Because the public AI tool is convenient. This is the shadow AI problem. We can't ban it. We need to replace it with something better.
>
> We need an AI workbench that:
>
> - Runs on our own GPU server. Air-gapped. Nothing leaves the premises.
> - Supports multiple models. A coding task needs a different model than a document summary. A vision task needs a different model than a reasoning task. New models should be addable without redesign.
> - Acts like an agent. Plan multi-step work. Read files. Write files. Execute code in a sandbox. Search internal documents. Iterate on a task instead of answering once and stopping.
> - Handles more than text. Scanned PDFs. Handwritten notes. Engineering drawings. Photographs. OCR and vision models on-device.
> - Produces real deliverables. Word approval notes. Excel calculations. PowerPoint presentations. Working code. Calculations with steps shown.
> - Grounds itself in our documents. Manuals. SOPs. Past correspondence. Historical inspection reports. Vendor manuals. OISD standards. With citations to source, revision, page number, equipment tag.
> - Proves it is air-gapped. Logs or network monitor showing zero external calls.
>
> But here's the thing: we don't want a chatbot. We want a system that reduces the time required to find, reconcile, and explain evidence, while leaving technical judgement, safety authorisation, commercial evaluation, and statutory approval with accountable personnel.
>
> We want an industrial evidence and document workbench. Not an autonomous refinery operator. Its core promise should be: find the right evidence, reconcile it, calculate transparently, draft the required output, and preserve the approval trail.
>
> This is not just our problem. Every PSU, every defence unit, every government department, every bank, every regulator has the same problem. Their most valuable data cannot go to cloud AI. They need a sovereign, air-gapped AI workbench. We are the beachhead. But the market is national.

## The core promise

Find the right evidence. Reconcile it. Calculate transparently. Draft the required output. Preserve the approval trail. All on-premise. Nothing leaves the premises.

## What the solution is NOT

- Not a chatbot
- Not an autonomous refinery operator
- Not a model invention (open-weight models exist)
- Not a generic RAG system (needs industrial entity resolution)
- Not a cloud service in disguise
- Not a system that makes safety, legal, financial, or statutory decisions

## What the solution IS

- An industrial evidence and document workbench
- Permission-aware retrieval
- Revision-aware document control
- Industrial entity resolution (equipment tag linking)
- Agentic multi-step workflows
- Real deliverable generation (Word, Excel, PPT)
- Air-gapped by design
- Cross-sector applicable
- Human-in-the-loop for all critical decisions
