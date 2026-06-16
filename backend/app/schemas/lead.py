from pydantic import BaseModel
from datetime import datetime


class LeadCreate(BaseModel):

    name: str
    email: str
    phone: str
    company: str
    position: str


class LeadResponse(BaseModel):

    id: int

    name: str
    email: str
    phone: str
    company: str
    position: str

    score: int
    status: str
    next_action: str | None = None

    created_at: datetime