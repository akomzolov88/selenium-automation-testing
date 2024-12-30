# 1.6.5 Задание: поиск элементов с помощью Selenium 
# Ссылка на задание: https://stepik.org/lesson/138920/step/5?unit=196194

# Импорт библиотек
# Импортиуем модуль webdriver из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common.by
from selenium.webdriver.common.by import By
# Импортируем модуль time для работы со временем при помощь функции sleep
import time
# Импортируем модуль math для работы с математическими функциями
import math

# Задаем переменную link и присваиваем ей ссылку на страницу
link = "http://suninjuly.github.io/find_link_text"

# Оборачиваем в блок try...finally для корректного завершения работы скрипта
try:
    # Создаем перемнную browser и присваиваем ей модуль webdriver.Chrome() для запуска браузера Google Chrome
    browser = webdriver.Chrome()
    # Открываем страницу используя метод get() передавая значение переменной link
    browser.get(link)

    # Расчитываем значение переменной linktext и приводим его к строковому типу
    linktext = str(math.ceil(math.pow(math.pi, math.e)*10000))

    # Создаём переменную link и присваиваем ей метод find_element класса By.LINK_TEXT передавая значение переменной linktext
    # Класс By.LINK_TEXT ищет элемент по тексту ссылки
    link = browser.find_element(By.LINK_TEXT, linktext)
    # Вызываем метод click() для перемен
    link.click()

    # Создаём переменную input1 и при помощи метода find_element класса By.TAG_NAME ищем элемент по тегу input
    # В переменной input1 сохраняем найденный элемент
    input1 = browser.find_element(By.TAG_NAME, "input")
    # Вызываем метод send_keys() для переменной input1 и передаем строку "Ivan"
    input1.send_keys("Ivan") # Вводим имя
    # Создаём переменную input2 и при помощи метода find_element класса By.NAME ищем элемент по имени(Name) first_name
    input2 = browser.find_element(By.NAME, "last_name")
    # Вызываем метод send_keys() для переменной input2 и передаем строку "Ivanov"
    input2.send_keys("Ivanov") # Вводим фамилию
    # Создаём переменную input3 и при помощи метода find_element класса By.CLASS_NAME ищем элемент по имени(Name) класса city
    input3 = browser.find_element(By.CLASS_NAME, "city")
    # Вызываем метод send_keys() для переменной input3 и передаем строку "Kursk"
    input3.send_keys("Kursk") # Вводим город
    # Создаём переменную input4 и при помощи метода find_element класса By.ID ищем элемент по имени(ID) country
    input4 = browser.find_element(By.ID, "country")
    # Вызываем метод send_keys() для переменной input4 и передаем строку "Russia"
    input4.send_keys("Russia") # Вводим страну
    # Создаём переменную button и при помощи метода find_element класса By.CSS_SELECTOR ищем элемент по имени класса button.btn
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Вызываем метод click() для переменной button
    # Метод click() нажимает на кнопку
    button.click()

# Обрабатываем исключение
finally:
    # Для того чтобы успеть скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла