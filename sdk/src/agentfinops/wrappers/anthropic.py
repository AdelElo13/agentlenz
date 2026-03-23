"""Wrapper for the Anthropic Python SDK."""

from __future__ import annotations

from typing import Any

from agentfinops.client import get_client
from agentfinops.spans import Span, SpanKind


class WrappedMessages:
    """Wraps client.messages to intercept create() calls."""

    def __init__(self, messages: Any) -> None:
        self._messages = messages

    def create(self, **kwargs: Any) -> Any:
        model = kwargs.get("model", "unknown")
        span = Span(
            name="messages.create",
            kind=SpanKind.LLM_CALL,
            provider="anthropic",
            model=model,
        )
        try:
            response = self._messages.create(**kwargs)
            span.input_tokens = response.usage.input_tokens
            span.output_tokens = response.usage.output_tokens
            span.model = response.model
            return response
        except Exception as e:
            span.error = str(e)
            raise
        finally:
            span.end()
            get_client().record(span)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._messages, name)


class WrappedAnthropicClient:
    """Wraps an anthropic.Anthropic() client."""

    def __init__(self, client: Any) -> None:
        self._client = client
        self.messages = WrappedMessages(client.messages)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._client, name)


def wrap_anthropic(client: Any) -> WrappedAnthropicClient:
    return WrappedAnthropicClient(client)
