# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day10.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("Day10/input_example.txt")

    expected = 288957

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("Day10/input.txt")

    expected = 2776842859

    result = solve(file_content)
    assert result == expected
