# 1.6.4 Задание: поиск элементов с помощью Selenium
# Ссылка на задание: https://stepik.org/lesson/138920/step/4?unit=196194

# Импортируем модуль webdriver из библиотеки selenium для управления браузером
from selenium import webdriver
# Импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
# Импортируем модуль time для использования Функции sleep (пауза в выполнении программы)
import time

# Создаём переменную link, в которой хранится ссылка на страницу
link = "http://suninjuly.github.io/simple_form_find_task.html"

# Оборачиваем выполнение кода в блок try-except, чтобы программа не завершалась аварийно при возникновении ошибок
try:
    # Инициализируем драйвер браузера Chrome. После этой команды откроется новое окно браузера
    browser = webdriver.Chrome()
    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    browser.get(link)

    # Находим элементы на странице
    # Ищем поле для ввода Имени
    input1 = browser.find_element(By.TAG_NAME, "input")
    # Вводим текст "Ivan" в найденное поле
    input1.send_keys("Ivan")
    # Ищем поле для ввода Фамилии
    input2 = browser.find_element(By.NAME, "last_name")
    # Вводим текст "Ivanov" в найденное поле
    input2.send_keys("Ivanov")
    # Ищем поле для ввода Города
    input3 = browser.find_element(By.CLASS_NAME, "city")
    # Вводим текст "Kursk" в найденное поле
    input3.send_keys("Kursk")
    # Ищем поле для ввода Страны
    input4 = browser.find_element(By.ID, "country")
    # Вводим текст "Russia" в найденное поле
    input4.send_keys("Russia")
    # Найдем кнопку, которая отправляет введенное решение.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе.
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла