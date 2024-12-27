import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Language for the browser")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('pref', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()