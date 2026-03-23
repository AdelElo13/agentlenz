"""OTEL-compatible span data model for AI agent telemetry."""

from __future__ import annotations

import time
import uuid
from dataclasses import dataclass, field
from enum import Enum


class SpanKind(str, Enum):
    LLM_CALL = "llm_call"
    TOOL_CALL = "tool_call"
    AGENT_STEP = "agent_step"


@dataclass
class Span:
    name: str
    kind: SpanKind
    provider: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    error: str | None = None
    trace_id: str = field(default_factory=lambda: uuid.uuid4().hex)
    span_id: str = field(default_factory=lambda: uuid.uuid4().hex[:16])
    parent_span_id: str | None = None
    start_time_ns: int = field(default_factory=time.time_ns)
    end_time_ns: int | None = None
    metadata: dict = field(default_factory=dict)

    @property
    def duration_ms(self) -> float | None:
        if self.end_time_ns is None:
            return None
        return (self.end_time_ns - self.start_time_ns) / 1_000_000

    def end(self) -> None:
        self.end_time_ns = time.time_ns()

    def to_otel_dict(self) -> dict:
        """Serialize to OTEL-compatible span format using gen_ai.* conventions."""
        return {
            "traceId": self.trace_id,
            "spanId": self.span_id,
            "parentSpanId": self.parent_span_id,
            "name": self.name,
            "kind": self.kind.value,
            "startTimeUnixNano": self.start_time_ns,
            "endTimeUnixNano": self.end_time_ns,
            "attributes": {
                "gen_ai.system": self.provider,
                "gen_ai.request.model": self.model,
                "gen_ai.usage.input_tokens": self.input_tokens,
                "gen_ai.usage.output_tokens": self.output_tokens,
                **({"error.message": self.error} if self.error else {}),
                **{f"agentlenz.{k}": v for k, v in self.metadata.items()},
            },
        }
