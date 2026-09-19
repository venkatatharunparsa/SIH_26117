# Capability Comparison

| Capability | Local chat tools | General enterprise AI | Infrastructure vendors | Proposed workbench |
|---|---:|---:|---:|---:|
| Local inference | Yes | Sometimes | Yes | Yes |
| Full air-gap | Possible | Contract-dependent | Specific products | Core design goal |
| OCR for scanned PDFs | Basic/variable | Usually | Not the core | Industrial-grade |
| Table extraction | Variable | Moderate | Not core | Required |
| Equipment/entity resolution | Rare | Generic | No | Core |
| Revision-aware retrieval | Rare | Variable | No | Core |
| Permission-preserving search | Basic/group-level | Often available | Infrastructure only | Document/paragraph/workflow level |
| Historian/EAM/ERP connectors | Rare | Generic connectors | No | Sector-specific |
| Approval-state awareness | Rare | Variable | No | Core |
| Word generation | Basic | Often | No | Template-controlled |
| Excel with formulas | Basic | Variable | No | Core |
| PowerPoint generation | Variable | Often | No | Controlled management output |
| Audit trail | Basic logs | Usually | Infrastructure logs | Immutable evidence lineage |
| Multi-model routing | Variable | Often | Infrastructure | Classification/task-aware |
| Agentic workflows | Basic | Increasing | No | Core, but approval-gated |
| Industrial calculations | Usually no | Generic | No | Unit-aware and source-backed |
| Cross-sector templates | No | Limited | No | Core |
| Offline update management | User-dependent | Contract-dependent | Product-specific | Required |

## Where existing tools fall short

The gaps are consistent across all existing categories:

- No industrial entity resolution
- No revision awareness
- No permission-preserving retrieval at document/paragraph level
- No approval-state awareness
- No sector-specific connectors
- No unit-aware calculations with source lineage
- No cross-sector document templates
- No offline update procedures
- No air-gap proof architecture
