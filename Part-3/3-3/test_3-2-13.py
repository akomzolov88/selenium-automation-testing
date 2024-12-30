# 3.3.3 Задание: вывод PyTest 
# Ccылка на задание: https://stepik.org/lesson/193188/step/3?unit=167629

# Необходимо запустите тесты созданные ранее в задании 3.2.13 Задание: оформляем тесты в стиле unittest 
# Ccылка на задание: https://stepik.org/lesson/36285/step/13?unit=162401

# Импортируем модуль webdriver для взаимодействия с веб-страницами из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By для использования селекторов
from selenium.webdriver.common.by import By
# Импортируем модуль time для работы со временем при помощи метода sleep
import time
# Импортируем модуль unittest для создания тестов
import unittest

# Создаем функцию PageTest, которая принимает аргумент link
def PageTest(link):
    # Создаем объект browser, который является экземпляром класса Chrome
    browser = webdriver.Chrome()
    # Передаём ссылку link в метод get объекта browser
    browser.get(link)
    # Создаем переменную first_name, которая находит элемент по xpath placeholder='Input your first name'
    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    # Вводим в поле first_name значение "Ivan"
    first_name.send_keys("Ivan") # Вводим имя
    # Создаем переменную last_name, которая находит элемент по xpath placeholder='Input your last name'
    last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    # Вводим в поле last_name значение "Petrov"
    last_name.send_keys("Petrov") # Вводим фамилию
    # Создаем переменную email, которая находит элемент по xpath placeholder='Input your email'
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    # Вводим в поле email электронную почту
    email.send_keys("ivan@mail.ru") # Вводим email
    # Создаем переменную phone, которая находит элемент по xpath placeholder='Input your phone'
    phone = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
    # Вводим в поле phone номер телефона
    phone.send_keys("+79207333355")
    # Создаем переменную address, которая находит элемент по xpath placeholder='Input your address'
    address = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
    # Вводим в поле address адрес
    address.send_keys("Russia, Kursk")
    # Создаем переменную button, которая находит элемент по css-селектору button.btn
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Нажимаем на кнопку button
    button.click()
    # Задержка в 1 секунду
    time.sleep(1)
    # Создаем переменную welcome_text_search, которая находит элемент по тегу h1
    welcome_text_search = browser.find_element(By.TAG_NAME, "h1")
    # Создаем переменную welcome_text, которая содержит текст элемента welcome_text_search
    welcome_text = welcome_text_search.text
    # Закрываем браузер и получаем текст welcome_text. Данный текст будет использоваться в тестах
    return welcome_text

# Создаем класс Case, который наследует класс unittest.TestCase
class Case(unittest.TestCase):
    # Создаем метод test_num1, который проверяет текст welcome_text на странице 
    def test_num1(self):
        # Создаем переменную link, которая содержит ссылку на страницу
        link = "http://suninjuly.github.io/registration1.html"
        # Создаем переменную welcome_text, которая содержит текст welcome_text на странице
        welcome_text = PageTest(link)
        # Проверяем, что welcome_text равен "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text,PageTest(link)), "Congratulations! You have successfully registered!"

    # Создаем метод test_num2, который проверяет текст welcome_text на странице
    def test_num2(self):
        # Создаем переменную link, которая содержит ссылку на страницу
        link = "http://suninjuly.github.io/registration2.html"
        # Создаем переменную welcome_text, которая содержит текст welcome_text на странице
        welcome_text = PageTest(link)
        # Проверяем, что welcome_text равен "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text,PageTest(link)), "Congratulations! You have successfully registered!"
# Если файл запущен напрямую, то запускаем тесты
if __name__ == "__main__":
    unittest.main()
    
