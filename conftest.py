import os
import pytest
from selenium import webdriver

SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture(scope="function")
def driver(request):
    """Fixture to initialize and close Chrome WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    request.node.driver = driver
    
    yield driver
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshot on failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            screenshot_path = os.path.join(SCREENSHOT_DIR, f"{item.name}_failure.png")
            driver.save_screenshot(screenshot_path)