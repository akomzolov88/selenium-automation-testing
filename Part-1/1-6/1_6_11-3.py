# 1.6.10 - 1.6.11 Задание: уникальность селекторов
# Ссылка на задание: https://stepik.org/lesson/138920/step/11?unit=196194 

# Импортируем модуль webdriver из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common
from selenium.webdriver.common.by import By
# Импортируем модуль time для работы со временем при помощи функции sleep
import time

# Оборачиваем наш код в блок try-except, чтобы программа не завершилась аварийно, если возникнет исключение
try:
    # Создаем переменную link и записываем в нее ссылку на страницу
    link = "http://suninjuly.github.io/registration2.html"
    # Создаём пееременную browser и записываем в неё экземпляр класса Chrome для работы с браузером
    browser = webdriver.Chrome()
    # Переходим по ссылке link переданной в метод get
    browser.get(link)
    # Создаем переменную button и записываем в нее кнопку найдя её при помощи CSS-селектора
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Нажимаем на кнопку
    button.click()
    # Ждем 1 секунду
    time.sleep(1)
    # Находим элемент по тегу h1 и записываем его в переменную welcome_text_search
    welcome_text_search = browser.find_element(By.TAG_NAME, "h1")
    # Записываем текст элемента welcome_text_search в переменную welcome_text
    welcome_text = welcome_text_search.text
    # C помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # Если тексты не совпадают, то assert генерирует исключение и программа завершается
    # Функция assert сравнивает два значения: "Congratulations! You have successfully registered!" и welcome_text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ждем 10 секунд
    time.sleep(10)
    # Закрываем браузер
    browser.quit()
