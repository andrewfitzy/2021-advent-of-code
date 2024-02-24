# From apps
from Day11.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day11/input_example.txt")

    expected = 1656

    result = solve(file_content)
    assert result == expected


def xtest_real_input():
    file_content = get_input("tests/Day11/input.txt")

    expected = 1594

    result = solve(file_content)
    assert result == expected
