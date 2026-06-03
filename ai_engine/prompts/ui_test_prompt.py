def ui_test_prompt(test_input):
    story = test_input.get("story")
    system = test_input.get("system", "web application")

    return f"""
Generate a Playwright UI automation test in Python using pytest.

Application:
{system}

Scenario:
{story}

Requirements:
- Use Playwright sync API
- Use pytest structure
- Include browser/page fixture
- Use reliable selectors
- Add assertions
- Use best practices
- Generate executable code only
- No explanations
- No markdown

Target Site:
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Valid credentials:
Username: Admin
Password: admin123

Expected outcome:
User successfully logs in and Dashboard is visible.
"""