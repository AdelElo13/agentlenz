# AgentLens

Cut your AI agent costs across every provider.

**Not just observability — optimization.** AgentLens traces agent behavior, detects waste, recommends cheaper model routing, and enforces per-task budgets.

## Packages

- `sdk/` — Python SDK (open-source, PyPI: `agentlens`)
- `backend/` — FastAPI API server
- `dashboard/` — Next.js web dashboard

## Quick Start

```python
import agentlens
import anthropic

agentlens.init(api_key="al_...")
client = agentlens.wrap(anthropic.Anthropic())

# Use client as normal — AgentLens tracks costs automatically
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
```
