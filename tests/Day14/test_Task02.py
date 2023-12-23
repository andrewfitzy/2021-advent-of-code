# From apps
from Day14.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day14/input_example.txt")

    expected = 2188189693529

    result = solve(file_content)
    assert result == expected


def test_real_input():
    file_content = get_input("tests/Day14/input.txt")

    expected = 2360298895777

    result = solve(file_content)
    assert result == expected
