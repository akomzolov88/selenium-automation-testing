# 2.2.8 Задание: загрузка файла
# Ссылка на задание: https://stepik.org/lesson/228249/step/8?unit=200781

# Импортируем модуль webdriver из библиотеки selenium
from selenium import webdriver
# Импортируем модуль By из библиотеки selenium.webdriver.common.by
from selenium.webdriver.common.by import By
# Импортруем модуль time для работы со временем при помощи функции sleep
import time
# Импортируем модуль os для работы с операционной системой
import os

# Оборачиваем в блок try-except для обработки исключений
try:
    # Создаем переменную link и присваиваем ей ссылку на страницу
    link = "https://suninjuly.github.io/file_input.html"
    # Создаем переменную browser и присваиваем ей экземпляр класса Chrome
    browser = webdriver.Chrome()
    # Передаем ссылку в метод get объекта browser и открываем страницу в браузере
    browser.get(link)
    # Находим элемент с name firstname и присваиваем его переменной firstName
    firstName = browser.find_element(By.NAME,'firstname')
    # Вводим текст в поле ввода firstName
    firstName.send_keys('Ivan') # Вводим имя
    # Находим элемент с name lastname и присваиваем его переменной lastName
    lastName = browser.find_element(By.NAME,'lastname')
    # Вводим текст в поле ввода lastName
    lastName.send_keys('Ivanov') # Вводим фамилию
    # Находим элемент с name email и присваиваем его переменной email
    email = browser.find_element(By.NAME,'email')
    # Вводим текст в поле ввода email
    email.send_keys('IronIvan@mail.ru') # Вводим email
    # Получаем путь к директории текущего исполняемого файла и присваиваем его переменной current_dir
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Присваиваем переменной file_path путь к файлу file.txt
    file_path = os.path.join(current_dir, 'file.txt')
    # Находим элемент с id file и присваиваем его переменной fileField
    fileField = browser.find_element(By.ID, 'file')
    # Передаем путь к файлу file.txt в поле ввода fileField
    fileField.send_keys(file_path)
    # Находим элемент с css-селектором button.btn.btn-primary и присваиваем его переменной submit
    submit = browser.find_element(By.CSS_SELECTOR,'button.btn.btn-primary')
    # Нажимаем на кнопку submit
    submit.click()

finally:
    # Пауза 10 секунд
    time.sleep(10)
    # Закрываем браузер
    browser.quit()