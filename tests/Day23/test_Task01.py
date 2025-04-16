# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day23.Task01 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    # SLOOOW, take about 1 minute to run
    file_content = get_input("tests/Day23/input_example.txt")

    expected = 12521

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    # SLOOOW, take about 1 minute to run
    file_content = get_input("tests/Day23/input.txt")

    expected = 17120

    result = solve(file_content)
    assert result == expected
