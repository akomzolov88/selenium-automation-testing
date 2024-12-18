from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    calcValue = browser.find_element(By.ID, 'input_value')
    x_value = calcValue.text
    x = x_value
    calcX = calc(x)

    answerField = browser.find_element(By.ID, 'answer')
    answerField.send_keys(calcX)

    robot = browser.find_element(By.ID, 'robotCheckbox')
    robot.click()

    robotRule = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotRule)
    robotRule.click()

    buttonSubmit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    buttonSubmit.click()

finally:
    time.sleep(10)
    browser.quit()