# From apps
from Dayxx.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Dayxx/input_example.txt")

    expected = 1

    result = solve(file_content)
    assert result == expected


def test_real_input():
    file_content = get_input("tests/Dayxx/input.txt")

    expected = 1

    result = solve(file_content)
    assert result == expected
