import allure

from ai_engine.utils.screenshot_utils import attach_screenshot
class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):

        with allure.step("Navigate to OrangeHRM login page"):

            self.page.goto(
                "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
            )

            attach_screenshot(self.page, "navigate_to_login")

    def login(self, username, password):

        with allure.step(f"Enter username: {username}"):

            self.page.fill('input[name="username"]', username)

            attach_screenshot(self.page, "username_entered")

        with allure.step("Enter password"):

            self.page.fill('input[name="password"]', password)

            attach_screenshot(self.page, "password_entered")

        with allure.step("Click Login button"):

            self.page.click('button[type="submit"]')

            attach_screenshot(self.page, "after_login_click")

    def is_dashboard_visible(self):

        with allure.step("Verify dashboard visibility"):

            attach_screenshot(self.page, "dashboard_validation")

            return self.page.locator("h6").inner_text() == "Dashboard"