"""Aggregates costs from events by provider, model, and time period."""

from __future__ import annotations

import uuid
from datetime import datetime, timedelta, timezone

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from agentlenz_api.models import Event
from agentlenz_api.schemas import CostBreakdown, CostResponse


async def get_cost_breakdown(
    db: AsyncSession,
    project_id: uuid.UUID,
    days: int = 30,
) -> CostResponse:
    period_end = datetime.now(timezone.utc)
    period_start = period_end - timedelta(days=days)

    query = (
        select(
            Event.provider,
            Event.model,
            func.sum(Event.cost_usd).label("total_cost"),
            func.sum(Event.input_tokens).label("total_input"),
            func.sum(Event.output_tokens).label("total_output"),
            func.count().label("call_count"),
        )
        .where(
            Event.project_id == project_id,
            Event.created_at >= period_start,
        )
        .group_by(Event.provider, Event.model)
        .order_by(func.sum(Event.cost_usd).desc())
    )

    result = await db.execute(query)
    rows = result.all()

    breakdown = [
        CostBreakdown(
            provider=row.provider,
            model=row.model,
            total_cost_usd=row.total_cost or 0,
            total_input_tokens=row.total_input or 0,
            total_output_tokens=row.total_output or 0,
            call_count=row.call_count,
        )
        for row in rows
    ]

    return CostResponse(
        total_cost_usd=sum(b.total_cost_usd for b in breakdown),
        breakdown=breakdown,
        period_start=period_start,
        period_end=period_end,
    )
