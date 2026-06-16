from app.config import (
    ANTHROPIC_API_KEY,
    OPENAI_API_KEY,
    LLM_PROVIDER
)

from langchain_anthropic import (
    ChatAnthropic
)

from langchain_openai import (
    ChatOpenAI
)


def get_llm():

    if LLM_PROVIDER == "openai":

        return ChatOpenAI(
            model="gpt-4o-mini",
            api_key=OPENAI_API_KEY,
            temperature=0.2
        )

    return ChatAnthropic(
        model="claude-3-5-sonnet-latest",
        anthropic_api_key=ANTHROPIC_API_KEY,
        temperature=0.2
    )