from fastapi import APIRouter

from app.services.lead_ai_analysis import (
    analyze_lead
)

router = APIRouter()


@router.get("/test")

def test_ai():

    result = analyze_lead(
        name="Carlos Silva",
        company="XPTO Bank",
        position="CISO"
    )

    return {
        "analysis": result
    }