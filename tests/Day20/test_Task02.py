# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day20.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("Day20/input_example.txt")

    expected = 3351

    result = solve(file_content, 50)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("Day20/input.txt")

    expected = 16383

    result = solve(file_content, 50)
    assert result == expected
