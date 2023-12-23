# From apps
from Day07.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day07/input_example.txt")

    expected = 168

    result = solve(file_content)
    assert result == expected


def test_real_input():
    file_content = get_input("tests/Day07/input.txt")

    expected = 92881128

    result = solve(file_content)
    assert result == expected
