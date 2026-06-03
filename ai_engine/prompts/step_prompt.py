def step_prompt(test_input):
    story = test_input.get("story")

    return f"""
Generate pytest-bdd step definitions in Python.

Requirements:
- Use pytest-bdd decorators
- Use reusable step methods
- Keep implementation clean
- Add Playwright page parameter where appropriate
- Use assertions
- Output only Python code

Scenario:
{story}
"""