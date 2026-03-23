import pytest
from agentlens_api.services.pricing import calculate_cost, MODEL_PRICING


def test_anthropic_sonnet_cost():
    cost = calculate_cost("claude-sonnet-4-20250514", input_tokens=1000, output_tokens=500)
    expected = (1000 * 3.0 / 1_000_000) + (500 * 15.0 / 1_000_000)
    assert cost == pytest.approx(expected)


def test_openai_gpt4o_cost():
    cost = calculate_cost("gpt-4o", input_tokens=1000, output_tokens=500)
    expected = (1000 * 2.50 / 1_000_000) + (500 * 10.0 / 1_000_000)
    assert cost == pytest.approx(expected)


def test_unknown_model_uses_default():
    cost = calculate_cost("unknown-model-v9", input_tokens=1000, output_tokens=500)
    assert cost > 0


def test_zero_tokens():
    cost = calculate_cost("claude-sonnet-4-20250514", input_tokens=0, output_tokens=0)
    assert cost == 0.0


def test_all_models_in_pricing_table_have_two_values():
    for model, prices in MODEL_PRICING.items():
        assert len(prices) == 2, f"{model} should have (input, output) pricing tuple"
        assert prices[0] >= 0, f"{model} input price should be non-negative"
        assert prices[1] >= 0, f"{model} output price should be non-negative"
