# Technical Brief — Knowledge Work Bench (SIH26117)

**Audience:** Jury technical round / mentors  
**Companion:** `solution/prototype/INDUSTRIAL_WORKBENCH_GAP_AND_PLAN.md`, `ORG_TECH_DESIGN.md`

---

## 1. Architecture (one page)

```
Desk (Electron kwb-app)
  → POST /orch/turn  (Session + Grant)
    → Specialists (extract / cite) + Skills/Roles pack
    → Pack → Gateway → local|/LAN OpenAI-shape /v1 (Ollama demo)
  → Artefacts (.docx) + Audit jsonl + Monitor A pack
```

**Hard rules:** Desk never calls LLM URL directly. Gateway allowlists hosts. Public model ids → deny.

---

## 2. Agentic behaviour (precise)

| Layer | Behaviour |
|---|---|
| Control | Fixed industrial phase machine in `orchestrator.py` |
| Phases | `idle` → `await_confirm_extract` → `await_review_cites` → `await_self_check` → `await_export` → `done` |
| Tools | attach/OCR, retrieve, word_draft, sandbox, MCP allowlist, workspace read |
| UI | Agent plan strip tracks phase; tool blocks + SSE `/orch/events` |
| Not claimed | Free LLM planner, token streaming like Cursor, plant write tools |

This matches Expected Solution “scan → findings → Word” better than an unbounded ReAct loop.

---

## 3. Model routing

- `inspection` → card `inspect-draft` → `llama3.2:3b` (when staged)  
- `coding` → card `code-assist` → `qwen2.5-coder:7b` (when staged)  
- Vision optional (`moondream`) on image attach  

Configs: `config/models.yaml`, `config/routing_rules.yaml`.

---

## 4. Multimodal ingest

| Input | Engine | Honesty |
|---|---|---|
| Text PDF | pypdf | live text layer |
| Image | Tesseract if installed | else fixture stub · NOT live OCR |
| Vision | moondream via Gateway | optional |

---

## 5. Security / sovereignty

- Grants + revoke  
- Artifact download grant-scoped  
- Sandbox host-process + network deny guard (not Docker `network=none` unless staged)  
- Secrets export-check  
- Audit chain verify  

**Claim language:** private LAN peer or loopback · **not** CERT · **not** air-gap unless venue NIC proof.

---

## 6. Desk surfaces

- Sessions rail (parallel grants)  
- Files tree (expand/collapse) + preview + Attach  
- Agent plan + model/agent chrome  
- Transcript + composer  
- Monitor (Live / Status / Share)  

---

## 7. Evidence packs

| File | Meaning |
|---|---|
| `eval/evidence/OUTSIDER_COMPLEX_E2E.json` | Complex PNG/PDF |
| `eval/evidence/OUTSIDER_MULTITASK_E2E.json` | Parallel inspection + coding |
| `eval/evidence/REDTEAM_ADV_REPORT.md` | Adversarial |
| `eval/evidence/PS_CONFIDENCE_SCORECARD.md` | Honest scores |

---

## 8. Known gaps (do not hide)

Excel path thin · entity resolution not built · true air-gap not proven · OCR live depends on Tesseract binary · agent plan is fixed not LLM-authored.
