# WP-20 System connection — FREEZE

**Date:** 2026-09-19  
**Status:** **FROZEN rev 1.0** — GATE_90 **A2** locked  
**Prior draft:** `../connection/WP-20_ORG_CONNECTION.md` (superseded as binding; keep as history)  
**Figure SoT:** `../prototype/ORG_ARCHITECTURE_DIAGRAMS.md` (O1–O6 ACCEPTED) · `../prototype/DEMO_ARCHITECTURE_DIAGRAMS.md` · `../prototype/APPLICATION_FLOW_COMMON.md` (A→J)  
**Aligns:** WP-00/01/05 rev 2.0 · WP-13/18 · no-pull adopt · assist→export  

**Stack brands:** not locked here — see `../connection/TECH_STACK_SOURCE_OF_TRUTH.md` and demo stack.

---

## 1. One-sentence contract

**KWB** connects every frozen WP into **one** offline workbench picture: **assist → self-HITL → export leave**; plant SoR **read-only**; inference only via **gateway → local `/v1`**; sovereignty via **Monitor A evidence pack** (**not CERT**).

---

## 2. Product boundary (binding)

| True | False / refuse |
|---|---|
| Assist → DRAFT → self-HITL → **export leave** | In-app Approver / accept-for-forward / plant decide |
| Paper Approver **outside** KWB | In-app H2/H3 as plant SoD |
| Admin = IT platform (cards, allowlists, stage) | Admin proxy worker HITL |
| Plant connectors **read-only** | Write DCS/EAM/ERP/DMS SoR |
| Monitor A = evidence pack / snapshot | CERT / verbal “WAN=0” badge without artefact |
| G1 floor/full honesty (WP-18) | Pull models to fake dual `model_id` |

---

## 3. Two planes (always)

```text
WORKBENCH SOFTWARE (no weight files)
  UI · session · grants · orchestrator · specialists · tools
  packer · gateway client · self-HITL · RAG · MCP · skills
  cards · gates · audit · lineage · monitors
        │ local /v1 only (verified)
RUNTIME HARDWARE
  staged open-weight · /v1 server · load/LRU · GPU
        sandbox ≠ GPU process
```

| Plane | Owns | WPs |
|---|---|---|
| Workbench | Product behaviour | 00–09, 11–19, 21–24 |
| Runtime | Weights + serve | **10** (+ 19 stage) |
| Sandbox | Code verify | **16** |

---

## 4. Master connection (logical)

Same boxes as draft §3, with naming locks:

- **HITL** = self-HITL H1/H2/H3(**export leave**)/H7/H9 (WP-05) — same operating user  
- **Monitor A** = egress **evidence pack** / start–stop snapshot (WP-13) — **not CERT**  
- **Only gateway** opens runtime socket  
- Orchestrator = software brain under grants — **not** plant decision-maker  

Figure detail: org O1–O6 · demo D1–D6.

---

## 5. End-to-end control loop

```text
1. Session ≠ plant access
2. Start job → task GRANT (sources, tools, ceiling, TTL)
3. Orchestrator → specialist + skills + Model Card (G1 routes logged)
4. If scan: INGEST → H1 → only then KB-as-truth path
5. RETRIEVE authz-first → claims / H7 when cites
6. PACKER → PackManifest
7. GATEWAY verify → ONLY path to local /v1 (deny public URL)
8. RUNTIME serves card model_id (adopted local tags only; no pull)
9. Tools / sandbox / MCP under grant ∩ allowlist
10. OUTPUT GATES before unmasked view / export leave
11. DRAFT in KWB store → self-HITL H2 → H3 export leave (off box)
12. Never write plant SoR; paper Approver outside
13. AUDIT fail-closed + lineage (lineage_degraded soft ≠ audit soft)
14. Monitor A/B evidence; eval/ G1–G10 for demo_ready
```

**On failure:** fail-closed (or degrade only where a freeze allows) — WP-18.

---

## 6. WP → box map

| WP | Box |
|---|---|
| **00** | Product contract, planes, Never, assist≠decide |
| **01** | Roles (Worker/Admin in-app; Approver paper outside), jobs, artefacts |
| **02** | Read-only connectors; KWB store + versions |
| **03** | Pre-LLM ingest OCR/VLM |
| **04** | Session ≠ grant; revoke |
| **05** | Self-HITL map; stale; export leave |
| **06** | Orchestrator = software brain |
| **07** | Specialists, skills, tools |
| **08** | Local MCP host |
| **09** | Gateway → local `/v1` only |
| **10** | Runtime load/serve |
| **11** | Authz-first RAG; cite-or-abstain |
| **12** | Output gates |
| **13** | Monitor A evidence pack + B own-task |
| **14** | Lineage |
| **15** | Personal `.md` |
| **16** | Sandbox ≠ GPU |
| **17** | Audit |
| **18** | G1–G10 / eval/ |
| **19** | USB offline import |
| **21–24** | Packer · claims · T0–T4 · cards |

---

## 7. Demo slice vs org

| Concern | Demo | Org |
|---|---|---|
| Jobs | inspect-to-note + code (+ multimodal) | Full catalog |
| Runtime | Ollama inference-only, local tags | vLLM GPU farm |
| Models | ≤3 cards; G1 floor OK single-tag | More cards; full G1 preferred |
| MCP | One MOCK later | Full local lifecycle |
| Gateway | In-process OK if no bypass | Separate host ambition |
| Monitor A | Start/stop snapshot WB+Ollama | Continuous / SOC ambition |
| Eval | G1–G10 + signed checklist | Same + more |

**Same architecture. Demo = slice, not a different product.**

---

## 8. Official Expected Solution — caption

| Clause | Satisfied by |
|---|---|
| Local deploy; smaller model OK | WP-00/10 · demo Ollama |
| Auto-select ≥2 task types | WP-06/24/18 G1 (floor/full) |
| Scan → findings → Word DRAFT | WP-03/01/05/18 G2 |
| Coding + sandbox | WP-16/18 G3/G10 |
| Multimodal | WP-03/18 G4 (fixture+H1 day-1 OK) |
| Network / sovereign proof | WP-13/17/18 G5 — evidence pack **not CERT** |
| Offline / no public pull | WP-00/09/19 Never |

---

## 9. Never (cross-cutting)

- Cloud LLM / public `base_url` / HF-in-UI / `ollama pull` from workbench  
- Write plant SoR  
- Safety/FFS/statutory autonomy  
- Fail-open to internet or unregistered model  
- App-only “SECURE” / CERT claim without host evidence  
- In-app Approver queue; Admin proxy HITL  
- Auto-promote personal → org without Admin H6  

---

## 10. Build order after this freeze

1. ~~Design SoT B-rows~~ — policy written (`DESK_IA`, fixtures, B3/B4 contracts); honest score still ~0.76 until wires + REAL gates.  
2. Apply `GATE_90_REDTEAM.md` Criticals · then implement desk + G1–G10 until `demo_ready`.  
3. PPT only after execute-ready ≥0.90.

---

## 11. Changelog

| Rev | Note |
|---|---|
| **1.0** | **FROZEN** 2026-09-19 GATE_90 A2: promote connection draft; bind assist→export, self-HITL, Monitor A ≠ CERT, G1 honesty; figures = org/demo ACCEPTED |

**Confidence:** **0.91**
