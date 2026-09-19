# OpenHands extract plan — workbench first (hardware later)

**Date:** 2026-09-18  
**Decision:** Design / build **Knowledge Work Bench software** first. **Runtime hardware** (Ollama / llama.cpp / vLLM) decided later — workbench stays OpenAI-shape `/v1` client.  
**License:** MIT (both clones) — attribute if we copy code.

---

## What we cloned

| Path | What it actually is | Role for us |
|---|---|---|
| `vendor/OpenHands/` | **Agent Canvas** (TS/React UI + launchers) | Study only — UI/control-center patterns; **not** our product shell |
| `vendor/software-agent-sdk/` | **Python SDK + Agent Server + tools + workspaces** | **Primary extract source** for coding sandbox / events / tools |

OpenHands moved: the old “all-in-one Python agent” is now mostly in **`software-agent-sdk`**. Canvas talks to Agent Server over HTTP/WS.

---

## Workbench-first boundary (locked)

```text
┌─────────────────────────────────────────┐
│  Knowledge Work Bench (WE BUILD)         │
│  grants · orch · HITL · Word · gates     │
│  gateway client · audit · WAN=0 proof    │
│  thin sandbox runner (inspired by OH)    │
└──────────────────┬──────────────────────┘
                   │ local /v1 only (URL configurable)
┌──────────────────▼──────────────────────┐
│  Runtime (LATER)                         │
│  Ollama / llama.cpp / vLLM — undecided   │
└─────────────────────────────────────────┘
```

Do **not** wait on GPU choice to design workbench modules.

---

## TAKE from OpenHands / SDK (slice only)

| Slice | Where in SDK | KWB module we compose | WP / G |
|---|---|---|---|
| **Jail ≠ inference** | Docs + `DockerWorkspace` vs local LLM | Sandbox never wraps GPU process | WP-16 · G3 |
| **Execute command in workspace** | `workspace.execute_command` / terminal tool | Thin `sandbox_runner.py` | G3, G10 |
| **Network isolation hook** | `DockerWorkspace.network` flag | Pass `--network=none` when Docker available; else process jail (de-Docker) | WP-16 |
| **Event / observation shape** | SDK events / terminal observations | Audit + H9 evidence report fields | WP-17 · H9 |
| **Tool loop idea** | tools: terminal, file ops | Coding specialist tools only (no browser) | WP-07 |
| **LLM as `base_url` + model** | LLM settings / profiles | Our gateway client (cards + grant) | WP-09/24 · G1 |
| **Skills on disk** | skills examples | Our `SKILL.md` progressive load | WP-07/15 |
| **Human intervention** | Canvas HITL / confirmation UX ideas | Our H1–H3/H9 hard gates (not their UI) | WP-05 |

### Priority files to **read** first (study, then reimplement thin)

**Copied into `KWB/required/` for easy integrate** (see `KWB/README.md`):

```text
KWB/required/01_execute_command/     ← command.py + redact.py
KWB/required/02_workspace_local/     ← local.py + models.py + base.py
KWB/required/03_docker_network/      ← docker_workspace.py
KWB/required/04_terminal/            ← terminal tool slice
KWB/required/05_llm_base_url/        ← chat options + base_url snippet
KWB/required/06_architecture/        ← architecture.md
```

Upstream originals (full clones still under `vendor/`):

```text
vendor/software-agent-sdk/openhands-workspace/openhands/workspace/docker/workspace.py
vendor/software-agent-sdk/openhands-sdk/openhands/sdk/workspace/local.py
vendor/software-agent-sdk/openhands-sdk/openhands/sdk/utils/command.py
vendor/software-agent-sdk/openhands-tools/openhands/tools/terminal/
vendor/OpenHands/docs/architecture.md
```

---

## REFUSE / do not take

| Item | Why |
|---|---|
| Fork Agent Canvas as KWB UI | Wrong product (coding IDE control center ≠ inspection Word workbench) |
| Browser / computer-use tools | WAN + not Expected Solution |
| OpenHands Cloud / remote hosted sandbox API | Breaks air-gap story |
| Slack/GitHub/Linear automations | Out of PS |
| ACP Claude/Codex cloud credential flows | Cloud brain |
| Full Agent Server as our orchestrator | We own grants/HITL/Word; OH is coding-agent infra |
| Marketplace / `npx -y` skill install at runtime | Offline Never |

---

## Compose into `backend/` (workbench modules)

| Our file (plan) | Inspired by OpenHands | Ours uniquely |
|---|---|---|
| `app/gateway.py` | LLM `base_url` client | Card + grant + deny public URL |
| `app/sandbox.py` | Workspace execute + network none | 60s · calc-in-jail · de-Docker · ≠ GPU |
| `app/grants.py` | — | Session ≠ grant · revoke G7 |
| `app/router.py` | Agent task routing idea | Task type → Model Card · G1 |
| `app/docx_draft.py` | — | python-docx inspection note · G2 |
| `app/hitl.py` | Human confirm idea | H1–H12 map |
| `app/audit.py` | Event stream idea | Already started · JSONL |
| `app/monitors.py` | — | Audience A WAN=0 snapshots · G5 |

---

## Extract workflow (do this next)

1. **Read** DockerWorkspace + local workspace + terminal executor (notes in this folder).  
2. **Write** `backend/app/sandbox.py` — smallest runner:  
   - input: script path / calc expression  
   - env: no network preference  
   - output: `{ok, stdout, stderr, exit_code, duration_ms}` for H9  
3. **Write** gateway client stub with injectable `base_url` (hardware later).  
4. **Do not** import OpenHands packages into production until we decide on a thin dependency vs reimplement.

---

## Relation to other vendor clones

| Vendor | Use with OpenHands extract |
|---|---|
| `vendor/python-sdk` · `vendor/fastmcp` | MCP MOCK host (after G1–G5) |
| Runtime binary | **Later** — only need mock/fixture LLM or local `/v1` when ready |

---

## Next

Composed:
- `backend/app/sandbox.py` — process jail (+ optional Docker `--network=none`)
- `backend/app/gateway.py` — local `/v1` client · hardware deferred
- Wired: `POST /sandbox/calc`, `/sandbox/python`, `/gateway/chat`, `GET /runtime/status`

Next spine: grants · Model Cards · router (G1) · Word DRAFT (G2).
