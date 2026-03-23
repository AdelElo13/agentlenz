"""@agentlens.trace decorator for instrumenting custom agent functions."""

from __future__ import annotations

import functools
from typing import Any, Callable

from agentlens.client import get_client
from agentlens.spans import Span, SpanKind


def trace(
    name: str | None = None,
    kind: SpanKind = SpanKind.AGENT_STEP,
) -> Callable:
    """Decorator that records a span for any function call."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            span_name = name or func.__name__
            span = Span(
                name=span_name,
                kind=kind,
                provider="custom",
                model="n/a",
            )
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                span.error = str(e)
                raise
            finally:
                span.end()
                get_client().record(span)

        return wrapper

    return decorator
