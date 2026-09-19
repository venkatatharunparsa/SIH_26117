# Data Classification Framework

## Important distinction

Classification is not uniform across India.

- Defence has formal national-security categories
- RBI and financial institutions use information-asset classifications such as public, internal and sensitive/confidential
- Government departments may use official-secrecy markings, departmental security categories and file-access rules
- PSUs generally combine government security obligations, CVC/CAG/audit controls, contractual confidentiality and their own information-security policies
- Private companies use internal labels such as public, internal, confidential, restricted and highly confidential

The Ministry of Defence Security Manual for Licensed Defence Industries (revised June 2025) expressly defines **Top Secret, Secret, Confidential, Restricted and Unclassified**.

RBI information-security guidance defines **Sensitive**, **Internal** and **Public**, with sensitive information including customer information, internal personnel information and departmental budgets or staffing plans.

## Unified cross-sector classification

| Unified level | Typical criteria | Examples | Access | Handling | External cloud processing | On-premise | Air gap |
|---|---|---|---|---|---|---|---|
| Public | Intentionally published or lawfully releasable | Annual reports, published tenders, press releases, gazette notifications, published judgments | Anyone | Normal corporate controls; preserve integrity and copyright | Usually permitted through approved services | Not required | Not required |
| Internal | Non-public but low-impact if disclosed | Internal directory, routine procedures, non-sensitive meeting notes, organisation charts | Employees and approved contractors | Authenticated access, ordinary encryption, controlled sharing | Usually possible with approved provider and contract | Not required | Not required |
| Restricted | Official-use information whose unauthorised disclosure could cause operational, administrative or commercial difficulty | Working files, maintenance schedules, internal procurement drafts, non-public environmental records | Need-to-know staff and approved contractors | Access control, logging, secure transmission, controlled printing, retention and destruction | Only approved enterprise/private or government cloud; no consumer AI | Preferred for critical workflows | Normally not required |
| Confidential | Disclosure could cause significant commercial, legal, safety, privacy or institutional harm | Vendor quotations, incident drafts, P&IDs, credit files, legal opinions, personal data, unreleased budgets | Named roles, project teams or cleared personnel | Encryption, DLP, source-system permissions, audit logs, controlled export and secure destruction | Only under a reviewed contract, jurisdictional control and no-training/retention safeguards; local deployment preferred | Strongly preferred | Required only where threat model or regulation demands |
| Secret / Highly confidential | Disclosure could cause serious national-security, critical-infrastructure, market, safety or strategic harm | OT architecture, protection settings, classified defence drawings, intelligence, strategic projects, major cyber incidents | Cleared personnel with explicit need to know | Secure enclave, controlled rooms, strong identity, removable-media controls, two-person or dual-control processes where required, full audit | Generally not permitted without explicit authority and accredited environment | Normally required | Often required |
| Top Secret / Mission-critical | Disclosure could cause exceptionally grave damage to national security or national interest | Highest-level defence information, strategic vulnerabilities, certain intelligence or nuclear-security information | Specifically cleared and authorised personnel only | Accredited classified network, physical and technical isolation, strict document accountability, secure destruction and controlled transfer | Ordinary external cloud not permitted | Required | Required |

The Top Secret definition in the defence manual is information whose unauthorised disclosure could cause "exceptionally grave damage" to national security or national interest. Secret concerns serious damage; Confidential concerns damage to national security, national interests or government functioning; Restricted is official-use information; Unclassified requires no security classification.

## Deployment rules by classification

### Public

- Cloud: generally acceptable
- AI: public or commercial AI may be used, subject to copyright and accuracy
- Controls: prevent accidental inclusion of unpublished annexures or personal data
- Example: published MRPL annual report or public tender notice

### Internal

- Cloud: approved enterprise cloud may be acceptable
- AI: use business accounts with contractual controls, no-training commitments and access logging
- Controls: do not mix with restricted repositories
- Example: routine internal administrative procedure

### Restricted

- Cloud: only approved providers and approved data flows
- AI: private deployment, Indian government cloud or enterprise tenant preferred
- Controls: role-based access, audit trails, retention limits and DLP
- Example: internal tender draft or non-public maintenance schedule

### Confidential

- Cloud: case-by-case security, legal and procurement approval
- AI: on-premise or controlled private cloud preferred; public consumer AI should be prohibited
- Controls: document-level permissions, prompt logging, redaction, model isolation and no external connectors by default
- Example: vendor negotiation note, inspection report or customer KYC data

### Secret/Top Secret

