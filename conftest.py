pytest_plugins = [
    "fixtures.browser_fixture"  # loads playwright
]

# Allure + screenshot hook...
import os
import pytest
import allure

from datetime import datetime


pytest_plugins = [
    "fixtures.browser_fixture"
]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Only trigger on actual test execution failures
    if report.when == "call" and report.failed:

        # Get Playwright page fixture
        page = item.funcargs.get("page")

        if page:

            # Ensure screenshot directory exists
            os.makedirs("reports/screenshots", exist_ok=True)

            # Timestamp for uniqueness
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_path = (
                f"reports/screenshots/"
                f"{item.name}_{timestamp}.png"
            )

            # Capture screenshot
            page.screenshot(path=screenshot_path)

            # Attach to Allure report
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )