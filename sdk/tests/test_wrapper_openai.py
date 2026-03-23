import pytest
from unittest.mock import MagicMock, patch
from agentlenz.config import init
from agentlenz.wrappers.openai import wrap_openai


@pytest.fixture(autouse=True)
def setup():
    init(api_key="alz_test123", endpoint="http://localhost:8000")


def test_wrap_openai_returns_wrapper():
    mock_client = MagicMock()
    wrapped = wrap_openai(mock_client)
    assert hasattr(wrapped, "chat")


def test_wrapped_chat_completions_create_records_span():
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.model = "gpt-4o"
    mock_response.usage.prompt_tokens = 80
    mock_response.usage.completion_tokens = 40
    mock_client.chat.completions.create.return_value = mock_response

    wrapped = wrap_openai(mock_client)

    with patch("agentlenz.wrappers.openai.get_client") as mock_get_client:
        mock_event_client = MagicMock()
        mock_get_client.return_value = mock_event_client

        result = wrapped.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "hi"}],
        )

        assert result is mock_response
        mock_event_client.record.assert_called_once()
        span = mock_event_client.record.call_args[0][0]
        assert span.provider == "openai"
        assert span.model == "gpt-4o"
        assert span.input_tokens == 80
        assert span.output_tokens == 40
