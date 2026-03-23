"""API key authentication dependency."""

from __future__ import annotations

import uuid
from hashlib import sha256

from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from agentfinops_api.db import get_db
from agentfinops_api.models import ApiKey

security = HTTPBearer()


async def get_project_id(
    credentials: HTTPAuthorizationCredentials = Security(security),
    db: AsyncSession = Depends(get_db),
) -> uuid.UUID:
    key_hash = sha256(credentials.credentials.encode()).hexdigest()
    result = await db.execute(
        select(ApiKey).where(ApiKey.key_hash == key_hash, ApiKey.is_active == True)
    )
    api_key = result.scalar_one_or_none()
    if api_key is None:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key.project_id
