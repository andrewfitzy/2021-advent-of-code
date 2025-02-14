# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day16.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example_input_01():
    file_content = get_input("tests/Day16/input_example01.txt")

    expected = 6

    result = solve(file_content)
    assert result == expected


def test_example_input_02():
    file_content = get_input("tests/Day16/input_example02.txt")

    expected = 16

    result = solve(file_content)
    assert result == expected


def test_example_input_03():
    file_content = get_input("tests/Day16/input_example03.txt")

    expected = 12

    result = solve(file_content)
    assert result == expected


def test_example_input_04():
    file_content = get_input("tests/Day16/input_example04.txt")

    expected = 23

    result = solve(file_content)
    assert result == expected


def test_example_input_05():
    file_content = get_input("tests/Day16/input_example05.txt")

    expected = 31

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("tests/Day16/input.txt")

    expected = 991

    result = solve(file_content)
    assert result == expected
