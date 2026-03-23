"""Wrapper for the OpenAI Python SDK."""

from __future__ import annotations

from typing import Any

from agentlens.client import get_client
from agentlens.spans import Span, SpanKind


class WrappedCompletions:
    def __init__(self, completions: Any) -> None:
        self._completions = completions

    def create(self, **kwargs: Any) -> Any:
        model = kwargs.get("model", "unknown")
        span = Span(
            name="chat.completions.create",
            kind=SpanKind.LLM_CALL,
            provider="openai",
            model=model,
        )
        try:
            response = self._completions.create(**kwargs)
            span.input_tokens = response.usage.prompt_tokens
            span.output_tokens = response.usage.completion_tokens
            span.model = response.model
            return response
        except Exception as e:
            span.error = str(e)
            raise
        finally:
            span.end()
            get_client().record(span)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._completions, name)


class WrappedChat:
    def __init__(self, chat: Any) -> None:
        self._chat = chat
        self.completions = WrappedCompletions(chat.completions)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._chat, name)


class WrappedOpenAIClient:
    def __init__(self, client: Any) -> None:
        self._client = client
        self.chat = WrappedChat(client.chat)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._client, name)


def wrap_openai(client: Any) -> WrappedOpenAIClient:
    return WrappedOpenAIClient(client)
