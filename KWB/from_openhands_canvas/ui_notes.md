# Agent Canvas — UI study notes (desk vibe)

**Status:** STUDY ONLY. Do not fork Canvas into `desk/`.

## What to study for desk vibe

1. **Boundary clarity** (`docs/architecture.md`): UI renders and translates actions; it does not execute sandbox work or hold LLM credentials. KWB desk should feel the same — assist surface, not jail or GPU.
2. **Confirmation as a gate, not decoration:** `useRespondToConfirmation` posts `{ accept }` back to the agent session. Pattern: privileged step pauses → human yes/no → resume. Map to our **self-HITL** (own extract / cites / draft / sandbox), not boss-forward queues.
3. **Conversation + evidence adjacency:** Canvas keeps chat, files, and terminal near each other. For KWB, keep draft / cites / H9 evidence near the task thread without IDE chrome.
4. **Mode honesty:** Canvas documents host-filesystem risk in local `dev`. Our desk copy should never imply “always isolated” when the runner is process-jail only.

## What to refuse

| Refuse | Why |
|---|---|
| Fork Agent Canvas / copy `src/components/**` as product | Coding IDE control center ≠ inspection Word workbench |
| Browser / computer-use panels | WAN + out of Expected Solution |
| Cloud / multi-backend switcher UX | Breaks air-gap / single local `/v1` story |
| Automation / schedule / Slack-style trigger UI | Out of PS |
| Marketplace skill install flows | Offline Never |
| In-app accept-for-forward / boss queues | Product boundary: assist → export only |
| Glow-heavy IDE chrome, multi-panel terminal fetish | Wrong brand for plant inspection desk |

## Integrate later?

**No** as UI code. **Yes** as interaction metaphors when designing `desk/` HITL screens (confirm own work → continue).
