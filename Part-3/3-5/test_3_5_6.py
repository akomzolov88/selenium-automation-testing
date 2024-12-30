# 3.5.6 Задание: пропуск тестов
# Ссылка на задание: https://stepik.org/lesson/236918/step/6?unit=209305

# Импортируем модуль pytest
# Pytest - это фреймворк для написания тестов на языке программирования Python.
# Pytest позволяет запускать тесты, используя более удобный синтаксис, чем стандартный модуль unittest.
import pytest

# mark.xfail(strict=True) - помечает тест как ожидаемо падающий
# strict=True - строгий режим, который говорит, что тест должен падать
@pytest.mark.xfail (strict=True)
def test_succeed():
    assert True

# mark.xfail - помечает тест как ожидаемо падающий
@pytest.mark.xfail
def test_not_succeed():
    assert False

# mark.skip - помечает тест как пропущенный
@pytest.mark.skip
def test_skipped():
    assert False