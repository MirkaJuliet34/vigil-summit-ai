from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.lead import Lead
from app.models.interaction import Interaction

router = APIRouter()


@router.get("/metrics")
def metrics(
    db: Session = Depends(get_db)
):

    total = db.query(Lead).count()

    hot = (
        db.query(Lead)
        .filter(Lead.status == "hot")
        .count()
    )

    warm = (
        db.query(Lead)
        .filter(Lead.status == "warm")
        .count()
    )

    cold = (
        db.query(Lead)
        .filter(Lead.status == "cold")
        .count()
    )

    confirmed = (
        db.query(Interaction)
        .filter(
            Interaction.interaction_type ==
            "confirmation_received"
        )
        .count()
    )

    meetings = (
        db.query(Interaction)
        .filter(
            Interaction.interaction_type ==
            "meeting_scheduled"
        )
        .count()
    )

    return {
        "total_leads": total,
        "hot": hot,
        "warm": warm,
        "cold": cold,
        "confirmed": confirmed,
        "meetings": meetings
    }