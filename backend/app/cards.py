"""Model cards + task→card router (G1 / G8)."""

from __future__ import annotations

from typing import Any

from .audit import log_event
from .config import get_settings, load_yaml


def list_cards() -> list[dict[str, Any]]:
    settings = get_settings()
    raw = load_yaml(settings.models_config_path) if settings.models_config_path.exists() else {}
    return list(raw.get("cards") or [])


def enabled_cards() -> list[dict[str, Any]]:
    return [c for c in list_cards() if c.get("enabled", True)]


def get_card(card_id: str) -> dict[str, Any] | None:
    for c in list_cards():
        if c.get("id") == card_id:
            return c
    return None


def enabled_model_ids() -> set[str]:
    return {c["model_id"] for c in enabled_cards() if c.get("model_id")}


def model_ids_for_card(card_id: str | None) -> set[str] | None:
    if not card_id:
        return enabled_model_ids()
    card = get_card(card_id)
    if not card or not card.get("enabled", True):
        return set()
    mid = card.get("model_id")
    return {mid} if mid else set()


def local_chat_tags() -> set[str]:
    """Best-effort: tags already on local Ollama (no pull)."""
    settings = get_settings()
    try:
        import httpx

        base = settings.llm_base_url.rstrip("/")
        if base.endswith("/v1"):
            base = base[:-3].rstrip("/")
        with httpx.Client(timeout=3.0) as client:
            r = client.get(f"{base}/api/tags")
            if r.status_code != 200:
                return set()
            models = (r.json() or {}).get("models") or []
            return {str(m.get("name") or "") for m in models if m.get("name")}
    except Exception:
        return set()


def _is_chat_coding_tag(tag: str, *, primary: str) -> bool:
    """Exclude embed + vision tags from coding-card second-tag adoption."""
    t = (tag or "").lower()
    if not t or t == primary.lower():
        return False
    if "embed" in t or "nomic" in t:
        return False
    if "moondream" in t or "llava" in t or "vision" in t:
        return False
    return True


def adopt_second_chat_tag(preferred: list[str] | None = None) -> str | None:
    """If a 2nd chat tag is already local, return it for coding card (never pull)."""
    tags = local_chat_tags()
    primary = "llama3.2:3b"
    # Prefer explicit preferred list, else any non-embed/non-vision tag ≠ primary
    candidates = preferred or [
        "qwen2.5-coder:7b",
        "qwen2.5:0.5b",
        "qwen2.5:1.5b",
        "phi3:mini",
        "gemma2:2b",
        "llama3.2:1b",
        "smollm2:135m",
    ]
    for c in candidates:
        if c in tags and _is_chat_coding_tag(c, primary=primary):
            return c
        # tolerate :latest / bare name mismatch
        for t in tags:
            if t == c or t.startswith(f"{c}:") or c.startswith(t.split(":")[0]):
                if _is_chat_coding_tag(t, primary=primary):
                    return t
    for t in sorted(tags):
        if _is_chat_coding_tag(t, primary=primary):
            return t
    return None


def route_task(task_type: str) -> dict[str, Any]:
    """Map task_type → card + model_id. Fail-closed if card missing/disabled."""
    settings = get_settings()
    routes = {}
    if settings.routing_config_path.exists():
        routes = (load_yaml(settings.routing_config_path) or {}).get("routes") or {}
    card_id = routes.get(task_type)
    if not card_id:
        log_event("router_deny", task_type=task_type, reason="no_route")
        return {"ok": False, "error": "no_route", "task_type": task_type}
    card = get_card(card_id)
    if not card or not card.get("enabled", True):
        log_event("router_deny", task_type=task_type, card_id=card_id, reason="card_disabled")
        return {"ok": False, "error": "card_disabled", "card_id": card_id}
    model_id = card.get("model_id")
    g1_mode = "floor_single_tag_adopt"
    # Coding card: prefer configured model if on station; else adopt 2nd chat tag
    if task_type == "coding" and card_id == "code-assist":
        tags = local_chat_tags()
        configured = str(model_id or "")
        matched = None
        if configured:
            for t in tags:
                if t == configured or t.startswith(f"{configured}:"):
                    matched = t
                    break
        if matched and matched != "llama3.2:3b":
            model_id = matched
            g1_mode = "full_two_tag"
        else:
            second = adopt_second_chat_tag(
                preferred=[configured, "qwen2.5-coder:7b"] if configured else None
            )
            if second:
                model_id = second
                g1_mode = "full_two_tag"
    if not model_id:
        return {"ok": False, "error": "card_missing_model", "card_id": card_id}
    if str(model_id).startswith("REPLACE_WITH"):
        log_event("router_deny", task_type=task_type, card_id=card_id, reason="tag_not_adopted")
        return {
            "ok": False,
            "error": "tag_not_adopted",
            "message": "Set model_id to a local pre-staged Ollama tag — never pull from workbench",
            "card_id": card_id,
        }
    log_event(
        "router_select",
        task_type=task_type,
        card_id=card_id,
        model_id=model_id,
        g1_mode=g1_mode,
    )
    return {
        "ok": True,
        "task_type": task_type,
        "card_id": card_id,
        "model_id": model_id,
        "card": {**card, "model_id": model_id},
        "g1_mode": g1_mode,
    }
