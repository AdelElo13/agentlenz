import pytest
from agentlens.budget import BudgetContext, BudgetExceededError


def test_budget_tracks_spending():
    budget = BudgetContext(max_cost_usd=1.00)
    budget.record_cost(0.25)
    assert budget.total_cost == pytest.approx(0.25)
    assert budget.remaining == pytest.approx(0.75)


def test_budget_exceeded_raises():
    budget = BudgetContext(max_cost_usd=0.10)
    budget.record_cost(0.08)
    with pytest.raises(BudgetExceededError):
        budget.check(estimated_cost=0.05)


def test_budget_not_exceeded():
    budget = BudgetContext(max_cost_usd=1.00)
    budget.record_cost(0.50)
    budget.check(estimated_cost=0.10)  # Should not raise


def test_budget_context_manager():
    with BudgetContext(max_cost_usd=1.00) as budget:
        budget.record_cost(0.25)
        assert budget.remaining == pytest.approx(0.75)


def test_budget_warns_at_threshold():
    budget = BudgetContext(max_cost_usd=1.00, warn_at_pct=0.80)
    budget.record_cost(0.85)
    assert budget.is_warning is True


def test_budget_suggest_cheaper_model():
    budget = BudgetContext(max_cost_usd=0.50)
    budget.record_cost(0.40)
    suggestion = budget.suggest_model_downgrade(
        current_model="claude-opus-4-20250514",
        estimated_cost=0.20,
    )
    assert suggestion is not None
    assert "cheaper" in suggestion.lower() or suggestion != "claude-opus-4-20250514"
