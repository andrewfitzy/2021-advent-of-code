# From apps
from Day08.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("Day08/input_example.txt")

    expected = 61229

    result = solve(file_content)
    assert result == expected


def xtest_real_input():
    file_content = get_input("Day08/input.txt")

    expected = 990964

    result = solve(file_content)
    assert result == expected
