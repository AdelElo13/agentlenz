"""GET /v1/costs — cost breakdown API."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from agentfinops_api.auth import get_project_id
from agentfinops_api.db import get_db
from agentfinops_api.schemas import CostResponse
from agentfinops_api.services.cost_engine import get_cost_breakdown

router = APIRouter()


@router.get("/v1/costs", response_model=CostResponse)
async def get_costs(
    days: int = Query(default=30, ge=1, le=365),
    project_id: uuid.UUID = Depends(get_project_id),
    db: AsyncSession = Depends(get_db),
) -> CostResponse:
    return await get_cost_breakdown(db, project_id, days=days)
