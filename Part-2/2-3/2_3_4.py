from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

#Функция для расчёта X
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
#Открываем ссылку
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
#Вызываем модальное окно Confirm
    submit = browser.find_element(By.CSS_SELECTOR,'button.btn.btn-primary')
    submit.click()
#Нажимаем "Подтвердить" в модальном окне Confirm
    confirm = browser.switch_to.alert
    confirm.accept()
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