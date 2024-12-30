# 2.1.7 Задание: поиск сокровища с помощью get_attribute
# Ссылка на задание: https://stepik.org/lesson/165493/step/7?unit=140087

# Импортируем модуль webdriver из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common.by
from selenium.webdriver.common.by import By
# Импортируем модуль time для работы со временем при помощи метода sleep
import time
# Импортируем модуль math для математических операций
import math

# Создаем функцию calc, которая принимает один аргумент x
def calc(x):
  # Возвращаем результат вычисления логарифма от модуля синуса от x
  return str(math.log(abs(12*math.sin(int(x)))))

# Оборачиваем наш код в блок try-except, чтобы программа не завершилась аварийно, если возникнет исключение
try:
    # Создаем переменную link и записываем в нее ссылку на страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    # Создаём пееременную browser и записываем в неё экземпляр класса Chrome для работы с браузером
    browser = webdriver.Chrome()
    # Переходим по ссылке link переданной в метод get
    browser.get(link)
    # Находим элемент по CSS-селектору img#treasure и записываем его в переменную treasureChest
    treasureChest = browser.find_element(By.CSS_SELECTOR, 'img#treasure')
    # Получаем значение атрибута valuex элемента treasureChest и записываем его в переменную x_treasureChest
    x_treasureChest = treasureChest.get_attribute("valuex")
    # Создаём переменную x и записываем в неё значение x_treasureChest
    x = x_treasureChest
    # Вычисляем значение функции calc от x и записываем его в переменную y
    y = calc(x)
    # Находим элемент по CSS-селектору input#answer и записываем его в переменную answerField
    answerField = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    # Вводим значение y в поле ввода
    answerField.send_keys(y)
    # Находим элемент по CSS-селектору input#robotCheckbox и записываем его в переменную robot
    robot = browser.find_element(By.ID, 'robotCheckbox')
    # Кликаем по Checkbox
    robot.click()
    # Находим элемент по CSS-селектору input#robotsRule и записываем его в переменную robotRule
    robotRule = browser.find_element(By.ID, 'robotsRule')
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