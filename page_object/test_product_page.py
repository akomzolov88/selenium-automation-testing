# 4.3.15 Финальное задание  в блоке: Применение патерна Page Object.
# Ссылка на задание: https://stepik.org/lesson/201964/step/15?unit=176022
# Ссылка на правила подготовки кода к ревью: https://stepik.org/lesson/201964/step/14?unit=176022 

# Импортируем модуль sys для работы с системными параметрами
import sys
# Импортируем модуль os для работы с функциями операционной системы
import os
# Добавляем в переменную sys.path абсолютный путь к директории page_object
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'D:/Projects/selenium-automation-testing/page_object')))

# Импортируем класс Item из файла base_page.py
from pages.product_page import Item
# Импортируем класс Login из файла login_page.py
from pages.login_page import Login
# Импортируем класс Cart из файла basket_page.py
from pages.basket_page import Cart
# Импортируем модуль time для работы со временем при помощи функции time()
import time
# Импортируем модуль pytest запуска тестов, их параметризации и маркировки
import pytest

# 4.3.2 Задание: добавление в корзину со страницы товара
class TestAddToBasket():
    # Создаём тестовый метод test_guest_can_add_product_to_basket для добавления товара в корзину и получения ответа на задачу
    def test_guest_can_add_product_to_basket(self, browser):
        # Создаём переменную link и присваиваем ей ссылку на страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Добавляем товар в корзину
        page.add_product_to_basket()
        # Получаем ответ на задачу и вводим его в поле для ответа
        page.solve_quiz_and_get_code()

# 4.3.3 Задание: независимость от данных
class TestDataIndependence():    
    # Создаём тестовый метод test_user_can_add_product_to_basket для сравнения названия и цены товара с названием и ценой в корзине и в уведомлении
    def test_user_can_add_product_to_basket(self, browser):
        # Создаём переменную link и присваиваем ей ссылку на страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Добавляем товар в корзину
        page.add_product_to_basket()
        # Проверяем наличие названия товара на странице товара
        page.should_be_product_name()
        # Проверяем наличие цены товара на странице товара
        page.should_be_product_price()
        # Проверяем наличие уведомления с названием товара
        page.should_be_succes_product_name()
        # Проверяем наличие уведомления с ценой товара
        page.should_be_succes_product_price()
        # Проверяем что название товара в уведомлении совпадает с названием товара на странице товара
        page.is_success_name_correct()
        # Проверяем что цена товара в уведомлении совпадает с ценой товара на странице товара
        page.is_success_price_correct()

# 4.3.4 Задание: независимость контента, ищем баг
class TestContentIndependenceLookingBug():
    # Испрользуя параметризацию, создаём список ссылок для поиска бага на страницах
    @pytest.mark.parametrize("link", 
        [
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
            pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
        ])
    def test_guest_can_add_product_to_basket(browser, link):
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        page.open()
        # Добавляем товар в корзину
        page.add_product_to_basket()
        # Получаем ответ на задачу и вводим его в поле для ответа
        page.solve_quiz_and_get_code()
        # Проверяем наличие названия товара на странице товара
        page.should_be_product_name()
        # Проверяем наличие цены товара на странице товара
        page.should_be_product_price()
        # Проверяем наличие уведомления с названием товара
        page.should_be_succes_product_name()
        # Проверяем наличие уведомления с ценой товара
        page.should_be_succes_product_price()
        # Проверяем что название товара в уведомлении совпадает с названием товара на странице товара
        page.is_success_name_correct()
        # Проверяем что цена товара в уведомлении совпадает с ценой товара на странице товара
        page.is_success_price_correct()

# 4.3.6 Задание: отрицательные проверки
class TestNegativeChecks():   
    @pytest.mark.xfail()
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        # Создаём переменную link и присваиваем ей ссылку на страницу товара
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Добавляем товар в корзину
        page.add_product_to_basket()
        # Проверяем что элемент с локатором alert-success не отображается
        page.should_not_be_success_product_name()
    
    # 4.3.6 Задание: отрицательные проверки
    def test_guest_cant_see_success_message(browser):
        # Создаём переменную link и присваиваем ей ссылку на страницу товара
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Проверяем что элемент с локатором alert-success не отображается
        page.should_not_be_success_product_name()

    # 4.3.6 Задание: отрицательные проверки 
    @pytest.mark.xfail()
    def test_message_disappeared_after_adding_product_to_basket(browser):
        # Создаём переменную link и присваиваем ей ссылку на страницу товара
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Добавляем товар в корзину
        page.add_product_to_basket()
        # Проверяем исчезновение элемента с локатором alert-success
        page.should_disappear_success_product_name()

