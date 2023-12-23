# From apps
from Day03.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day03/input_example.txt")

    expected = 198

    result = solve(file_content)
    assert result == expected


def test_real_input():
    file_content = get_input("tests/Day03/input.txt")

    expected = 3912944

    result = solve(file_content)
    assert result == expected
