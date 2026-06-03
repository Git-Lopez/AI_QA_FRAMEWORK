from ai_engine.llm_client import generate_from_llm
from ai_engine.prompts.ui_test_prompt import ui_test_prompt

#temporaly code to work outside llm end to end. this becomes real executable python
def generate_ui_test(test_input):

    story = test_input.get("story")

    return f'''
from playwright.sync_api import Page


def test_generated_ui(page: Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    actual_title = page.title()
    expected_title = "OrangeHRM"

    assert actual_title == expected_title, (
        f"Expected '{{expected_title}}' but got '{{actual_title}}'"
    )
'''

#Future code to work with LLM 
#python->prompt builder->llm call->dynamic playwright code

"""from ai_engine.llm_client import generate_from_llm
from ai_engine.prompts.ui_test_prompt import ui_test_prompt


def generate_ui_test(test_input):

    # Build AI prompt
    prompt = ui_test_prompt(test_input)

    # Send to LLM
    generated_code = generate_from_llm(prompt)

    # Return AI-generated Playwright code
    return generated_code"""