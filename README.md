# AgentFinOps

Cut your AI agent costs across every provider.

**Not just observability — optimization.** AgentFinOps traces agent behavior, detects waste, recommends cheaper model routing, and enforces per-task budgets.

## Packages

- `sdk/` — Python SDK (open-source, PyPI: `agentfinops`)
- `backend/` — FastAPI API server
- `dashboard/` — Next.js web dashboard

## Quick Start

```python
import agentfinops
import anthropic

agentfinops.init(api_key="af_...")
client = agentfinops.wrap(anthropic.Anthropic())

# Use client as normal — AgentFinOps tracks costs automatically
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
```
