"""Database engine and session management."""

from __future__ import annotations

import os
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

_raw_url = os.environ.get(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/agentlenz",
)

# Fly.io uses postgres:// but SQLAlchemy needs postgresql+asyncpg://
DATABASE_URL = _raw_url
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

# asyncpg doesn't support sslmode as a query param
DATABASE_URL = DATABASE_URL.replace("?sslmode=disable", "")

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"ssl": None} if "flycast" in DATABASE_URL or "internal" in DATABASE_URL else {},
)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
