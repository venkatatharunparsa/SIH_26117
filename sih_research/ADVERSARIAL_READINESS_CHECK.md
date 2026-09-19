# Adversarial readiness check — SIH26117

**Date:** 2026-09-16  
**Question:** Do we have enough information to *design* a solution that is not a fake?  
**Verdict (bottom line):** **Yes to design the prototype architecture. No to claim production industrial completeness. High risk of “demo theatre” if we oversell and under-prove.**

---

## 1. Between the lines of the PS

### What the PS *says* vs what it *contracts*

| Layer | Content | Binding force |
|---|---|---|
| Background | Shadow AI; Claude/Codex UX gap; confidential industrial knowledge work | **Motivation** — jury story |
| Description | Air-gap GPU server; multi-model; agent + tools; multimodal; Office deliverables; local KB | **Product shape** — design target |
| Expected Solution | Mid-GPU deploy; ≥2-task model auto-select; inspection→Word; sandbox coding; multimodal; **visible zero-egress** | **Acceptance test** — what must work |

**Reading between the lines:**

1. **Expected Solution is the law.** Description is the ambition. If we build a beautiful “platform” that fails any Expected Solution bullet, we fail.
2. **“Claude or Codex way” is a usefulness bar**, not a request for frontier-model parity. Mid-range GPU + smaller models are explicitly allowed.
3. **“Nothing deployable exists…”** is PS rhetoric. We already know adjacent products exist. Claiming absolute uniqueness is a trap; claiming “Claude-class local industrial workflow with proof of sovereignty” is the honest bar.
4. **Example workflow is the primary demo** (“for example… inspection → Word”). Other description items (PPT, drawings, handwriting) are *capabilities*, not all mandatory demo paths.
5. **Agent ≠ multi-agent swarm.** PS says plan multi-step work and call tools. A single orchestrated agent with tools satisfies the letter; multi-agent is optional complexity.
6. **Air-gap proof is non-negotiable.** “We ran offline” without a visible monitor/logs is a statement, not proof — PS says so explicitly.
7. **Calculations with steps shown** implies deterministic computation (sandbox), not LLM arithmetic — otherwise judges will break you on a wrong number.
8. **Local KB connector** can be a folder / Chroma / JSON corpus for the prototype; it does *not* require SAP.
9. Typo/oddity: “do the work manually resulting in productivity **gain**” — almost certainly meant loss/pain. Ignore literal reading; intent is shadow AI + manual burden.

### Hidden / easy-to-miss requirements

- Models must be **addable later without redesign** → need a model registry interface, not hard-coded one model.
- Coding task must be **verified** (tests/run), not “generated code that looks right.”
- Multimodal must be **on-device** OCR/vision — no cloud OCR API (that would break air-gap).
- File R/W + spreadsheet tools are listed — inspection path needs file ingest; Excel output or spreadsheet tool satisfies spirit.
- Venue may lack 120B hardware → **design for 7B–14B / 16–24GB VRAM** or we design a fake that only works on fantasy hardware.

---

## 2. Attack our own findings (adversarial)

| Our finding / decision | Attack | Status |
|---|---|---|
| “Evidence workbench not chatbot” | PS never uses that phrase; it asks for Claude/Codex-like assistant | **Still valid** — framing for industrial honesty; must still *feel* useful like an assistant |
| Inspection → Word as primary | Only an “example” | **Safe** — Expected Solution elevates it; best single path covering agentic+multimodal+deliverable |
| Classification policy engine / Public→TS | Not in Expected Solution | **Prototype risk** — valuable for judging novelty, but if it delays E2E, cut to badge+draft label only |
| Industrial entity resolution (P-204A) | Hard; easy to fake with regex on clean text | **Honest scope:** rule-based tag match on synthetic data = OK if labelled; claiming plant-scale ontology = fake |
| MRPL process-AI gap | True from chairman speech | **Jury useful**, not a build requirement |
| Org-scale architecture first | Can delay working demo | **Tension** — keep one diagram; **build** only MVP path |
| “Air-gap as strongest posture” | PS requires full air-gap for demo | **For SIH:** air-gap is mandatory, not optional |
| Selective OSS harness borrow | Can become rabbit hole | **Risk of fake progress** — researching harnesses forever without a thin working loop |
| Time-to-draft 2 days→2h | Unvalidated | **Do not claim as measured** |

---

## 3. Fake-solution traps (unbuildable or dishonest demos)

These are the ways we could *look* done and still fail:

| Trap | Why it’s fake | How to avoid |
|---|---|---|
| **Hardcoded OCR / scripted “agent”** | Looks E2E; dies on new PDF | Real OCR on held-out scan; show confidence; tolerate errors |
| **Chat text pasted into .docx** | Not a deliverable pipeline | Template → structured fields → python-docx |
| **LLM invents thickness / CR** | Engineering lie | Sandbox `CR=(t_prev-t_curr)/Δt` with printed inputs |
| **Egress “off” but HF/Ollama pulls at runtime** | Network monitor catches it | Pre-stage weights/images; offline pack; no registry calls |
| **One model with fake “routing” logs** | Fails ≥2 task types | Actually load/route two roles (e.g. vision/extract vs draft/code) — even if both small |
| **Sandbox that isn’t isolated** | Coding “verified” on host = weak | `network=none` container or equivalent; show test run |
| **Claim P&ID understanding** | Description mentions drawings; Expected Solution doesn’t require P&ID symbol AI | Photos/scans of *tables/text* first; drawings = stretch |
| **Claim real MRPL integration** | Unbuildable without access | Mock connectors, honest labelling |
| **Claude-quality on 8GB VRAM** | Unrealistic | Promise mid-GPU small models; show usefulness not magic |
| **Policy/ACL theatre without E2E** | Novelty slide, no working path | Ship E2E first; ACL as thin role gate |
| **Multi-agent LangGraph sprawl** | Complexity cosplay | One planner + tools until E2E works |
| **“Useful like Claude” without iteration** | Agent must iterate | Show ≥1 retry/tool loop in logs |

