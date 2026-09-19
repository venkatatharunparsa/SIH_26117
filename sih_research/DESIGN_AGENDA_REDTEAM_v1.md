# Red-team: org design agenda (SIH26117)

**Date:** 2026-09-17  
**Target:** `DESIGN_AGENDA_ORG_v1.md` plus the 2026-09-17 user intent (MCP/plugins, task agents, `.md` personalization, version–task relations, smart routing + data-to-pass, revoke-after-task, citation RAG, valid gateway, operator monitors).  
**Mode:** Adversarial. Nothing here is a stack lock. Nothing here is a freeze until the matching WP is walked.

Grades: **Official** = PS / named spec / statute. **Observed** = vendor docs, IETF drafts, papers, operator guides. **Unverified** = we have not independently reproduced it. **Invalidated** = contradicts Official.

---

## Verdict

The 21-WP queue is the right spine. It is **not complete** for the product you described.

Your 11 parts are all real org layers. The missing risk is not “forget RAG.” The missing risk is **trust boundaries**: plugins that can talk to the WAN, sessions that see too much, retrieval that cannot tell a user claim from a controlled SOP, and an intelligent layer that dumps whole files into the model.

PS Background is the product metaphor: industrial users should work **the way they use Claude or Codex**, on premises. PS Expected Solution is the acceptance test: two-task auto-select, scan→Word, sandbox-verified code, multimodal, **visible zero-egress**. Those two sentences must live together. A Claude-class plugin host that fetches MCP from npm or a public directory **fails the sovereign claim**.

---

## Source-of-truth table

