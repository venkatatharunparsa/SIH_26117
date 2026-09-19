# Digital Personal Data Protection Act, 2023

The DPDP Act regulates digital personal data and establishes obligations for data fiduciaries and processors.

## Key obligations

- Purpose limitation
- Lawful processing
- Notice and consent where required
- Reasonable security safeguards
- Processor governance
- Data-principal rights
- Breach management
- Additional obligations for significant data fiduciaries
- Control over model prompts, logs and generated output containing personal data

## Cross-border approach

The Act does **not** automatically require all personal data to remain in India. Its cross-border approach allows transfers unless restricted by the government, subject to applicable requirements.

Therefore, DPDP compliance alone does not create a universal air-gap mandate. It does, however, make uncontrolled external AI processing risky.

## Implications for AI workbench

- Prompts and outputs may contain personal data; retention and access must be controlled
- Model training on personal data must follow lawful processing requirements
- Generated documents containing personal data must respect retention and correction rights
- Audit logs containing personal data must be protected
- Significant data fiduciaries may face additional obligations (DPIA, audit, DPO)

## Practical design implications

| Requirement | Workbench design response |
|---|---|
| Purpose limitation | Log purpose per request; restrict reuse |
| Security safeguards | Encryption at rest and in transit; access controls |
| Processor governance | No external processors unless contracted |
| Data-principal rights | Enable correction and deletion of generated content |
| Breach management | Isolated incident response; no external telemetry |
| Significant data fiduciary obligations | Support DPIA, audit trail, DPO review workflow |
