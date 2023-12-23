# From apps
from Day20.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day20/input_example.txt")

    expected = 35

    result = solve(file_content, 2)
    assert result == expected


def test_real_input():
    file_content = get_input("tests/Day20/input.txt")

    expected = 5391

    result = solve(file_content, 2)
    assert result == expected
