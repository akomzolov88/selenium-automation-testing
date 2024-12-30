# 2.3.4 Задание: принимаем alert
# Ссылка на задание: https://stepik.org/lesson/184253/step/4?unit=158843

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
    link = "https://suninjuly.github.io/alert_accept.html"
    # Создаем переменную browser и присваиваем ей экземпляр класса Chrome
    browser = webdriver.Chrome()
    # Передаем ссылку в метод get объекта browser и открываем страницу в браузере
    browser.get(link)
    # Находим элемент с css-селектором button.btn.btn-primary и присваиваем его переменной submit
    submit = browser.find_element(By.CSS_SELECTOR,'button.btn.btn-primary')
    # Нажимаем на кнопку submit
    submit.click()
    # Переключаемся на окно confirm и присваиваем его переменной confirm
    confirm = browser.switch_to.alert
    # Нажимаем на кнопку OK в окне confirm
    confirm.accept()
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
    # Находим элемент с css-селектором button.btn.btn-primary и присваиваем его переменной submit
    submit = browser.find_element(By.CSS_SELECTOR,'button.btn.btn-primary')
    # Нажимаем на кнопку submit
    submit.click()

finally:
    # Пауза 10 секунд
    time.sleep(10)
    # Закрываем браузер
    browser.quit()