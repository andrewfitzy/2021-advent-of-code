# From apps
from Day12.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example01_input():
    file_content = get_input("tests/Day12/input_example01.txt")

    expected = 10

    result = solve(file_content)
    assert result == expected


def test_example02_input():
    file_content = get_input("tests/Day12/input_example02.txt")

    expected = 19

    result = solve(file_content)
    assert result == expected


def test_example03_input():
    file_content = get_input("tests/Day12/input_example03.txt")

    expected = 226

    result = solve(file_content)
    assert result == expected


def xtest_real_input():
    file_content = get_input("tests/Day12/input.txt")

    expected = 5254

    result = solve(file_content)
    assert result == expected
