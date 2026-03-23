import uuid
from agentfinops.spans import Span, SpanKind


def test_span_creation():
    span = Span(
        name="messages.create",
        kind=SpanKind.LLM_CALL,
        provider="anthropic",
        model="claude-sonnet-4-20250514",
        input_tokens=100,
        output_tokens=50,
    )
    assert span.provider == "anthropic"
    assert span.model == "claude-sonnet-4-20250514"
    assert span.input_tokens == 100
    assert span.output_tokens == 50
    assert span.trace_id is not None
    assert span.span_id is not None


def test_span_to_otel_dict():
    span = Span(
        name="messages.create",
        kind=SpanKind.LLM_CALL,
        provider="anthropic",
        model="claude-sonnet-4-20250514",
        input_tokens=100,
        output_tokens=50,
    )
    d = span.to_otel_dict()
    assert d["attributes"]["gen_ai.system"] == "anthropic"
    assert d["attributes"]["gen_ai.request.model"] == "claude-sonnet-4-20250514"
    assert d["attributes"]["gen_ai.usage.input_tokens"] == 100
    assert d["attributes"]["gen_ai.usage.output_tokens"] == 50
    assert "traceId" in d
    assert "spanId" in d


def test_span_duration():
    span = Span(
        name="test",
        kind=SpanKind.LLM_CALL,
        provider="openai",
        model="gpt-4o",
        input_tokens=10,
        output_tokens=10,
    )
    span.end()
    assert span.duration_ms is not None
    assert span.duration_ms >= 0
