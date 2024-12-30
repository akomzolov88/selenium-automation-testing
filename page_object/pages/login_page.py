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
# Импортируем класс LoginPageLocators из файла locators.py для использования локаторов страницы Авторизации/Регистрации
from locators import LoginPageLocators

# Создаём класс LoginPage, который наследует класс BasePage
class Login(BasePage):
    # Создаём метод should_be_login_page для проверки что на странице присутстует форма для входа пользователя и форма для регистрации нового пользователя
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Создаём метод should_be_login_url для проверки что URL страницы содержит подстроку "login"
    def should_be_login_url(self):
        # Проверяем, что подстрока "login" содержится в URL страницы
        assert "login" in self.browser.current_url, "URL страницы не содержит подстроку 'login'"

    # Создаём метод should_be_login_form для проверки наличия формы Авторизации
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма авторизации не найдена"

    # Создаём метод should_be_register_form для проверки наличия формы Регистрации нового пользователя
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации нового пользователя не найдена"
    
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_SUBMIT).click()