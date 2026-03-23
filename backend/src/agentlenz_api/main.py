"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agentlenz_api.routes import ingest, costs, waste, recommendations, budgets

app = FastAPI(
    title="AgentLenz API",
    version="0.1.0",
    description="AI agent cost optimization platform",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest.router, tags=["ingest"])
app.include_router(costs.router, tags=["costs"])
app.include_router(waste.router, tags=["waste"])
app.include_router(recommendations.router, tags=["recommendations"])
app.include_router(budgets.router, tags=["budgets"])


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
