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
    # Присваиваем переменной link ссылку на страницу веб-сайта
    link = "http://suninjuly.github.io/registration1.html"
    # Инициализируем драйвер браузера Chrome в переменной browser
    browser = webdriver.Chrome()
    # Передаём сслыку на страницу веб-сайта при помощи метода get и открываем страницу
    browser.get(link)
    # Находим элемент по тексту placeholder'а используя XPath-селектор и присваиваем его переменной first_name
    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    # Отправляем текст "Ivan" в найденный элемент
    first_name.send_keys("Ivan") # Вводим имя
    # Находим элемент по тексту placeholder'а XPath-селектор и присваиваем его переменной last_name
    last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    # Отправляем текст "Ivanov" в найденный элемент
    last_name.send_keys("Ivanov") # Вводим фамилию
    # Находим элемент по тексту placeholder'а XPath-селектор и присваиваем его переменной email
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    # Отправляем текст электронной почты в найденный элемент
    email.send_keys("ivan@mail.ru") # Вводим электронную почту
    # Находим элемент по тексту placeholder'а используя XPath-селектор и присваиваем его переменной phone
    phone = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
    # Отправляем текст номера телефона в найденный элемент
    phone.send_keys("+79207333355") # Вводим номер телефона
    # Находим элемент тексту placeholder'а используя XPath-селектор и присваиваем его переменной address
    address = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
    # Отправляем текст адреса в найденный элемент
    address.send_keys("Russia, Kursk") # Вводим адрес
    # Находим кнопку отправки формы по CSS-селектору
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Нажимаем на кнопку при помощи метода click
    button.click()
    # Пауза для того чтобы точно появился следующий элемент
    time.sleep(1)
    # Находим элемент по тегу h1 и присваиваем его переменной welcome_text_search
    welcome_text_search = browser.find_element(By.TAG_NAME, "h1")
    # Присваиваем переменной welcome_text текст найденного элемента
    welcome_text = welcome_text_search.text

    # C помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # Если тексты не совпадают, то assert генерирует исключение и программа завершается
    # Функция assert сравнивает два значения: "Congratulations! You have successfully registered!" и welcome_text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Пауза перед закрытием браузера
    time.sleep(10)
    # Закрываем браузер
    browser.quit()
