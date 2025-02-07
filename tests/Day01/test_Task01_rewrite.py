# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day01.Task01_rewrite import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("Day01/input_example.txt")

    expected = 7

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("Day01/input.txt")

    expected = 1616

    result = solve(file_content)
    assert result == expected
