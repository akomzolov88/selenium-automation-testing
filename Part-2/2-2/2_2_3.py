# 2.2.3 Задание: работа с выпадающим списком
# Ссылка на задание: https://stepik.org/lesson/228249/step/3?unit=200781

# Импортируем модуль webdriver из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common.by
from selenium.webdriver.common.by import By
# Импортруем модуль time для работы со временем при помощи функции sleep
import time
# Импортируем модуль Select из библиотеки selenium.webdriver.support.ui
from selenium.webdriver.support.ui import Select

# Оборачиваем в блок try-except для обработки исключений
try:
    # Создаем переменную link и присваиваем ей ссылку на страницу
    link = "http://suninjuly.github.io/selects1.html"
    # Создаем переменную browser и присваиваем ей экземпляр класса Chrome
    browser = webdriver.Chrome()
    # Передаем ссылку в метод get объекта browser и открываем страницу в браузере
    browser.get(link)
    # Находим элемент с id num1 и присваиваем его переменной num1_element
    num1_element = browser.find_element(By.ID, "num1")
    # Получаем текст элемента num1_element и присваиваем его переменной num1
    num1 = num1_element.text
    # Преобразуем текст num1 в число и присваиваем его переменной num1_int
    num1_int = int(num1)
    # Находим элемент с id num2 и присваиваем его переменной num2_element
    num2_element = browser.find_element(By.ID, "num2")
    # Получаем текст элемента num2_element и присваиваем его переменной num2
    num2 = num2_element.text
    # Преобразуем текст num2 в число и присваиваем его переменной num2_int
    num2_int = int(num2)
    # Складываем числа num1_int и num2_int и присваиваем результат переменной findSum
    findSum = num1_int + num2_int
    # Преобразуем результат сложения в строку и присваиваем переменной SumText
    SumText = str(findSum)
    # Находим элемент с id dropdown и присваиваем его переменной selectValue
    selectValue = Select(browser.find_element(By.ID, "dropdown"))
    # Выбираем значение SumText в выпадающем списке используя метод select_by_value.
    # Метод select_by_value принимает значение из атрибута value элемента option
    # Метод select_by_value выбирает элемент с заданным значением. Значение переменной SumText передается в качестве аргумента
    selectValue.select_by_value(SumText)
    # Находим элемент с css-селектором button.btn.btn-default и присваиваем его переменной buttonSubmit
    buttonSubmit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    # Нажимаем на кнопку buttonSubmit
    buttonSubmit.click()

finally:
    # Пауза 10 секунд
    time.sleep(10)
    # Закрываем браузер
    browser.quit()



