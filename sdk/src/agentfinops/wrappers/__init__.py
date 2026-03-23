"""Provider-specific client wrappers."""

from __future__ import annotations

from typing import Any


def wrap(client: Any) -> Any:
    """Wrap an AI provider client to track costs with AgentFinOps.

    Supports: anthropic.Anthropic(), openai.OpenAI()
    """
    client_type = type(client).__module__

    if "anthropic" in client_type:
        from agentfinops.wrappers.anthropic import wrap_anthropic
        return wrap_anthropic(client)
    elif "openai" in client_type:
        from agentfinops.wrappers.openai import wrap_openai
        return wrap_openai(client)
    else:
        raise ValueError(
            f"Unsupported client type: {type(client).__name__}. "
            "AgentFinOps supports anthropic.Anthropic() and openai.OpenAI()."
        )
