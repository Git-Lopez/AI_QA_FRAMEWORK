from ai_engine.llm_client import generate_from_llm
from ai_engine.prompt_templates import api_prompt

def generate_api_tests(story: str) -> str:
    return generate_from_llm(api_prompt(story))