# From apps
from Day10.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day10/input_example.txt")

    expected = 288957

    result = solve(file_content)
    assert result == expected


def test_real_input():
    file_content = get_input("tests/Day10/input.txt")

    expected = 2776842859

    result = solve(file_content)
    assert result == expected
