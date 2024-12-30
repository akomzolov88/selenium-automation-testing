# 1.6.10 - 1.6.11 Задание: уникальность селекторов
# Ссылка на задание: https://stepik.org/lesson/138920/step/11?unit=196194 

# Импортируем модуль webdriver из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common.by
from selenium.webdriver.common.by import By
# Импортируем модуль time для работы со временем при помощи функции sleep
import time

# Оборачиваем выполнение кода в блок try-except, чтобы при возникновении ошибки программа не завершалась
try:
    # Создаём переменную link и записываем в неё ссылку на страницу сайта
    link = "http://suninjuly.github.io/registration1.html"
    # Инициализируем драйвер браузера Chrome в переменной browser
    browser = webdriver.Chrome()
    # Передаём ссылку на страницу сайта при помощи метода get и открываем страницу
    browser.get(link)
    # Находим элемент по тексту placeholder'а используя XPath-селектор и присваиваем его переменной first_name
    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    # Отправляем текст "Ivan" в найденный элемент
    first_name.send_keys("Ivan") # Вводим имя
    # Находим элемент по тексту placeholder'а используя XPath-селектор и присваиваем его переменной last_name
    last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    # Отправляем текст "Ivanov" в найденный элемент
    last_name.send_keys("Ivanov") # Вводим фамилию
    # Находим элемент по тексту placeholder'а используя XPath-селектор и присваиваем его переменной email
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    # Отправляем текст электронной почты в найденный элемент
    email.send_keys("ivan@mail.ru") # Вводим электронную почту
    # Находим элемент по тексту placeholder'а используя XPath-селектор и присваиваем его переменной phone
    phone = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
    # Отправляем текст "+79207333355" в найденный элемент
    phone.send_keys("+79207333355") # Вводим номер телефона
    # Находим элемент по тексту placeholder'а используя XPath-селектор и присваиваем его переменной address
    address = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
    # Отправляем текст "Russia, Kursk" в найденный элемент
    address.send_keys("Russia, Kursk") # Вводим адрес
    # Находим кнопку по тексту на ней и присваиваем её переменной button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Нажимаем на кнопку
    button.click()
    # Ждём 1 секунду
    time.sleep(1)
    # Находим элемент по тегу и присваиваем его переменной welcome_text_search
    welcome_text_search = browser.find_element(By.TAG_NAME, "h1")
    # Получаем текст элемента и присваиваем его переменной welcome_text
    welcome_text = welcome_text_search.text

    # C помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # Если тексты не совпадают, то assert генерирует исключение и программа завершается
    # Функция assert сравнивает два значения: "Congratulations! You have successfully registered!" и welcome_text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ждём 10 секунд
    time.sleep(10)
    # Закрываем браузер
    browser.quit()
