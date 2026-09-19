# Deployment Matrix

This matrix determines the deployment path for each data type. The workbench's policy engine enforces these rules.

| Data type | Sector | Classification | Public cloud? | Private/govt cloud? | On-premise? | Air-gapped? |
|---|---|---|---|---|---|---|
| Published annual report | All | Public | Yes | Optional | No | No |
| Published tender notice | PSU, defence, govt | Public | Yes | Optional | No | No |
| Unreleased tender specification | All procurement | Restricted/Confidential | Only approved | Yes | Preferred | No, unless classified |
| Vendor price and negotiation note | PSU, defence, manufacturing | Confidential | Normally no | Controlled | Preferred | Sometimes |
| P&ID and engineering drawing | Refinery, power, manufacturing | Confidential/Restricted | Not consumer cloud | Controlled private | Preferred | If critical infrastructure |
| DCS/SCADA architecture | Refinery, power, telecom, ports | Secret/Highly confidential | No | Dedicated restricted cloud only if accredited | Yes | Often |
| Public financial statement | Listed entities | Public | Yes | Optional | No | No |
| Internal budget and forecast | All | Confidential | Conditional | Yes | Preferred | No |
| Customer KYC/account data | Banks, insurance, telecom | Confidential/Sensitive | Only approved regulated processing | Yes | Preferred | Not normally, except investigation |
| Classified defence drawing | Defence | Secret/Top Secret | No ordinary cloud | Classified private environment | Yes | Yes |
| Cabinet note before decision | Government | Confidential/Secret | No consumer cloud | Government-controlled only | Preferred | If security-related |
| Published court judgment | Legal | Public | Yes | Optional | No | No |
| Sealed court record | Legal | Confidential/Restricted | No ordinary cloud | Restricted legal environment | Preferred | Case-dependent |
| Patient/clinical trial data | Pharma | Confidential/Sensitive | Controlled only | Yes | Preferred | Case-dependent |
| Patent draft before filing | R&D/pharma/space/defence | Confidential | Conditional but usually local | Yes | Preferred | No |
| Grid topology and relay settings | Power | Secret/Highly confidential | No ordinary cloud | Restricted utility infrastructure | Yes | Often |
| Environmental clearance already published | Industry | Public | Yes | Optional | No | No |
| Internal compliance evidence | All regulated sectors | Restricted/Confidential | Conditional | Yes | Preferred | No |
| Public timetable | Railways | Public | Yes | Optional | No | No |
| Train-control configuration | Railways | Highly confidential/Critical | No ordinary cloud | Dedicated | Yes | Often |
| Geological reserve model | Mining | Confidential | Controlled | Yes | Preferred | No |
| Published agricultural scheme | Government/agriculture | Public | Yes | Optional | No | No |
| Distribution stock/location data | Food corporations | Restricted/Confidential | Conditional | Yes | Preferred | Sometimes |

## Policy engine decision tree

User request arrives
↓
Classify the request (classification level)
↓
Check user identity and role
↓
Check user access to this classification
↓
Route to eligible model (by classification)
↓
Retrieve from eligible index (by classification)
↓
Generate output with classification badge
↓
Check export eligibility
↓
Apply DLP if applicable
↓
Log all steps to audit trail

## Model eligibility by classification

| Classification | Eligible models |
|---|---|
| Public | Any (including approved external) |
| Internal | Approved enterprise models |
| Restricted | Local models only |
| Confidential | Local models only; local index only |
| Secret | Cleared models in classified enclave |
| Top Secret | Air-gapped models only; isolated index |

## Export eligibility by classification

| Classification | Export to Word/Excel/PPT | External transfer |
|---|---|---|
| Public | Yes | Yes |
| Internal | Yes | Controlled |
| Restricted | Controlled | No |
| Confidential | Approval + DLP | No |
| Secret | Controlled media | No |
| Top Secret | Formal procedure | No |
