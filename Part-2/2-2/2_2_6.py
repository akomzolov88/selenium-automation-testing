# 2.2.6 Задание: Задание на execute_script
# Ссылка на задание: https://stepik.org/lesson/228249/step/6?unit=200781

# Импортируем модуль webdriver из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common.by
from selenium.webdriver.common.by import By
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
    link = "http://suninjuly.github.io/execute_script.html"
    # Создаем переменную browser и присваиваем ей экземпляр класса Chrome
    browser = webdriver.Chrome()
    # Передаем ссылку в метод get объекта browser и открываем страницу в браузере
    browser.get(link)
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
    # Передаем значение calcX в поле ввода answerField
    answerField.send_keys(calcX)
    # Находим элемент с id robotCheckbox и присваиваем его переменной robot
    robot = browser.find_element(By.ID, 'robotCheckbox')
    # Нажимаем на чекбокс I'm the robot
    robot.click()
    # Находим элемент с id robotsRule и присваиваем его переменной robotRule
    robotRule = browser.find_element(By.ID, 'robotsRule')
    # Прокручиваем страницу вниз к элементу robotRule
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotRule)
    # Нажимаем на radiobutton Robots rule!
    robotRule.click()
    # Находим элемент с css-селектором button.btn.btn-primary и присваиваем его переменной buttonSubmit
    buttonSubmit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    # Нажимаем на кнопку Submit
    buttonSubmit.click()

finally:
    # Пауза 10 секунд
    time.sleep(10)
    # Закрываем браузер
    browser.quit()