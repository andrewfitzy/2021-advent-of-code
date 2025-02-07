# From apps
from Dayxx.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("Dayxx/input_example.txt")

    expected = 1

    result = solve(file_content)
    assert result == expected


def xtest_real_input():
    file_content = get_input("Dayxx/input.txt")

    expected = 1

    result = solve(file_content)
    assert result == expected
