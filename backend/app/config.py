"""Application configuration and path helpers."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Annotated

import yaml
from pydantic import field_validator
from pydantic_settings import BaseSettings, NoDecode

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"
DATA_DIR = ROOT / "data"
WORKSPACE_DIR = ROOT / "workspace"
ARTIFACTS_DIR = WORKSPACE_DIR / "artifacts"
UPLOADS_DIR = WORKSPACE_DIR / "uploads"
SANDBOX_DIR = WORKSPACE_DIR / "sandbox"
TEMPLATES_DIR = WORKSPACE_DIR / "templates"
KNOWLEDGE_DIR = WORKSPACE_DIR / "knowledge"
KB_DIR = DATA_DIR / "kb"
SOP_DIR = DATA_DIR / "sop"
AUDIT_DIR = WORKSPACE_DIR / "audit"
CHROMA_DIR = WORKSPACE_DIR / "chroma"


def _parse_host_list(v: object) -> list[str]:
    """Accept comma-separated hosts or a JSON list (pydantic-settings default)."""
    if v is None or v == "":
        return []
    if isinstance(v, list):
        return [str(h).strip() for h in v if str(h).strip()]
    if isinstance(v, str):
        s = v.strip()
        if s.startswith("["):
            parsed = json.loads(s)
            if not isinstance(parsed, list):
                raise ValueError("inference_allow_hosts JSON must be a list")
            return [str(h).strip() for h in parsed if str(h).strip()]
        return [h.strip() for h in s.split(",") if h.strip()]
    raise TypeError(f"inference_allow_hosts: unsupported type {type(v)!r}")


class Settings(BaseSettings):
    models_config_path: Path = CONFIG_DIR / "models.yaml"
    routing_config_path: Path = CONFIG_DIR / "routing_rules.yaml"
    # Hardware deferred — any OpenAI-shape local server; Ollama default is a convenience.
    llm_base_url: str = "http://127.0.0.1:11434"
    bind_host: str = "127.0.0.1"
    bind_port: int = 8080
    sandbox_image: str = "python:3.12-slim"
    sandbox_network: str = "none"
    sandbox_timeout_s: float = 60.0
    max_agent_steps: int = 8
    egress_poll_seconds: float = 2.0
    # Two-laptop LAN mode: plain IP / comma list (NoDecode) or JSON list
    inference_allow_hosts: Annotated[list[str], NoDecode] = []
    # Optional station credential from Model Workstation (Laptop-1) — not a cloud API key
    station_token: str = ""

    class Config:
        env_prefix = "SOVEREIGN_"

    @field_validator("inference_allow_hosts", mode="before")
    @classmethod
    def _hosts_from_env(cls, v: object) -> list[str]:
        return _parse_host_list(v)

    @property
    def ollama_base_url(self) -> str:
        """Alias kept for older call sites."""
        return self.llm_base_url


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    raw = {}
    if settings.models_config_path.exists():
        with open(settings.models_config_path, encoding="utf-8") as f:
            raw = yaml.safe_load(f) or {}
    if "llm_base_url" in raw:
        settings.llm_base_url = raw["llm_base_url"]
    elif "ollama_base_url" in raw:
        settings.llm_base_url = raw["ollama_base_url"]
    if "bind_host" in raw:
        settings.bind_host = raw["bind_host"]
    if "bind_port" in raw:
        settings.bind_port = int(raw["bind_port"])
    if "sandbox_timeout_s" in raw:
        settings.sandbox_timeout_s = float(raw["sandbox_timeout_s"])
    if "inference_allow_hosts" in raw and isinstance(raw["inference_allow_hosts"], list):
        settings.inference_allow_hosts = [str(h).strip() for h in raw["inference_allow_hosts"] if str(h).strip()]
    if "station_token" in raw and raw["station_token"]:
        settings.station_token = str(raw["station_token"])
    # Env override for two-laptop without editing yaml mid-demo
    import os

    env_hosts = os.environ.get("SOVEREIGN_INFERENCE_ALLOW_HOSTS", "").strip()
    if env_hosts:
        settings.inference_allow_hosts = [h.strip() for h in env_hosts.split(",") if h.strip()]
    env_url = os.environ.get("SOVEREIGN_LLM_BASE_URL", "").strip()
    if env_url:
        settings.llm_base_url = env_url
    env_tok = os.environ.get("SOVEREIGN_STATION_TOKEN", "").strip()
    if env_tok:
        settings.station_token = env_tok
    return settings


def ensure_dirs() -> None:
    for d in (
        WORKSPACE_DIR,
        ARTIFACTS_DIR,
        UPLOADS_DIR,
        SANDBOX_DIR,
        TEMPLATES_DIR,
        KNOWLEDGE_DIR,
        KB_DIR,
        SOP_DIR,
        AUDIT_DIR,
        CHROMA_DIR,
        DATA_DIR / "fixtures",
    ):
        d.mkdir(parents=True, exist_ok=True)


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}