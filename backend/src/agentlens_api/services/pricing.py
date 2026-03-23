"""Model pricing lookup — maps (provider, model) to cost per token."""

from __future__ import annotations

MODEL_PRICING: dict[str, tuple[float, float]] = {
    "claude-opus-4-20250514": (15.0 / 1_000_000, 75.0 / 1_000_000),
    "claude-sonnet-4-20250514": (3.0 / 1_000_000, 15.0 / 1_000_000),
    "claude-haiku-4-5-20251001": (0.80 / 1_000_000, 4.0 / 1_000_000),
    "gpt-4o": (2.50 / 1_000_000, 10.0 / 1_000_000),
    "gpt-4o-mini": (0.15 / 1_000_000, 0.60 / 1_000_000),
    "gpt-4.1": (2.0 / 1_000_000, 8.0 / 1_000_000),
    "gpt-4.1-mini": (0.40 / 1_000_000, 1.60 / 1_000_000),
    "gpt-4.1-nano": (0.10 / 1_000_000, 0.40 / 1_000_000),
    "gemini-2.5-pro": (1.25 / 1_000_000, 10.0 / 1_000_000),
    "gemini-2.5-flash": (0.15 / 1_000_000, 0.60 / 1_000_000),
}

DEFAULT_PRICING = (5.0 / 1_000_000, 15.0 / 1_000_000)


def calculate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    input_price, output_price = MODEL_PRICING.get(model, DEFAULT_PRICING)
    return (input_tokens * input_price) + (output_tokens * output_price)
