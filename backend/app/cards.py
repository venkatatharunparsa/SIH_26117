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
    log_event("router_select", task_type=task_type, card_id=card_id, model_id=model_id)
    return {
        "ok": True,
        "task_type": task_type,
        "card_id": card_id,
        "model_id": model_id,
        "card": card,
    }
