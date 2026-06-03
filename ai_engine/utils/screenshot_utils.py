import os
import allure

from datetime import datetime


def attach_screenshot(page, step_name):

    os.makedirs("reports/screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    path = f"reports/screenshots/{step_name}_{timestamp}.png"

    page.screenshot(path=path)

    allure.attach.file(
        path,
        name=step_name,
        attachment_type=allure.attachment_type.PNG
    )