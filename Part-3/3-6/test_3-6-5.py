# 3.6.5 Задание: параметризация тестов
# Ссылка на задание: https://stepik.org/lesson/237240/step/5?unit=209628

# Импортируем модуль webdriver для взаимодействия с веб-страницами из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By для использования селекторов
from selenium.webdriver.common.by import By
# Импортируем модуль WebDriverWait из библиотеки selenium.webdriver.support.ui
# Модуль WebDriverWait предоставляет все необходимые методы для ожидания элементов
from selenium.webdriver.support.ui import WebDriverWait
# Импортируем модуль expected_conditions из библиотеки selenium.webdriver.support
# Модуль expected_conditions предоставляет все необходимые методы для ожидания определенных условий
from selenium.webdriver.support import expected_conditions as EC
# Импортируем модуль time для работы со временем при помощи метода sleep
import time
# Импортируем модуль math для работы с математическими функциями
import math
# Импортируем модуль pytest
# Pytest - это фреймворк для написания тестов на языке программирования Python
import pytest

# Создаём переменную, которая будет хранить список ссылок на тестируемые страницы
linksList = [
    'https://stepik.org/lesson/236895/step/1', 
    'https://stepik.org/lesson/236896/step/1', 
    'https://stepik.org/lesson/236897/step/1', 
    'https://stepik.org/lesson/236898/step/1', 
    'https://stepik.org/lesson/236899/step/1', 
    'https://stepik.org/lesson/236903/step/1', 
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]

# Создаём функцию для получения числа (используется в поле "Ответ")
def answer():
    # возвращаем логарифм от текущего времени
    return str(math.log(int(time.time())))

# Создаём фикстуру browser
# Фикстура - это функция, которая выполняется перед каждым тестом и после каждого теста
@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

# Создаём функцию Login для авторизации на сайте
# В качестве параметра передаём переменную browser, которая хранит веб-драйвер
def login(browser):
    # Передаём ссылку на страницу при помощи метода get
    browser.get("https://stepik.org/login")
    # Ожидаем, что поле для ввода email будет доступно для взаимодеявия
    # Параметры: browser - переменная, которая хранит веб-драйвер, 20 - время ожидания
    # Параметры: EC.element_to_be_clickable((By.ID, "id_login_email")) - ожидание элемента, который будет доступен для взаимодействия
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "id_login_email")))

    # Ищем поле для ввода email при помощи метода find_elemnt по ID и передаём в него значение пользовательского ввода
    # Вместо xxx необходимо указать свой email для авторизации на сайте Stepik
    browser.find_element(By.ID, "id_login_email").send_keys("xxx")
    # Ищем поле для ввода пароля при помощи метода find_elemnt по ID и передаём в него значение пользовательского ввода
    # Вместо xxx необходимо указать свой пароль для авторизации на сайте Stepik
    browser.find_element(By.ID, "id_login_password").send_keys("xxx")
    # Ищем кнопку длл отправки данных и авторизации пользователя при помощи метода find_element по CSS-селектору и кликаем на неё
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # Добавляем паузу в 5 секунд для того, чтобы авторизация пользовтеля завершилась успешно, так как без ожидания авторизация не срабатывает
    time.sleep(5)

# Создаём класс TestLinks в котором будут храниться тесты
class TestLinks():
    # Отмечаем тест как параметризованный
    # Парамтризованный тест - это тест, который запускается несколько раз с разными входными данными.
    # В данном случае в параметре @pytest.mark.parametrize указываем, что тест test_links будет запускаться с разными ссылками из списка linksList
    @pytest.mark.parametrize('link', linksList)
    # Создаём тест test_links
    # Название теста должно начинаться с test_
    def test_links(self, browser, link):
        # Вызываем функцию Login для авторизации на сайте
        login(browser)
        # После успешной авторизации передаём ссылку на тестируемую страницу при помощи метода get
        browser.get(link)
        # Ожидаем, что поле для ввода ответа будет доступно для взаимодействия
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
         # Ищем поле для ввода ответа при помощи метода find_element по CSS-селектору
        textarea = browser.find_element(By.CSS_SELECTOR, "textarea")
        #  Передаём в поле для ввода ответа результат выполнения функции answer()
        textarea.send_keys(answer())
        # Ищем кнопку для отправки ответа при помощи метода find_element по CSS-селектору
        button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        # Кликаем на кнопку для отправки ответа
        button.click()
        # Ожидаем, что элемент с подсказкой будет доступен для взаимодействия
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint")))
        # Ищем элемент с подсказкой при помощи метода find_element по CSS-селектору
        feedback = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
        # Ниже при помощи функции text в переменной feedback проверяем, что в тексте подсказки содержится слово "Correct!"
        assert "Correct!" in feedback.text