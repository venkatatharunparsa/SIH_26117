# WP-05 rev 2.0 — adversarial research + red-team verify

**Date:** 2026-09-19  
**Target:** DM answers on discuss §16 + Admin-as-IT clarification  
**Verdict:** **GO — we are going the right way** for KWB product shape, **with hard limits** on Admin and honesty labels (below). Not CERT. Not plant four-eyes.

---

## DM answers locked (this pass)

| # | Answer | Red-team result |
|---|---|---|
| **1** Self-HITL H1/H2/H3/H7/H9 | **Yes** | **PASS with label** — valid for assist→export; **fails** if sold as plant dual-control |
| **2** H3 = export leave; paper Approver outside | **Yes** | **PASS** — matches F6/D8/D9; strongest consistency win vs rev 1.1 |
| **3** Admin = IT-style full control of the **application** | **Yes** | **PASS with scope fence** — platform/config only; **not** content HITL; **cannot** break Never |
| **4** Stale / version re-check | Verify via red-team | **PASS** — keep; attacks below addressed |

---

## External research hits (patterns)

| Pattern | Implication for us |
|---|---|
| Self-approval of **critical / record-facing** actions = rubber stamp (SoD literature) | Our H2/H3 must stay **own-work / export leave**, **never** “plant approved”. Plant = **H12 outside**. |
| Reviewer identity ≠ requester for dual control | We **do not** claim in-app dual control. Paper outside may do SoD. |
| Admin / break-glass must be audited and time-boxed; least privilege | Admin = **IT platform** role; sparse assignment; immutable audit |
| Policy engine ≠ model | Unchanged — gates are deterministic, not LLM |

---

## Attack table (rev 2.0)

| ID | Attack | Result | Mitigation in freeze |
|---|---|---|---|
| **RT1** | Sell self-HITL as plant four-eyes | **Kill** if overclaimed | Limits + H2 “not plant approval” + H12 outside |
| **RT2** | Worker rubber-stamps H2/H3 without reading | Residual risk (any self-HITL) | Explicit control + audit + stale on edit; **not** eliminated — honesty |
| **RT3** | Admin clicks H2/H3 for worker (“IT fixed it”) | Bypass self-HITL | **Forbid** Admin as actor on H1/H2/H3/H7/H9 (M9) |
| **RT4** | Admin “full control” → break Never / plant write | WP-00 violation | Admin **cannot** override Never; no plant write |
| **RT5** | Admin enables public `/v1` or pull | Air-gap kill | Cards/gateway still deny public URL; no-pull policy |
| **RT6** | Skip stale after edit → export old accept | Classic bypass | H3 requires fresh H2/H1/H9 |
| **RT7** | Agent rewrites DRAFT after H2 | Silent change | Material change → stale (W10) |
| **RT8** | Sandbox green = H9 skipped | Code “approved” | H9 hard; sandbox-red blocks export |
| **RT9** | H7 auto-pick user over policy | Policy drift | H7 surface; escalate **outside** |
| **RT10** | WP-01 still lists in-app Approver | Dual freeze story | **Must reopen WP-01** after WP-05 2.0 freeze |
| **RT11** | Dual-role demo “I’m Approver now” for export | Brings back 1.1 confusion | Removed from must-work |
| **RT12** | Admin installs malicious MCP | Supply chain | H5 Admin + USB/quarantine + grant ∩ allowlist |

---

## Admin-as-IT — allowed vs forbidden (binding fence)

### Admin **may** (application / IT control)

- Model **cards** enable/disable (local tags only; no pull)  
- MCP / skill **allowlist** (H5/H6)  
- Org **templates** / org shelves (H4)  
- Offline USB **intake ack** / staging  
- Audience A monitor evidence path config  
- High-class grant expand UX (H8) under policy  
- See sovereign / host evidence tooling  

### Admin **must not**

- Override **Never** (WP-00)  
- Write **plant** SoR  
- Pass **H1/H2/H3/H7/H9** for another user (no proxy self-HITL)  
- Act as in-app **plant Approver**  
- Enable **public** inference URL or registry pull  
- Silent break-glass without **audit**  

**One line:** Admin = **IT owns the box**; Worker = **owns the task decisions**; Paper officer = **outside**.

---

## Stale / version — red-team verify

| Check | Hold? |
|---|---|
| Accept binds to `artefact_version` | **Yes** — keep |
| Material edit → void prior H2 | **Yes** — keep |
| Export denied while stale | **Yes** — keep (G10-shaped with H9) |
| Debounce / batch versions | **Yes** — avoid per-keystroke spam |
| Preview PDF ≠ export | **Yes** — keep D6 |

**Residual:** fingerprint algorithm not locked (OK for discuss). Implementation must not soft-skip stale checks.

---

## Consistency with locked product

| Lock | Aligns with rev 2.0 + Admin fence? |
|---|---|
| F6 self-HITL | **Yes** |
| Assist→export | **Yes** |
| No forward-accept | **Yes** |
| Ollama inference only / no pull | **Yes** (Admin cannot pull via policy) |
| Org/demo diagrams | **Yes** |
| WP-00 Never | **Yes** if Admin fence held |
| WP-01 Approver role text | **No — gap** until WP-01 reopen |

---

## Confidence after this verify

| Axis | Score | Note |
|---|---|---|
| WP-05 rev 2.0 direction (product-right) | **0.91** | GO |
| WP-05 ready to mark FROZEN 2.0 | **0.88** | After applying Admin fence + RT notes into freeze |
| Architecture freeze (post WP-05 only) | **~0.78** | Still need WP-01 reopen + WP-20 + G1 honesty for ≥0.90 |
| Risk if we overclaim SoD in PPT | **High** | Caption discipline required |

---

## Final verdict

### We are going **RIGHT** if we:

1. Freeze WP-05 **2.0** with self-HITL + export leave + paper outside.  
2. Define Admin as **IT platform control** with the **forbidden** list above.  
3. Keep stale/version hard.  
4. Never market H2/H3 as plant approval.  
5. Reopen **WP-01** next so Approver is **org paper only**, not in-app DRAFT acceptor.

### We are going **WRONG** if we:

- Let Admin pass worker gates  
- Let Admin break Never  
- Claim four-eyes / CERT / plant SoD from self-HITL  
- Leave WP-01 Approver-in-app text live beside WP-05 2.0  

**Recommendation:** Apply Admin fence into freeze → DM mark **FROZEN rev 2.0** → schedule **WP-01** reopen (Approver = outside paper only).
