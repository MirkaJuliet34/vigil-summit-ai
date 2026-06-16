from fastapi import APIRouter

from app.config import (
    LLM_PROVIDER
)

router = APIRouter()


@router.get("/provider")
def provider():

    return {
        "provider": LLM_PROVIDER
    }