**Buildability verdict for Expected Solution:** Each bullet is **buildable** with open tools on a mid GPU **if** we stay narrow and honest about mocks.  
**Unbuildable in hackathon:** production ACL inheritance, real historian/EAM, certified air-gap accreditation, Claude-parity reasoning, industrial P&ID CAD understanding.

---

## 4. Do we have enough information?

| Decision level | Enough? | Confidence | Missing |
|---|---|---|---|
| **What problem to solve** | YES | 0.95 | Official SIH PDF copy (nice-to-have) |
| **What prototype must prove** | YES | 0.95 | — |
| **Component architecture (logical)** | YES | 0.85 | GPU reality check |
| **Exact model names / quant / VRAM fit** | NO | 0.40 | Hardware + offline offline pack list |
| **Exact harness (compose vs fork)** | NO — and shouldn’t block design | 0.50 | Preference + spike spike later |
| **Production MRPL deployment design** | PARTIAL | 0.55 | Real system names, templates, IdP — post-SIH |
| **Go build code tomorrow** | CONDITIONAL | 0.70 | Hardware + sample docs + team skill map |

**Overall:** We have **enough to design** the solution architecture and freeze the prototype acceptance tests. We do **not** yet have enough to freeze implementation stack without a short hardware/model spike. Designing now is not premature; **coding a sprawling “platform” now would be premature.**

---

## 5. Adversarial questions we must answer before build

### Product / honesty
1. If the judge uploads a *new* scan we never saw, does the path still run (even poorly)?  
2. If OCR fails, do we fail loudly or hallucinate findings?  
3. Can we show two *different* models actually serving two task types?  
4. Does “verified” coding mean `pytest`/`python` exit 0 in sandbox?  
5. Is the network monitor showing *process* egress or just Wi-Fi off? (Wi-Fi off alone is weak if local services call WAN.)

### Scope discipline
6. Are we building one E2E path or a fake platform shell?  
7. Is PPT required for MVP or optional (Description yes, Expected example no)?  
8. Is handwriting in MVP or deferred?  
9. Is “engineering drawings” deferred?  

### Feasibility
10. What VRAM do we actually have?  
11. Can both a VLM and a text/coder model fit (sequentially vs simultaneously)?  
12. Are all weights/containers downloadable before air-gap rehearsal?  
13. Who owns offline pack creation?

### Jury / PS fit
14. Does our story match Expected Solution bullets in order?  
15. Are we overselling production industrial claims that the prototype cannot show?

---

## 6. Research / materials you can bring (to raise confidence)

**Highest value (bring if you can):**
1. **GPU inventory** — exact GPU model, VRAM, RAM, disk, OS (Windows/Linux).  
2. **1–3 sample inspection PDFs** — synthetic/redacted thickness/NDT scans (or permission to generate fixtures).  
3. **Offline constraint list** — can venue be fully offline? proxy?  
4. **Team skill map** — who does UI / backend / ML / domain / demo.  
5. **Official SIH26117 PDF / portal export** if different from KB verbatim.

**Useful but not blocking design:**
6. Any preferred open-weight families already downloaded (Qwen-VL, Llama, Mistral, etc.).  
7. College internal-hackathon rubric if any.  
8. Whether PPT is required in *your* internal round.

**Not needed for prototype design (do not block):**
- Real MRPL SAP/EAM credentials  
- Real P&IDs  
- Formal security accreditation docs  

---

## 7. Possibilities (valid solution shapes)

| Shape | Fits PS? | Fake risk | Note |
|---|---|---|---|
| A. Thin orchestrator + local inference + tools + templates | YES | Low | **Recommended** |
| B. Fork OpenHands/DeerFlow heavily | Maybe | Medium | Time sink; only if spike proves faster |
| C. Open WebUI + scripts | Partial | High | Weak agent/routing/egress story |
| D. Multi-agent “platform” + many connectors | Overshoot | High | Looks impressive, fails E2E |
| E. Vision-only industrial CAD product | No | High | Misses coding + routing + agent contract |

---

## 8. Recommendation

**We have enough information to design.**  
Freeze:

1. Acceptance tests = Expected Solution checklist (binary).  
2. Logical architecture (registry, router, agent+tools, OCR/VLM, sandbox, KB, docx/xlsx, egress monitor).  
3. Explicit out-of-scope list for prototype.  
4. Honest demo narrative (real vs mock).

**Do not yet freeze:** exact model SKUs, exact harness repo, UI framework — until GPU + offline pack known.

**Confidence to design:** **0.82**  
**Confidence Expected Solution is buildable if scoped:** **0.78**  
**Confidence we avoid a fake demo without discipline:** **0.55 → rises to ~0.8** if we adopt the anti-fake rules in §3 and you provide GPU + sample docs.

---

## 9. Discussion prompts for you

1. Confirm: **Expected Solution checklist = only MVP definition**?  
2. Confirm: PPT / handwriting / P&ID = **post-MVP**?  
3. Can you share **GPU/VRAM** (or “unknown — design for 16–24GB”)?  
4. Sample inspection docs: you bring / I generate synthetic?  
5. After that: proceed to **architecture ADR only** (still no code)?
