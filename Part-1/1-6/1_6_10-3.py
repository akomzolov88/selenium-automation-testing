# 1.6.10 - 1.6.11 Задание: уникальность селекторов
# Ссылка на задание: https://stepik.org/lesson/138920/step/11?unit=196194 

# Импортируем библиотеку webdriver из библиотеки selenium для управления браузером
from selenium import webdriver
# Импортируем класс By из библиотеки selenium.webdriver.common.by для использования селекторов
from selenium.webdriver.common.by import By
# Импортируем модуль time для работы со временем при помощи функции sleep
import time

# Оборачиваем выполнение кода в блок try-except, чтобы при возникновении ошибки программа не завершалась
try:
    # Создаем переменную link и записываем в нее ссылку на страницу сайта
    link = "http://suninjuly.github.io/registration1.html"
    # Инициализируем драйвер браузера Chrome в переменной browser
    browser = webdriver.Chrome()
    # Передаём сслыку на страницу веб-сайта
    browser.get(link)
    # Создаем переменную Button и записываем в нее элемент кнопки по CSS-селектору
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Нажимаем на кнопку
    button.click()
    # Ждем 1 секунду
    time.sleep(1)
    # Создаем переменную welcome_text_search и записываем в нее элемент заголовка страницы по тегу
    welcome_text_search = browser.find_element(By.TAG_NAME, "h1")
    # Создаем переменную welcome_text и записываем в нее текст элемента welcome_text_search
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
