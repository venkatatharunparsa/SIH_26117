# REAL spine red-team — 2026-09-19

**Scope:** `backend/` vs accepted D1–D6 · DEMO_TECH_STACK · G1–G10  
**Verdict prior:** ~0.55 implementation-ready · **after fixes:** ~0.78  

## Mistakes found → fixed

| ID | Issue | Fix |
|---|---|---|
| **R1** | `grant_id` optional on sandbox/gateway → **G7 bypass** | `grant_id` **required** on privileged routes |
| **R2** | Client `base_url` override on chat | Ignored under grant; settings only |
| **R3** | `/v1` doubled if base already ends with `/v1` | `normalize_base_url` |
| **R4** | Any `model` string accepted | Bound to **card model_id** set |
| **R5** | H7 opt-in (`require_h7_ack=False`) | H7 **mandatory** when cites exist |
| **R6** | Audit JSONL with no chain | SHA-256 **prev_hash** chain + `/audit/verify` |
| **R7** | No export leave path / H2 | `/task/export` with **h2_acked** |
| **R8** | CORS `null` (file://) | Removed |
| **R9** | Monitor A sessions RAM-only | Persist under `artifacts/monitor_a_sessions` |

## Still open (need your input or later thicken)

| ID | Item | Ask / plan |
|---|---|---|
| **O1** | Ollama tags | **Adopted 2026-09-19:** `llama3.2:3b` for all chat cards. Embed `nomic-embed-text` not used for chat. Second distinct chat model = when staged offline (no pull). |
| **O2** | G4 OCR/H1 extract | Not built yet — fixture path only |
| **O3** | Desk UI | Not built yet |
| **O4** | Docx binary secret scan | Findings scanned; full docx unzip scan = later |
| **O5** | Audit HMAC key | Unkeyed SHA-256 chain (honest: detects edit, not keyed CERT) |

## Residual honesty

Monitor A ≠ CERT · hash chain ≠ accreditation · best-effort sandbox · assist→export only.
