"""Pydantic request/response schemas."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel


class SpanEvent(BaseModel):
    traceId: str
    spanId: str
    parentSpanId: str | None = None
    name: str
    kind: str
    startTimeUnixNano: int
    endTimeUnixNano: int | None = None
    attributes: dict[str, Any]


class IngestRequest(BaseModel):
    events: list[SpanEvent]


class IngestResponse(BaseModel):
    accepted: int


class CostBreakdown(BaseModel):
    provider: str
    model: str
    total_cost_usd: float
    total_input_tokens: int
    total_output_tokens: int
    call_count: int


class CostResponse(BaseModel):
    total_cost_usd: float
    breakdown: list[CostBreakdown]
    period_start: datetime
    period_end: datetime


class WasteItem(BaseModel):
    type: str
    description: str
    potential_savings_usd: float
    affected_traces: int
    recommendation: str


class WasteResponse(BaseModel):
    total_potential_savings_usd: float
    items: list[WasteItem]


class Recommendation(BaseModel):
    current_model: str
    recommended_model: str
    estimated_savings_pct: float
    estimated_savings_usd: float
    affected_calls: int
    reason: str


class RecommendationsResponse(BaseModel):
    recommendations: list[Recommendation]
    total_potential_savings_usd: float


class BudgetCreate(BaseModel):
    name: str
    max_cost_usd: float
    period: str = "monthly"


class BudgetResponse(BaseModel):
    id: uuid.UUID
    name: str
    max_cost_usd: float
    period: str
    is_active: bool
    current_spend_usd: float = 0.0
    created_at: datetime
