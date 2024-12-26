import time
from selenium.webdriver.common.by import By

def test_button_add_to_basket_exist_on_page(browser):
    # Ссылка на страницу с товаром
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # Открываем страницу
    browser.get(link)
    # Ждем загрузки страницы
    time.sleep(30)
    # Проверка наличия кнопки добавления товара в корзину
    assert browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")