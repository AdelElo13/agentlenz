import pytest
from tests.conftest import TEST_API_KEY


@pytest.mark.asyncio
async def test_create_budget(client):
    response = await client.post(
        "/v1/budgets",
        json={"name": "Monthly Agent Budget", "max_cost_usd": 500.00, "period": "monthly"},
        headers={"Authorization": f"Bearer {TEST_API_KEY}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Monthly Agent Budget"
    assert data["max_cost_usd"] == 500.00


@pytest.mark.asyncio
async def test_list_budgets(client):
    await client.post(
        "/v1/budgets",
        json={"name": "Budget A", "max_cost_usd": 100.00},
        headers={"Authorization": f"Bearer {TEST_API_KEY}"},
    )
    await client.post(
        "/v1/budgets",
        json={"name": "Budget B", "max_cost_usd": 200.00},
        headers={"Authorization": f"Bearer {TEST_API_KEY}"},
    )
    response = await client.get(
        "/v1/budgets",
        headers={"Authorization": f"Bearer {TEST_API_KEY}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


@pytest.mark.asyncio
async def test_delete_budget(client):
    create_resp = await client.post(
        "/v1/budgets",
        json={"name": "Temp Budget", "max_cost_usd": 50.00},
        headers={"Authorization": f"Bearer {TEST_API_KEY}"},
    )
    budget_id = create_resp.json()["id"]
    delete_resp = await client.delete(
        f"/v1/budgets/{budget_id}",
        headers={"Authorization": f"Bearer {TEST_API_KEY}"},
    )
    assert delete_resp.status_code == 200
