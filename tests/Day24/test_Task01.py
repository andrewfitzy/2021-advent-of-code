# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day24.Task01 import process_model_number, solve
from tests.test_utils.get_input import get_input


def test_process_model_number_01():
    file_content = get_input("tests/Day24/input_example_01.txt")

    result = process_model_number(file_content, 5)
    assert result["w"] == 0
    assert result["x"] == -5
    assert result["y"] == 0
    assert result["z"] == 0


def test_process_model_number_02_with_equal_true():
    file_content = get_input("tests/Day24/input_example_02.txt")

    result = process_model_number(file_content, 39)
    assert result["w"] == 0
    assert result["x"] == 9
    assert result["y"] == 0
    assert result["z"] == 1


def test_process_model_number_03_with_equal_false():
    file_content = get_input("tests/Day24/input_example_02.txt")

    result = process_model_number(file_content, 49)
    assert result["w"] == 0
    assert result["x"] == 9
    assert result["y"] == 0
    assert result["z"] == 0


def test_process_model_number_04():
    file_content = get_input("tests/Day24/input_example_03.txt")

    result = process_model_number(file_content, 7)
    assert result["w"] == 0
    assert result["x"] == 1
    assert result["y"] == 1
    assert result["z"] == 1


def test_process_model_number_05():
    file_content = get_input("tests/Day24/input.txt")

    result = process_model_number(file_content, 12345678912345)
    assert result["w"] == 5
    assert result["x"] == 1
    assert result["y"] == 9
    assert result["z"] == 67926387


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("tests/Day24/input.txt")

    expected = 91897399498995

    result = solve(file_content)
    assert result == expected
