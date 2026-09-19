# Workflows Overview

This section documents the step-by-step, system-by-system workflows that users perform daily at MRPL-type refineries. Each workflow shows:

- What the user does, step by step
- Which systems they access
- What documents are created or modified
- What data is sensitive
- Where AI can intervene
- What human approval gate remains

## The recurring pattern

Across all personas, the recurring work pattern is:

1. Find the latest approved information across ERP, historian, DCS, EAM, laboratory systems, email, shared drives and document repositories
2. Compare current conditions with design basis, operating limits, previous events or standards
3. Prepare a technically defensible document or approval note
4. Obtain reviews and signatures from multiple departments
5. Preserve evidence for audits, statutory review, incident investigation or future troubleshooting

## Workflows documented

| # | Workflow | Primary persona | Typical elapsed time |
|---|---|---|---|
| 1 | Morning daily performance review | Process engineer | 1–3 hours daily |
| 2 | Sulphur deviation investigation | Process engineer | 0.5–3 days |
| 3 | Monthly unit-performance report | Process engineer | 1–3 days |
| 4 | Scanned inspection report processing | Inspection engineer | 1–5 days |
| 5 | Corrosion-rate calculation and RBI update | Inspection engineer | 2–8 hours |
| 6 | Fitness-for-service assessment | Inspection engineer | 1–5 days |
| 7 | Recurring pump failure investigation | Maintenance engineer | 1–5 days |
| 8 | MOC review | HSE officer | 1–10 days |
| 9 | Technical bid evaluation | Procurement officer | 3–15 days |
| 10 | Shift handover and abnormal event | Shift engineer | 0.5–2 hours per shift |
| 11 | Monthly maintenance cost variance | Finance officer | 2–10 days |
| 12 | Capital-expenditure approval | Senior manager | 1–10 days |
| 13 | Coding task in sandbox | Inspection engineer (demo); any persona with a calculation | Minutes to hours |

## Time breakdown across all workflows

| Workflow | Total elapsed | People | Finding/assembling | Analysis | AI target |
|---|---:|---:|---:|---:|---:|
| Daily process review | 1–3 hours daily | 3–8 | 30–50% | 20–40% | Minutes |
| Sulphur deviation | 0.5–3 days | 5–12 | 40–60% | 25–45% | Hours |
| Monthly unit report | 1–3 days | 5–12 | 40–60% | 20–35% | Hours |
| Scanned inspection report | 1–5 days | 3–8 | 50–70% | 20–40% | 2–3 hours |
| Complex FFS | 1–5 days | 4–10 | 30–50% | 40–60% | 1–2 days |
| Recurring pump RCA | 1–5 days | 4–10 | 40–60% | 25–45% | Hours |
| MOC review | 1–10 days | 5–15 | 40–70% | 20–40% | 1–3 days |
| Compressor bid | 3–15 days | 5–12 | 60–80% | 15–30% | 3–5 days |
| Shift handover | 0.5–2 hours | 2–6 | 30–60% | 15–30% | Minutes |
| Abnormal event | 2–8 hours | 3–12 | 30–60% | 25–50% | Hours |
| Monthly cost variance | 2–10 days | 5–15 | 50–70% | 15–30% | 1–2 days |
| ₹25-crore approval | 1–10 days | 8–20 | 30–50% | 25–45% | 1–3 days |
| Coding sandbox (corrosion rate) | Minutes–hours | 1–3 | 20–40% | 40–70% | Minutes |

These are industry-based estimates, not MRPL performance benchmarks.

## AI intervention principle

The AI should reduce the time required to find, reconcile and explain evidence, while leaving technical judgement, safety authorisation, commercial evaluation and statutory approval with accountable personnel.

## Risk-level guardrails

| Risk level | Example | AI role |
|---|---|---|
| Low | Find a procedure or previous report | Direct answer with citation |
| Medium | Draft a daily report or comparison | Draft with review |
| High | Interpret equipment degradation or process deviation | Advisory analysis with engineer approval |
| Critical | Permit approval, isolation, DCS action or emergency decision | No autonomous action; human-controlled workflow only |
