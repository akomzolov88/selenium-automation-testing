# 4.3.15 Финальное задание  в блоке: Применение патерна Page Object.
# Ссылка на задание: https://stepik.org/lesson/201964/step/15?unit=176022
# Ссылка на правила подготовки кода к ревью: https://stepik.org/lesson/201964/step/14?unit=176022 

# Импортируем модуль sys для работы с системными параметрами
import sys
# Импортируем модуль os для работы с функциями операционной системы
import os
# Добавляем в переменную sys.path абсолютный путь к директории page_object
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'D:/Projects/selenium-automation-testing/page_object')))

# Импортируем модуль sys для работы с системными параметрами
import sys
# Импортируем модуль os для работы с функциями операционной системы
import os
# Добавляем в переменную sys.path абсолютный путь к директории page_object
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'D:/Projects/selenium-automation-testing/page_object')))

# Импортируем класс BasePage из файла base_page.py
from pages.main_page import MainPage
# Импортируем класс LoginPage из файла login_page.py
from pages.login_page import LoginPage
# Импортируем класс CartPage из файла basket_page.py
from pages.basket_page import CartPage
# Импортируем модуль pytest запуска тестов, их параметризации и маркировки
import pytest

@pytest.mark.ineheritance_and_negative_checks
class TestInheritanceAndNegativeChecks():
    # 4.3.10 Задание: наследование и отрицательные проверки
    # Создаём тестовый метод test_guest_cant_see_product_in_basket_opened_from_main_page для проверки что у гостя пустая корзина
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Создаём переменную link и присваиваем ей ссылку на главную страницу магазина
        link = 'http://selenium1py.pythonanywhere.com'
        # Создаём переменную page и присваиваем ей объект класса MainPage
        page = MainPage(browser, link)
        # Открываем страницу
        page.open()
        # Переходим в корзину
        page.go_to_cart_page()
        # Создаём переменную basket_page и присваиваем ей объект класса BasketPage
        cart = CartPage(browser, browser.current_url)
        # Проверяем что корзина пуста
        cart.should_not_be_basket_summary()
        # Проверяем что есть сообщение о том что корзина пуста
        cart.should_be_empty_basket_message()

# 4.3.11 Группировка тестов: setup 
@pytest.mark.login_guest
class TestLoginFromMainPage():
    # Создаём тестовый метод test_guest_can_go_to_login_page для проверки что гость может перейти на страницу авторизации
    def test_guest_can_go_to_login_page(self, browser):
        # Создаём переменную link и присваиваем ей ссылку на главную страницу магазина
        link = 'http://selenium1py.pythonanywhere.com'
        # Создаём переменную page и присваиваем ей объект класса MainPage
        page = MainPage(browser, link)
        # Открываем страницу
        page.open()
        # Переходим на страницу Авторизации
        page.go_to_login_page()
        # Создаём переменную login_page и присваиваем ей объект класса LoginPage
        login = LoginPage(browser, browser.current_url)
        # Проверяем что открылась страница авторизации
        login .should_be_login_page()

    # Создаём тестовый метод test_guest_should_see_login_link для проверки что у гостя есть ссылка на страницу авторизации
    def test_guest_should_see_login_link(self, browser):
        # Создаём переменную link и присваиваем ей ссылку на главную страницу магазина
        link ='http://selenium1py.pythonanywhere.com'
        # Создаём переменную page и присваиваем ей объект класса MainPage
        page = MainPage(browser, link)
        # Открываем страницу
        page.open()
        # Проверяем что есть ссылка на страницу авторизации
        page.should_be_login_link()
