# 2.4.8 Задание: ждем нужный текст на странице
# Ссылка на задание: https://stepik.org/lesson/181384/step/8?unit=156009

# Импортируем модуль webdriver из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common.by
from selenium.webdriver.common.by import By
# Импортируем модуль WebDriverWait из библиотеки selenium.webdriver.support.ui
# Модуль WebDriverWait предоставляет все необходимые методы для ожидания элементов
from selenium.webdriver.support.ui import WebDriverWait
# Импортируем модуль expected_conditions из библиотеки selenium.webdriver.support
# Модуль expected_conditions предоставляет все необходимые методы для ожидания определенных условий
from selenium.webdriver.support import expected_conditions as EC
# Импортруем модуль time для работы со временем при помощи функции sleep
import time
# Импортируем модуль math для работы с математическими функциями
import math

# Создаем функцию calc, которая принимает один аргумент x
def calc(x):
  # Возвращаем результат вычисления логарифма от модуля произведения 12 и синуса от x
  return str(math.log(abs(12*math.sin(int(x)))))

# Оборачиваем в блок try-except для обработки исключений
try:
    # Создаем переменную link и присваиваем ей ссылку на страницу
    link = "https://suninjuly.github.io/explicit_wait2.html"
    # Создаем переменную browser и присваиваем ей экземпляр класса Chrome
    browser = webdriver.Chrome()
    # Передаем ссылку в метод get объекта browser и открываем страницу в браузере
    browser.get(link)
    # Ждем пока цена не станет равной 100$ и присваиваем результат переменной price
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    # Находим элемент с id book и присваиваем его переменной rent
    rent = browser.find_element(By.ID, 'book')
    # Нажимаем на кнопку rent
    rent.click()
    # Находим элемент с id input_value и присваиваем его переменной calcValue
    calcValue = browser.find_element(By.ID, 'input_value')
    # Получаем текст элемента calcValue и присваиваем его переменной x_value
    x_value = calcValue.text
    # Создаем переменную x и присваиваем ей значение x_value
    x = x_value
    # Вызываем функцию calc и передаем ей аргумент x, результат присваиваем переменной calcX
    calcX = calc(x)
    # Находим элемент с id answer и присваиваем его переменной answerField
    answerField = browser.find_element(By.ID, 'answer')
    # Прокручиваем страницу вниз к элементу answerField
    browser.execute_script("return arguments[0].scrollIntoView(true);", answerField)
    # Передаем значение calcX в поле ввода answerField
    answerField.send_keys(calcX)
    # Находим элемент с id solve и присваиваем его переменной submit
    submit = browser.find_element(By.ID,'solve')
    # Нажимаем на кнопку submit
    submit.click()

finally:
    # Пауза 10 секунд
    time.sleep(10)
    # Закрываем браузер
    browser.quit()