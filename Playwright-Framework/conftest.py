import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    # Manual start to ensure driver stays alive for the failure hook
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=True) # Change to False to see the browser locally
    context = browser.new_context()
    page = context.new_page()
    
    yield page
    
    browser.close()
    pw.stop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            page.screenshot(path=f"screenshots/{item.name}.png")