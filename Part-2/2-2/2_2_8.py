from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.NAME,'firstname')
    firstName.send_keys('Ivan')
    lastName = browser.find_element(By.NAME,'lastname')
    lastName.send_keys('Ivanov')
    email = browser.find_element(By.NAME,'email')
    email.send_keys('IronIvan@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    fileField = browser.find_element(By.ID, 'file')
    fileField.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR,'button.btn.btn-primary')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()