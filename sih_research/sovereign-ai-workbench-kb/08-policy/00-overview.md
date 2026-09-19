# Policy Overview

Indian data-sovereignty and AI policy context relevant to designing an air-gapped AI workbench.

## Key policies and frameworks

| Policy / framework | Relevance |
|---|---|
| DPDP Act, 2023 | Governs digital personal data; obligations for data fiduciaries and processors |
| CERT-In Directions (2022) | 180-day log retention within Indian jurisdiction |
| National Data Governance Framework | Data availability, standardisation, interoperability, responsible use |
| MeghRaj / NIC National Cloud | Government-controlled cloud infrastructure |
| IndiaAI Mission | ₹10,371.92 crore outlay; 7 pillars including compute, foundation models, datasets, applications, skills, responsible AI |
| AIKosh | National platform for datasets, models, toolkits |
| BharatGen | Government-supported multimodal, multilingual foundation-model initiative |
| Bhashini | Language-AI initiative (speech, translation, multilingual) |
| AI4Bharat | IIT Madras initiative for Indic language datasets, models |
| Defence Security Manual (SMLDI) | Top Secret, Secret, Confidential, Restricted classifications |
| DAP 2020 | Defence procurement; restricted information under Official Secrets |
| RBI Guidelines | Data localisation, responsible-AI framework |
| DRDO ETAI framework | Trustworthy AI for armed forces |

## Data sovereignty vs. air-gapping

These terms should not be conflated:

- **Data residency:** Data is stored in a particular country
- **Data sovereignty:** Data is subject to the jurisdiction and control of the organisation or country
- **Private cloud:** Infrastructure is logically dedicated to one customer but may still be externally operated
- **On-premise:** Infrastructure is inside the organisation's premises or controlled data centre
- **Air-gapped:** Environment is physically or strongly logically isolated from external networks

A bank may accept Indian private cloud for one workload, a refinery may require on-premise for OT data, and a defence lab may require an air gap for classified material.

## Risk-tiered deployment

| Data class | Suitable deployment |
|---|---|
| Public information | Public cloud or public web systems |
| Internal administrative data | Approved government cloud or departmental private cloud |
| Personal and regulated data | India-hosted, access-controlled private or government cloud |
| Critical infrastructure operational data | Segmented private/on-premise infrastructure |
| Defence classified data | Classified network, potentially air-gapped |
| Cabinet, intelligence or highly sensitive legal files | Restricted departmental or air-gapped enclave |

## Why this matters

The AI workbench must support a **policy engine** that maps classification to deployment, model selection, index access, export control and audit obligation. Indian policy does not impose one universal rule; it creates a risk-tiered environment that the workbench must respect.
