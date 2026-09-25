"""Restart FastAPI on :8080 so secrets.py changes load."""
from __future__ import annotations

import os
import signal
import subprocess
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def listen_pid() -> int | None:
    try:
        out = subprocess.check_output(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "(Get-NetTCPConnection -LocalPort 8080 -State Listen "
                "-ErrorAction SilentlyContinue | Select-Object -First 1 "
                "-ExpandProperty OwningProcess)",
            ],
            text=True,
        ).strip()
    except subprocess.CalledProcessError:
        return None
    return int(out) if out.isdigit() else None


def main() -> None:
    pid = listen_pid()
    if pid:
        print(f"stopping pid {pid}")
        try:
            os.kill(pid, signal.SIGTERM)
        except OSError as e:
            print("kill", e)
        time.sleep(2)

    print("starting uvicorn")
    subprocess.Popen(
        ["python", "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8080"],
        cwd=ROOT,
        creationflags=getattr(subprocess, "CREATE_NEW_CONSOLE", 0),
    )
    for _ in range(30):
        time.sleep(0.5)
        try:
            urllib.request.urlopen("http://127.0.0.1:8080/health", timeout=1)
            print("healthy")
            break
        except Exception:
            pass
    else:
        raise SystemExit("API did not come up")

    body = b'{"text":"AKIAIOSFODNN7EXAMPLE secret_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"}'
    req = urllib.request.Request(
        "http://127.0.0.1:8080/task/export-check",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as r:
            print("g9 unexpected", r.status, r.read().decode())
    except urllib.error.HTTPError as e:
        print("g9", e.code, e.read().decode())


if __name__ == "__main__":
    main()
