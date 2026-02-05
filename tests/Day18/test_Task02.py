# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day18.Task02 import add, calculate_magnitude, explode, needs_exploding, needs_splitting, solve, split
from tests.test_utils.get_input import get_input


def test_add():
    input01 = "[1,2]"
    input02 = "[[3,4],5]"

    expected = "[[1,2],[[3,4],5]]"

    result = add(input01, input02)
    assert result == expected


def test_needs_exploding_true():
    input = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"

    expected = True

    result = needs_exploding(input)
    assert result == expected


def test_needs_exploding_false():
    input = "[[3,[2,[8,0]]],[9,[5,[4,0]]]]"

    expected = False

    result = needs_exploding(input)
    assert result == expected


def test_explode_01():
    input = "[[[[[9,8],1],2],3],4]"

    expected = "[[[[0,9],2],3],4]"

    result = explode(input)
    assert result == expected


def test_explode_02():
    input = "[7,[6,[5,[4,[3,2]]]]]"

    expected = "[7,[6,[5,[7,0]]]]"

    result = explode(input)
    assert result == expected


def test_explode_03():
    input = "[[6,[5,[4,[3,2]]]],1]"

    expected = "[[6,[5,[7,0]]],3]"

    result = explode(input)
    assert result == expected


def test_explode_04():
    input = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"

    expected = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"

    result = explode(input)
    assert result == expected


def test_explode_05():
    input = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"

    expected = "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"

    result = explode(input)
    assert result == expected


def test_needs_splitting_true():
    input = "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"

    expected = True

    result = needs_splitting(input)
    assert result == expected


def test_needs_splitting_false():
    input = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"

    expected = False

    result = needs_splitting(input)
    assert result == expected


def test_split_01():
    input = "[[[[0,7],4],[15,[0,13]]],[1,1]]"

    expected = "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"

    result = split(input)
    assert result == expected


def test_split_02():
    input = "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"

    expected = "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"

    result = split(input)
    assert result == expected


def test_calculate_magnitude_01():
    input = "[[1,2],[[3,4],5]]"

    expected = 143

    result = calculate_magnitude(input)
    assert result == expected


def test_calculate_magnitude_02():
    input = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

    expected = 1384

    result = calculate_magnitude(input)
    assert result == expected


def test_calculate_magnitude_03():
    input = "[[[[1,1],[2,2]],[3,3]],[4,4]]"

    expected = 445

    result = calculate_magnitude(input)
    assert result == expected


def test_calculate_magnitude_04():
    input = "[[[[3,0],[5,3]],[4,4]],[5,5]]"

    expected = 791

    result = calculate_magnitude(input)
    assert result == expected


def test_calculate_magnitude_05():
    input = "[[[[5,0],[7,4]],[5,5]],[6,6]]"

    expected = 1137

    result = calculate_magnitude(input)
    assert result == expected


def test_calculate_magnitude_06():
    input = "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"

    expected = 3488

    result = calculate_magnitude(input)
    assert result == expected


def test_example_input01():
    file_content = get_input("tests/Day18/input_example01.txt")

    expected = 3805

    result = solve(file_content)
    assert result == expected


def test_example_input02():
    file_content = get_input("tests/Day18/input_example02.txt")

    expected = 3993

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("tests/Day18/input.txt")

    expected = 4855

    result = solve(file_content)
    assert result == expected
