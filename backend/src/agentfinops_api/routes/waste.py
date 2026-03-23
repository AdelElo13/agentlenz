"""GET /v1/waste — waste detection API."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from agentfinops_api.auth import get_project_id
from agentfinops_api.db import get_db
from agentfinops_api.schemas import WasteResponse
from agentfinops_api.services.waste_detector import detect_waste

router = APIRouter()


@router.get("/v1/waste", response_model=WasteResponse)
async def get_waste(
    days: int = Query(default=30, ge=1, le=365),
    project_id: uuid.UUID = Depends(get_project_id),
    db: AsyncSession = Depends(get_db),
) -> WasteResponse:
    return await detect_waste(db, project_id, days=days)
