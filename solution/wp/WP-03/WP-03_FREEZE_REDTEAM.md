# WP-03 freeze — adversarial red-team (second pass)

**Date:** 2026-09-18  
**Target:** `WP-03_FREEZE.md` rev 1.0  
**Against:** Official PS multimodal/OCR; WP-00–05; DM R0/Q1–Q6; Observed enterprise ingest security (MIME sniff, rasterize-before-trust, metadata/Unicode strip, quarantine partials, provenance).  
**Prior:** `WP-03_REDTEAM.md` (pre-freeze). This pass attacks the **freeze**.

**Stack:** not locked. Full injection rails = **WP-23** (this WP only sets ingest-side prerequisites).

---

## Verdict

| Question | Answer |
|---|---|
| Direction + DM answers in freeze? | **Yes** |
| Missing for freeze-grade ingest? | **Yes — F1–F14** (security/provenance/partial-failure) |
| Overhyped in rev 1.0? | Mild — “normalize” underspecified; digital PDF hidden-text not named |
| Beyond KWB bounds? | **No** if AV/malware product and full injection stay deferred/WP-23 |
| Confidence rev 1.0 | **0.87** |
| Confidence after rev **1.1** fills | **~0.90** |

**Disposition:** **Applied** in `WP-03_FREEZE.md` rev **1.1**. **GO** to WP-23.

No stack lock. No app code.

---

## 1. Missing (must fill in WP-03)

| ID | Gap | Why it matters | Overreach? |
|---|---|---|---|
| **F1** | **MIME / content sniff** at S0 (not trust extension alone) | Wrong type / polyglot files | No |
| **F2** | **Allowlisted media types** for must-work | Unbounded “handle everything” | No — list PDF/PNG/JPEG/WebP/TIFF + plain text supplement |
| **F3** | **Keep original bytes immutable**; extract is derived | Substitution / lost provenance | No |
| **F4** | **`parser_version` + engine versions** on artefact | Replay / audit (WP-17 feed) | No |
| **F5** | **Digital PDF policy:** prefer **rasterize → OCR** (human-visible) for untrusted/external-origin; do not silently trust hidden text layer | Hidden-text / metadata injection (Observed) | No — principle; dual-diff = ambition |
| **F6** | **S4 hygiene:** strip PDF/image **metadata** for model path; Unicode normalize; strip zero-width/invisible chars; log strips | Ingest attack surface | No |
| **F7** | **Partial unit failure** = flag/quarantine unit — pack cannot be fully `verified` while any required unit `unusable` without explicit skip-with-issue | Silent garbage pages | No |
| **F8** | **Encrypted / password PDF** → fail-closed + issue | Hang/parse abuse | No |
| **F9** | **Embedded file / attachment** in PDF → deny or quarantine (not auto-extract into extract) | Nested payload | No |
| **F10** | **Trust label on artefact:** `machine_extract` → after H1 `human_verified` (still **untrusted-as-instructions** for WP-23) | Stops “verified = safe prompt” | No |
| **F11** | **Drafter hand-off content:** default **normalized text/fields** after H1; page rasters for **H1 UI / ingest VLM only**, not dumped as raw PDF to draft LLM | R0 clarity | No |
| **F12** | **Demo byte ceiling** alongside 5 pages (e.g. soft MB cap — exact N not brand-locked, but **must have a bound**) | Resource DoS | Soft number OK |
| **F13** | Two-source diff (native text vs OCR) | Strong detector | **Ambition** |
| **F14** | Full malware AV / signed quarantine product | Enterprise nice | **Deferred**; offline media Admin path already WP-00 |

---

## 2. Overhyped / soft claims

| Attack | Issue | Fix |
|---|---|---|
| **A1** Normalize = done | Underspecified | F6 hygiene steps |
| **A2** Pre-LLM = no model risk | VLM in S3 still model | Keep; WP-23 treats VLM/OCR out as untrusted until delimited |
| **A3** H1 verifies ⇒ trusted instructions | Human can miss injection | F10 + WP-23 |
| **A4** Topic-by-topic | Already limited | Keep Limits |
| **A5** Allow “skip S5” if “explicitly accepted” in §4 S6 | Ambiguous vs hard H1 | Tighten: S6 only after H1 **confirm** or **reject**; no third path |

---

## 3. Bound check

| Item | In bounds? |
|---|---|
| Pre-LLM plane + 5 pages + OCR/VLM | Yes — Official + DM |
| Rasterize preference for digital PDF | Yes — security hygiene, still on-prem |
| Cloud Document AI / remote URL | Correctly Never |
| Full AV suite as must-work | Beyond SIH — deferred |

---

## 4. Adopt (patterns only) — additions

| Pattern | Adopt into WP-03 | Not |
|---|---|---|
| Content-type sniff + allowlist | F1–F2 | Trust `.pdf` extension |
| Rasterize-then-OCR for hostile/unknown PDFs | F5 | Claim zero OCR error |
| Metadata + Unicode strip | F6 | Cloud scrubbing SaaS |
| Quarantine partial pages | F7 | Silent index |
| Provenance hash + parser_version | F3–F4 | — |
| Prompt delimiters / tool inheritance | **WP-23** | Duplicate here |

---

## 5. Micro-fills for rev 1.1

1. S0: sniff MIME; allowlist; size+page bounds; immutable original.  
2. S1: encrypted PDF / embedded attach → issue/deny.  
3. S1/S3: digital PDF → prefer raster+OCR path (F5).  
4. S4: metadata strip + Unicode/ZWSP hygiene; parser_version fields.  
5. Partial units + F7.  
6. Trust labels F10; S6 tighten; drafter gets text/fields F11.  
7. Soft MB demo cap F12 (state “Admin-configurable; demo default required”).  
8. Ambition: text-layer vs OCR diff (F13).

---

## 6. Confidence

| Theme | Score |
|---|---|
| DM + Official coverage | 0.92 |
| Pre-LLM R0 completeness after F fills | 0.90 |
| Ingest security hygiene | 0.70 → **0.88** with F1–F12 |
| Injection (full) | 0.55 — correctly WP-23 |
| **Overall after 1.1** | **~0.90** |
