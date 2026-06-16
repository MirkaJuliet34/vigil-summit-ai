from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.interaction import Interaction


router = APIRouter()


@router.post("/followup/{lead_id}")
def send_followup(
    lead_id: int,
    db: Session = Depends(get_db)
):

    interaction = Interaction(
        lead_id=lead_id,
        channel="email",
        interaction_type="followup_sent",
        content="Personalized follow-up sent",
        status="completed"
    )

    db.add(interaction)
    db.commit()

    return {
        "lead_id": lead_id,
        "status": "followup_sent"
    }


@router.post("/meeting/{lead_id}")
def schedule_meeting(
    lead_id: int,
    db: Session = Depends(get_db)
):

    interaction = Interaction(
        lead_id=lead_id,
        channel="email",
        interaction_type="meeting_scheduled",
        content="Commercial meeting scheduled",
        status="completed"
    )

    db.add(interaction)
    db.commit()

    return {
        "lead_id": lead_id,
        "status": "meeting_scheduled"
    }