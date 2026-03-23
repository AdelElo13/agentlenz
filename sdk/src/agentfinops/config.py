"""Global AgentFinOps configuration."""

from __future__ import annotations

import os
from dataclasses import dataclass

_config: AgentFinOpsConfig | None = None


@dataclass
class AgentFinOpsConfig:
    api_key: str
    endpoint: str = "https://api.agentfinops.dev"
    enabled: bool = True
    flush_interval: float = 5.0
    batch_size: int = 100


def init(
    *,
    api_key: str | None = None,
    endpoint: str | None = None,
    enabled: bool = True,
) -> None:
    """Initialize AgentFinOps with your API key."""
    global _config
    resolved_key = api_key or os.environ.get("AGENTFINOPS_API_KEY", "")
    if not resolved_key and enabled:
        raise ValueError(
            "AgentFinOps API key required. Pass api_key= or set AGENTFINOPS_API_KEY env var."
        )
    _config = AgentFinOpsConfig(
        api_key=resolved_key,
        endpoint=endpoint or os.environ.get("AGENTFINOPS_ENDPOINT", "https://api.agentfinops.dev"),
        enabled=enabled,
    )


def get_config() -> AgentFinOpsConfig:
    """Get the current config. Raises if init() not called."""
    if _config is None:
        raise RuntimeError("Call agentfinops.init() before using AgentFinOps")
    return _config
