# Standard Library
import re


def solve(file_content):
    input = file_content[0]

    _, _, bottom, _ = map(int, re.findall(r"-?\d+", input))

    y_end = abs(bottom)  # for pt 1 we only want to go up

    height = 0
    for count in reversed(range(y_end)):
        height = height + count

    return height
