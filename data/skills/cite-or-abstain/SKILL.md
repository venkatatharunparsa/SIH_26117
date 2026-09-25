---
name: cite-or-abstain
description: >
  Retrieval grounding rules — never cite what was not retrieved under the grant.
task_families: [inspection, freestyle]
license: MIT
---

# Cite or abstain

- Only cite paths/snippets returned by Workbench retrieve under the active grant shelves.
- If nothing matches: write **NOT FOUND — no grounded citations**.
- Do not use public web knowledge as a citation.
- H7 / Review citations is a human gate before Word DRAFT.

## Agent steps

- retrieve | Retrieve under the grant | Only shelves the grant allows
- review_cites | Cite or abstain | If nothing matches, write NOT FOUND — do not invent
