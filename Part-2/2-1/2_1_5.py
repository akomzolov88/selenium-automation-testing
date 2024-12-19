from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
    x = x_element.text
    y = calc(x)

    answerField = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    answerField.send_keys(y)

    robot = browser.find_element(By.CSS_SELECTOR, 'label.form-check-label')
    robot.click()

    robotRule = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule.form-check-input')
    robotRule.click()

    buttonSubmit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    buttonSubmit.click()

finally:
    time.sleep(10)
    browser.quit()