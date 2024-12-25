from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest

# Список ссылок на тестируемые страницы
linksList = [
    #'https://stepik.org/lesson/236895/step/1', 
    #'https://stepik.org/lesson/236896/step/1', 
    #'https://stepik.org/lesson/236897/step/1', 
    #'https://stepik.org/lesson/236898/step/1', 
    #'https://stepik.org/lesson/236899/step/1', 
    #'https://stepik.org/lesson/236903/step/1', 
    #'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]

# функция для получения числа (используется в поле "Ответ")
def answer():
    return str(math.log(int(time.time())))

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def login(browser):
    #browser.find_element(By.ID, "ember240").click()

    browser.get("https://stepik.org/login")
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "id_login_email")))

    # Указать email
    browser.find_element(By.ID, "id_login_email").send_keys("XXX")
    # Указать пароль
    browser.find_element(By.ID, "id_login_password").send_keys("XXX")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# тест проверяет, что ответы на задания правильные
class TestLinks():
    @pytest.mark.parametrize('link', linksList)
    def test_links(self, browser, link):
        login(browser)
        browser.get(link)
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
        textarea = browser.find_element(By.CSS_SELECTOR, "textarea")
        textarea.send_keys(answer())
        button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        button.click()
        feedback = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint")))
        assert "Correct!" in feedback.text