# AgentLenz

Cut your AI agent costs across every provider.

**Not just observability — optimization.** AgentLenz traces agent behavior, detects waste, recommends cheaper model routing, and enforces per-task budgets.

## Packages

- `sdk/` — Python SDK (open-source, PyPI: `agentlenz`)
- `backend/` — FastAPI API server
- `dashboard/` — Next.js web dashboard

## Quick Start

```python
import agentlenz
import anthropic

agentlenz.init(api_key="alz_...")
client = agentlenz.wrap(anthropic.Anthropic())

# Use client as normal — AgentLenz tracks costs automatically
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
```
