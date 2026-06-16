from fastapi import APIRouter

from app.agents.workflow import graph

router = APIRouter()


@router.post("/test")

def test_agent():

    result = graph.invoke({

        "lead_id": 1,

        "lead_name": "Carlos",

        "company": "XPTO",

        "position": "CISO",

        "score": 80,

        "status": "hot",

        "next_action": ""
    })

    return result