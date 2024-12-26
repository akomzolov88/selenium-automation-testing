import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# Функция для запуска с нужным языком
def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru", help="Выберите свой язык для браузера")

# Фикстура для запуска браузера с указанным языком
@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"\nЗапустить браузер для тестирования с использованием языка: {language}..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print(f"\nВыход из браузера..")
    browser.quit()