"""Global AgentLens configuration."""

from __future__ import annotations

import os
from dataclasses import dataclass

_config: AgentLensConfig | None = None


@dataclass
class AgentLensConfig:
    api_key: str
    endpoint: str = "https://api.agentlens.dev"
    enabled: bool = True
    flush_interval: float = 5.0
    batch_size: int = 100


def init(
    *,
    api_key: str | None = None,
    endpoint: str | None = None,
    enabled: bool = True,
) -> None:
    """Initialize AgentLens with your API key."""
    global _config
    resolved_key = api_key or os.environ.get("AGENTLENS_API_KEY", "")
    if not resolved_key and enabled:
        raise ValueError(
            "AgentLens API key required. Pass api_key= or set AGENTLENS_API_KEY env var."
        )
    _config = AgentLensConfig(
        api_key=resolved_key,
        endpoint=endpoint or os.environ.get("AGENTLENS_ENDPOINT", "https://api.agentlens.dev"),
        enabled=enabled,
    )


def get_config() -> AgentLensConfig:
    """Get the current config. Raises if init() not called."""
    if _config is None:
        raise RuntimeError("Call agentlens.init() before using AgentLens")
    return _config
