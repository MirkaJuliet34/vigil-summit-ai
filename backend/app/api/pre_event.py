from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.interaction import Interaction


router = APIRouter()


@router.post("/confirm/{lead_id}")
def confirm_attendance(
    lead_id: int,
    db: Session = Depends(get_db)
):

    interaction = Interaction(
        lead_id=lead_id,
        channel="email",
        interaction_type="confirmation_received",
        content="Lead confirmed attendance",
        status="completed"
    )

    db.add(interaction)
    db.commit()

    return {
        "lead_id": lead_id,
        "status": "confirmed"
    }