- Cloud: ordinary public cloud is not appropriate
- AI: accredited classified environment, usually on-premise or dedicated classified infrastructure
- Controls: cleared users, isolated networks, secure media transfer and formal configuration management
- Example: classified defence system design or military operational information

## Sector differences

| Sector | Typical classification approach | Main governing concern |
|---|---|---|
| Government departments | Public, internal/official use, restricted, confidential/secret material under departmental and official-secrecy procedures | State business, personal data, cabinet confidentiality, law and order, legal privilege |
| Defence | Unclassified, Restricted, Confidential, Secret, Top Secret | National security, defence capability, classified information and controlled dissemination |
| PSUs | Usually internal policy labels plus government security, CVC, CAG, contract, cyber and sectoral requirements | Public accountability combined with commercial, safety and infrastructure sensitivity |
| Banking | Public, internal, confidential/sensitive, restricted; information-asset classification under RBI and bank policy | Customer confidentiality, financial crime, cyber risk, payment data, regulatory information |
| Private industry | Public, internal, confidential, restricted/highly confidential | Trade secrets, IP, contracts, safety, privacy and competitive information |
| Regulators | Public, internal, restricted/confidential, protected investigation or supervisory information | Licensee confidentiality, enforcement integrity, market sensitivity and safety |
| Legal/judicial | Public record, restricted filing, confidential, privileged, sealed/classified | Legal privilege, evidence integrity, personal data, sealed matters and investigations |

CVC, CAG and DPE do not provide one universal PSU classification table. They impose accountability, procurement, financial, audit and governance obligations, while each PSU's security policy determines specific labels. That means your product should support **customer-defined classifications and policy mappings**, not hard-code a single taxonomy.

## Unified handling policy for AI

| Control | Public | Internal | Restricted | Confidential | Secret/Top Secret |
|---|---|---|---|---|---|
| External LLM | Usually allowed | Approved service | Conditional | Normally prohibited unless explicitly approved | Prohibited in ordinary cloud |
| Local RAG | Optional | Useful | Preferred | Required/preferred | Required |
| Prompt retention | Normal | Logged | Controlled | Minimal and auditable | Restricted to accredited system |
| Indexing | Public index | Department index | Role/project index | Document/paragraph permission index | Cleared enclave index |
| Human approval | For high-impact claims | Usually not | Required for official output | Required | Mandatory |
| Export to Word/Excel/PPT | Allowed | Controlled | Controlled | Approval and DLP | Controlled media/process |
| Internet access | Allowed | Controlled | Restricted | Usually disabled | Air-gapped |
| Model updates | Normal | Approved | Security-reviewed | Offline/controlled update | Formal media-transfer procedure |

## Sector classification mapping (quick reference)

| Data type | Classification |
|---|---|
| Published annual report | Public |
| Published tender notice | Public |
| Unreleased tender specification | Restricted/Confidential |
| Vendor price and negotiation note | Confidential |
| P&ID and engineering drawing | Confidential/Restricted |
| DCS/SCADA architecture | Secret/Highly Confidential |
| Public financial statement | Public |
| Internal budget and forecast | Confidential |
| Customer KYC/account data | Confidential/Sensitive |
| Classified defence drawing | Secret/Top Secret |
| Cabinet note before decision | Confidential/Secret |
| Published court judgment | Public |
| Sealed court record | Confidential/Restricted |
| Patient/clinical trial data | Confidential/Sensitive |
| Patent draft before filing | Confidential |
| Grid topology and relay settings | Secret/Highly Confidential |
| Environmental clearance already published | Public |
| Internal compliance evidence | Restricted/Confidential |
| Public timetable | Public |
| Train-control configuration | Highly Confidential/Critical |
| Geological reserve model | Confidential |
| Published agricultural scheme | Public |
| Distribution stock/location data | Restricted/Confidential |

## The product requirement

The workbench needs a policy engine that determines the permitted model, index, connector, user group and export path based on classification. Classification must be:

- Set per document, per paragraph and per request
- Inherited from source-system permissions
- Enforced at model-routing time
- Enforced at retrieval time
- Enforced at export time
- Logged in the audit trail

## Why this is not a simple RBAC problem

Traditional role-based access control answers "can this user see this document?" The classification-aware policy engine must answer:

- Can this model process this classification?
- Can this index hold this classification?
- Can this output be exported to Word, Excel or PPT?
- Can this output leave the enclave?
- What audit log is required?
- What human approval gate applies?

Classification is not just about access. It is about model eligibility, index eligibility, export eligibility and audit obligation.
