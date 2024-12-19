num1 = int(input())
num2 = int(input())

assert num1 != num2, \
    f"expected {num1}, got {num2}"

def test_input_text(expected_result, actual_result):
    expected_result = num1
    actual_result = num2

    assert expected_result != actual_result, \
        f"expected {expected_result}, got {actual_result}"