| Claim | Grade | Source |
|---|---|---|
| Workbench must feel like Claude/Codex for confidential work; cloud assistants are forbidden for P&IDs/financials/etc. | **Official** | SIH26117 Background (`01-problem-statement.md`) |
| Agent must plan, call **local** tools (file R/W, sandbox code, spreadsheet, internal search), iterate; local KB; nothing external | **Official** | SIH26117 Description |
| Binding demo: ≥2 task types auto-select; inspection scan → Word; sandbox coding; OCR/vision; logs or **visible network monitor** = no external calls | **Official** | SIH26117 Expected Solution |
| MCP is an open protocol: host (client) ↔ server (tools/resources/prompts); local stdio + Streamable HTTP | **Official** | [modelcontextprotocol.io transports 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports); [Anthropic MCP announcement](https://www.anthropic.com/news/model-context-protocol) |
| Claude Desktop / Claude Code: users **add** local or remote MCP servers; scopes: local / project / enterprise | **Observed** | [Connect local MCP servers](https://modelcontextprotocol.org/docs/develop/connect-local-servers); [Claude Code MCP](https://code.claude.com/docs/en/mcp) |
| Anthropic Messages API MCP connector requires **public HTTPS**; **cannot** attach local stdio | **Observed** | [Claude MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector) — do not copy this pattern into an air-gap workbench |
| Agent Skills = directory + `SKILL.md` (YAML + markdown); progressive disclosure | **Official** | [agentskills.io/specification](https://agentskills.io/specification) |
| Agent Plugins 1.0 packages `plugin.json` + `skills/` + `mcp.json`; Cursor/Codex/Copilot/VS Code listed at launch; spec **does not** define portable permissions, secrets, or registries | **Observed** | [Google Developers Blog](https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/); [Cursor plugins reference](https://cursor.com/docs/reference/plugins). Anthropic is **not** listed as a 1.0 maintainer in secondary write-ups — **Unverified** as a legal claim; treat as “do not assume one plugin format everywhere.” |
| MCP spec has **no normative security requirements**; SSRF, tool poisoning, egress | **Observed** | [IETF draft-mohiuddin-mcp-security-considerations-00](https://www.ietf.org/archive/id/draft-mohiuddin-mcp-security-considerations-00.html) |
| Malicious MCP servers are easy; scanners insufficient; allowlist + isolation recommended | **Observed** | [arXiv 2509.24272](https://arxiv.org/html/2509.24272v1); [Docker MCP security](https://www.docker.com/blog/mcp-security-explained/) |
| Air-gapped MCP is **not the default**; npm/PyPI/registry assumed; catalog shrinks | **Observed** | [ConnectorZone air-gapped MCP](https://connector.zone/guides/air-gapped-and-self-hosted-mcp/) |
| Least privilege: only access needed for the **assigned task**; apply to processes too | **Official** | [NIST SP 800-53 Rev 5 AC-6](https://csf.tools/reference/nist-sp-800-53/r5/ac/ac-6/) |
| JIT / revoke-after-use is a PAM pattern that implements AC-6; it is **not** a complete security programme | **Observed** | NIST AC-6 text + PAM industry practice. User already stated this correctly. |
| RAG grounds generation in retrieved docs; retrieval quality ≠ generation quality | **Official** (paper) | Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP*, NeurIPS 2020 |
| OpenAI-compatible LCD: `POST /v1/chat/completions`, `GET /v1/models`, Bearer; vision as `data:` base64 not remote URLs | **Observed** (our prior lock) | `ARCHITECTURE_LOGICAL_v1.md` — still **not frozen** as a product WP until WP-09 |
| CERT-In logging / DPDP / NIST AI 600-1 as org constraints | **Observed** | Prior KB policy notes; cite the statute/advisory in WP-17, do not invent MRPL-specific SLAs |

---

## User intent vs agenda (what was wrong)

| You said | Agenda v1 treated it as | Red-team correction |
|---|---|---|
| Workbench where users **add MCP or plugins** and use them | WP-08 optional adapter; “decide yes/no” | **Product intent: we are an MCP/plugin host**, like Claude Desktop / Cursor / Codex. The WP freeze is *how* (air-gap, allowlist, isolation), not *whether*. Native tools still exist; plugins wrap or extend them. |
| Separate agents for **defined tasks** | WP-07 “thin, not a swarm until justified” | Keep the warning. Allow **specialist agents** (inspection-note, coding, spreadsheet) behind **one orchestrator**. Swarm-of-peers with shared full access is the failure mode. |
| Self-learning = daily-task `.md` personalization | WP-15 “high fake-risk / maybe reject learning” | Meaning accepted. Name it **personal workflow files**, not self-training. Still HITL before a personal `.md` becomes an org skill. |
| Graph = relations of **data versions and tasks** | WP-14 “graph DB yes/no” | Do **not** start from Neo4j. Freeze a **lineage model**: artefact version ↔ task ↔ model ↔ citations. Storage engine later. |
| Intelligent layer = route models **and** what data to pass | Buried inside WP-06 | Split: WP-06 routes; **WP-21** packs/minimizes context. |
| Session must not grant whole-system data; **revoke after task** | WP-04 identity/ACL only | Add **task-scoped grants**. You are right that this is not complete security. |
| RAG must verify claims vs file / user / policy; slower OK | WP-11 retrieve + WP-12 gates, underspecified | Add **three-source verification** (WP-22). Latency is a product choice, not a bug. |
| Gateway must send **valid** requests | WP-09 auth/timeout/`/v1` | Add **schema + Model Card capability check**. Invalid request never becomes a WAN retry. |
| Monitors that satisfy **users**, not only jury | WP-13 “visible air-gap” | Two audiences: **sovereign proof** (WAN=0) and **operator proof** (routing, citations, HITL, plugin calls, grants). |

---

## Per-WP adversarial notes (queue order)

### WP-00 Product contract

**Must stay:** evidence/document workbench; HITL forever; never DCS/SIS/PLC/EAM write; Expected Solution = acceptance; Description = org ambition.

**New never:** “Claude-like” must not be read as “Claude cloud connectors” or “public MCP directory.”  
**New never:** plugin marketplace with internet install.

If WP-00 does not write **plugin host + local-only install**, WP-08 will smuggle WAN.

### WP-01 Users / artefacts

**Missing:** three artefact classes — (a) plant-controlled (SOP revision), (b) workbench-generated (draft Word), (c) personal `.md`. Mixing them in one folder is how personal notes become fake SOPs.

**Missing:** plugin author vs plugin user vs approver.

### WP-02 Plant systems

MCP that “connects to SAP/Maximo” is org-ambition **read-only** with a declared destination. Unrestricted MCP to EAM is a write path in disguise.

### WP-04 Identity / session / data access

Full-session plant dump is the bug you named.

**Design target (proposal, not freeze):**

- Session authenticates the **person**.
- Task opens a **grant**: sources, tools, plugins, classification ceiling, TTL.
- Task end / timeout / user abort → grant **revoked**. Tokens and retrieved chunks dropped from working memory.
- Standing role still exists (who may request a grant). Grant ≠ role.

**Adversarial:** revoke-theatre. If the model already copied P&IDs into chat history or a draft `.md`, revoke does nothing. Need: no standing copies outside the grant store; generated files inherit classification; personal `.md` cannot silently hold live grants.

NIST AC-6 is the Official hook. JIT PAM is Observed practice. **Not complete security** — still need HITL, sandbox, classification, air-gap, no plant write.

### WP-05 HITL

Plugin install, org-skill promotion, export, and “policy vs user contradiction” need gates. If HITL is only “approve the Word file,” plugins and `.md` bypass it.

### WP-03 Ingest

Scans/OCR are untrusted content. They can carry prompt-injection. Treat OCR text like MCP tool output: untrusted.

### WP-11 Retrieve / RAG

PS wants grounding in manuals/SOPs/correspondence. You want **claim verification**, even if slower.

**Must design:**

- Retrieval is **revision-aware** (which SOP version).
- Retrieval is **ACL-aware** (grant, not role dump).
- Citations are **mandatory** on grounded claims; `NOT FOUND` is a valid output.
- User utterance is a **claim source**, not a fact.
- Company policy is a **third corpus**, not a system prompt footnote.

Vectors-only is not plant storage. EAM/DMS remain systems of record.

### WP-07 Tools / prompts / agents

PS tool list is Official: file, sandbox, spreadsheet, internal search.

**Specialist agents:** one orchestrator; task-typed agents; **no shared super-context**. Inspection agent does not inherit the coding sandbox grant.

System prompt is policy, not a skill. Skills/plugins are loaded by task (Agent Skills progressive disclosure — Official).

### WP-16 Sandbox

Sandbox is for **generated code**, not for GPU, not for MCP by default. If an MCP server is untrusted, it may *also* need isolation — that is WP-08, not “wrap the GPU.”

### WP-08 Plugin host (MCP)

This is the largest agenda error in v1.

**Correct product reading of the PS:** users add tools the way they add them in Claude/Codex/Cursor. MCP + Agent Skills + (Observed) Agent Plugins is how that industry works in 2026.

**Correct air-gap reading of the PS:** nothing leaves premises; visible monitor.

**Tension (must be designed, not wished away):**

1. Workbench is an MCP **host**.
2. Allowed servers: **stdio or localhost HTTP**, shipped on approved media, **allowlisted**, signed/pinned if we later freeze a scheme.
3. **No** public HTTPS MCP connector pattern (Anthropic API — Observed, wrong for us).
4. **No** `npx`/`pip install` at runtime (ConnectorZone — Observed).
5. Each plugin: default-deny egress at process/container, not in Python.
6. Tool names/descriptions are untrusted (arXiv 2509.24272; IETF draft).
7. User can enable a plugin; **org policy can forbid** classes (WAN, mail-forward, arbitrary filesystem).
8. Every plugin call is audited (WP-17) and can require HITL (WP-05).

Prototype may ship **zero community plugins** and still be a host (install UI + one local demo server). That is honest. A slide that says “MCP ecosystem” with WAN install is fake.

### WP-06 Orchestration + task intelligence

PS Description: pick the right model for the task (coding ≠ summary). Expected Solution: show auto-select on ≥2 types.

**Must never:** model picks safety/FFS/statutory outcome.

**Missing until WP-21:** routing without data-minimization will put whole manuals into a 7B context and call it intelligence.

Routing inputs: task type, Model Cards (vision/tools/context), grant classification, plugin needs. Not VRAM as the product story (hardware is WP-10).

### WP-09 LLM gateway

Software socket. Send **valid** `/v1` requests only:

- Schema valid (messages, model id, optional vision `data:` only).
- Model id on the **runtime catalog**.
- Capability flags match the task (no `tool_choice` if LCD forbids it — prior lock, re-confirm in WP-09).
- Size, timeout, auth.
- Fail closed. Do not “helpfully” rewrite to a cloud base_url.

Gateway is not the plugin bus. MCP stays on the workbench host unless we later freeze a broker.

### WP-10 Runtime

Unchanged: catalog, load, add-model-without-redesign. Plugins must not assume they can load weights.

### WP-12 Validation gates

Before the user **sees or downloads**: citation check, export classification, PII/secret scan, sandbox verdict. Slow is OK. Silent pass is not.

### WP-17 Audit / lineage

Must log: person, task id, grant, model id, plugins/tools, retrieval revisions, HITL, export. CERT-In-shaped. Lineage here **feeds** WP-14; they are not duplicates.

### WP-14 Generated storage / relations

**Not** “do we buy a graph database.”

**Yes:** relation store of `task → input versions → tool/plugin calls → model → draft artefact versions → HITL → export`.

That is how an engineer sees *what they are building*. SQL, files+manifest, or a graph engine are implementation. PPT must say **lineage**, not Neo4j, until a WP freeze names an engine.

### WP-13 Monitors

**Audience A — sovereign proof (Official):** WAN/external call count = 0, visible.

**Audience B — user (your requirement):** live task, selected model, **why**, citations pending, HITL queue, sandbox pass/fail, **active grant** (what data/plugins), plugin allow/deny, last `.md` skill loaded.

App-only WAN widget is weak if the OS still egresses. Org paper needs host/OS evidence, not only a React panel.

### WP-15 Harness / personal `.md`

Matches Agent Skills. Daily use → workbench writes/updates personal markdown (task patterns, preferred templates, folder conventions).

**Never:** unsupervised weight updates on plant data.  
**Never:** auto-promote personal file to plant SOP.  
**Promotion path:** personal → proposed skill → HITL → org skill pack (offline).  
**Poison path:** injected instructions in a `.md` the user did not review.

`compatibility: requires internet` skills are unloadable here.

### WP-18 Fail-closed + eval

Add evals: wrong model routed; citation missing; plugin denied; grant expired mid-task; policy/user contradiction.

### WP-19 Offline update

Applies to **weights and plugins**. USB/approved media. No silent registry pull.

### WP-20 Connection diagram

Must show: person → session → **grant** → orchestrator → specialist agent → (tools | **plugin host**) → gateway → runtime; retrieve with revision; lineage; monitors A and B; HITL.

---

## Missing work packages (add to agenda)

| New WP | Why v1 missed it | If we skip it |
|---|---|---|
| **WP-21** Context assembly / data-to-pass | “Intelligence” was only routing | Model sees whole plant or sees nothing useful |
| **WP-22** Three-source claim verification | RAG was storage-shaped, not verification-shaped | User claim overwrites SOP; policy ignored |
| **WP-23** Untrusted content / prompt injection | Ingest, RAG, MCP, `.md` are all instruction channels | Plugins and personal files jailbreak the agent |

Also **fold into existing WPs** (not extra numbers): plugin supply-chain, per-plugin egress, personal vs org artefact classes, grant revoke vs copied data, specialist-agent isolation.

---

## Direct attacks on the 11-part list (still true after your clarifications)

1. **MCP without host isolation** = WAN and local filesystem as tools. Fails Expected Solution.  
2. **Self-learning as fine-tune** = policy hole. Your `.md` reading is the surviving meaning.  
3. **Graph DB as uniqueness** = fake. Lineage is the need.  
4. **Intelligent layer as decision-maker** = contradicts HITL product definition.  
5. **Session = security** = leak. Grants + classification + HITL + air-gap together.  
6. **RAG = Chroma** = misses revision and policy corpora.  
7. **Gateway = GPU** = category error.  
8. **Monitor in the app only** = weak sovereign proof.  
9. **New:** plugin install from the internet = Claude-cloud behaviour, not this PS.  
10. **New:** one agent with all plugins loaded = standing privilege.  
11. **New:** personal `.md` stored next to controlled SOPs = document-control failure.  
12. **New:** “verify every claim” without a contradiction policy = the model picks the friendliest sentence.

---

## Honest limits of this red-team

- We did not re-fetch CERT-In directives or DPDP full text in this pass; WP-17 must cite them at freeze, not from memory.  
- Agent Plugins 1.0 client list is from vendor blogs (Observed), not a court-grade spec dump.  
- No MRPL IdP/DMS interface is verified. WP-02 stays “surrounding systems,” not connectors we claim to have.  
- Hardware 8 GB sequential 7B is a **prototype** fact, not an org-paper uniqueness claim.

---

## What changes in the agenda file

- MCP/plugin **host** is product intent; freeze at WP-08 is constraints, not existence.  
- Self-learning and graph rows retitled to your meanings.  
- WP-21, WP-22, WP-23 inserted in the queue.  
- Adversarial flags updated.  
- Still: one WP at a time; stack not locked; no PPT fill; no app code.

Queue still starts at **WP-00** when you say go.

---

## Addendum 2026-09-17 — pluggable models + PS sweep

User catch: add/remove model must not change the workbench. **Correct.** Agenda v2 buried this in WP-10 (GPU). It is a **workbench catalog** (now WP-24). PS Official: “not locked to one model”; “addable later without redesigning.” Remove is the inverse of add (user extension). OCR/vision models are plugs too. `/v1` is transport, not an allowlist. Hugging Face at demo time fails “no external calls at any point.”

Full clause matrix: `DESIGN_PS_COMPLETENESS_v1.md`. Other buried Official clauses: file **write**; **iterate**; KB **connector** + correspondence; PPT and **calculations with steps**; workstation **or** server; open-weight policy; classification of financials/vendor/P&ID. Same *kind* of plug as models: plugins, runtime `base_url`, KB connector target. Not plugs: HITL, air-gap, never-write-DCS.
