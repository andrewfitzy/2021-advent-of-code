# From apps
from Day01.Task01_rewrite import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day01/input_example.txt")

    expected = 7

    result = solve(file_content)
    assert result == expected


def test_real_input():
    file_content = get_input("tests/Day01/input.txt")

    expected = 1616

    result = solve(file_content)
    assert result == expected
