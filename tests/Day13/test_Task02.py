# From apps
from Day13.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day13/input_example.txt")

    expected = 16

    result = solve(file_content)
    assert result == expected


def xtest_real_input():
    file_content = get_input("tests/Day13/input.txt")

    # Will be in the format HGAJBEHC
    expected = 103

    result = solve(file_content)
    assert result == expected
