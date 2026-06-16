from typing import TypedDict


class LeadState(TypedDict):

    lead_id: int

    lead_name: str

    company: str

    position: str

    score: int

    status: str

    next_action: str