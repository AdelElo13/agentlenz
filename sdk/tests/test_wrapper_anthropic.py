import pytest
from unittest.mock import MagicMock, patch
from agentlenz.config import init
from agentlenz.wrappers.anthropic import wrap_anthropic


@pytest.fixture(autouse=True)
def setup():
    init(api_key="alz_test123", endpoint="http://localhost:8000")


def test_wrap_anthropic_returns_wrapper():
    mock_client = MagicMock()
    wrapped = wrap_anthropic(mock_client)
    assert hasattr(wrapped, "messages")


def test_wrapped_messages_create_records_span():
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.model = "claude-sonnet-4-20250514"
    mock_response.usage.input_tokens = 100
    mock_response.usage.output_tokens = 50
    mock_client.messages.create.return_value = mock_response

    wrapped = wrap_anthropic(mock_client)

    with patch("agentlenz.wrappers.anthropic.get_client") as mock_get_client:
        mock_event_client = MagicMock()
        mock_get_client.return_value = mock_event_client

        result = wrapped.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": "hi"}],
        )

        assert result is mock_response
        mock_event_client.record.assert_called_once()
        span = mock_event_client.record.call_args[0][0]
        assert span.provider == "anthropic"
        assert span.model == "claude-sonnet-4-20250514"
        assert span.input_tokens == 100
        assert span.output_tokens == 50


def test_wrapped_messages_create_records_error():
    mock_client = MagicMock()
    mock_client.messages.create.side_effect = Exception("API error")

    wrapped = wrap_anthropic(mock_client)

    with patch("agentlenz.wrappers.anthropic.get_client") as mock_get_client:
        mock_event_client = MagicMock()
        mock_get_client.return_value = mock_event_client

        with pytest.raises(Exception, match="API error"):
            wrapped.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": "hi"}],
            )

        mock_event_client.record.assert_called_once()
        span = mock_event_client.record.call_args[0][0]
        assert span.error == "API error"
