# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day11.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/Day11/input_example.txt")

    expected = 195

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("tests/Day11/input.txt")

    expected = 437

    result = solve(file_content)
    assert result == expected
