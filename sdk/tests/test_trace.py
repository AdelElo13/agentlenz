import pytest
from unittest.mock import patch, MagicMock
from agentlens.config import init
from agentlens.trace import trace


@pytest.fixture(autouse=True)
def setup():
    init(api_key="al_test123", endpoint="http://localhost:8000")


def test_trace_decorator_records_span():
    with patch("agentlens.trace.get_client") as mock_get_client:
        mock_event_client = MagicMock()
        mock_get_client.return_value = mock_event_client

        @trace(name="my_agent_step")
        def my_function(x: int) -> int:
            return x * 2

        result = my_function(5)
        assert result == 10
        mock_event_client.record.assert_called_once()
        span = mock_event_client.record.call_args[0][0]
        assert span.name == "my_agent_step"
        assert span.kind.value == "agent_step"


def test_trace_decorator_records_error():
    with patch("agentlens.trace.get_client") as mock_get_client:
        mock_event_client = MagicMock()
        mock_get_client.return_value = mock_event_client

        @trace(name="failing_step")
        def bad_function() -> None:
            raise ValueError("something broke")

        with pytest.raises(ValueError, match="something broke"):
            bad_function()

        span = mock_event_client.record.call_args[0][0]
        assert span.error == "something broke"


def test_trace_decorator_default_name():
    with patch("agentlens.trace.get_client") as mock_get_client:
        mock_event_client = MagicMock()
        mock_get_client.return_value = mock_event_client

        @trace()
        def process_data() -> str:
            return "done"

        process_data()
        span = mock_event_client.record.call_args[0][0]
        assert span.name == "process_data"
