# From apps
from Day09.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day09/input_example.txt")

    expected = 15

    result = solve(file_content)
    assert result == expected


def test_real_input():
    file_content = get_input("tests/Day09/input.txt")

    expected = 417

    result = solve(file_content)
    assert result == expected
