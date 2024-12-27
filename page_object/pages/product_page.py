import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'D:/Projects/selenium-automation-testing/page_object')))
import math

from pages.base_page import BasePageTest
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ProductPageTest(BasePageTest):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()

    def should_not_be_success_item_name(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ITEM_NAME), \
        "Отображается сообщение об успешном завершении, но его не должно быть"

    def should_disappear_success_item_name(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ITEM_NAME), \
        "Отображается  сообщение об успешном завершении, но оно должно исчезнуть"

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), \
        "На странице товара нет кнопки 'добавить в корзину'."
    
    def should_be_succes_item_price(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ITEM_PRICE), \
        "На странице товара нет уведомления о цене товара"
    
    def should_be_succes_item_name(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ITEM_NAME), \
        "На странице товара отсутствует уведомление о названии товара"

    def should_be_item_price(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), \
        "Цена товара не указана на странице товара"

    def should_be_item_name(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), \
        "Название продукта отсутствует на странице товара"

    def get_item_price(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def get_item_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def get_success_item_price(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_ITEM_PRICE).text

    def get_success_item_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_ITEM_NAME).text
    
    def is_success_name_correct(self):
        assert self.get_product_name() == self.get_success_product_name(), \
        "Названия добавленного товара и название товара не совпадают"
    
    def is_success_price_correct(self):
        self.get_product_price() == self.get_success_product_price(), \
        "Цена добавленного товара и товара не совпадают"
       
    def solve_quiz_and_get_code(self):
        import math
        def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))
        x_element = self.browser.find_element(*ProductPageLocators.X)
        x = x_element.text
        y = calc(x)
        input_field = self.browser.find_element(*ProductPageLocators.INPUT_FIELD)
        input_field.send_keys(y)
        submit_button = self.browser.find_element(*ProductPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")