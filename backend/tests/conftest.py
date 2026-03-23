"""Shared test fixtures — uses SQLite for fast isolated tests."""

import uuid
from hashlib import sha256

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from agentlens_api.models import Base, Project, ApiKey
from agentlens_api.db import get_db
from agentlens_api.main import app

TEST_API_KEY = "al_test_abc123"
TEST_KEY_HASH = sha256(TEST_API_KEY.encode()).hexdigest()

engine = create_async_engine("sqlite+aiosqlite:///:memory:")
test_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@pytest_asyncio.fixture
async def db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with test_session() as session:
        project = Project(id=uuid.uuid4(), name="Test Project")
        session.add(project)
        api_key = ApiKey(
            id=uuid.uuid4(),
            key_hash=TEST_KEY_HASH,
            key_prefix="al_test_",
            project_id=project.id,
        )
        session.add(api_key)
        await session.commit()
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def client(db):
    async def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        yield ac
    app.dependency_overrides.clear()
