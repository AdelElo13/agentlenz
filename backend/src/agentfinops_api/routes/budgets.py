"""CRUD /v1/budgets — budget configuration API."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from agentfinops_api.auth import get_project_id
from agentfinops_api.db import get_db
from agentfinops_api.models import Budget
from agentfinops_api.schemas import BudgetCreate, BudgetResponse

router = APIRouter()


@router.post("/v1/budgets", response_model=BudgetResponse)
async def create_budget(
    body: BudgetCreate,
    project_id: uuid.UUID = Depends(get_project_id),
    db: AsyncSession = Depends(get_db),
) -> BudgetResponse:
    budget = Budget(
        project_id=project_id,
        name=body.name,
        max_cost_usd=body.max_cost_usd,
        period=body.period,
    )
    db.add(budget)
    await db.commit()
    await db.refresh(budget)
    return BudgetResponse(
        id=budget.id,
        name=budget.name,
        max_cost_usd=budget.max_cost_usd,
        period=budget.period,
        is_active=budget.is_active,
        created_at=budget.created_at,
    )


@router.get("/v1/budgets", response_model=list[BudgetResponse])
async def list_budgets(
    project_id: uuid.UUID = Depends(get_project_id),
    db: AsyncSession = Depends(get_db),
) -> list[BudgetResponse]:
    result = await db.execute(
        select(Budget).where(Budget.project_id == project_id, Budget.is_active == True)
    )
    budgets = result.scalars().all()
    return [
        BudgetResponse(
            id=b.id, name=b.name, max_cost_usd=b.max_cost_usd,
            period=b.period, is_active=b.is_active, created_at=b.created_at,
        )
        for b in budgets
    ]


@router.delete("/v1/budgets/{budget_id}")
async def delete_budget(
    budget_id: uuid.UUID,
    project_id: uuid.UUID = Depends(get_project_id),
    db: AsyncSession = Depends(get_db),
) -> dict:
    result = await db.execute(
        select(Budget).where(Budget.id == budget_id, Budget.project_id == project_id)
    )
    budget = result.scalar_one_or_none()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    budget.is_active = False
    await db.commit()
    return {"status": "deleted"}
