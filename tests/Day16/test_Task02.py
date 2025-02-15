# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day16.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input_01():
    file_content = get_input("tests/Day16/input_example01.txt")

    expected = 2021

    result = solve(file_content)
    assert result == expected


def test_example_input_02():
    file_content = get_input("tests/Day16/input_example02.txt")

    expected = 15

    result = solve(file_content)
    assert result == expected


def test_example_input_03():
    file_content = get_input("tests/Day16/input_example03.txt")

    expected = 46

    result = solve(file_content)
    assert result == expected


def test_example_input_04():
    file_content = get_input("tests/Day16/input_example04.txt")

    expected = 46

    result = solve(file_content)
    assert result == expected


def test_example_input_05():
    file_content = get_input("tests/Day16/input_example05.txt")

    expected = 54

    result = solve(file_content)
    assert result == expected


def test_example_input_06():
    file_content = get_input("tests/Day16/input_example06.txt")

    expected = 3

    result = solve(file_content)
    assert result == expected


def test_example_input_07():
    file_content = get_input("tests/Day16/input_example07.txt")

    expected = 54

    result = solve(file_content)
    assert result == expected


def test_example_input_08():
    file_content = get_input("tests/Day16/input_example08.txt")

    expected = 7

    result = solve(file_content)
    assert result == expected


def test_example_input_09():
    file_content = get_input("tests/Day16/input_example09.txt")

    expected = 9

    result = solve(file_content)
    assert result == expected


def test_example_input_10():
    file_content = get_input("tests/Day16/input_example10.txt")

    expected = 1

    result = solve(file_content)
    assert result == expected


def test_example_input_11():
    file_content = get_input("tests/Day16/input_example11.txt")

    expected = 0

    result = solve(file_content)
    assert result == expected


def test_example_input_12():
    file_content = get_input("tests/Day16/input_example12.txt")

    expected = 0

    result = solve(file_content)
    assert result == expected


def test_example_input_13():
    file_content = get_input("tests/Day16/input_example13.txt")

    expected = 1

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("tests/Day16/input.txt")

    expected = 1264485568252

    result = solve(file_content)
    assert result == expected
