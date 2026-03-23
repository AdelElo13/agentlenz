import pytest
from tests.conftest import TEST_API_KEY


@pytest.mark.asyncio
async def test_ingest_events(client):
    response = await client.post(
        "/v1/events",
        json={
            "events": [
                {
                    "traceId": "abc123",
                    "spanId": "span001",
                    "name": "messages.create",
                    "kind": "llm_call",
                    "startTimeUnixNano": 1000000000,
                    "endTimeUnixNano": 2000000000,
                    "attributes": {
                        "gen_ai.system": "anthropic",
                        "gen_ai.request.model": "claude-sonnet-4-20250514",
                        "gen_ai.usage.input_tokens": 100,
                        "gen_ai.usage.output_tokens": 50,
                    },
                }
            ]
        },
        headers={"Authorization": f"Bearer {TEST_API_KEY}"},
    )
    assert response.status_code == 200
    assert response.json()["accepted"] == 1


@pytest.mark.asyncio
async def test_ingest_rejects_no_auth(client):
    response = await client.post(
        "/v1/events",
        json={"events": []},
    )
    assert response.status_code in (401, 403)


@pytest.mark.asyncio
async def test_ingest_rejects_bad_key(client):
    response = await client.post(
        "/v1/events",
        json={"events": []},
        headers={"Authorization": "Bearer al_wrong_key"},
    )
    assert response.status_code == 401
