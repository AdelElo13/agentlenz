"""GET /v1/recommendations — model routing recommendations."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from agentlenz_api.auth import get_project_id
from agentlenz_api.db import get_db
from agentlenz_api.schemas import RecommendationsResponse
from agentlenz_api.services.recommender import get_recommendations

router = APIRouter()


@router.get("/v1/recommendations", response_model=RecommendationsResponse)
async def get_recs(
    days: int = Query(default=30, ge=1, le=365),
    project_id: uuid.UUID = Depends(get_project_id),
    db: AsyncSession = Depends(get_db),
) -> RecommendationsResponse:
    return await get_recommendations(db, project_id, days=days)
