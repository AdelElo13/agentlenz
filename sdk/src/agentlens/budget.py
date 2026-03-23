"""Per-task budget enforcement for AI agent costs."""

from __future__ import annotations

from dataclasses import dataclass, field

# Rough model cost tiers ($/1M input tokens) — used for downgrade suggestions
MODEL_COST_TIERS = {
    "claude-opus-4-20250514": 15.0,
    "claude-sonnet-4-20250514": 3.0,
    "claude-haiku-4-5-20251001": 0.80,
    "gpt-4o": 2.50,
    "gpt-4o-mini": 0.15,
    "gpt-4.1": 2.0,
    "gpt-4.1-mini": 0.40,
    "gpt-4.1-nano": 0.10,
}

# Ordered cheapest → most expensive for downgrade suggestions
MODEL_DOWNGRADE_ORDER = sorted(MODEL_COST_TIERS.keys(), key=lambda m: MODEL_COST_TIERS[m])


class BudgetExceededError(Exception):
    """Raised when a task would exceed its cost budget."""

    def __init__(self, budget: float, spent: float, estimated: float) -> None:
        self.budget = budget
        self.spent = spent
        self.estimated = estimated
        super().__init__(
            f"Budget exceeded: ${spent:.4f} spent + ${estimated:.4f} estimated "
            f"> ${budget:.4f} budget"
        )


@dataclass
class BudgetContext:
    max_cost_usd: float
    warn_at_pct: float = 0.80
    total_cost: float = 0.0

    @property
    def remaining(self) -> float:
        return max(0.0, self.max_cost_usd - self.total_cost)

    @property
    def is_warning(self) -> bool:
        return self.total_cost >= self.max_cost_usd * self.warn_at_pct

    def record_cost(self, cost_usd: float) -> None:
        self.total_cost += cost_usd

    def check(self, estimated_cost: float) -> None:
        """Raise BudgetExceededError if the next call would exceed budget."""
        if self.total_cost + estimated_cost > self.max_cost_usd:
            raise BudgetExceededError(self.max_cost_usd, self.total_cost, estimated_cost)

    def suggest_model_downgrade(
        self, current_model: str, estimated_cost: float
    ) -> str | None:
        """Suggest a cheaper model if current call would exceed remaining budget."""
        if self.total_cost + estimated_cost <= self.max_cost_usd:
            return None

        current_tier = MODEL_COST_TIERS.get(current_model, float("inf"))
        for model in MODEL_DOWNGRADE_ORDER:
            if MODEL_COST_TIERS[model] < current_tier:
                return model
        return None

    def __enter__(self) -> BudgetContext:
        return self

    def __exit__(self, *args: object) -> None:
        pass
