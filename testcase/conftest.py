import pytest
from selenium import webdriver


# --- Command-line option for browser ---
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")


# --- Browser fixture to read CLI option ---
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# --- WebDriver fixture with setup and teardown ---
@pytest.fixture()
def setup(browser):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser.lower() == 'ie':
        driver = webdriver.Ie()
        print("Launching IE browser")
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver  # Provide the driver to the test

    print("Closing browser")
    driver.quit()


# conftest.py
def pytest_html_report_title(report):
    report.title = "Selenium Test Report"
