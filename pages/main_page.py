from .base_page import BasePageTest
from selenium.webdriver.common.by import By

class MainPageTest(BasePageTest): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()