def feature_prompt(test_input):
    story = test_input.get("story")
    feature = test_input.get("feature", "General Feature")
    tags = test_input.get("tags", [])

    tag_string = " ".join([f"@{tag}" for tag in tags])

    return f"""
Generate a professional Gherkin feature file.

Requirements:
- Use proper BDD syntax
- Include Feature, Scenario, Given, When, Then
- Add regression tags
- Keep steps reusable
- Use concise business language

Feature Name:
{feature}

User Story:
{story}

Tags:
{tag_string}

Output only valid Gherkin.
"""