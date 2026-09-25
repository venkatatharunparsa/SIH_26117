"""Lightweight specialists — Workbench-side helpers Orch can call (not LLM side-doors)."""

from __future__ import annotations

from typing import Any

from . import pptx_draft, retrieve


def extract_specialist(text: str) -> dict[str, Any]:
    bullets = pptx_draft.extract_key_points(text)
    query = pptx_draft.build_retrieve_query(text, bullets)
    return {
        "name": "extract_specialist",
        "ok": True,
        "bullets": bullets,
        "query": query,
    }


def cite_specialist(query: str, shelves: list[str] | None, *, k: int = 5) -> dict[str, Any]:
    hit = retrieve.retrieve(query, shelves=shelves, k=k)
    cites = hit.get("cites") or []
    return {
        "name": "cite_specialist",
        "ok": True,
        "verdict": hit.get("verdict"),
        "cites": cites,
        "match_notes": [f"{c.get('path')}: {c.get('snippet')}" for c in cites[:5]],
    }


def run_specialist(name: str, **kwargs: Any) -> dict[str, Any]:
    if name == "extract":
        return extract_specialist(str(kwargs.get("text") or ""))
    if name == "cite":
        return cite_specialist(
            str(kwargs.get("query") or ""),
            kwargs.get("shelves"),
            k=int(kwargs.get("k") or 5),
        )
    return {"name": name, "ok": False, "error": "unknown_specialist"}
