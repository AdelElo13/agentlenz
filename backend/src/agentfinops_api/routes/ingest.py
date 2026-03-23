"""POST /v1/events — ingest span events from the SDK."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from agentfinops_api.auth import get_project_id
from agentfinops_api.db import get_db
from agentfinops_api.models import Event
from agentfinops_api.schemas import IngestRequest, IngestResponse
from agentfinops_api.services.pricing import calculate_cost

router = APIRouter()


@router.post("/v1/events", response_model=IngestResponse)
async def ingest_events(
    body: IngestRequest,
    project_id: uuid.UUID = Depends(get_project_id),
    db: AsyncSession = Depends(get_db),
) -> IngestResponse:
    for span in body.events:
        attrs = span.attributes
        input_tokens = attrs.get("gen_ai.usage.input_tokens", 0)
        output_tokens = attrs.get("gen_ai.usage.output_tokens", 0)
        model = attrs.get("gen_ai.request.model", "unknown")
        provider = attrs.get("gen_ai.system", "unknown")

        duration_ms = None
        if span.endTimeUnixNano and span.startTimeUnixNano:
            duration_ms = (span.endTimeUnixNano - span.startTimeUnixNano) / 1_000_000

        event = Event(
            project_id=project_id,
            trace_id=span.traceId,
            span_id=span.spanId,
            parent_span_id=span.parentSpanId,
            name=span.name,
            kind=span.kind,
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost_usd=calculate_cost(model, input_tokens, output_tokens),
            duration_ms=duration_ms,
            error=attrs.get("error.message"),
        )
        db.add(event)

    await db.commit()
    return IngestResponse(accepted=len(body.events))
