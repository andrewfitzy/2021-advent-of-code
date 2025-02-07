# From apps
from Day04.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("Day04/input_example.txt")

    expected = 1924

    result = solve(file_content)
    assert result == expected


def xtest_real_input():
    file_content = get_input("Day04/input.txt")

    expected = 2730

    result = solve(file_content)
    assert result == expected
