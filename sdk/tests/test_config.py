from agentlens.config import AgentLensConfig, init, get_config


def test_init_sets_api_key():
    init(api_key="al_test123")
    cfg = get_config()
    assert cfg.api_key == "al_test123"


def test_init_sets_default_endpoint():
    init(api_key="al_test123")
    cfg = get_config()
    assert cfg.endpoint == "https://api.agentlens.dev"


def test_init_custom_endpoint():
    init(api_key="al_test123", endpoint="http://localhost:8000")
    cfg = get_config()
    assert cfg.endpoint == "http://localhost:8000"


def test_init_disabled():
    init(api_key="al_test123", enabled=False)
    cfg = get_config()
    assert cfg.enabled is False


def test_config_from_env(monkeypatch):
    monkeypatch.setenv("AGENTLENS_API_KEY", "al_env_key")
    init()
    cfg = get_config()
    assert cfg.api_key == "al_env_key"
