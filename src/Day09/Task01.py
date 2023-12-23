def get_output_values(file_content):
    chart = []
    for line in file_content:
        char_list = list(line.strip())
        char_mapped_to_int = map(int, char_list)
        row = list(char_mapped_to_int)
        chart.append(row)
    return chart


def get_adjacent_cells(chart, row_pointer, column_pointer):
    """
    given a board and a co-ordinate, gets the adjacent cells around that point

    """
    cell_left = chart[row_pointer][column_pointer - 1] if column_pointer - 1 >= 0 else ""
    cell_right = chart[row_pointer][column_pointer + 1] if column_pointer + 1 < len(chart[row_pointer]) else ""
    cell_above = chart[row_pointer - 1][column_pointer] if row_pointer - 1 >= 0 else ""
    cell_below = chart[row_pointer + 1][column_pointer] if row_pointer + 1 < len(chart) else ""

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


def solve(file_content):
    chart = get_output_values(file_content)
    low_points = get_low_points(chart)
    risk_level = get_risk_level(low_points)
    return risk_level
