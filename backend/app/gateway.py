"""Local OpenAI-shape /v1 client — hardware-agnostic.

Ollama (demo) = inference only. This module NEVER calls pull/registry APIs.
Adopt model tags that already exist in the local runtime store.

Continue.dev triad (KWB/from_continue_web — comments only; equivalent already):
  provider ≈ OpenAI-shape HTTP · model ≈ Model Card model_id · apiBase ≈ llm_base_url
We stay on /v1/chat/completions + /v1/models (LCD). No LiteLLM. No public WAN.

KWB inspiration:
  - KWB/required/05_llm_base_url — model + base_url fields
  - KWB/from_continue_web — apiBase + model triad (study)
G1/G8: local host allowlist + optional Model Card allowlist (allowed_model_ids).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from urllib.parse import urlparse

import httpx

from .audit import log_event
from .config import get_settings

_PRIVATE_HOSTS = frozenset({"127.0.0.1", "localhost", "::1"})


@dataclass
class GatewayDeny:
    reason: str


def _is_rfc1918(host: str) -> bool:
    """Allow only private IPv4 literals for LAN peer mode (no public WAN)."""
    parts = host.split(".")
    if len(parts) != 4:
        return False
    try:
        nums = [int(p) for p in parts]
    except ValueError:
        return False
    if any(n < 0 or n > 255 for n in nums):
        return False
    a, b = nums[0], nums[1]
    if a == 10:
        return True
    if a == 172 and 16 <= b <= 31:
        return True
    if a == 192 and b == 168:
        return True
    return False


def normalize_base_url(base_url: str) -> str:
    """Strip trailing slash and a trailing /v1 so we always append /v1/chat/completions once."""
    u = (base_url or "").rstrip("/")
    if u.endswith("/v1"):
        u = u[:-3].rstrip("/")
    return u


def assert_local_base_url(base_url: str) -> GatewayDeny | None:
    """G8 / WP-09 — refuse public WAN; allow localhost + explicit private peers.

    Two-laptop LAN: put Model Workstation IP in config `inference_allow_hosts`
    (RFC1918 only). Prefer SSH tunnel to keep llm_base_url on 127.0.0.1.
    """
    try:
        parsed = urlparse(base_url)
    except Exception:
        return GatewayDeny("invalid_base_url")
    if parsed.scheme not in ("http", "https"):
        return GatewayDeny("scheme_not_http")
    host = (parsed.hostname or "").lower()
    if host in _PRIVATE_HOSTS:
        return None
    settings = get_settings()
    allowed = {h.lower() for h in (settings.inference_allow_hosts or [])}
    if host in allowed and _is_rfc1918(host):
        return None
    if host in allowed and not _is_rfc1918(host):
        return GatewayDeny(f"peer_not_private:{host}")
    return GatewayDeny(f"non_local_host:{host or '?'}")


def inference_target() -> dict[str, Any]:
    """Where Gateway will dial for /v1 — local vs LAN peer (Laptop-A)."""
    settings = get_settings()
    base = normalize_base_url(settings.llm_base_url)
    try:
        host = (urlparse(base).hostname or "").lower()
    except Exception:
        host = ""
    is_loopback = host in _PRIVATE_HOSTS
    allow = list(settings.inference_allow_hosts or [])
    mode = "local_workbench_ollama" if is_loopback else "lan_peer_laptop_a"
    label = (
        "LOCAL (this Laptop-B Ollama)"
        if is_loopback
        else f"LAPTOP-A peer ({host})"
    )
    deny = assert_local_base_url(base)
    return {
        "llm_base_url": base,
        "host": host or "?",
        "mode": mode,
        "label": label,
        "is_local": is_loopback,
        "inference_allow_hosts": allow,
        "gateway_host_ok": deny is None,
        "gateway_deny_reason": deny.reason if deny else None,
    }


def chat_completions(
    *,
    messages: list[dict[str, Any]],
    model: str,
    base_url: str | None = None,
    temperature: float = 0.1,
    max_tokens: int = 512,
    timeout_s: float = 120.0,
    allow_base_override: bool = False,
    allowed_model_ids: set[str] | None = None,
    grant_id: str | None = None,
    phase: str | None = None,
) -> dict[str, Any]:
    """POST {base}/v1/chat/completions — OpenAI-compatible local servers.

    Card allowlist: when allowed_model_ids is set, model must be on the grant card.
    """
    settings = get_settings()
    if allow_base_override and base_url:
        url_base = normalize_base_url(base_url)
    else:
        url_base = normalize_base_url(settings.llm_base_url)

    deny = assert_local_base_url(url_base)
    if deny:
        log_event(
            "gateway_deny",
            reason=deny.reason,
            base_url=url_base,
            model=model,
            grant_id=grant_id,
        )
        return {"ok": False, "error": "gateway_deny", "reason": deny.reason}

    if allowed_model_ids is not None and model not in allowed_model_ids:
        log_event(
            "gateway_deny",
            reason="model_not_on_card",
            model=model,
            grant_id=grant_id,
        )
        return {
            "ok": False,
            "error": "gateway_deny",
            "reason": "model_not_on_card",
            "model": model,
        }

    host = urlparse(url_base).hostname or ""
    label = (
        "LOCAL (Laptop-B)"
        if host.lower() in _PRIVATE_HOSTS
        else f"LAPTOP-A ({host})"
    )
    log_event(
        "gateway_chat_start",
        grant_id=grant_id,
        model=model,
        base_url=url_base,
        inference_host=host,
        inference_label=label,
        phase=phase or "gateway_call",
    )
    log_event(
        "orch_phase",
        grant_id=grant_id,
        phase=phase or "calling_model",
        label=f"Calling {model} @ {label}",
        model=model,
    )

    endpoint = f"{url_base}/v1/chat/completions"
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False,
    }
    try:
        with httpx.Client(timeout=timeout_s) as client:
            resp = client.post(endpoint, json=payload)
        body: Any
        try:
            body = resp.json()
        except Exception:
            body = {"raw": resp.text[:2000]}
        ok = resp.is_success
        log_event(
            "gateway_chat",
            ok=ok,
            status=resp.status_code,
            model=model,
            base_url=url_base,
            inference_host=host,
            inference_label=label,
            grant_id=grant_id,
        )
        return {
            "ok": ok,
            "status": resp.status_code,
            "base_url": url_base,
            "model": model,
            "inference_host": host,
            "inference_label": label,
            "body": body,
        }
    except httpx.HTTPError as e:
        log_event(
            "gateway_error",
            error=type(e).__name__,
            model=model,
            base_url=url_base,
            grant_id=grant_id,
        )
        return {
            "ok": False,
            "error": "http_error",
            "detail": str(e),
            "base_url": url_base,
            "model": model,
        }


def runtime_status() -> dict[str, Any]:
    """Probe configured runtime without locking which binary serves it."""
    settings = get_settings()
    base = normalize_base_url(settings.llm_base_url)
    deny = assert_local_base_url(base)
    if deny:
        return {"reachable": False, "denied": deny.reason, "base_url": base}

    tags_ok = False
    models_ok = False
    detail: dict[str, Any] = {}
    try:
        with httpx.Client(timeout=3.0) as client:
            r1 = client.get(f"{base}/api/tags")
            tags_ok = r1.status_code == 200
            detail["ollama_tags"] = r1.status_code
            r2 = client.get(f"{base}/v1/models")
            models_ok = r2.status_code == 200
            detail["v1_models"] = r2.status_code
    except httpx.HTTPError as e:
        detail["error"] = f"{type(e).__name__}: {e}"

    return {
        "reachable": tags_ok or models_ok,
        "base_url": base,
        "probes": detail,
    }
