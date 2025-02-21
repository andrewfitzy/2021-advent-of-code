# Standard Library
import re


def solve(file_content):
    input = file_content[0]

    left, right, bottom, top = map(int, re.findall(r"-?\d+", input))

    min_x, max_x = get_min_max_x(right)
    min_y, max_y = get_min_max_y(bottom, top)

    starting_combinations = set()
    for x_pointer in range(min_x, max_x):
        for y_pointer in range(min_y, max_y):
            if position_enters_trench(x_pointer, y_pointer, left, right, bottom, top):
                starting_combinations.add((x_pointer, y_pointer))
    return len(starting_combinations)


def get_min_max_x(right):
    x_start = 0
    x_end = right + 1
    return (x_start, x_end)


def get_min_max_y(bottom, top):
    y_start = bottom
    y_end = abs(bottom) + 1
    return (y_start, y_end)


def position_enters_trench(x_pointer, y_pointer, left, right, bottom, top):
    x = 0
    y = 0
    range_end = right if right > abs(bottom) else abs(bottom)
    range_end = range_end * 2
    for iterator in range(range_end):
        x_step = x_pointer - iterator
        x_step = x_step if x_step > 0 else 0
        x = x + x_step
        y_step = y_pointer - iterator
        y = y + y_step
        if x > right or y < bottom:
            break
        if left <= x <= right and bottom <= y <= top:
            return True
    return False
