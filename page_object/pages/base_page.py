# 4.3.15 Финальное задание  в блоке: Применение патерна Page Object.
# Ссылка на задание: https://stepik.org/lesson/201964/step/15?unit=176022
# Ссылка на правила подготовки кода к ревью: https://stepik.org/lesson/201964/step/14?unit=176022 

# В BasePage находится реализация поиска элементов на странице, а также методы для открытия страницы.

# Page Object (Page Object Model, POM) — это паттерн проектирования, используемый в автоматизации тестирования веб-приложений. 
# Он помогает сделать тесты более читаемыми, поддерживаемыми и повторно используемыми.
'''
Основные идеи Page Object:
1. Разделение логики тестов и логики взаимодействия с веб-страницами:
- Логика взаимодействия с элементами страницы (нажатие кнопок, ввод текста и т.д.) инкапсулируется в классах, представляющих страницы.
- Логика тестов остается в тестовых методах, которые используют эти классы.

2. Классы для каждой страницы:
- Каждая веб-страница представлена отдельным классом.
- Методы класса реализуют действия, которые можно выполнить на странице (например, login, add_to_cart).

3. Локаторы элементов:
- Локаторы элементов страницы хранятся в классе или отдельном файле, что упрощает их изменение.

Page Object Model помогает сделать тесты более структурированными и легкими в поддержке.
'''

# Импортируем модуль sys для работы с системными параметрами
import sys
# Импортируем модуль os для работы с функциями операционной системы
import os
# Добавляем в переменную sys.path абсолютный путь к директории page_object
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'D:/Projects/selenium-automation-testing/page_object')))

# Импортируем класс BasePageLocators из файла Locators.py
from pages.locators import BasePageLocators
# Импортируем класс WebDriverWait из модуля selenium.webdriver.support.ui
# Класс WebDriverWait используется для ожидания повяления элементов на странице
from selenium.webdriver.support.ui import WebDriverWait
# Импортируем класс expected_conditions из модуля selenium.webdriver.support для работы с таймаутами
from selenium.webdriver.support import expected_conditions as EC
# Импортируем класс TimeoutException из модуля selenium.common.exceptions
# Класс TimeoutException используется для обработки исключений, возникающих при работе с таймаутами
from selenium.common.exceptions import TimeoutException
# Импортируем класс NoSuchElementException из модуля selenium.common.exceptions для обработки исключений связанных с отсутствием элементов на странице
from selenium.common.exceptions import NoSuchElementException
# Импортируем класс NoAlertPresentException из модуля selenium.common.exceptions для обработки исключений связанных с отсутствием всплывающих окон
from selenium.common.exceptions import NoAlertPresentException
# Импортируем модуль math для работы с математическими функциями
import math

