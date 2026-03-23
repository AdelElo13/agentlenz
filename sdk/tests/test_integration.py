"""End-to-end: SDK → Backend — smoke test.
Skip in CI unless explicitly enabled.
"""

import os
import pytest

pytestmark = pytest.mark.skipif(
    os.environ.get("AGENTFINOPS_INTEGRATION") != "1",
    reason="Set AGENTFINOPS_INTEGRATION=1 to run",
)


def test_sdk_sends_events_to_backend():
    import agentfinops
    from agentfinops.client import get_client

    agentfinops.init(
        api_key=os.environ.get("AGENTFINOPS_API_KEY", "af_test_key"),
        endpoint=os.environ.get("AGENTFINOPS_ENDPOINT", "http://localhost:8000"),
    )

    client = get_client()

    from agentfinops.spans import Span, SpanKind
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
