"""Detects wasteful patterns in agent event data."""

from __future__ import annotations

import uuid
from datetime import datetime, timedelta, timezone

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from agentlens_api.models import Event
from agentlens_api.schemas import WasteItem, WasteResponse
from agentlens_api.services.pricing import MODEL_PRICING

EXPENSIVE_MODELS = {
    "claude-opus-4-20250514": "claude-haiku-4-5-20251001",
    "gpt-4o": "gpt-4o-mini",
    "gpt-4.1": "gpt-4.1-mini",
}

LOOP_THRESHOLD = 15
SHORT_OUTPUT_THRESHOLD = 100


async def detect_waste(
    db: AsyncSession,
    project_id: uuid.UUID,
    days: int = 30,
) -> WasteResponse:
    since = datetime.now(timezone.utc) - timedelta(days=days)
    items: list[WasteItem] = []

    for expensive_model, cheap_alternative in EXPENSIVE_MODELS.items():
        query = select(
            func.count().label("call_count"),
            func.sum(Event.cost_usd).label("total_cost"),
            func.sum(Event.input_tokens).label("total_input"),
            func.sum(Event.output_tokens).label("total_output"),
        ).where(
            Event.project_id == project_id,
            Event.model == expensive_model,
            Event.output_tokens < SHORT_OUTPUT_THRESHOLD,
            Event.created_at >= since,
        )
        result = await db.execute(query)
        row = result.one()

        if row.call_count and row.call_count > 0:
            cheap_input, cheap_output = MODEL_PRICING.get(cheap_alternative, (0, 0))
            cheap_cost = (row.total_input * cheap_input) + (row.total_output * cheap_output)
            savings = row.total_cost - cheap_cost

            if savings > 0:
                items.append(WasteItem(
                    type="expensive_model_overuse",
                    description=(
                        f"{row.call_count} calls used {expensive_model} with <{SHORT_OUTPUT_THRESHOLD} "
                        f"output tokens — {cheap_alternative} would likely produce the same result"
                    ),
                    potential_savings_usd=savings,
                    affected_traces=row.call_count,
                    recommendation=f"Switch to {cheap_alternative} for short-output tasks",
                ))

    loop_query = (
        select(
            Event.trace_id,
            func.count().label("span_count"),
            func.sum(Event.cost_usd).label("trace_cost"),
        )
        .where(Event.project_id == project_id, Event.created_at >= since)
        .group_by(Event.trace_id)
        .having(func.count() > LOOP_THRESHOLD)
    )
    loop_result = await db.execute(loop_query)
    loop_rows = loop_result.all()

    if loop_rows:
        total_loop_cost = sum(r.trace_cost for r in loop_rows)
        estimated_waste = total_loop_cost * 0.5
        items.append(WasteItem(
            type="stuck_loop",
            description=(
                f"{len(loop_rows)} traces have >{LOOP_THRESHOLD} LLM calls each — "
                f"possible stuck agent loops"
            ),
            potential_savings_usd=estimated_waste,
            affected_traces=len(loop_rows),
            recommendation="Add loop detection or max-iteration limits to your agent workflows",
        ))

    return WasteResponse(
        total_potential_savings_usd=sum(i.potential_savings_usd for i in items),
        items=items,
    )
