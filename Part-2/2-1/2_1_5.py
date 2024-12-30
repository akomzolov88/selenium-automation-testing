# 2.1.5 Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
# Ссылка на задание: https://stepik.org/lesson/165493/step/5?unit=140087

# Импортируем модуль webdriver из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common
from selenium.webdriver.common.by import By
# Импортируем модуль time для работы со временем при помощи функции sleep
import time
# Импортируем модуль math для работы с математическими функциями
import math

# Создаем функцию calc, которая принимает один аргумент x
def calc(x):
  # Возвращаем результат вычисления логарифма от модуля синуса от x
  return str(math.log(abs(12*math.sin(int(x)))))

# Оборачиваем наш код в блок try-except, чтобы программа не завершилась аварийно, если возникнет исключение
try:
    # Создаем переменную link и записываем в нее ссылку на страницу
    link = "https://suninjuly.github.io/math.html"
    # Создаём пееременную browser и записываем в неё экземпляр класса Chrome для работы с браузером
    browser = webdriver.Chrome()
    # Переходим по ссылке link переданной в метод get
    browser.get(link)
    # Находим элемент по CSS-селектору span#input_value.nowrap и записываем его в переменную x_element
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
    # Записываем текст элемента x_element в переменную x
    x = x_element.text
    # Вычисляем значение функции calc от x и записываем его в переменную y
    y = calc(x)
    # Находим элемент по CSS-селектору input#answer.form-control и записываем его в переменную answerField
    answerField = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    # Вводим значение y в поле ввода
    answerField.send_keys(y)
    # Находим элемент по CSS-селектору input#robot.form-check-input и записываем его в переменную robot
    robot = browser.find_element(By.CSS_SELECTOR, 'label.form-check-label')
    # Кликаем по Checkbox
    robot.click()
    # Находим элемент по CSS-селектору input#robotsRule.form-check-input и записываем его в переменную robotRule
    robotRule = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule.form-check-input')
    # Кликаем по Radiobutton
    robotRule.click()
    # Находим элемент по CSS-селектору button.btn.btn-default и записываем его в переменную buttonSubmit
    buttonSubmit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    # Нажимаем на кнопку
    buttonSubmit.click()

finally:
    # Ждем 10 секунд
    time.sleep(10)
    # Закрываем браузер
    browser.quit()