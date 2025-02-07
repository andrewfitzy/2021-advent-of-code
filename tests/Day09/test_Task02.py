# From apps
from Day09.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("Day09/input_example.txt")

    expected = 1134

    result = solve(file_content)
    assert result == expected


def xtest_real_input():
    file_content = get_input("Day09/input.txt")

    expected = 1148965

    result = solve(file_content)
    assert result == expected
