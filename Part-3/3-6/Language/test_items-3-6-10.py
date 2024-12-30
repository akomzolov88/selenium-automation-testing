# 3.6.10 Задание: запуск автотестов для разных языков интерфейса
# Ссылка на задание: https://stepik.org/lesson/237240/step/10?unit=209628

# Импортируем модуль time для работы со временем при помощи метода sleep
import time
# Импортируем модуль By из библиотеки selebnium.webdriver.comon.by для использования поиска элементов
from selenium.webdriver.common.by import By

# Создаём функцию test_button_add_to_basket_exist_on_page для проверки наличия кнопки добавления товара в корзину
def test_button_add_to_basket_exist_on_page(browser):
    # В пременной link записываем ссылку на страницу с товаром
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # При помощи метода get открываем страницу
    browser.get(link)
    # Ждем загрузки страницы
    time.sleep(30)
    # Проверяем начличие кнопки добавления товара в корзину на странице, используя CSS-селектор
    assert browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")