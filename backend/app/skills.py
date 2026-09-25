"""Progressive skill library — load on-disk SKILL.md packs into orch context.

Org design: org/plugin/personal shelves. Demo: single shelf under data/skills/.
Not a marketplace runner; grant-scoped progressive disclosure only.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .audit import log_event
from .config import ROOT

SKILLS_DIR = ROOT / "data" / "skills"
_FRONT_MATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)


def _parse_skill(path: Path) -> dict[str, Any] | None:
    raw = path.read_text(encoding="utf-8")
    name = path.parent.name
    meta: dict[str, str] = {"name": name}
    body = raw
    m = _FRONT_MATTER.match(raw)
    if m:
        fm, body = m.group(1), m.group(2)
        for line in fm.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")
    return {
        "id": meta.get("name") or name,
        "name": meta.get("name") or name,
        "description": (meta.get("description") or "").replace(">", "").strip(),
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "body": body.strip(),
        "task_families": _families_from_meta(meta, name, body),
    }


def _families_from_meta(meta: dict[str, str], name: str, body: str) -> list[str]:
    raw = meta.get("task_families") or meta.get("tasks") or ""
    if raw:
        return [p.strip() for p in raw.replace("[", "").replace("]", "").split(",") if p.strip()]
    blob = f"{name} {body[:400]}".lower()
    fams: list[str] = []
    if any(x in blob for x in ("code", "python", "style")):
        fams.append("coding")
    if any(x in blob for x in ("inspect", "thickness", "cite", "vessel", "integrity")):
        fams.append("inspection")
    if not fams:
        fams = ["inspection", "coding", "freestyle"]
    return fams


def list_skills() -> list[dict[str, Any]]:
    if not SKILLS_DIR.is_dir():
        return []
    out: list[dict[str, Any]] = []
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        parsed = _parse_skill(skill_md)
        if parsed:
            out.append({k: v for k, v in parsed.items() if k != "body"})
    return out


def load_skill(skill_id: str) -> dict[str, Any] | None:
    path = SKILLS_DIR / skill_id / "SKILL.md"
    if not path.is_file():
        return None
    return _parse_skill(path)


def select_skills_for_task(task_type: str, *, limit: int = 2) -> list[dict[str, Any]]:
    """Progressive load: at most `limit` skill bodies for this task family."""
    selected: list[dict[str, Any]] = []
    for meta in list_skills():
        full = load_skill(meta["id"])
        if not full:
            continue
        fams = full.get("task_families") or []
        if task_type in fams or "freestyle" in fams:
            selected.append(full)
        if len(selected) >= limit:
            break
    log_event(
        "skills_select",
        task_type=task_type,
        skill_ids=[s["id"] for s in selected],
        count=len(selected),
    )
    return selected


def skills_context_block(task_type: str, *, max_chars: int = 3500) -> str:
    packs = select_skills_for_task(task_type, limit=2)
    if not packs:
        return ""
    parts = ["--- trust:skills ---"]
    used = 0
    for p in packs:
        chunk = f"## skill:{p['id']}\n{(p.get('body') or '')[:1800]}\n"
        if used + len(chunk) > max_chars:
            break
        parts.append(chunk)
        used += len(chunk)
    return "\n".join(parts)


_STEP_LINE = re.compile(
    r"^[-*]\s+([a-z0-9_]+)\s*\|\s*([^|]+?)\s*\|\s*(.+?)\s*$",
    re.IGNORECASE,
)

_HINTS: dict[str, tuple[str, ...]] = {
    "inspection-note": (
        "inspect",
        "inspection",
        "thickness",
        "vessel",
        "scan",
        "pdf",
        "png",
        "sop",
        "note",
        "draft",
        "word",
        "ut",
        "weld",
    ),
    "cite-or-abstain": ("cite", "sop", "source", "retrieve", "abstain", "ground"),
    "code-style-guide": (
        "code",
        "python",
        "calc",
        "sandbox",
        "function",
        "script",
        "debug",
    ),
}


def _agent_steps(body: str) -> list[dict[str, str]]:
    """Parse `## Agent steps` lines: `- id | label | detail`."""
    steps: list[dict[str, str]] = []
    in_block = False
    for line in (body or "").splitlines():
        if line.strip().lower().startswith("## agent steps"):
            in_block = True
            continue
        if in_block and line.startswith("## "):
            break
        if not in_block:
            continue
        m = _STEP_LINE.match(line.strip())
        if not m:
            continue
        steps.append(
            {
                "id": m.group(1).strip().lower(),
                "label": m.group(2).strip(),
                "detail": m.group(3).strip(),
            }
        )
    return steps


def recommend_plan(
    *,
    message: str = "",
    filename: str = "",
    task_type: str = "",
) -> dict[str, Any]:
    """Recommend a skill-authored step list from the operator's input.

    Not an LLM planner. Scores on-disk SKILL.md packs, then returns their
    Agent steps in match order (later skills only add new step ids).
    """
    blob = f"{message} {filename}".lower().strip()
    has_input = bool(blob)
    scored: list[tuple[int, dict[str, Any], list[dict[str, str]]]] = []
    if not has_input:
        return {
            "ok": True,
            "reason": "Waiting for a task or a file. Skills propose steps only after there is input.",
            "skills": [],
            "steps": [],
            "empty": True,
        }
    for meta in list_skills():
        full = load_skill(str(meta["id"]))
        if not full:
            continue
        score = 0
        fams = [str(f).lower() for f in (full.get("task_families") or [])]
        if task_type and task_type.lower() in fams:
            score += 4
        for hint in _HINTS.get(str(full["id"]), ()):
            if hint in blob:
                score += 2
        # Filename type hints
        lower_name = filename.lower()
        if full["id"] == "inspection-note" and lower_name.endswith(
            (".png", ".jpg", ".jpeg", ".pdf", ".md", ".txt")
        ):
            score += 3
        if full["id"] == "code-style-guide" and lower_name.endswith(".py"):
            score += 3
        steps = _agent_steps(str(full.get("body") or ""))
        if score > 0 and steps:
            scored.append((score, full, steps))
    scored.sort(key=lambda row: row[0], reverse=True)
    if (task_type or "").lower() == "coding":
        scored = [
            row
            for row in scored
            if row[1]["id"] != "inspection-note"
            or any(k in blob for k in ("scan", "pdf", "inspect", "sop", "vessel"))
        ]
    if (task_type or "").lower() == "inspection":
        scored = [
            row
            for row in scored
            if row[1]["id"] != "code-style-guide"
            or any(k in blob for k in ("python", "sandbox", "def ", ".py"))
        ]

    merged: list[dict[str, str]] = []
    seen: set[str] = set()
    picked: list[dict[str, Any]] = []
    for score, full, steps in scored[:3]:
        picked.append(
            {
                "id": full["id"],
                "description": full.get("description") or "",
                "score": score,
                "task_families": full.get("task_families") or [],
            }
        )
        for step in steps:
            if step["id"] in seen:
                continue
            seen.add(step["id"])
            merged.append({**step, "skill_id": str(full["id"])})

    reason = (
        "Matched "
        + ", ".join(p["id"] for p in picked)
        + " from this input."
        if picked
        else "No skill matched yet — type a task or attach a scan, note, or code file."
    )
    log_event(
        "skills_recommend",
        task_type=task_type or None,
        skill_ids=[p["id"] for p in picked],
        step_ids=[s["id"] for s in merged],
    )
    return {
        "ok": True,
        "reason": reason,
        "skills": picked,
        "steps": merged,
        "empty": not merged,
    }
