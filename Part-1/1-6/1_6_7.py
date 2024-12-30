# 1.6.7 Задание: использование метода find_elements
# Ссылка на задание: https://stepik.org/lesson/138920/step/7?unit=196194

# Импортируем модуль webdriver из библиотеки selenium
# Модуль WebDriver позволяет взаимодействовать с веб-страницами
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common.by
from selenium.webdriver.common.by import By
# Импортируем модуль time для работы со временем при помощи функции sleep
import time

# Оборачиваем выполнение кода в блок try-except, чтобы при возникновении ошибки программа не завершалась
try:
    # Инициализируем драйвер браузера Chrome в переменной browser
    browser = webdriver.Chrome()
    # Передаём сслыку на страницу веб-сайта.
    # При помощи метода get открываем страницу.
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Находим все элементы с тегом input на странице
    elements = browser.find_elements(By.TAG_NAME, "input")
    # Перебираем все найденные элементы при помощи цикла for
    # Цикл for позволяет выполнить один и тот же код для каждого элемента
    for element in elements:
        # Для каждого найденного элемента отправляем текст "Мой ответ"
        element.send_keys("Мой ответ")

    # Находим кнопку отправки формы по CSS-селектору
    # Присваиваем найденный элемент переменной button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Нажимаем на кнопку при помощи метода click
    button.click()

finally:
    # Пауза перед закрытием браузера
    time.sleep(30)
    # Закрываем браузер
    browser.quit()
