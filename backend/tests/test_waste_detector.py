import uuid
import pytest
from agentlenz_api.models import Event
from agentlenz_api.services.waste_detector import detect_waste
from tests.conftest import TEST_API_KEY


async def _seed_wasteful_events(db, project_id):
    events = []
    for i in range(20):
        events.append(Event(
            project_id=project_id, trace_id=f"t_opus_{i}", span_id=f"s{i}",
            name="call", kind="llm_call", provider="anthropic",
            model="claude-opus-4-20250514",
            input_tokens=50, output_tokens=30, cost_usd=0.003,
        ))
    for i in range(18):
        events.append(Event(
            project_id=project_id, trace_id="t_loop", span_id=f"loop_{i}",
            name="messages.create", kind="llm_call", provider="anthropic",
            model="claude-sonnet-4-20250514",
            input_tokens=500, output_tokens=200, cost_usd=0.0045,
        ))
    for e in events:
        db.add(e)
    await db.commit()


@pytest.mark.asyncio
async def test_detect_expensive_model_overuse(db):
    from sqlalchemy import select
    from agentlenz_api.models import ApiKey
    result = await db.execute(select(ApiKey))
    api_key = result.scalar_one()
    await _seed_wasteful_events(db, api_key.project_id)

    waste = await detect_waste(db, api_key.project_id)
    types = [item.type for item in waste.items]
    assert "expensive_model_overuse" in types


@pytest.mark.asyncio
async def test_detect_stuck_loop(db):
    from sqlalchemy import select
    from agentlenz_api.models import ApiKey
    result = await db.execute(select(ApiKey))
    api_key = result.scalar_one()
    await _seed_wasteful_events(db, api_key.project_id)

    waste = await detect_waste(db, api_key.project_id)
    types = [item.type for item in waste.items]
    assert "stuck_loop" in types


@pytest.mark.asyncio
async def test_waste_has_savings_estimate(db):
    from sqlalchemy import select
    from agentlenz_api.models import ApiKey
    result = await db.execute(select(ApiKey))
    api_key = result.scalar_one()
    await _seed_wasteful_events(db, api_key.project_id)

    waste = await detect_waste(db, api_key.project_id)
    assert waste.total_potential_savings_usd > 0
