# Plain language for PPT (no H1/H2/H3 codes on slides)

**Rule:** Official idea PDF and spoken pitch use **everyday labels**. Internal codes (H1, H2, H7, H9, G1–G10) stay in **speaker backup / Q&A only**.

---

## Checkpoint dictionary (use these words on slides)

| Internal code | **Say / print on PPT** | What the engineer does |
|---|---|---|
| H1 | **Confirm extract** | Reviews OCR/fixture text before the system treats it as input |
| H7 | **Review citations** | Checks retrieved cites / gaps before drafting |
| H2 | **Self-check DRAFT** | Confirms the Word DRAFT for the current version before leave |
| H3 / export leave | **Export leave** | Takes soft-copy DRAFT off the box — solution path ends |
| H9 | **Accept sandbox result** | Reviews calc/code run output before leave (if sandbox used) |
| HITL / self-HITL | **Human checkpoints** · **engineer confirms** | Same user verifies own work — no in-app Approver |
| Grant | **Task grant** | Time-bounded permission shelf for tools |
| Model Card | **Task model card** | Which open-weight model role this task may use |
| G1 floor | **Two task types · one model tag** (honest) | Inspection + coding cards; single adopted tag OK |
| G8 | **Block unregistered / public model** | e.g. deny `gpt-4o` |
| G9 | **Block secrets in leave pack** | e.g. API-key-like text denied |
| G10 | **Block leave after failed sandbox** | Sandbox-red / reject blocks export |
| G1–G10 | **Demo proof checklist** | Do not print “G1–G10” on the idea PDF |
| Monitor A | **Evidence pack** (always add **≠ CERT**) | Start/stop snapshot — not a certificate |
| Monitor B | **Task monitor** (on demand) | Own-task audit view |
| DRAFT | **DRAFT Word** (status badge) | Soft copy — not plant record |
| NOT FOUND | **Cite or abstain** | Honest miss — no invented cites |

---

## Preferred process strip (print this)

```
Start task → Confirm extract → Retrieve knowledge → Review citations
  → Generate DRAFT Word → Self-check DRAFT → Export leave
```

Coding branch:

```
Start coding task → Run sandbox calc/code → Accept sandbox result
  → (optional note) → Self-check → Export leave
```

---

## Phrases to avoid on the PDF

- Bare `H1`, `H2`, `H3`, `H7`, `H9` without expansion  
- `G1–G10`, `G8`, `G9` as unexplained badges  
- `self-HITL` without “engineer confirms”  
- `A→J` walk codes  

OK in **Q&A** if asked: “Internally we label confirm-extract as H1…”
