# 3.5.7 Задание: запуск тестов
# Ссылка на задание: https://stepik.org/lesson/236918/step/7?unit=209305

# Импортируем модуль pytest
# Pytest - это фреймворк для написания тестов на языке программирования Python.
# Pytest позволяет запускать тесты, используя более удобный синтаксис, чем стандартный модуль unittest.
import pytest

# Создаем класс TestMainPage
# PyTest автоматически обнаруживает и запускает тесты внутри классов, названия которых начинаются с Test.
class TestMainPage():
    # номер 1
    @pytest.mark.xfail # Помечаем тест как ожидаемо падающий
    @pytest.mark.smoke # Помечаем тест как smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression # Помечаем тест как Regress
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet") # Помечаем тест как пропущенный c указанием причины
    @pytest.mark.smoke # Помечаем тест как smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke # Помечаем тест как smoke
    def test_guest_can_see_total_price(self, browser):
        assert True


@pytest.mark.skip # Помечаем тест как пропущенный
class TestBookPage():
    # номер 5
    @pytest.mark.smoke # Помечаем тест как smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression # Помечаем тест как Regress
    def test_guest_can_see_book_price(self, browser):
        assert True


# номер 7
@pytest.mark.beta_users # Помечаем тест как beta_users. Это пользователи, которые используют бета-версию сайта
@pytest.mark.smoke # Помечаем тест как smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True