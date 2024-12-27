import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'page_object')))

from page_object.pages.base_page import BasePageTest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class MainPageTest(BasePageTest): 
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "a#login_link")
        login_link.click()
    
    def should_be_login_link(self):
        # Реализация метода проверки наличия ссылки на логин
        assert self.is_element_present(By.CSS_SELECTOR, "a#login_link_invalid"), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True