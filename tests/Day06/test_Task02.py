# From apps
from Day06.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day06/input_example.txt")

    expected = 26984457539

    result = solve(file_content)
    assert result == expected


def test_real_input():
    file_content = get_input("tests/Day06/input.txt")

    expected = 1604361182149

    result = solve(file_content)
    assert result == expected
