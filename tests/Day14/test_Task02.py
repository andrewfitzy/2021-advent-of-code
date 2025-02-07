# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day14.Task02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("Day14/input_example.txt")

    expected = 2188189693529

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("Day14/input.txt")

    expected = 2360298895777

    result = solve(file_content)
    assert result == expected
