---
name: code-style-guide
description: >
  Project coding standards and style guidelines for Knowledge Work Bench.
  Offline skills pack placeholder — progressive load later (not wired to a runner).
license: MIT
---

# Code Style Guide

Follow these conventions for all code in this project.

Adapted from `KWB/from_software_agent_sdk/08_skills_example` (layout only).
This pack is **offline documentation** until a skill runner is designed.

## Python

- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black default)
- Use type hints for function signatures
- Prefer f-strings over `.format()` or `%` formatting

## Naming Conventions

- Classes: `PascalCase`
- Functions/variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private members: `_leading_underscore`

## Documentation

- All public functions must have docstrings
- Use Google-style docstrings
- Include type information in docstrings when not using type hints

## KWB product constraints

- Prefer patterns copied into `backend/app/*` — do not import `openhands.*` from KWB
- Jail ≠ GPU inference; Gateway stays local-only; HITL gates stay fail-closed
