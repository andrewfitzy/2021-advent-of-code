# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day22.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example_input_01():
    file_content = get_input("tests/Day22/input_example_01.txt")

    expected = 39

    result = solve(file_content)
    assert result == expected


def test_example_input_02():
    file_content = get_input("tests/Day22/input_example_02.txt")

    expected = 590784

    result = solve(file_content)
    assert result == expected


def test_example_input_03():
    file_content = get_input("tests/Day22/input_example_03.txt")

    expected = 474140

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("tests/Day22/input.txt")

    expected = 658691

    result = solve(file_content)
    assert result == expected