# Создаём класс BasePage для работы с методами, которые будут использоваться в других классах при помощи наследования (импорта)
class BasePage():
    # Создаём конструктор класса BasePage
    def __init__(self, browser, url, timeout=10):
        # Инициализируем атрибуты класса BasePage
        self.browser = browser
        # Присваиваем атрибуту url переданное значение
        self.url = url
        # Устанавливаем неявное ожидание для поиска элементов на странице
        self.browser.implicitly_wait(timeout)

    '''
    Страница Авторизации пользователя
    '''

    # Создаём метод go_to_login_page для перехода на страницу авторизации пользователя
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # Создаём метод should_be_login_link для проверки наличия ссылки на страницу авторизации
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка на страницу авторизации пользователя не найдена"    

    # Создаём метод should_be_authorized_user для проверки залогинен пользователь или нет
    # В данной проверке мы ищем элемент с локатором USER_ICON на странице, если его нет, то пользователь не авторизован
    def should_be_authorized_user(self):
        # Проверяем, что элемент присутсвует на странице
        assert self.is_element_present(*BasePageLocators.USER_ICON), "Значок пользователя не отображается"

    '''
    Страница Корзины товаров
    '''

    # Создаём метод go_to_cart_page для прехода на страницу корзины
    def go_to_cart_page(self):
        button = self.browser.find_element(*BasePageLocators.CART_BUTTON)
        button.click()

    # Создаём метод should_be_basket_button для проверки наличия кнопки корзины на странице
    # В данной проверке мы ищем жлемент с локатором BASKET_BUTTON на странице, если его нет, то кнопка корзины не отображается
    def should_be_basket_button(self):
        # Проверяем, что элемент присутсвует на странице
        assert self.is_element_present(*BasePageLocators.CART_BUTTON), "Кнопка корзины не отображается"

    '''
    Общие методы для работы с веб-страницей
    '''

    # Создаём метод open для открытия веб-страницы
    def open(self):
        # Открываем страницу по ссылке, которая хранится в атрибуте url передавая его в метод get
        self.browser.get(self.url)

    # Создаём метод is_element_present для проверки наличия элемента на странице
    # Параметр self необходим для обращения к атрибутам и методам класса BasePage
    # Параметры how и what передаются в метод find_element для поиска элемента на странице при помощи селектора
    def is_element_present(self, how, what):
        try:
            # Ищем элемент на странице
            self.browser.find_element(how, what)
        # Если элемент не найден, то возникает исключение NoSuchElementException
        except NoSuchElementException:
            # Возвращаем False, если элемент не найден
            return False
        # Возвращаем True, если элемент найден
        return True

    # Создаём метод is_disappeared для проверки исчезновения элемента со страницы
    # Параметр self необходим для обращения к атрибутам и методам класса BasePage
    # Параметры how и what передаются в метод find_element для поиска элемента на странице при помощи селектора 
    # Параметр timeout устанавливает время ожидания элемента на странице
    def is_disappeared(self, how, what, timeout=10):
        try:
            # Ожидаем исчезновения элемента на странице используя метод unit_not
            WebDriverWait(self.browser, timeout, 5, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        # Если элемент не исчезает, то возникает исключение TimeoutException
        except TimeoutException:
            # Возвращаем False, если элемент не исчез
            return False
        # Возвращаем True, если элемент исчез
        return True

    # Создаём метод is_not_element_present для проверки отсутствия элемента на странице
    # Параметр self необходим для обращения к атрибутам и методам класса BasePage
    # Параметры how и what передаются в метод find_element для поиска элемента на странице при помощи селектора 
    # Параметр timeout устанавливает время ожидания элемента на странице
    def is_not_element_present(self, how, what, timeout=5):
        try:
            # Ожидаем отсутствия элемента на странице используя метод until
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        # Если элемент отсутствует, то возникает исключение TimeoutException
        except TimeoutException:
            # Возвращаем True, если элемент отсутствует
            return True
        # Возвращаем False, если элемент присутствует
        return False

    # Создаём метод solve_quiz_and_get_code для решения математической задачи и получения "кода"
    def solve_quiz_and_get_code(self):
        # Создаём переменную alert для хранения всплывающего окна
        alert = self.browser.switch_to.alert
        # Создаём переменную x для хранения значения из всплывающего окна
        x = alert.text.split(" ")[2]
        # Создаём переменную answer для хранения ответа на математическую задачу
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        # Передаём ответ во всплывающее окно
        alert.send_keys(answer)
        # Закрываем всплывающее окно
        alert.accept()
        try:
            # Создаём переменную alert для хранения всплывающего окна
            alert = self.browser.switch_to.alert
            # Создаём переменную alert_text для хранения текста из всплывающего окна
            alert_text = alert.text
            # Выводим в консоль "код" из всплывающего окна
            print(f"Ваш код: {alert_text}")
            # Закрываем всплывающее окно
            alert.accept()
        # Если всплывающее окно не найдено, то возникает исключение NoAlertPresentException
        except NoAlertPresentException:
            # Выводим в консоль текст "Нет окна..."
            print("Нет окна для отправки ответа")