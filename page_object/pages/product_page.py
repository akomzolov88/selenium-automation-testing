# 4.3.15 Финальное задание  в блоке: Применение патерна Page Object.
# Ссылка на задание: https://stepik.org/lesson/201964/step/15?unit=176022
# Ссылка на правила подготовки кода к ревью: https://stepik.org/lesson/201964/step/14?unit=176022 

# Импортируем модуль sys для работы с системными параметрами
import sys
# Импортируем модуль os для работы с функциями операционной системы
import os
# Добавляем в переменную sys.path абсолютный путь к директории page_object
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'D:/Projects/selenium-automation-testing/page_object')))

# Импортируем класс BasePage из файла base_page.py
from pages.base_page import BasePage
# Импортируем класс ProductPageLocators из файла locators.py для использования локаторов страницы товара
from pages.locators import ItemPageLocators

# Создаём класс ProductPage, который наследует класс BasePage
class Item(BasePage):
    # Создаём метод add_product_to_basket для добавления товара в корзину
    def add_product_to_basket(self):
        # Создаём переменную add_button и присваиваем ей элемент кнопки добавления товара в корзину указывая локатор кнопки
        add_button = self.browser.find_element(*ItemPageLocators.ADD_TO_CART_BUTTON)
        # Нажимаем на кнопку добавления товара в корзину
        add_button.click()

    # Создаём метод should_be_product_name для проверки наличия названия товара на странице товара
    def should_be_product_name(self):
        assert self.is_element_present(*ItemPageLocators.ITEM_NAME), "Название товара не отображается на странице товара"

    # Создаём метод should_be_product_price для проверки наличия цены товара на странице товара
    def should_be_product_price(self):
        assert self.is_element_present(*ItemPageLocators.ITEM_PRICE), "Цена товара не отображается на странице товара"    

    # Создаём метод should_be_add_to_basket_button для проверки наличия кнопки добавления товара в корзину
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ItemPageLocators.ADD_TO_CART_BUTTON), "На странице товара нет кнопки 'добавить в корзину'."
    
    # Создаём метод should_be_succes_product_price для проверки оповещения с общей стоимостью товров в корзине
    def should_be_succes_product_price(self):
        assert self.is_element_present(*ItemPageLocators.SUCCESS_MESSAGE_ITEM_PRICE), "На странице товара нет уведомления с общей стоимостью товров в корзине"
    
    # Создаём метод should_not_be_success_product_name для проверки что элемент с локатором alert-success не отображается
    def should_not_be_success_product_name(self):
        assert self.is_not_element_present(*ItemPageLocators.SUCCESS_MESSAGE_ITEM_NAME), "alert-success отображается, но не должен"

    # Создаём метод should_disappear_success_product_name для проверки исчезновения элемента с локатором alert-success
    def should_disappear_success_product_name(self):
        assert self.is_disappeared(*ItemPageLocators.SUCCESS_MESSAGE_ITEM_NAME), "alert-success отображается, но должно было исчезнуть"

    # Создаём метод should_be_succes_product_name для проверки наличия элемента с локатором alert-success
    def should_be_succes_product_name(self):
        assert self.is_element_present(*ItemPageLocators.SUCCESS_MESSAGE_ITEM_NAME), "alert-success не отображается"

    # Создаём метод get_product_price для получения цены товара
    def get_product_price(self):
        return self.browser.find_element(*ItemPageLocators.ITEM_PRICE).text

    # Создаём метод get_product_name для получения названия товара
    def get_product_name(self):
        return self.browser.find_element(*ItemPageLocators.ITEM_NAME).text

    # Создаём метод get_success_product_price для получения цены из уведомления с общей стоимостью товаров в корзине
    def get_success_product_price(self):
        return self.browser.find_element(*ItemPageLocators.SUCCESS_MESSAGE_ITEM_PRICE).text

    # Создаём метод get_success_product_name для получения текста из элемепнта с локатором alert-success
    def get_success_product_name(self):
        return self.browser.find_element(*ItemPageLocators.SUCCESS_MESSAGE_ITEM_NAME).text
    
    # Создаём метод is_success_name_correct для проверки соответствия названия товара и названия товара в уведомлении о добавлении в корзину
    def is_success_name_correct(self):
        assert self.get_product_name() == self.get_success_product_name(), "Названия добавляемого товара и товара в уведомлении о добавлении в корзину не совпадают"
    
    # Создаём метод is_success_price_correct для проверки соотвествия цены товара и цены товара в уведомлении с общей стоимостью товаров в корзине
    def is_success_price_correct(self):
        self.get_product_price() == self.get_success_product_price(), "Цена добавленного товара и цена товара в уведомлении с общей стоимостью корзины не совпадает"
