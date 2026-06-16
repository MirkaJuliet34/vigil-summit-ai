from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.models.lead import Lead
from app.models.enriched_profile import EnrichedProfile
from app.models.interaction import Interaction

from app.api.leads import router as lead_router
from app.api.agent import router as agent_router
from app.api.ai import router as ai_router
from app.api.pre_event import router as pre_event_router
from app.api.dashboard import (
    router as dashboard_router
)
from app.api.post_event import router as post_event_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vigil Summit AI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    lead_router,
    prefix="/leads",
    tags=["Leads"]
)

app.include_router(
    agent_router,
    prefix="/agent",
    tags=["Agent"]
)

app.include_router(
    ai_router,
    prefix="/ai",
    tags=["AI"]
)

app.include_router(
    pre_event_router,
    prefix="/pre-event",
    tags=["Pre Event"]
)

app.include_router(
    dashboard_router,
    prefix="/dashboard",
    tags=["Dashboard"]
)

app.include_router(
    post_event_router,
    prefix="/post-event",
    tags=["Post Event"]
)

@app.get("/")
def health():

    return {
        "status": "running"
    }