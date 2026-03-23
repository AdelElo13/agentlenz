"""Global AgentLenz configuration."""

from __future__ import annotations

import os
from dataclasses import dataclass

_config: AgentLenzConfig | None = None


@dataclass
class AgentLenzConfig:
    api_key: str
    endpoint: str = "https://api.agentlenz.dev"
    enabled: bool = True
    flush_interval: float = 5.0
    batch_size: int = 100


def init(
    *,
    api_key: str | None = None,
    endpoint: str | None = None,
    enabled: bool = True,
) -> None:
    """Initialize AgentLenz with your API key."""
    global _config
    resolved_key = api_key or os.environ.get("AGENTLENZ_API_KEY", "")
    if not resolved_key and enabled:
        raise ValueError(
            "AgentLenz API key required. Pass api_key= or set AGENTLENZ_API_KEY env var."
        )
    _config = AgentLenzConfig(
        api_key=resolved_key,
        endpoint=endpoint or os.environ.get("AGENTLENZ_ENDPOINT", "https://api.agentlenz.dev"),
        enabled=enabled,
    )


def get_config() -> AgentLenzConfig:
    """Get the current config. Raises if init() not called."""
    if _config is None:
        raise RuntimeError("Call agentlenz.init() before using AgentLenz")
    return _config
