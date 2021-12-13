"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?
"""


def get_output_values(filename):
    """
    Takes a filename and returns a list of ints from the file
    """
    chart = []
    with open(filename) as f:
        for line in f:
            char_list = list(line.strip())
            char_mapped_to_int = map(int, char_list)
            row = list(char_mapped_to_int)
            chart.append(row)
    return chart


def get_adjacent_cells(chart, row_pointer, column_pointer):
    """
    given a board and a co-ordinate, gets the adjacent cells around that point

    """
    cell_left = chart[row_pointer][column_pointer - 1] if column_pointer - 1 >= 0 else ''
    cell_right = chart[row_pointer][column_pointer + 1] if column_pointer + 1 < len(chart[row_pointer]) else ''
    cell_above = chart[row_pointer - 1][column_pointer] if row_pointer - 1 >= 0 else ''
    cell_below = chart[row_pointer + 1][column_pointer] if row_pointer + 1 < len(chart) else ''

    adjacent_cells = []

    if len(str(cell_left)) > 0:
        adjacent_cells.append(cell_left)

    if len(str(cell_right)) > 0:
        adjacent_cells.append(cell_right)

    if len(str(cell_above)) > 0:
        adjacent_cells.append(cell_above)

    if len(str(cell_below)) > 0:
        adjacent_cells.append(cell_below)

    return adjacent_cells


def is_low_point(cell, adjacent_cells):
    """
    takes a board and finds all the points that are lower than all the surrounding points
    """
    for adjacent_cell in adjacent_cells:
        if adjacent_cell <= cell:
            return False
    return True


def get_low_points(chart):
    """
    takes a board and finds all the points that are lower than all the surrounding points
    """
    low_points = []
    row_pointer = 0
    while row_pointer < len(chart):
        column_pointer = 0
        while column_pointer < len(chart[row_pointer]):
            adjacent_cells = get_adjacent_cells(chart, row_pointer, column_pointer)
            cell = chart[row_pointer][column_pointer]
            if is_low_point(cell, adjacent_cells):
                low_points.append(cell)

            column_pointer += 1
        row_pointer += 1

    return low_points


def get_risk_level(low_points):
    risk_level = 0
    for low_point in low_points:
        risk_level = risk_level + low_point
        risk_level = risk_level + 1
    return risk_level


if __name__ == '__main__':
    # get file content
    chart = get_output_values('input.txt')
    low_points = get_low_points(chart)
    risk_level = get_risk_level(low_points)
    print(low_points)
    print(risk_level)
