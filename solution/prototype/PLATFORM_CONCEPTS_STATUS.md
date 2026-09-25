# Platform concepts — demo implementation status (2026-09-20)

Honest map after implementing partial/missing slices.

| Concept | Status | What exists |
|---|---|---|
| Skill library | **Demo wired** | `data/skills/*` + `backend/app/skills.py` progressive load into `/orch/turn` pack |
| Role-based prompts | **Demo wired** | `backend/app/roles.py` — inspection/coding/freestyle/summary |
| Base Word template | **Demo wired** | `workspace/templates/kwb_inspection_note.docx` seeded; filled by `word_draft` |
| MCP | **Demo host** | In-process allowlist (`mcp_host.py`), default ON; `/mcp/status|tools|call` — **not** full stdio/SSE lifecycle / registry |
| Specialists | **Demo wired** | `specialists.py` extract + cite used on attach |
| Multi-model cards | **Partial** | ≥2 task→card routes; coding auto-binds **2nd local tag if already on Ollama** (no pull). Today often still **floor** single `llama3.2:3b` |
| Multimodal vision | **Not done** | Still paused / needs offline-staged vision tag |
| Full Admin / SSO / plant MCP | **Out** | Org Later |

Smokes: `python backend/scripts/smoke_platform.py` · `smoke_orch_word.py`
