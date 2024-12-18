from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

#Функция для расчёта X
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
#Открываем ссылку
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
#Нажимаем кнопку
    submit = browser.find_element(By.CSS_SELECTOR,'button.trollface.btn.btn-primary')
    submit.click()
#Запоминаем текущее окно
    main_window = browser.window_handles[0]
#Запоминаем новое окно
    new_window = browser.window_handles[1]
#Переключаемся на новое окно
    browser.switch_to.window(new_window)
#Получаем значение X
    calcValue = browser.find_element(By.ID, 'input_value')
    x_value = calcValue.text
#Рассчитываем значение X
    x = x_value
    calcX = calc(x)
#Вводим результат вычисления X
    answerField = browser.find_element(By.ID, 'answer')
    answerField.send_keys(calcX)
#Получаем число с ответом нажав на кнопку "Submit"
    submit = browser.find_element(By.CSS_SELECTOR,'button.btn.btn-primary')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()