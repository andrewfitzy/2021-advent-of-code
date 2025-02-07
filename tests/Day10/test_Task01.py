# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day10.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day10/input_example.txt")

    expected = 26397

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("tests/Day10/input.txt")

    expected = 167379

    result = solve(file_content)
    assert result == expected
