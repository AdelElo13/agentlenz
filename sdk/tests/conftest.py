"""Reset global SDK state between tests to prevent flaky ordering issues."""

import pytest
import agentlens.config as config_mod
import agentlens.client as client_mod


@pytest.fixture(autouse=True)
def reset_sdk_state():
    """Reset config and client singletons before each test."""
    yield
    config_mod._config = None
    client_mod._client = None
