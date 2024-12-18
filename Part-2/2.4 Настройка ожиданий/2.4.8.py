from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

#Функция для расчёта X
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
#Открываем ссылку
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
#Проверяем и ждём пока сумма не станет 100$ price
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
#После того как сумма равна 100$ жмём кнопку 'Book'
    rent = browser.find_element(By.ID, 'book')
    rent.click()
#Получаем значение X
    calcValue = browser.find_element(By.ID, 'input_value')
    x_value = calcValue.text
#Рассчитываем значение X
    x = x_value
    calcX = calc(x)
#Вводим результат вычисления X прокрутив экран чтобы кнопка "Submit" стала видимой
    answerField = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answerField)
    answerField.send_keys(calcX)
#Получаем число с ответом нажав на кнопку "Submit"
    submit = browser.find_element(By.ID,'solve')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()