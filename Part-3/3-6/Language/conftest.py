# Confest.py это файл, который содержит фикстуры, которые используются во всех остальных тестах в папке и подпапках относительно расположения этого файла
# Фикстура - это функция, которая выполняется до или после теста, и может возвращать какие-то данные, которые будут использоваться в тестах

# Импортируем модуль pytest для использования фикстур
import pytest
# Импортируем модуль webdriver из библиотеки selenium для работы с веб-драйвером
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common.by для использования селекторов
from selenium.webdriver.common.by import By

# Cоздаём фикстуру browser
# scope="function" - это фикстура, которая будет выполняться перед каждым тестом и после каждого теста
@pytest.fixture(scope="function")
# Создаём функцию browser
def browser():
    # Выводим соббщение в консоль "Запуска браузера для теста.."
    print("\nstart browser for test..")
    # Создаём переменную Browser и присваиваем ей значение webdriver.chrome() для запуска браузера Google Chrome
    browser = webdriver.Chrome()
    # yield - это ключевое слово, которое возвращает значение переменной browser после выполнения теста
    yield browser
    # выводим сообщение в консоль "Закрытие браузера.."
    print("\nquit browser..")
    # Закрываем браузер при помощи метода quit()
    browser.quit()

# Создаём функцию pytest_addoption для добавления опции выбора языка браузера
# parser - это объект, который содержит методы для добавления опций командной строки и их парсинга
# Для запуска теста с указанным языком необходимо ввести команду pytest --language=ru, где ru - это язык браузера (по умолчанию ru)
# Для запуска на испанском команда в терминале будет выглядеть так: pytest --lanhuage=es
def pytest_addoption(parser):
    # Добавляем опцию --language для выбора языка браузера
    parser.addoption("--language", action="store", default="ru", help="Выберите свой язык для браузера")

# Создаём фикстуру browser с параметром request для запуска браузера с выбранным языком
@pytest.fixture(scope="function")
# Создаём функцию browser с параметром request
def browser(request):
    # Создаём перемнную language и присваиваем ей значение request.config.getoption("language")
    # request.config.getoption("language") - это метод, который возвращает значение языка, который был выбран при запуске теста
    language = request.config.getoption("language")
    # Выводим сообщение в консоль о запуске браузера с выбранным языком
    print(f"\nЗапустить браузер для тестирования с использованием языка: {language}..")
    # Создаём переменную options и присваиваем ей значение webdrver.ChromeOptions()
    # Данная переменная позволяет добавить опции для запуска браузера Chrome
    options = webdriver.ChromeOptions()
    # Добавляем опции для выбора языка при помощи метода add_experimental_option
    # prefs - это словарь, который содержит настройки для браузера
    # При помощи ключа 'intl.accept_languages' и значения language мы выбираем язык браузера укзанный при запуске теста командой, например pytest --language=en
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # Создаём переменную browser и присваиваем ей значение webdriver.Chrome(options=options) для запуска браузера Google Chrome с выбранными настройками
    browser = webdriver.Chrome(options=options)
    # yield - это ключевое слово, которое возвращает значение переменной browser после выполнения теста
    yield browser
    # выводим сообщение в консоль "Выход из браузера.." после выполнения теста
    print(f"\nВыход из браузера..")
    # Закрываем браузер при помощи метода quit()
    browser.quit()