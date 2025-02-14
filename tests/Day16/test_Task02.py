# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day16.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day16/input_example01.txt")

    expected = 1

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("tests/Day16/input.txt")

    expected = 1

    result = solve(file_content)
    assert result == expected
