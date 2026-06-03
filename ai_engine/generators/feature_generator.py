from ai_engine.llm_client import generate_from_llm
from ai_engine.prompts.feature_prompt import feature_prompt


def generate_feature(test_input):
    prompt = feature_prompt(test_input)
    return generate_from_llm(prompt)