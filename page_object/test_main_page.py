import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'D:/Projects/selenium-automation-testing/page_object')))

from pages.main_page import MainPageTest

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPageTest(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы — переходим на страницу логина                      
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPageTest(browser, link)
    page.open()
    page.should_be_login_link()