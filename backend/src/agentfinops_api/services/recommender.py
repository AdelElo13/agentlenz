"""Rules-based model routing recommendations."""

from __future__ import annotations

import uuid
from datetime import datetime, timedelta, timezone

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from agentfinops_api.models import Event
from agentfinops_api.schemas import Recommendation, RecommendationsResponse
from agentfinops_api.services.pricing import MODEL_PRICING, calculate_cost

DOWNGRADE_MAP: dict[str, list[str]] = {
    "claude-opus-4-20250514": ["claude-sonnet-4-20250514", "claude-haiku-4-5-20251001"],
    "claude-sonnet-4-20250514": ["claude-haiku-4-5-20251001"],
    "gpt-4o": ["gpt-4o-mini", "gpt-4.1-mini"],
    "gpt-4.1": ["gpt-4.1-mini", "gpt-4.1-nano"],
}


async def get_recommendations(
    db: AsyncSession,
    project_id: uuid.UUID,
    days: int = 30,
) -> RecommendationsResponse:
    since = datetime.now(timezone.utc) - timedelta(days=days)
    recommendations: list[Recommendation] = []

    for current_model, alternatives in DOWNGRADE_MAP.items():
        query = select(
            func.count().label("call_count"),
            func.sum(Event.cost_usd).label("total_cost"),
            func.sum(Event.input_tokens).label("total_input"),
            func.sum(Event.output_tokens).label("total_output"),
        ).where(
            Event.project_id == project_id,
            Event.model == current_model,
            Event.created_at >= since,
        )
        result = await db.execute(query)
        row = result.one()

        if not row.call_count or row.call_count == 0:
            continue

        recommended = alternatives[0]
        new_cost = calculate_cost(recommended, row.total_input, row.total_output)
        savings = row.total_cost - new_cost
        savings_pct = (savings / row.total_cost * 100) if row.total_cost > 0 else 0

        if savings > 0.01:
            recommendations.append(Recommendation(
                current_model=current_model,
                recommended_model=recommended,
                estimated_savings_pct=round(savings_pct, 1),
                estimated_savings_usd=round(savings, 4),
                affected_calls=row.call_count,
                reason=(
                    f"{row.call_count} calls to {current_model} could use {recommended} "
                    f"for ~{savings_pct:.0f}% cost reduction"
                ),
            ))

    recommendations.sort(key=lambda r: r.estimated_savings_usd, reverse=True)

    return RecommendationsResponse(
        recommendations=recommendations,
        total_potential_savings_usd=sum(r.estimated_savings_usd for r in recommendations),
    )
