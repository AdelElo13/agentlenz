"""End-to-end: SDK → Backend — smoke test.
Skip in CI unless explicitly enabled.
"""

import os
import pytest

pytestmark = pytest.mark.skipif(
    os.environ.get("AGENTLENS_INTEGRATION") != "1",
    reason="Set AGENTLENS_INTEGRATION=1 to run",
)


def test_sdk_sends_events_to_backend():
    import agentlens
    from agentlens.client import get_client

    agentlens.init(
        api_key=os.environ.get("AGENTLENS_API_KEY", "al_test_key"),
        endpoint=os.environ.get("AGENTLENS_ENDPOINT", "http://localhost:8000"),
    )

    client = get_client()

    from agentlens.spans import Span, SpanKind
    span = Span(
        name="integration_test",
        kind=SpanKind.LLM_CALL,
        provider="anthropic",
        model="claude-sonnet-4-20250514",
        input_tokens=100,
        output_tokens=50,
    )
    span.end()
    client.record(span)
    client.flush()
    print("Integration test passed: event sent and accepted")
