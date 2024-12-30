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
from base_page import BasePage
# Импортируем класс CartPageLocators из файла locators.py для использования локаторов
from locators import CartPageLocators

# Создаём класс BasketPage, который наследует класс BasePage
class Cart(BasePage):
    # Создаём метод should_not_be_basket_summary для проверки что корзина пустая
    def should_not_be_basket_summary(self):
        # Проверяем, что элемент с локатором BASKET_SUMMARY не присутсвует на странице
        assert self.is_not_element_present(*CartPageLocators.CART_SUMMARY), "Корзина должна быть пустой"

    # Создаём метод should_be_empty_basket_message для проверки наличия сообщения о пустой корзине
    def should_be_empty_basket_message(self):
        # Cоздаём переменную cart_expected_message и храним в ней ожидаемое сообщение о пустой корзине
        cart_expected_message = "Ваша корзина пуста Продолжить покупки"
        # Проверяем, что элемент с локатором EMPTY_MESSAGE присутсвует на странице
        assert self.is_element_present(*CartPageLocators.CART_EMPTY_MESSAGE), "На странице корзины нет cообщения о пустой корзине"
        # Создаём переменную cart_actual_message и храним в ней фактическое сообщение о пустой корзине
        cart_actual_message = self.browser.find_element(*CartPageLocators.CART_EMPTY_MESSAGE)
        assert cart_expected_message == cart_actual_message.text, f"Текст не соответсвует ожидаемому '{cart_actual_message.text}'"      
