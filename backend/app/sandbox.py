"""Thin code jail — inspired by OpenHands LocalWorkspace / DockerWorkspace.network.

WP-16: network none · 60s default · calc-in-jail · de-Docker · jail ≠ GPU inference.
We reimplement a minimal runner; we do not import OpenHands packages.

KWB inspiration (patterns only — never import openhands.*):
  - KWB/required/01_execute_command/command.py  — sanitized_env strip + prefixes
  - KWB/required/01_execute_command/redact.py   — SECRET_KEY_PATTERNS for env names
  - KWB/required/02_workspace_local/models.py   — CommandResult field shape
  - KWB/required/03_docker_network/             — --network hook (we force none)
  - KWB/from_software_agent_sdk/07_events_observation — audit observation fields
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import time
import uuid
from dataclasses import asdict, dataclass
from typing import Any

from .audit import log_event
from .config import SANDBOX_DIR, ensure_dirs, get_settings

# Explicit names from OH command.py + common local/cloud keys we must not leak into jail.
_STRIP_ENV = frozenset(
    {
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
        "OLLAMA_API_KEY",
        "SESSION_API_KEY",
        "OH_SECRET_KEY",
        "AWS_SECRET_ACCESS_KEY",
        "AWS_ACCESS_KEY_ID",
        "SOVEREIGN_LLM_API_KEY",
        "GITHUB_TOKEN",
        "GH_TOKEN",
        "HF_TOKEN",
        "HUGGING_FACE_HUB_TOKEN",
    }
)

# OH V1 indexed session keys: OH_SESSION_API_KEYS_0 … N
_STRIP_ENV_PREFIXES: tuple[str, ...] = ("OH_SESSION_API_KEYS_",)

# From KWB/required/01_execute_command/redact.py SECRET_KEY_PATTERNS —
# substring match (case-insensitive) against env var *names* only.
_SECRET_ENV_NAME_PATTERNS = frozenset(
    {
        "AUTHORIZATION",
        "COOKIE",
        "CREDENTIAL",
        "PASSWORD",
        "SECRET",
        "TOKEN",
        # "KEY" alone is too broad (KEYBOARD, MONKEYPATH); require *_KEY / KEY_* shape via helper.
    }
)


def _is_secret_env_name(key: str) -> bool:
    """True if env var name looks secret-bearing (OH redact-inspired)."""
    ku = key.upper()
    if ku in _STRIP_ENV:
        return True
    if any(ku.startswith(p) for p in _STRIP_ENV_PREFIXES):
        return True
    if any(p in ku for p in _SECRET_ENV_NAME_PATTERNS):
        return True
    # API_KEY, X_ACCESS_KEY, SESSION_KEY — avoid bare "KEY" false positives.
    if ku.endswith("_KEY") or ku.startswith("KEY_") or "_API_KEY" in ku:
        return True
    if "APIKEY" in ku.replace("_", ""):
        return True
    return False


@dataclass
class SandboxResult:
    """CommandResult-like observation (KWB/required/02 + 07).

    Fields mirror OH CommandResult (command, exit_code, stdout, stderr,
    timeout_occurred) plus KWB/H9 extras: ok, mode, duration_ms, network, work_dir.
    """

    ok: bool
    mode: str  # "process" | "docker"
    exit_code: int
    stdout: str
    stderr: str
    duration_ms: int
    timeout_occurred: bool
    network: str
    command: str
    work_dir: str

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)

    def observation_fields(self) -> dict[str, Any]:
        """Stable subset for audit / H9 (07_events_observation shape)."""
        return {
            "ok": self.ok,
            "exit_code": self.exit_code,
            "duration_ms": self.duration_ms,
            "timeout_occurred": self.timeout_occurred,
            "mode": self.mode,
            "network": self.network,
            "stderr": self.stderr,  # already truncated via _truncate
            "stdout_len": len(self.stdout),
        }


def _sanitized_env() -> dict[str, str]:
    env = {k: v for k, v in os.environ.items() if not _is_secret_env_name(k)}
    # Prefer UTF-8 on Windows consoles for jury-readable logs.
    env.setdefault("PYTHONIOENCODING", "utf-8")
    env.setdefault("PYTHONUTF8", "1")
    return env


def _truncate(text: str, limit: int = 8000) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n… truncated ({len(text)} chars)"


def _docker_available() -> bool:
    if shutil.which("docker") is None:
        return False
    try:
        r = subprocess.run(
            ["docker", "version", "--format", "{{.Server.Version}}"],
            capture_output=True,
            text=True,
            timeout=5,
            env=_sanitized_env(),
        )
        return r.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def run_python(
    source: str,
    *,
    timeout_s: float | None = None,
    prefer_docker: bool = False,
    label: str = "python",
) -> SandboxResult:
    """Run Python source in jail. Default = process jail (de-Docker must-work)."""
    settings = get_settings()
    timeout = float(timeout_s if timeout_s is not None else settings.sandbox_timeout_s)
    ensure_dirs()

    if prefer_docker and _docker_available():
        return _run_docker_python(source, timeout=timeout, label=label)

    return _run_process_python(source, timeout=timeout, label=label)


def run_calc(expression: str, *, timeout_s: float | None = None) -> SandboxResult:
    """WP-16 D5 — numeric verify must run inside the jail (not LLM arithmetic)."""
    # Expression is evaluated only via ast in the child — no eval of raw host string here.
    src = (
        "import ast, operator as op\n"
        "_ops = {\n"
        "  ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv,\n"
        "  ast.Pow: op.pow, ast.USub: op.neg, ast.Mod: op.mod,\n"
        "}\n"
        "def _eval(node):\n"
        "  if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):\n"
        "    return node.value\n"
        "  if isinstance(node, ast.UnaryOp) and type(node.op) in _ops:\n"
        "    return _ops[type(node.op)](_eval(node.operand))\n"
        "  if isinstance(node, ast.BinOp) and type(node.op) in _ops:\n"
        "    return _ops[type(node.op)](_eval(node.left), _eval(node.right))\n"
        "  raise ValueError('disallowed')\n"
        f"expr = {expression!r}\n"
        "tree = ast.parse(expr, mode='eval')\n"
        "print(_eval(tree.body))\n"
    )
    return run_python(src, timeout_s=timeout_s, label="calc")


def _audit_sandbox(label: str, result: SandboxResult) -> None:
    """Emit observation-like audit event (H9 evidence)."""
    log_event(
        "sandbox_run",
        label=label,
        **result.observation_fields(),
    )


def _run_process_python(source: str, *, timeout: float, label: str) -> SandboxResult:
    """Non-Docker process jail — cwd under workspace/sandbox; best-effort no-net guard."""
    run_id = uuid.uuid4().hex[:12]
    work = SANDBOX_DIR / run_id
    work.mkdir(parents=True, exist_ok=True)
    script = work / "job.py"
    # Red-team E1: block outbound sockets in host-process jail (not a full container).
    guard = (
        "import socket as _socket\n"
        "_orig_socket = _socket.socket\n"
        "class _SandboxSocket(_orig_socket):\n"
        "    def connect(self, address):\n"
        "        raise OSError('sandbox_network_denied')\n"
        "    def connect_ex(self, address):\n"
        "        raise OSError('sandbox_network_denied')\n"
        "_socket.socket = _SandboxSocket\n"
        "try:\n"
        "    import urllib.request as _ur\n"
        "    def _blocked_urlopen(*a, **k):\n"
        "        raise OSError('sandbox_network_denied')\n"
        "    _ur.urlopen = _blocked_urlopen\n"
        "except Exception:\n"
        "    pass\n"
        "\n"
    )
    script.write_text(guard + source, encoding="utf-8")

    cmd = [sys.executable, str(script)]
    t0 = time.perf_counter()
    timeout_occurred = False
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(work),
            capture_output=True,
            text=True,
            timeout=timeout,
            env=_sanitized_env(),
        )
        exit_code = proc.returncode
        stdout, stderr = proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as e:
        timeout_occurred = True
        exit_code = -1
        stdout = (e.stdout or "") if isinstance(e.stdout, str) else ""
        stderr = (e.stderr or "") if isinstance(e.stderr, str) else f"timeout after {timeout}s"

    duration_ms = int((time.perf_counter() - t0) * 1000)
    result = SandboxResult(
        ok=(exit_code == 0 and not timeout_occurred),
        mode="process",
        exit_code=exit_code,
        stdout=_truncate(stdout or ""),
        stderr=_truncate(stderr or ""),
        duration_ms=duration_ms,
        timeout_occurred=timeout_occurred,
        network="host-process + socket/urlopen deny guard (not docker network=none)",
        command=" ".join(cmd),
        work_dir=str(work),
    )
    _audit_sandbox(label, result)
    return result


def _run_docker_python(source: str, *, timeout: float, label: str) -> SandboxResult:
    """Optional Docker path — OpenHands-style `--network` (we force none)."""
    settings = get_settings()
    network = settings.sandbox_network or "none"
    run_id = uuid.uuid4().hex[:12]
    host_dir = SANDBOX_DIR / run_id
    host_dir.mkdir(parents=True, exist_ok=True)
    (host_dir / "job.py").write_text(source, encoding="utf-8")

    # Mount only this job dir; network=none; no GPU flags (jail ≠ inference).
    cmd = [
        "docker",
        "run",
        "--rm",
        "--network",
        network,
        "--memory",
        "256m",
        "--cpus",
        "1",
        "-v",
        f"{host_dir.resolve()}:/job:ro",
        "-w",
        "/job",
        settings.sandbox_image,
        "python",
        "job.py",
    ]
    t0 = time.perf_counter()
    timeout_occurred = False
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout + 15,  # pull/start slack
            env=_sanitized_env(),
        )
        exit_code = proc.returncode
        stdout, stderr = proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as e:
        timeout_occurred = True
        exit_code = -1
        stdout = (e.stdout or "") if isinstance(e.stdout, str) else ""
        stderr = (e.stderr or "") if isinstance(e.stderr, str) else f"timeout after {timeout}s"

    duration_ms = int((time.perf_counter() - t0) * 1000)
    result = SandboxResult(
        ok=(exit_code == 0 and not timeout_occurred),
        mode="docker",
        exit_code=exit_code,
        stdout=_truncate(stdout or ""),
        stderr=_truncate(stderr or ""),
        duration_ms=duration_ms,
        timeout_occurred=timeout_occurred,
        network=network,
        command=" ".join(cmd),
        work_dir=str(host_dir),
    )
    _audit_sandbox(label, result)
    return result
