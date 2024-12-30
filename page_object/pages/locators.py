# 4.3.15 Финальное задание  в блоке: Применение патерна Page Object.
# Ссылка на задание: https://stepik.org/lesson/201964/step/15?unit=176022
# Ссылка на правила подготовки кода к ревью: https://stepik.org/lesson/201964/step/14?unit=176022 

# Импортируем модуль sys для работы с системными параметрами
import sys
# Импортируем модуль os для работы с функциями операционной системы
import os
# Добавляем в переменную sys.path абсолютный путь к директории page_object
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'D:/Projects/selenium-automation-testing/page_object')))

# Импортируем класс By из модуля selenium.webdriver.common.by для работы с CSS-селекторами
from selenium.webdriver.common.by import By

# Создаём класс BaseLocators для хранения локаторов элементов главной страницы
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    CART_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")

# Создаём класс ItemPageLocators для хранения локаторов элементов страницы товара
class ItemPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE_ITEM_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE_ITEM_PRICE = (By.CSS_SELECTOR, ".alert-info strong")

# Создаём класс LoginPageLocators для хранения локаторов элементов страницы авторизации и регистрации пользователя
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name=registration-email]")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "[name=registration-password1]")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "[name=registration-password2]")
    REGISTER_BUTTON_SUBMIT = (By.CSS_SELECTOR, "[name=registration_submit]")

# Создаём класс CartPageLocators для хранения локаторов элементов страницы корзины
class CartPageLocators():
    CART_SUMMARY = (By.CSS_SELECTOR, '.basket_summary')
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    