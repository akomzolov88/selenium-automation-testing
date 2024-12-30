# 3.2.8 Задание: составные сообщения об ошибках
# Ссылка на задание: https://stepik.org/lesson/36285/step/8?unit=162401

# Создаём функцию, которая принимает два значения и сравнивает их
def test_input_text(expected_result, actual_result):
    # Если значения равны, то выводим сообщение об успехе
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'
# Вызываем функцию и передаём в неё значения
'''
Sample Input 1:
8 11
Sample Input 2:
11 11
Sample Input 3:
11 15
'''
test = test_input_text(8, 11)