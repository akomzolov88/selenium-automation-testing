from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def PageTest(link):
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    last_name.send_keys("Petrov")
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

    return welcome_text

class Case(unittest.TestCase):
    def test_num1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = PageTest(link)

        self.assertEqual(welcome_text,PageTest(link)), "Congratulations! You have successfully registered!"

    def test_num2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = PageTest(link)

        self.assertEqual(welcome_text,PageTest(link)), "Congratulations! You have successfully registered!"

if __name__ == "__main__":
    unittest.main()
