from ai_engine.llm_client import generate_from_llm
from ai_engine.prompts.step_prompt import step_prompt


def generate_steps(test_input):
    prompt = step_prompt(test_input)
    return generate_from_llm(prompt)