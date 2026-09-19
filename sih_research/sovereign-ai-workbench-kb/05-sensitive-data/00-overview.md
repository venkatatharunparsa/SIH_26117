# Sensitive Data Overview

This section documents the data classification framework, the sensitive data inventory, what is and is not confidential, and the deployment rules for an air-gapped AI workbench.

## Why this matters

The problem statement explicitly says the data cannot go through cloud AI because it is confidential: Piping & Instrument Diagrams, financials, vendor negotiations, unreleased designs, internal correspondence, confidential business strategies. Company policy keeps this data on premises.

For the AI workbench to be defensible, it must:

- Know what data is sensitive and what is not
- Classify each document and each request
- Route the request to the correct model and index
- Enforce permissions
- Control export
- Preserve audit lineage

## What this section covers

| File | Contents |
|---|---|
| `01-classification-framework.md` | 6-level unified classification framework with handling rules |
| `02-sensitive-data-inventory.md` | Detailed sensitive data types across sectors |
| `03-what-is-not-confidential.md` | Public and low-sensitivity data by sector |
| `04-deployment-matrix.md` | Data-type vs. deployment-option matrix |
| `05-sector-specific-sensitive-data.md` | Per-sector sensitive data breakdown |

## The key insight

The problem is not that every customer legally requires a fully air-gapped deployment. Many customers need a deployment option in which:

- Sensitive data remains inside their controlled security boundary
- Prompts and outputs remain controlled
- Retrieval indexes do not leave the enclave
- Model inference is local
- Logs can remain within Indian jurisdiction
- OT and classified networks can be isolated

For defence and some critical infrastructure, that boundary may be genuinely air-gapped. For other PSUs, banks and government departments, it may be an Indian government cloud, private cloud, dedicated data centre or segmented on-premise environment.

## The product requirement

The workbench needs a **policy engine** that determines:

- Permitted model
- Permitted index
- Permitted connectors
- Permitted user group
- Permitted export path

This decision is driven by data classification.

## Deployment posture across sectors

| Sector | Likely deployment posture |
|---|---|
| Oil and gas PSUs | On-premise or controlled private/sovereign cloud for high-sensitivity workloads |
| Power generation and transmission | Segmented OT and private or government-controlled AI |
| Defence PSUs and DRDO | Classified networks, restricted enclaves and potentially air-gapped AI |
| Government departments | NIC/MeghRaj, departmental data centres or isolated systems |
| Regulators | Controlled government infrastructure; highly restricted technical repositories |
| Heavy industry | Private or on-premise deployment for plant and R&D data |
| Railways | Segmented railway networks and controlled government platforms |
| Banking and insurance | Strongly governed private/cloud or on-premise environments |
| Legal and judicial | Restricted legal repositories; local inference strongly preferred |
| Space | On-premise or isolated infrastructure |
| Atomic energy | Air-gapped or heavily segmented infrastructure |

## The classification principle

Classification is not uniform across India. Defence has formal national-security categories. RBI uses information-asset classifications. Government departments use official-secrecy markings. PSUs combine government security obligations with their own information-security policies.

The unified framework in this section is a practical cross-sector model. The workbench should support **customer-defined classifications and policy mappings**, not hard-code a single taxonomy.

## What "confidential" means in practice

Confidential data is information whose unauthorised disclosure could cause significant commercial, legal, safety, privacy or institutional harm. Examples include:

- Vendor quotations and negotiation notes
- Incident drafts and investigation files
- P&IDs and engineering drawings
- Credit files and KYC data
- Legal opinions and board notes
- Unreleased budgets and strategic plans
- Personal data and contractor records

## What "not confidential" means in practice

Public data is information that is intentionally published or lawfully releasable. Examples include:

- Published annual reports
- Published tender notices
- Press releases
- Gazette notifications
- Published judgments
- Public financial statements
- Public standards and guidance

Public availability does not mean every copy or context is safe. A published annual report is public; an internal draft of the next annual report is not. A published tender notice is public; bidder evaluations and negotiation notes are confidential.
