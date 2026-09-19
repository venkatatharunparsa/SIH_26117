"""Application configuration and path helpers."""

from __future__ import annotations

from pathlib import Path
from functools import lru_cache

import yaml
from pydantic_settings import BaseSettings

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"
DATA_DIR = ROOT / "data"
WORKSPACE_DIR = ROOT / "workspace"
ARTIFACTS_DIR = WORKSPACE_DIR / "artifacts"
UPLOADS_DIR = WORKSPACE_DIR / "uploads"
SANDBOX_DIR = WORKSPACE_DIR / "sandbox"
KB_DIR = DATA_DIR / "kb"
SOP_DIR = DATA_DIR / "sop"
AUDIT_DIR = WORKSPACE_DIR / "audit"
CHROMA_DIR = WORKSPACE_DIR / "chroma"


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

    class Config:
        env_prefix = "SOVEREIGN_"

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
    return settings


def ensure_dirs() -> None:
    for d in (
        WORKSPACE_DIR,
        ARTIFACTS_DIR,
        UPLOADS_DIR,
        SANDBOX_DIR,
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