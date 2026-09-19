# CERT-In Directions (2022)

CERT-In's 2022 directions require government organisations and covered entities to maintain ICT-system logs securely for 180 days within Indian jurisdiction.

## Implications for AI workbench

The workbench must consider:

- Prompt logs
- Retrieval logs
- Authentication logs
- Model-server logs
- Document-access logs
- Export and download logs
- Incident-response evidence

If an external AI provider retains such information outside India or outside the organisation's audit control, the compliance and incident-response posture becomes more difficult.

## Design requirements

- All logs stored within Indian jurisdiction
- Minimum 180-day retention (longer for defence/nuclear)
- Logs immutable and encrypted
- Access to logs controlled and audited
- Log retention policies documented
- Logs support incident investigation
- Logs integrated with internal SOC (not external telemetry)

## Covered entities

- Government organisations
- Critical infrastructure operators
- Financial institutions
- Healthcare providers
- Telecom operators
- Cloud service providers
- Data centres

For the AI workbench, this means that even the AI system's own logs are subject to CERT-In retention requirements.
