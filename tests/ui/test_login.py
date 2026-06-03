
from pages.login_page import LoginPage
from config.settings import USERNAME, PASSWORD


def test_login(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(USERNAME, PASSWORD)

    actual_result = login_page.is_dashboard_visible()

    assert actual_result is True, (
        f"""
Expected Result:
Dashboard should be visible after successful login.

Actual Result:
Dashboard visible = {actual_result}

Test Data:
Username = {USERNAME}
"""
    )