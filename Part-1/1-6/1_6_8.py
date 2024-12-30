# 1.6.8 Задание: поиск элемента по XPath
# Ссылка на задание: https://stepik.org/lesson/138920/step/8?unit=196194

# Импортируем модуль webdriver из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common.by
from selenium.webdriver.common.by import By
# Импортируем модуль time для работы со временем при помощи функции sleep
import time

# Присваиваем переменной link ссылку на страницу веб-сайта
link = "http://suninjuly.github.io/find_xpath_form"

# Оборачиваем выполнение кода в блок try-except, чтобы при возникновении ошибки программа не завершалась
try:
    # Инициализируем драйвер браузера Chrome в переменной browser
    browser = webdriver.Chrome()
    # Передаём сслыку на страницу веб-сайта при помощи метода get и открываем страницу
    browser.get(link)

    # Находим элемент по тегу input и присваиваем его переменной input1
    input1 = browser.find_element(By.TAG_NAME, "input")
    # Отправляем текст "Ivan" в найденный элемент
    input1.send_keys("Ivan") # Вводим имя
    # Находим элемент по имени name="last_name" и присваиваем его переменной input2
    input2 = browser.find_element(By.NAME, "last_name")
    # Отправляем текст "Ivanov" в найденный элемент
    input2.send_keys("Ivanov") # Вводим фамилию
    # Находим элементи по имени класса city и присваиваем его переменной input3
    input3 = browser.find_element(By.CLASS_NAME, "city")
    # Отправляем текст "Kursk" в найденный элемент
    input3.send_keys("Kursk") # Вводим город
    # Находим элемент по id country и присваиваем его переменной input4
    input4 = browser.find_element(By.ID, "country")
    # Отправляем текст "Russia" в найденный элемент
    input4.send_keys("Russia") # Вводим страну
    # Находим кнопку отправки формы по XPath-селектору
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    # Нажимаем на кнопку при помощи метода click
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла