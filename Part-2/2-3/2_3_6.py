# 2.3.6 Задание: переход на новую вкладку
# Ссылка на задание: https://stepik.org/lesson/184253/step/6?unit=158843

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
    link = "https://suninjuly.github.io/redirect_accept.html"
    # Создаем переменную browser и присваиваем ей экземпляр класса Chrome
    browser = webdriver.Chrome()
    # Передаем ссылку в метод get объекта browser и открываем страницу в браузере
    browser.get(link)
    # Создаем переменную submit и присваиваем ей элемент с css-селектором button.trollface.btn.btn-primary
    submit = browser.find_element(By.CSS_SELECTOR,'button.trollface.btn.btn-primary')
    # Нажимаем на кнопку submit
    submit.click()
    # Запоминаем текущее окно записав его в переменную main_window
    main_window = browser.window_handles[0]
    # Запоминаем новое окно записав его в переменную new_window
    new_window = browser.window_handles[1]
    # Переключаемся на новое окно при помощи метода switch_to.window и передаем ему переменную new_window
    browser.switch_to.window(new_window)
    # Создаем переменную calcValue и присваиваем ей элемент с id input_value
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