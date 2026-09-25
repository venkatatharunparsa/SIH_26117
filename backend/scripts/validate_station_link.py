"""Preflight: Model Workstation link + Model Card tags for two-laptop demo.

Usage (API not required):
  python backend/scripts/validate_station_link.py

Checks:
  - llm_base_url host is localhost OR allowlisted private peer
  - GET {llm}/api/tags (Ollama) or /v1/models
  - Every enabled card model_id appears in station tags
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen, Request

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "backend"))

from app.config import get_settings, load_yaml  # noqa: E402
from app.gateway import assert_local_base_url, normalize_base_url  # noqa: E402
from app import cards as cards_mod  # noqa: E402


def fetch_tags(base: str) -> set[str]:
    base = normalize_base_url(base)
    names: set[str] = set()
    # Ollama native
    try:
        with urlopen(Request(f"{base}/api/tags"), timeout=8) as r:
            data = json.loads(r.read().decode())
            for m in data.get("models") or []:
                n = m.get("name") or m.get("model")
                if n:
                    names.add(str(n))
    except Exception:
        pass
    # OpenAI-shape
    try:
        with urlopen(Request(f"{base}/v1/models"), timeout=8) as r:
            data = json.loads(r.read().decode())
            for m in data.get("data") or []:
                n = m.get("id")
                if n:
                    names.add(str(n))
    except Exception:
        pass
    return names


def main() -> int:
    get_settings.cache_clear()
    s = get_settings()
    url = s.llm_base_url
    # Prefer live API inference target when workbench is already linked (hotspot)
    try:
        with urlopen(Request("http://127.0.0.1:8080/inference/status"), timeout=3) as r:
            live = json.loads(r.read().decode())
            if live.get("ok") and live.get("llm_base_url"):
                url = str(live["llm_base_url"])
                if live.get("inference_allow_hosts") and not s.inference_allow_hosts:
                    # mirror allowlist for gateway check when API has LAN peer
                    os.environ.setdefault(
                        "SOVEREIGN_INFERENCE_ALLOW_HOSTS",
                        ",".join(live["inference_allow_hosts"]),
                    )
                    get_settings.cache_clear()
                    s = get_settings()
                print(f"(from live API) mode={live.get('mode')} label={live.get('label')}")
    except Exception:
        pass
    print(f"llm_base_url = {url}")
    print(f"inference_allow_hosts = {s.inference_allow_hosts}")
    print(f"station_token set = {bool(s.station_token)}")

    deny = assert_local_base_url(url)
    if deny:
        print(f"FAIL gateway policy: {deny.reason}")
        print("  Fix: SSH tunnel to 127.0.0.1 OR add RFC1918 peer to inference_allow_hosts")
        return 1
    print("PASS gateway host policy")

    host = (urlparse(url).hostname or "").lower()
    tags = fetch_tags(url)
    if not tags:
        print(f"FAIL cannot list models at {url} (is Laptop-1 Ollama up? tunnel/LAN?)")
        return 1
    print(f"PASS station reachable · {len(tags)} tag(s)")

    missing = []
    for c in cards_mod.enabled_cards():
        mid = c.get("model_id")
        if not mid:
            continue
        if mid not in tags and not any(t.startswith(mid) or mid.startswith(t.split(":")[0]) for t in tags):
            # exact match preferred
            if mid not in tags:
                missing.append((c.get("id"), mid))
    if missing:
        print("FAIL Model Card tags not on station:")
        for cid, mid in missing:
            print(f"  card={cid} model_id={mid}")
        print(f"  station tags sample: {sorted(list(tags))[:12]}")
        return 1
    print("PASS all enabled card model_ids present on station")
    print("OK — Laptop-2 may start workbench against this station")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
