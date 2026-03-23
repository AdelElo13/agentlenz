import uuid
import pytest
from agentlenz_api.models import Event
from tests.conftest import TEST_API_KEY


async def _seed_events(db, project_id: uuid.UUID):
    events = [
        Event(project_id=project_id, trace_id="t1", span_id="s1", name="call",
              kind="llm_call", provider="anthropic", model="claude-sonnet-4-20250514",
              input_tokens=1000, output_tokens=500, cost_usd=0.0105),
        Event(project_id=project_id, trace_id="t1", span_id="s2", name="call",
              kind="llm_call", provider="openai", model="gpt-4o",
              input_tokens=800, output_tokens=200, cost_usd=0.004),
        Event(project_id=project_id, trace_id="t2", span_id="s3", name="call",
              kind="llm_call", provider="anthropic", model="claude-sonnet-4-20250514",
              input_tokens=500, output_tokens=100, cost_usd=0.003),
    ]
    for e in events:
        db.add(e)
    await db.commit()


@pytest.mark.asyncio
async def test_get_costs(client, db):
    from sqlalchemy import select
    from agentlenz_api.models import ApiKey
    result = await db.execute(select(ApiKey))
    api_key = result.scalar_one()
    await _seed_events(db, api_key.project_id)

    response = await client.get(
        "/v1/costs",
        headers={"Authorization": f"Bearer {TEST_API_KEY}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total_cost_usd"] == pytest.approx(0.0175, abs=0.001)
    assert len(data["breakdown"]) == 2
