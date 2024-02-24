# From apps
from Day13.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day13/input_example.txt")

    expected = 17

    result = solve(file_content)
    assert result == expected


def xtest_real_input():
    file_content = get_input("tests/Day13/input.txt")

    expected = 704

    result = solve(file_content)
    assert result == expected
