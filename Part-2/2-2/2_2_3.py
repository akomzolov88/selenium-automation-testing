from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1")
    num1 = num1_element.text
    num1_int = int(num1)
    num2_element = browser.find_element(By.ID, "num2")
    num2 = num2_element.text
    num2_int = int(num2)
    findSum = num1_int + num2_int
    SumText = str(findSum)

    selectValue = Select(browser.find_element(By.ID, "dropdown"))
    selectValue.select_by_value(SumText)

    buttonSubmit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    buttonSubmit.click()

finally:
    time.sleep(10)
    browser.quit()



