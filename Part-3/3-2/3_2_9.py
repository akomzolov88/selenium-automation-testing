# 3.2.9 Задание: составные сообщения об ошибках и поиск подстроки
# Ссылка на задание: https://stepik.org/lesson/36285/step/9?unit=162401

# Создаём функцию, которая принимает два значения и сравнивает их
def test_substring(full_string, substring):
    # Если подстрока не является подстрокой строки, то выводим сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

'''
Sample Input 1:
fulltext some_value
Sample Input 2:
1 1
Sample Input 3:
some_text some
'''

test = test_substring('fulltext', 'some_value')