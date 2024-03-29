# From apps
from Day02.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day02/input_example.txt")

    expected = 900

    result = solve(file_content)
    assert result == expected


def xtest_real_input():
    file_content = get_input("tests/Day02/input.txt")

    expected = 2086261056

    result = solve(file_content)
    assert result == expected
