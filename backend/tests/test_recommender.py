import uuid
import pytest
from agentlenz_api.models import Event
from agentlenz_api.services.recommender import get_recommendations
from tests.conftest import TEST_API_KEY


async def _seed_events(db, project_id):
    events = [
        *[Event(
            project_id=project_id, trace_id=f"t{i}", span_id=f"s{i}",
            name="call", kind="llm_call", provider="anthropic",
            model="claude-opus-4-20250514",
            input_tokens=500, output_tokens=300, cost_usd=0.030,
        ) for i in range(50)],
        *[Event(
            project_id=project_id, trace_id=f"g{i}", span_id=f"gs{i}",
            name="call", kind="llm_call", provider="openai",
            model="gpt-4o",
            input_tokens=200, output_tokens=100, cost_usd=0.0015,
        ) for i in range(30)],
    ]
    for e in events:
        db.add(e)
    await db.commit()


@pytest.mark.asyncio
async def test_recommender_suggests_downgrades(db):
    from sqlalchemy import select
    from agentlenz_api.models import ApiKey
    result = await db.execute(select(ApiKey))
    api_key = result.scalar_one()
    await _seed_events(db, api_key.project_id)

    recs = await get_recommendations(db, api_key.project_id)
    assert len(recs.recommendations) > 0
    assert recs.total_potential_savings_usd > 0


@pytest.mark.asyncio
async def test_recommender_cross_provider(db):
    from sqlalchemy import select
    from agentlenz_api.models import ApiKey
    result = await db.execute(select(ApiKey))
    api_key = result.scalar_one()
    await _seed_events(db, api_key.project_id)

    recs = await get_recommendations(db, api_key.project_id)
    models = [r.recommended_model for r in recs.recommendations]
    assert any(m != "claude-opus-4-20250514" for m in models)