# 4.3.8 Плюсы наследования: пример
class TestInheritanceExample():
    def test_guest_can_go_to_login_page(browser):
        # Создаём переменную link и присваиваем ей ссылку на главную страницу магазина
        link = 'http://selenium1py.pythonanywhere.com'
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Переходим на страницу Авторизации
        page.go_to_login_page()
        # Создаём переменную login_page и присваиваем ей объект класса LoginPage
        login = Login(browser, browser.current_url)
        # Проверяем что открылась страница авторизации
        login.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(browser):
        # Создаём переменную link и присваиваем ей ссылку на страницу товара
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Проверяем наличие ссылки на страницу авторизации
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(browser):
        # Создаём переменную link и присваиваем ей ссылку на главную страницу магазина
        link = 'http://selenium1py.pythonanywhere.com'
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Переходим на страницу Авторизации
        page.go_to_login_page()
        # Создаём переменную login_page и присваиваем ей объект класса LoginPage
        login = Login(browser, browser.current_url)
        # Проверяем что открылась страница авторизации
        login.should_be_login_page()

# 4.3.10 Задание: наследование и отрицательные проверки
class TestInheritanceAndNegativeChecks():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        # Создаём переменную link и присваиваем ей ссылку на главную страницу магазина
        link = 'http://selenium1py.pythonanywhere.com'
        # Создаём переменную page и присваиваем ей объект класса MainPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Переходим в корзину
        page.go_to_basket_page()
        # Создаём переменную basket_page и присваиваем ей объект класса BasketPage
        cart = Cart(browser, browser.current_url)
        # Проверяем что корзина пуста
        cart.should_not_be_basket_summary()
        # Проверяем что есть сообщение о том что корзина пуста
        cart.should_be_empty_basket_message()

# 4.3.13 Задание: группировка тестов и setup
class TestSetupGrouping():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Создаём переменную link и присваиваем ей ссылку на главную страницу магазина
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        # Создаём переменную page и присваиваем ей объект класса LoginPage
        page = Login(browser, link)
        # Открываем страницу
        page.open()
        # Создаём переменную email и присваиваем ей значение времени в секундах + почта
        email = str(time.time()) + "@mail.ru"
        # Создаём переменную passwd и присваиваем ей значение времени в секундах
        password = str(time.time())
        # Регистрируем нового пользователя
        page.register_new_user(email, password)
        ## Проверяем что пользователь авторизован
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Создаём переменную link и присваиваем ей ссылку на страницу товара
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Проверяем что элемент с локатором alert-success не отображается
        page.should_not_be_success_product_name()

# 4.3.14 Финишная прямая: готовим код к ревью
class TestPrepareCodeToReview():
    @pytest.mark.need_review
    # Создаём тестовый метод test_user_can_add_product_to_basket для сравнения названия и цены товара с названием и ценой в корзине и в уведомлении
    def test_user_can_add_product_to_basket(self, browser):
        # Создаём переменную link и присваиваем ей ссылку на страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Добавляем товар в корзину
        page.add_product_to_basket()
        # Проверяем наличие названия товара на странице товара
        page.should_be_product_name()
        # Проверяем наличие цены товара на странице товара
        page.should_be_product_price()
        # Проверяем наличие уведомления с названием товара
        page.should_be_succes_product_name()
        # Проверяем наличие уведомления с ценой товара
        page.should_be_succes_product_price()
        # Проверяем что название товара в уведомлении совпадает с названием товара на странице товара
        page.is_success_name_correct()
        # Проверяем что цена товара в уведомлении совпадает с ценой товара на странице товара
        page.is_success_price_correct()

    @pytest.mark.need_review
    # Испрользуя параметризацию, создаём список ссылок для поиска бага на страницах
    @pytest.mark.parametrize("link", 
        [
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
            pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
        ])
    def test_guest_can_add_product_to_basket(browser, link):
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        page.open()
        # Добавляем товар в корзину
        page.add_product_to_basket()
        # Получаем ответ на задачу и вводим его в поле для ответа
        page.solve_quiz_and_get_code()
        # Проверяем наличие названия товара на странице товара
        page.should_be_product_name()
        # Проверяем наличие цены товара на странице товара
        page.should_be_product_price()
        # Проверяем наличие уведомления с названием товара
        page.should_be_succes_product_name()
        # Проверяем наличие уведомления с ценой товара
        page.should_be_succes_product_price()
        # Проверяем что название товара в уведомлении совпадает с названием товара на странице товара
        page.is_success_name_correct()
        # Проверяем что цена товара в уведомлении совпадает с ценой товара на странице товара
        page.is_success_price_correct()

    @pytest.mark.need_review
    @pytest.mark.xfail()
    def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        # Создаём переменную link и присваиваем ей ссылку на главную страницу магазина
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Переходим в корзину
        page.add_product_to_basket()
        # Проверяем чт элемент с локатором alert-success не отображается
        page.should_not_be_success_product_name()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(browser):
        # Создаём переменную link и присваиваем ей ссылку на главную страницу магазина
        link = 'http://selenium1py.pythonanywhere.com'
        # Создаём переменную page и присваиваем ей объект класса ProductPage
        page = Item(browser, link)
        # Открываем страницу
        page.open()
        # Переходим на страницу Авторизации
        page.go_to_login_page()
        # Создаём переменную login_page и присваиваем ей объект класса LoginPage
        login = Login(browser, browser.current_url)
        # Проверяем что открылась страница авторизации
        login.should_be_login_page()
