# Tech-stack review — VERIFICATION (not ultimate lock)

**Date:** 2026-09-19  
**Input:** External/adversarial critique of `TECH_STACK_REDTEAM.md` BEST set  
**Status:** **ACCEPTED as working baseline** (DM 2026-09-19). Org-scale red-team: `TECH_STACK_ORG_REDTEAM.md`. Demo narrow = later.

---

## Overall verdict on the critique

| Question | Answer |
|---|---|
| Is the critique directionally sound? | **Yes** — especially sandbox wording, audit dual-store, PDF text-before-OCR *with caveats*, React not brand-locked |
| Is it the ultimate choice for us? | **No** — verified adjustments only until DM says **Lock** |
| Does it break freezes? | **No major break** if worded carefully (see AGPL + WP-03 PDF trust below) |

---

## Row-by-row verification

| Proposed change | Verify | Against SoT | Result |
|---|---|---|---|
| Keep FastAPI + Uvicorn; sync threads for OCR/docx/subprocess | Sound | No freeze locks brand; async≠non-blocking is correct eng practice | **PASS — candidate** |
| Keep docxtpl + python-docx; early table/header tests | Sound | WP-00/01 Word; repo map | **PASS — candidate** |
| Pin Python 3.11 **or** 3.12 exact | Sound | Hygiene | **PASS — candidate** |
| Rename “process jail” → **best-effort process isolation**; Job Objects; optional Docker; no CERT claims | Sound + **required honesty** | WP-16 already allows “OS job object”; de-Docker; pass/fail = evidence H9; refuse overclaim | **PASS — strong** |
| Windows Sandbox as **optional** only | Sound | Must not become new Desktop-class dependency | **PASS if optional**; **FAIL if required** |
| Audit: **SQLite transactional store + JSONL export + hash chain** | Sound | WP-17: append-only evidence, fail-closed, reconstructible — **storage brand not locked** | **PASS — candidate** (better than JSONL-only for concurrent UI) |
| Grants/session SQLite + revoke-before-tool | Sound | WP-04 G7 | **PASS — candidate** |
| Tesseract + fixture; add **PDF text extract before OCR** | Sound **with WP-03 caveat** | WP-03 S1 parse; for **untrusted digital PDF** freeze prefers **rasterize→OCR** over blind trust of hidden text layer | **PASS as pipeline:** detect type → if digital text: extract **and** label trust; if scan/empty: OCR; never skip H1 |
| **PyMuPDF** named | **CAVEAT — license** | Research: PyMuPDF often **AGPL-3.0** (or commercial). SIH/org may refuse AGPL embed | **NOT free ultimate** — prefer **MIT pdfplumber** and/or **pypdf** + rasterize; PyMuPDF only if DM accepts AGPL/commercial |
| pdfplumber | Sound for tables/MIT | Complements OCR path | **PASS — preferred PDF text candidate** |
| Lexical FTS5/BM25 k≤5 + grant-first + deterministic reranker (no vector yet) | Sound | WP-11 lexical must-work; k=5; authz-first | **PASS — candidate enhancement** |
| Cite-or-abstain deterministic | Sound | G6; WP-11/22 | **PASS — strong** |
| Thin orch; LangGraph not owner of grants/HITL | Sound | WP-06; T3 no in-app Approver | **PASS** |
| React+Vite keep but **not hard requirement** if team faster with SSR/HTML | Sound | T1 locked **desk shape** (Claude-like), **not** React brand | **PASS — UI brand still open**; desk layout locked |
| Prebuild SPA assets before demo | Sound | Offline jury | **PASS** |
| httpx loopback-only gateway | Sound | WP-09 | **PASS** |
| Runtime defer; test Ollama **and** llama.cpp | Sound | Hardware deferred; `/v1` contract | **PASS** |
| FastMCP after spine | Sound | Overlay | **PASS** |
| Presidio off critical path; regex first | Sound | Presidio project itself warns incomplete detection | **PASS** |
| SQLCipher / DuckDB / Tantivy / PySide6 / Flask as defaults | Correctly **not** defaults | Overbuild / wrong job | **PASS as “conditional only”** |

---

## Three corrections that should stick (still not ultimate until DM locks)

### 1) Sandbox language — VERIFIED MUST FIX wording
WP-16 allows non-Docker process path and Job Objects. Claiming “jail = secure arbitrary code” is **false**.  
**Verified wording:**

> Best-effort local execution isolation: timeout, workspace restriction, secret stripping, process-tree limits (Windows Job Objects when available), optional `--network=none` container. Evidence for H9 — **not** CERT / malware / kernel isolation.

### 2) Audit dual-store — VERIFIED IMPROVEMENT (candidate)
WP-17 needs append-only reconstructible log + fail-closed — not “JSONL file only.”  
**Verified design candidate:** SQLite = operational truth for writes/UI; exported JSONL+hash chain = jury artefact + manifest.

### 3) PDF → text then OCR — VERIFIED WITH TRUST RULE
Do **not** silently trust PDF text layer (WP-03).  
**Verified pipeline candidate:**

```text
PDF in → classify page
  ├─ selectable text → extract + trust_label=machine_extract (still H1)
  ├─ image/scan/empty → rasterize → Tesseract (+ fixture fallback)
  └─ encrypted / embeds → fail-closed
```

**Library:** prefer **pdfplumber (MIT)** and/or pypdf for text; **do not lock PyMuPDF** until AGPL accepted.

---

## What we deliberately do **not** treat as ultimate

- React as the only allowed UI toolkit  
- PyMuPDF as the PDF engine  
- Ollama vs llama.cpp winner  
- Windows Sandbox as required  
- Any claim that local isolation = secure sandbox  
- Full “recommended final lock” list until **you** say Lock  

---

## Verified candidate stack (for DM to accept / edit — not locked)

```text
Python 3.11 or 3.12 (pinned)
FastAPI + Uvicorn @ 127.0.0.1 (blocking work in threads)
UI: Claude-like task desk — React+Vite OR lighter SSR/HTML if faster (layout locked, brand open)
docxtpl + python-docx
PDF: text extract (pdfplumber/pypdf preferred) → OCR Tesseract + fixture; H1 always
Audit: SQLite events + JSONL export + hash chain + manifest
State: SQLite sessions/grants (revoke before tools)
Retrieve: grant → FTS5/BM25 → deterministic boosts → k≤5
Verifier: deterministic cite-or-abstain
Orch: thin custom loop
Exec: best-effort isolation + Job Objects when available + optional Docker network=none
Gateway: httpx loopback /v1 only
Runtime: deferred; test Ollama and llama.cpp
MCP: FastMCP mock after spine
Presidio: optional only
```

---

## DM next

1. **Accept verified candidates as working baseline** (still reopenable), or  
2. **Change** any row, or  
3. **Lock** when ready (then we freeze into TECH_STACK SoT + reopen WP-05 wording).

Say which of 1 / 2 / 3.
