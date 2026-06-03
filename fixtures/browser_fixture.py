import os
import pytest

from playwright.sync_api import sync_playwright

# This code has debugging capability to trace records:
"""DOM state
* clicks
* selectors
* screenshots
* network calls
* timing
* console
* assertions"""

@pytest.fixture
def page():

    # ---------------------------------
    # CREATE TRACE FOLDER
    # ---------------------------------

    os.makedirs("reports/traces", exist_ok=True)

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        context = browser.new_context(
            viewport={
                "width": 1920,
                "height": 1080
            }
        )

        # ---------------------------------
        # START PLAYWRIGHT TRACE
        # ---------------------------------

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        # ---------------------------------
        # TEST EXECUTION
        # ---------------------------------

        yield page

        # ---------------------------------
        # WAIT FOR FINAL UI STABILIZATION
        # ---------------------------------

        page.wait_for_timeout(2000)

        # ---------------------------------
        # SAVE TRACE
        # ---------------------------------

        context.tracing.stop(
            path="reports/traces/trace.zip"
        )

        # ---------------------------------
        # CLEANUP
        # ---------------------------------

        context.close()

        browser.close()

