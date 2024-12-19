from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    last_name.send_keys("Ivanov")
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    email.send_keys("ivan@mail.ru")

    phone = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
    phone.send_keys("+79207333355")
    address = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
    address.send_keys("Russia, Kursk")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_search = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_search.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
