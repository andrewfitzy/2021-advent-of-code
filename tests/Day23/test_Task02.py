# Standard Library
import os

# Dependencies
import pytest

# From apps
from Day23.Task02 import is_valid_option, solve
from tests.test_utils.get_input import get_input
from util.point import Point


def test_is_valid_option_with_target_not_empty():
    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "B", "#", "A", "#", "C", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(
        3, 2, Point(5, 2), [Point(3, 1), Point(4, 1), Point(5, 1), Point(5, 2)], floor_plan
    )
    assert valid is False
    assert response == "555: TARGET NOT EMPTY"


def test_is_valid_option_with_blocked_path_to_target():
    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "A", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "B", "#", ".", "#", "C", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(
        3, 2, Point(5, 2), [Point(3, 1), Point(4, 1), Point(5, 1), Point(5, 2)], floor_plan
    )
    assert valid is False
    assert response == "555: PATH TO TARGET NOT EMPTY"


def test_is_valid_option_with_valid_hallway_target():
    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "B", "#", "A", "#", "C", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(
        3, 2, Point(6, 1), [Point(3, 1), Point(4, 1), Point(5, 1), Point(6, 1)], floor_plan
    )
    assert valid is True
    assert response == "000: VALID HALLWAY POINT"


def test_is_valid_option_with_not_a_hallway_target():
    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "B", "#", "A", "#", "C", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(3, 2, Point(5, 1), [Point(3, 1), Point(4, 1), Point(5, 1)], floor_plan)
    assert valid is False
    assert response == "555: NOT A TARGET ROOM"


def test_is_valid_option_with_not_a_valid_target_room():
    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "C", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "B", "#", "A", "#", ".", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(
        3, 2, Point(7, 2), [Point(3, 1), Point(4, 1), Point(5, 1), Point(6, 1), Point(7, 1), Point(7, 2)], floor_plan
    )
    assert valid is False
    assert response == "555: NOT A TARGET ROOM"


def test_is_valid_option_with_moves_in_a_room():
    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "C", "C", ".", ".", ".", ".", ".", ".", ".", ".", "C", "#"],
        ["#", "#", "#", "B", "#", "A", "#", ".", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(7, 5, Point(7, 4), [Point(7, 4)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"

    valid, response = is_valid_option(7, 5, Point(7, 3), [Point(7, 4), Point(7, 3)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"

    valid, response = is_valid_option(7, 5, Point(7, 2), [Point(7, 4), Point(7, 3), Point(7, 2)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"

    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "C", "C", ".", ".", ".", ".", ".", ".", ".", ".", "C", "#"],
        ["#", "#", "#", "B", "#", "A", "#", ".", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(7, 4, Point(7, 3), [Point(7, 3)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"

    valid, response = is_valid_option(7, 4, Point(7, 2), [Point(7, 3), Point(7, 2)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"

    valid, response = is_valid_option(7, 4, Point(7, 5), [Point(7, 5)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"

    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "C", "C", ".", ".", ".", ".", ".", ".", ".", ".", "C", "#"],
        ["#", "#", "#", "B", "#", "A", "#", ".", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(7, 3, Point(7, 2), [Point(7, 2)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"

    valid, response = is_valid_option(7, 3, Point(7, 4), [Point(7, 4)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"

    valid, response = is_valid_option(7, 3, Point(7, 5), [Point(7, 4), Point(7, 5)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"

    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "C", "C", ".", ".", ".", ".", ".", ".", ".", ".", "C", "#"],
        ["#", "#", "#", "B", "#", "A", "#", "C", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]

    valid, response = is_valid_option(7, 2, Point(7, 3), [Point(7, 3)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"

    valid, response = is_valid_option(7, 2, Point(7, 4), [Point(7, 3), Point(7, 4)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"

    valid, response = is_valid_option(7, 2, Point(7, 5), [Point(7, 3), Point(7, 4), Point(7, 5)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN A ROOM"


def test_is_valid_option_with_moving_in_hallway():
    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "C", "C", ".", ".", ".", ".", ".", ".", ".", ".", "C", "#"],
        ["#", "#", "#", "C", "#", "A", "#", ".", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "B", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(2, 1, Point(4, 1), [Point(3, 1), Point(4, 1)], floor_plan)
    assert valid is False
    assert response == "555: MOVING IN the HALLWAY"


def test_is_valid_option_with_incorrect_amphipod_in_the_room_in_a_room():
    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "C", "C", ".", ".", ".", ".", ".", ".", ".", ".", "C", "#"],
        ["#", "#", "#", "C", "#", "A", "#", ".", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", "B", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(
        3,
        2,
        Point(7, 4),
        [Point(3, 1), Point(4, 1), Point(5, 1), Point(6, 1), Point(7, 1), Point(7, 2), Point(7, 3), Point(7, 4)],
        floor_plan,
    )
    assert valid is False
    assert response == "555: ROOM CONTAINS OTHER AMPHIPODS"


def test_is_valid_option():
    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "C", "C", ".", ".", ".", ".", ".", ".", ".", "B", "C", "#"],
        ["#", "#", "#", "C", "#", "A", "#", ".", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(
        3,
        2,
        Point(7, 5),
        [
            Point(3, 1),
            Point(4, 1),
            Point(5, 1),
            Point(6, 1),
            Point(7, 1),
            Point(7, 2),
            Point(7, 3),
            Point(7, 4),
            Point(7, 5),
        ],
        floor_plan,
    )
    assert valid is True
    assert response == "000: ALL CHECKS PASSED"


def test_is_valid_option_with_target_not_furthest_into_room():
    floor_plan = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "C", "C", ".", ".", ".", ".", ".", ".", ".", "B", "C", "#"],
        ["#", "#", "#", "C", "#", "A", "#", ".", "#", "D", "#", "#", "#"],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "A", "#", "B", "#", ".", "#", "D", "#", " ", " "],
        [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    ]
    valid, response = is_valid_option(
        3,
        2,
        Point(7, 4),
        [Point(3, 1), Point(4, 1), Point(5, 1), Point(6, 1), Point(7, 1), Point(7, 2), Point(7, 3), Point(7, 4)],
        floor_plan,
    )
    assert valid is False
    assert response == "555: NOT FURTHEST IN ROOM"

    valid, response = is_valid_option(
        3,
        2,
        Point(7, 3),
        [Point(3, 1), Point(4, 1), Point(5, 1), Point(6, 1), Point(7, 1), Point(7, 2), Point(7, 3)],
        floor_plan,
    )
    assert valid is False
    assert response == "555: NOT FURTHEST IN ROOM"

    valid, response = is_valid_option(
        3, 2, Point(7, 2), [Point(3, 1), Point(4, 1), Point(5, 1), Point(6, 1), Point(7, 1), Point(7, 2)], floor_plan
    )
    assert valid is False
    assert response == "555: NOT FURTHEST IN ROOM"


def test_example_input():
    file_content = get_input("tests/Day23/input_example.txt")

    expected = 44169

    result = solve(file_content)
    assert result == expected


@pytest.mark.skipif(
    os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
)
def test_real_input():
    file_content = get_input("tests/Day23/input.txt")

    expected = 47234

    result = solve(file_content)
    assert result == expected
