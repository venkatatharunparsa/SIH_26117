# WP-23 untrusted content — adversarial red-team + adopt map

**Date:** 2026-09-18  
**Target:** `WP-23_ARCHITECT_PERSPECTIVE.md`  
**DM answers:** see §0  
**Against:** WP-00 Never; WP-03 trust_label; WP-04 grants; WP-05 HITL/H9; IETF MCP security draft *ideas*; tool-poisoning Observed; repo map WP-23.

---

## 0. Decision-maker answers (binding)

| Q | Decision |
|---|---|
| **1 Demo refuse** | **OCR MOCK** inject → refuse + visible proof (must-work). RAG inject still in product rules; demo proof = OCR. |
| **2 Chat** | **T1 claim** (not plant fact; WP-22). |
| **3 Sandbox** | **Always HITL before sandbox exec** when the proposal/context is T2–T4-influenced (agent path). Clarifies WP-05: machine-only run without pre-HITL is **not** the agent default. |
| **4 Override detect** | **Heuristic refuse + log = must-work**. |
| **5 Skills** | **Always T3 delimited** (org skill after H6 still T3 data; T0 = policy only). |
| **6 Export scan** | **Must-work light heuristics** before H3 export (local only). |

---

## Verdict

| Question | Answer |
|---|---|
| Architect direction correct? | **Yes** |
| Missing before freeze? | **Yes — M1–M10** |
| Overhyped? | Heuristics as “security”; delimiters unbreakable; H1/OCR mock = complete |
| Align WP-05 sandbox spine? | **Tension** — fixed by pre-exec HITL for T2–T4 (DM Q3) |
| Confidence after fills | **~0.88** → **GO WP-11** |

---

## 1. Missing → fill

| ID | Gap | Fill |
|---|---|---|
| **M1** | Pre-exec sandbox HITL vs WP-05 “machine run” | Agent/T2–T4-influenced: **HITL before exec**; then run; **H9** still for decision accept |
| **M2** | Heuristic catalog minimum | Must detect/refuse patterns: ignore policy/Never, disable HITL, expand grant, WAN/exfil, “you are now”, tool self-install |
| **M3** | Delimiter escape / breakout | Refuse nested fake end-markers; treat residual as T3; log |
| **M4** | Multi-turn persistence | Injected OCR text must not become standing T0 across turns; re-delimit each pack |
| **M5** | Tool-description poisoning | MCP names/descriptions = T3; cannot add tools |
| **M6** | Indirect injection via draft citing OCR | Citations/quotes remain T2/T3 data in later turns |
| **M7** | T1 cannot break Never | Explicit: human chat cannot authorize Never bypass |
| **M8** | Light secret-scan scope | Heuristics: key-like patterns, private key PEM headers, obvious passwords — local; not full DLP product |
| **M9** | Fail-closed if heuristics engine missing | No side-effect / no export without scan+refuse path in must-work |
| **M10** | Demo acceptance | OCR MOCK with inject → refuse+log showable; not RAG-required for demo |

---

## 2. Overhyped → fix

| Attack | Fix |
|---|---|
| **A1** Heuristics = solved injection | Pattern assist only; delimiters + grant + HITL + Never remain primary |
| **A2** OCR MOCK demo = full RAG/MCP safe | Product rules cover all channels; demo proves one channel |
| **A3** Delimiters perfect | Escape handling + lowest-trust tools; not crypto proof |
| **A4** Always HITL = zero sandbox risk | Still need jail ≠ GPU (WP-16); HITL is not complete security |
| **A5** Secret scan = DPDP done | Light heuristics only |
| **A6** T1 “claim” = ignore user | User claims feed draft; verification is WP-22 — not discard chat |

---

## 3. Adopt / refuse

| Adopt | Refuse |
|---|---|
| Delimiters, lowest-trust tool inheritance, local guardrail *ideas* | Cloud moderator |
| Presidio-*idea* light patterns | Full DLP suite as must-work |
| Boundary below model | Skill restrictions as security |

---

## 4. Disposition

**Applied.** → **`WP-23_FREEZE.md` rev 1.0**. Confidence **0.88**. **GO** → **WP-11**.
