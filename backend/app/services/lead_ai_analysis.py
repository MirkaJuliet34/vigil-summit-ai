from app.services.llm_service import get_llm

from app.prompts.enrichment_prompt import (
    ENRICHMENT_PROMPT
)


def analyze_lead(
    name,
    company,
    position
):

    llm = get_llm()

    prompt = ENRICHMENT_PROMPT.format(
        name=name,
        company=company,
        position=position
    )

    response = llm.invoke(prompt)

    return response.content