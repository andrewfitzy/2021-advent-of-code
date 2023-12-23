# From apps
from Day12.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example01_input():
    file_content = get_input("tests/Day12/input_example01.txt")

    expected = 36

    result = solve(file_content)
    assert result == expected


def test_example02_input():
    file_content = get_input("tests/Day12/input_example02.txt")

    expected = 103

    result = solve(file_content)
    assert result == expected


def test_example03_input():
    file_content = get_input("tests/Day12/input_example03.txt")

    expected = 3509

    result = solve(file_content)
    assert result == expected


# remove the x to run this test... if you have the time
def xtest_real_input():
    file_content = get_input("tests/Day12/input.txt")

    expected = 149385

    result = solve(file_content)
    assert result == expected
