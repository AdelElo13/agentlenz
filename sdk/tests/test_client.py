import pytest
from unittest.mock import AsyncMock, patch
from agentfinops.config import init
from agentfinops.client import EventClient, get_client
from agentfinops.spans import Span, SpanKind


@pytest.fixture(autouse=True)
def setup_config():
    init(api_key="af_test123", endpoint="http://localhost:8000")


def test_get_client_returns_singleton():
    c1 = get_client()
    c2 = get_client()
    assert c1 is c2


def test_client_queues_span():
    client = EventClient()
    span = Span(
        name="test", kind=SpanKind.LLM_CALL,
        provider="anthropic", model="claude-sonnet-4-20250514",
        input_tokens=10, output_tokens=5,
    )
    span.end()
    client.record(span)
    assert len(client._queue) == 1


def test_client_disabled_skips_record():
    init(api_key="af_test123", enabled=False)
    client = EventClient()
    span = Span(
        name="test", kind=SpanKind.LLM_CALL,
        provider="anthropic", model="claude-sonnet-4-20250514",
    )
    client.record(span)
    assert len(client._queue) == 0
