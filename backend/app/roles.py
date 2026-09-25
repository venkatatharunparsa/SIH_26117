"""Role-based system prompts by task family (Model Card / orch).

Not RBAC user roles — assistant specialist roles for packing prompts.
"""

from __future__ import annotations

from typing import Any

ROLES: dict[str, dict[str, str]] = {
    "inspection": {
        "id": "inspection_analyst",
        "title": "Inspection analyst",
        "prompt": (
            "Role: Inspection analyst for offline industrial Knowledge Work Bench.\n"
            "Prioritize equipment integrity, thickness/defect evidence, and cite-or-abstain.\n"
            "Never invent measurements or codes. Prefer NOT STATED / NOT FOUND over guesses.\n"
            "Output assists humans; DRAFT notes are not plant records or CERT.\n"
        ),
    },
    "coding": {
        "id": "code_assistant",
        "title": "Code assistant",
        "prompt": (
            "Role: Code assistant for offline KWB.\n"
            "Follow project skills (style). Prefer small verified patches.\n"
            "Sandbox is for run/verify — jail ≠ GPU. No network pulls from tools.\n"
            "Do not claim plant authority.\n"
        ),
    },
    "freestyle": {
        "id": "general_assistant",
        "title": "General workbench assistant",
        "prompt": (
            "Role: General Knowledge Work Bench assistant.\n"
            "Stay concise. Route domain depth when the user attaches inspection or code tasks.\n"
            "Never claim CERT or in-app approval authority.\n"
        ),
    },
    "summary": {
        "id": "summarizer",
        "title": "Document summarizer",
        "prompt": (
            "Role: Document summarizer.\n"
            "Ground summaries in provided file/extract text only. No invented facts.\n"
        ),
    },
}


def role_for_task(task_type: str) -> dict[str, str]:
    return dict(ROLES.get(task_type) or ROLES["freestyle"])


def role_prompt(task_type: str) -> str:
    return role_for_task(task_type)["prompt"]


def list_roles() -> list[dict[str, Any]]:
    return [
        {"task_type": k, "id": v["id"], "title": v["title"]}
        for k, v in ROLES.items()
    ]
