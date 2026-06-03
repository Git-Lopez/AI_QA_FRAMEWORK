
from playwright.sync_api import Page


def test_generated_ui(page: Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    actual_title = page.title()
    expected_title = "OrangeHRM"

    assert actual_title == expected_title, (
        f"Expected '{expected_title}' but got '{actual_title}'"
    )
