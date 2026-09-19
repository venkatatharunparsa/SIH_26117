# SOURCE — from_openhands_canvas (STUDY ONLY)

**Upstream:** `vendor/OpenHands/` (Agent Canvas — React/TS UI)  
**License:** MIT (`vendor/OpenHands/LICENSE`)  
**Role:** Desk-vibe study notes + architecture docs. **Not** a UI fork.

## What was copied

| KWB path | Upstream path |
|---|---|
| `docs/architecture.md` | `docs/architecture.md` |

## MISSING — short HITL / confirm docs

| Sought | Result |
|---|---|
| Dedicated HITL / confirmation markdown under `vendor/OpenHands/docs/` | **MISSING** — no HITL-specific doc; confirm UX lives in TS |

**Study pointers (do not copy full UI tree):**

- `src/hooks/mutation/use-respond-to-confirmation.ts` — accept/reject API mutation
- `src/components/shared/buttons/conversation-confirmation-buttons.tsx`
- `src/components/shared/modals/confirmation-modal.tsx`
- `src/components/features/chat/confirmation-mode-enabled.tsx`

See `ui_notes.md` for what to study vs refuse.

## What KWB will use later

- Product-boundary ideas: Canvas renders conversation; Agent Server owns execution (mirrors our desk ≠ sandbox ≠ gateway).
- Confirmation **interaction pattern** only → map to our self-HITL gates (H1/H7/H2/H9), not Canvas components.

## What NOT to import as product

- Entire Agent Canvas / `@openhands/agent-canvas` as KWB desk.
- Browser panel, terminal IDE chrome, automation server UI, cloud backend switcher.
- Library embed entrypoints (`build:lib`) as our product shell.
