from agentfinops.config import AgentFinOpsConfig, init, get_config


def test_init_sets_api_key():
    init(api_key="af_test123")
    cfg = get_config()
    assert cfg.api_key == "af_test123"


def test_init_sets_default_endpoint():
    init(api_key="af_test123")
    cfg = get_config()
    assert cfg.endpoint == "https://api.agentfinops.dev"


def test_init_custom_endpoint():
    init(api_key="af_test123", endpoint="http://localhost:8000")
    cfg = get_config()
    assert cfg.endpoint == "http://localhost:8000"


def test_init_disabled():
    init(api_key="af_test123", enabled=False)
    cfg = get_config()
    assert cfg.enabled is False


def test_config_from_env(monkeypatch):
    monkeypatch.setenv("AGENTFINOPS_API_KEY", "af_env_key")
    init()
    cfg = get_config()
    assert cfg.api_key == "af_env_key"
