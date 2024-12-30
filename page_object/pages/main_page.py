# 4.3.15 Финальное задание  в блоке: Применение патерна Page Object.
# Ссылка на задание: https://stepik.org/lesson/201964/step/15?unit=176022
# Ссылка на правила подготовки кода к ревью: https://stepik.org/lesson/201964/step/14?unit=176022 

# Импортируем модуль sys для работы с системными параметрами
import sys
# Импортируем модуль os для работы с функциями операционной системы
import os
# Добавляем в переменную sys.path абсолютный путь к директории page_object
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'D:/Projects/selenium-automation-testing/page_object')))

# Импортируем класс BasePage из файла base_page.py
from pages.base_page import BasePage

class MainPage(BasePage):
    # Создаём конструктор класса BasePage
    def __init__(self, browser, url, timeout=10):
        # Инициализируем атрибуты класса BasePage
        self.browser = browser
        # Присваиваем атрибуту url переданное значение
        self.url = url
        # Устанавливаем неявное ожидание для поиска элементов на странице
        self.browser.implicitly_wait(timeout)
    