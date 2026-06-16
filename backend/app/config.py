from dotenv import load_dotenv
import os

load_dotenv()

ANTHROPIC_API_KEY = os.getenv(
    "ANTHROPIC_API_KEY"
)

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "anthropic"
)