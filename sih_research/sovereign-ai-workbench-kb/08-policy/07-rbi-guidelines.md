# RBI Guidelines

## Information-asset classification

RBI information-security guidance defines **Sensitive**, **Internal** and **Public**, with sensitive information including customer information, internal personnel information and departmental budgets or staffing plans.

## Payment-system data localisation

RBI's payment-system data directions require system providers to store the entire payment-system data in India, including the full end-to-end transaction information processed as part of a payment instruction.

This is not a blanket requirement for every banking AI workload to be air-gapped, but it materially strengthens the case for India-controlled infrastructure and careful processor arrangements.

## Responsible-AI framework

RBI's 2025 FREE-AI committee report provides a responsible-AI framework for financial-sector adoption. Its existence is evidence that financial AI requires governance, infrastructure, policy, capacity, protection and assurance rather than simple API access.

## Applicable concerns

- DPDP Act obligations
- RBI outsourcing and cyber-risk controls
- Payment-data localisation where applicable
- Model-risk management
- Explainability for credit, fraud and claims decisions
- Privileged-access controls
- Auditability
- Customer grievance and correction rights
- Retention and deletion
- Data leakage through prompts and logs

## AI use cases

- KYC-document extraction
- Credit-file completeness
- Financial-statement analysis
- Fraud-case chronology
- AML alert triage
- Regulatory-report drafting
- Claims-document extraction (insurance-adjacent)
- Underwriting evidence search
- Policy comparison

AI should remain advisory for lending, claims repudiation, fraud accusation and regulatory enforcement.

## Design implications

| Requirement | Workbench design response |
|---|---|
| Payment-data localisation | All storage and processing within India |
| Model-risk management | Document model versions, evaluations, approvals |
| Explainability | Source citations and reproducible calculations |
| Privileged access | Strong identity and access controls |
| Auditability | Immutable logs |
| Customer rights | Support correction and deletion workflows |
| Retention and deletion | Configurable retention policies |
| Data-leakage prevention | Prompt and log controls |
