# Architecture diagram — discussion draft (demo + org ghost)

**Date:** 2026-09-19  
**Status:** **SUPERSEDED FOR ORDER** — org diagrams first: see `ORG_ARCHITECTURE_DIAGRAMS.md`. This file remains a draft for **later demo narrow** of diagrams.  
**SoT:** `DEMO_TECH_STACK.md` · `ORG_TECH_DESIGN.md` · Flow A→J  

---

## What we need from you next

Confirm which diagrams we finalize (recommend **all three**):

1. **Context** — who talks to what (jury machine)  
2. **Planes** — Workbench / Runtime / Sandbox  
3. **Component** — demo boxes ON (solid) · org-only (dashed ghost)  

---

## Diagram A — Context (demo)

```mermaid
flowchart LR
  W[Knowledge worker<br/>same user HITL]
  Desk[Task desk UI]
  API[Workbench API]
  RT[Local /v1 runtime<br/>Demo: Ollama · Org: vLLM]
  Pack[Local SOP packs]
  Out[Word DRAFT + audit<br/>± sandbox proof]
  Paper[Paper / officer<br/>OUTSIDE app]

  W --> Desk --> API
  API --> RT
  API --> Pack
  API --> Out
  Out -.-> Paper
```

## Diagram B — Three planes (always)

```mermaid
flowchart TB
  subgraph A["A WORKBENCH — demo ON"]
    UI[Desk]
    ORCH[Orch + cards + grants]
    DOC[Word + extract + verifier]
    AUD[Audit SQLite+JSONL]
    GW[Gateway client]
  end
  subgraph B["B RUNTIME — separate process"]
    V1["OpenAI-shape /v1<br/>Demo Ollama · Org vLLM"]
  end
  subgraph C["C SANDBOX — best-effort"]
    SB[Code/calc verify]
  end
  UI --> ORCH --> GW --> V1
  ORCH --> DOC
  ORCH --> SB
  ORCH --> AUD
```

## Diagram C — Components (demo solid / org dashed)

```mermaid
flowchart TB
  Desk[Task desk]
  API[FastAPI workbench]
  Grants[Grants SQLite]
  Cards[Model Cards]
  Ext[PDF/OCR + H1]
  Ret[FTS retrieve k≤5]
  Ver[Cite-or-abstain]
  Word[docxtpl DRAFT]
  SB[Sandbox best-effort]
  Aud[Audit + export]
  GW[Gateway httpx]
  RT[Runtime /v1]

  Desk --> API
  API --> Grants & Cards & Ext & Ret & Ver & Word & SB & Aud & GW
  GW --> RT
  Ret -.->|MOCK packs| Packs[(Local files)]

  Conn{{Plant connectors}}:::ghost
  SSO{{SSO}}:::ghost
  Hyb{{Hybrid RAG}}:::ghost
  MCP{{Full MCP}}:::ghost
  API -.-> Conn & SSO & Hyb & MCP

  classDef ghost stroke-dasharray: 5 5,opacity:0.55
```

---

## Open questions for diagram clarity

1. Show **gateway** as box inside workbench (demo) or always draw separate process?  
2. Show **Audience A** monitor as its own box?  
3. One diagram for PPT later vs three technical diagrams now?

Reply with edits + answers; we freeze diagram set next.
