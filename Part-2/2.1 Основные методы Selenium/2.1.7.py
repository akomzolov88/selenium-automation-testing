from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasureChest = browser.find_element(By.CSS_SELECTOR, 'img#treasure')
    x_treasureChest = treasureChest.get_attribute("valuex")
    x = x_treasureChest
    y = calc(x)

    answerField = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answerField.send_keys(y)

    robot = browser.find_element(By.ID, 'robotCheckbox')
    robot.click()

    robotRule = browser.find_element(By.ID, 'robotsRule')
    robotRule.click()

    buttonSubmit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    buttonSubmit.click()

finally:
    time.sleep(10)
    browser.quit()