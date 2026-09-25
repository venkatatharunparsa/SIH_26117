"""Laptop-A live status + request log — run ON THE MODEL SERVER.

  python laptop_a_ollama_watch.py

Shows: IP hint, tags, currently loaded model, and polls /api/ps so you see
when Laptop-B causes a model to load.
"""
from __future__ import annotations

import json
import socket
import time
import urllib.request
from datetime import datetime, timezone

BASE = "http://127.0.0.1:11434"


def get(path: str) -> dict | list | None:
    try:
        with urllib.request.urlopen(f"{BASE}{path}", timeout=3) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        print(f"[{_ts()}] ERR {path}: {e}")
        return None


def _ts() -> str:
    return datetime.now(timezone.utc).strftime("%H:%M:%S")


def local_ips() -> list[str]:
    ips: list[str] = []
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
            ip = info[4][0]
            if not ip.startswith("127."):
                ips.append(ip)
    except Exception:
        pass
    return sorted(set(ips))


def main() -> None:
    print("=== Laptop-A Ollama watch (leave this window open) ===")
    print("Share hotspot IPv4 with Laptop-B for hotspot_link_workbench.ps1")
    print("Candidate IPv4s:", ", ".join(local_ips()) or "(run ipconfig)")
    print()
    tags = get("/api/tags") or {}
    names = [m.get("name") for m in (tags.get("models") or []) if m.get("name")]
    print("Tags:", ", ".join(names) or "(none)")
    print("Watching /api/ps — when B calls Gateway, a model should appear here.")
    print("-" * 60)
    last = None
    while True:
        ps = get("/api/ps") or {}
        models = ps.get("models") or []
        sig = tuple(sorted((m.get("name") or m.get("model") or "?") for m in models))
        if sig != last:
            last = sig
            if not sig:
                print(f"[{_ts()}] loaded: (idle — no model in VRAM)")
            else:
                print(f"[{_ts()}] loaded: {', '.join(sig)}")
        time.sleep(2)


if __name__ == "__main__":
    main()
