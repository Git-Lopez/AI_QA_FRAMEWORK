import os

from ai_engine.generators.feature_generator import generate_feature
from ai_engine.generators.step_generator import generate_steps
from ai_engine.generators.ui_test_generator import generate_ui_test
from ai_engine.utils.file_writer import write_file as save_file  # 👈 ADD THIS LINE


def run_llm_test_generation(test_input):
    # Extract story (works for both modes)
    story = test_input.get("story")

    # Generate content
    feature = generate_feature(test_input)
    steps = generate_steps(test_input)
    ui_test = generate_ui_test(test_input)

    # File naming
    file_name = story.lower().replace(" ", "_").replace("?", "").replace("/", "_")

    # Paths
    feature_path = f"tests/features/{file_name}.feature"
    steps_path = f"tests/step_defs/test_{file_name}_steps.py"
    ui_path = f"tests/ui/test_{file_name}.py"

    # Save
    save_file(feature_path, feature)
    save_file(steps_path, steps)
    save_file(ui_path, ui_test)

    return {
        "feature_file": feature_path,
        "steps_file": steps_path,
        "ui_test_file": ui_path
    }

# Future orchestrator.py
# we will use the below code when jira is integrated :
"""from ai_engine.generators.feature_generator import generate_feature
from ai_engine.generators.step_generator import generate_steps
from ai_engine.generators.ui_test_generator import generate_ui_test

from ai_engine.file_writer import write_file


def run_llm_test_generation(test_input):

    # Universal normalized model
    story = test_input.get("story")

    # Generate assets
    feature = generate_feature(test_input)
    steps = generate_steps(test_input)
    ui_test = generate_ui_test(test_input)

    # Dynamic naming
    file_name = (
        story.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("?", "")
    )

    # Paths
    feature_path = f"tests/features/{file_name}.feature"
    steps_path = f"tests/step_defs/test_{file_name}_steps.py"
    ui_path = f"tests/ui/test_{file_name}.py"

    # Save assets
    write_file(feature_path, feature)
    write_file(steps_path, steps)
    write_file(ui_path, ui_test)

    return {
        "feature_file": feature_path,
        "steps_file": steps_path,
        "ui_test_file": ui_path
    }"""
