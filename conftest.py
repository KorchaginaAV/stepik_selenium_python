import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Choose language browser"
    )
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        chr_options = ChromeOptions()
        chr_options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )
        chr_options.add_argument('headless')
        chr_options.add_argument('window-size=1920x935')
        browser = webdriver.Chrome(options=chr_options)
    elif browser_name == "firefox":
        fp_options = FirefoxOptions()
        fp_options.set_preference("intl.accept_languages", user_language)
        fp_options.add_argument('headless')
        fp_options.add_argument('window-size=1920x935')
        browser = webdriver.Firefox(options=fp_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
