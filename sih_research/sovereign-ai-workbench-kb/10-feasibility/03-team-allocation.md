# Team Allocation

## Four-person team roles

| Person | Responsibility |
|---|---|
| AI/ML engineer | Local model serving, embeddings, inference and evaluation |
| Backend/data engineer | Ingestion, metadata, search, APIs, calculations and document lineage |
| Full-stack/product engineer | UI, workflow screens, exports and role-based interaction |
| Domain/security engineer | Industrial schemas, document templates, threat model, test data and demo narrative |

## Parallel work streams

While the AI/ML engineer builds the model layer, the backend engineer builds ingestion and indexing. While both work, the full-stack engineer builds the UI and the domain engineer prepares test data and demo narrative.

## Handoff points

| Hour | Milestone |
|---|---|
| 4 | Architecture agreed, data prepared |
| 10 | Local stack running, network disabled |
| 18 | Ingestion and retrieval working |
| 26 | Workflow agent running end-to-end |
| 32 | UI and controls complete |
| 36 | Demo rehearsed, evidence captured |

## What each person must not forget

- AI/ML engineer: model routing logs visible; no external API calls
- Backend engineer: permission checks enforced; citations in every output
- Full-stack engineer: classification badges visible; draft status labelled
- Domain engineer: realistic test data; air-gap proof visible to judges

## Presentation roles

- One person drives the demo
- One person handles questions about models and architecture
- One person handles questions about domain and users
- One person handles questions about policy and compliance
