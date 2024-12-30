# 4.3.15 Финальное задание  в блоке: Применение патерна Page Object.
# Ссылка на задание: https://stepik.org/lesson/201964/step/15?unit=176022
# Ссылка на правила подготовки кода к ревью: https://stepik.org/lesson/201964/step/14?unit=176022 

# Confest.py это файл, который содержит фикстуры, которые используются во всех остальных тестах в папке и подпапках относительно расположения этого файла
# Фикстура - это функция, которая выполняется до или после теста, и может возвращать какие-то данные, которые будут использоваться в тестах

# Импортируем модуль pytest для использования фикстур
import pytest
# Импортируем модуль webdriver из библиотеки selenium для работы с веб-драйвером
from selenium import webdriver
# Импортируем модуль Options из библиотеки selenium.webdriver.chrome.options для использования опций браузера
from selenium.webdriver.chrome.options import Options

# Создаём функцию pytest_addoption для добавления опции выбора языка браузера
def pytest_addoption(parser):
    # Добавляем опцию --language для выбора языка браузера
    parser.addoption('--language', action='store', default='ru', help='Выберите язык: en, ru, es, fr')

# Создаём фикстуру browser
# scope="function" - это фикстура, которая будет выполняться перед каждым тестом и после каждого теста
@pytest.fixture(scope="function")
# Создаём функцию browser с параметром request для запуска браузера с выбранным языком
def browser(request):
    # Создаём переменную options и инициализируем в ней объект Options()
    # Options() - это класс, который позволяет добавить опции для запуска браузера Chrome
    options = Options()
    # Создаём перемнную language и присваиваем ей значение request.config.getoption("language")
    # request.config.getoption("language") - это метод, который возвращает значение языка, который был выбран при запуске теста
    language = request.config.getoption("language")
    # Добавляем опции для выбора языка при помощи метода add_experimental_option
    # prefs - это словарь, который содержит настройки для браузера
    # При помощи ключа 'intl.accept_languages' и значения language мы выбираем язык браузера укзанный при запуске теста командой, например pytest --language=en
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # Создаём переменную Browser и инициализируем в ней объект webdriver.Chrome с параметром options=options для запуска браузера Chrome с опциями
    browser = webdriver.Chrome(options=options)
    # Возвращаем результат работы функции browser
    yield browser
    # Закрываем браузер после окончания работы теста
    browser.quit()
