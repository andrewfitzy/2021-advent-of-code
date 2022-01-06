"""
--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
"""


def get_input(filename):
    """
    Takes a filename and returns a list of lines from the file
    """
    output = []
    with open(filename) as f:
        for line in f:
            tmp_line = line.strip()
            output.append(tmp_line)
    return output


def make_chart(input):
    """
    Takes a filename and returns a list of ints from the file
    """
    chart = []
    for line in input:
        char_list = list(line.strip())
        char_mapped_to_int = map(int, char_list)
        row = list(char_mapped_to_int)
        chart.append(row)
    return chart


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
    low_point_locations = {}
    basin_number = 0
    row_pointer = 0
    while row_pointer < len(chart):
        column_pointer = 0
        while column_pointer < len(chart[row_pointer]):
            adjacent_cells = get_adjacent_cells(chart, row_pointer, column_pointer)
            cell = chart[row_pointer][column_pointer]
            if is_low_point(cell, adjacent_cells):
                low_points.append(cell)

                low_point_locations[str(basin_number)] = {
                    'row': row_pointer,
                    'col': column_pointer,
                }

                basin_number += 1

            column_pointer += 1
        row_pointer += 1

    return low_point_locations


def get_valid_adjacent_cells(visited_cells, chart, row_pointer, column_pointer):
    """
    given a board and a co-ordinate, gets the adjacent cells around that point if
    - they are within bounds
    - not 9
    - not already seen
    """
    valid_adjacent_cells = {}
    if column_pointer - 1 >= 0:
        if chart[row_pointer][column_pointer - 1] < 9:
            left = str(column_pointer-1)+","+str(row_pointer)
            if left not in visited_cells:
                valid_adjacent_cells['left'] = {
                    'row': row_pointer,
                    'col': column_pointer-1
                }

    if column_pointer + 1 < len(chart[row_pointer]):
        if chart[row_pointer][column_pointer + 1] < 9:
            right = str(column_pointer+1)+","+str(row_pointer)
            if right not in visited_cells:
                valid_adjacent_cells['right'] = {
                    'row': row_pointer,
                    'col': column_pointer+1
                }

    if row_pointer - 1 >= 0:
        if chart[row_pointer - 1][column_pointer] < 9:
            above = str(column_pointer)+","+str(row_pointer-1)
            if above not in visited_cells:
                valid_adjacent_cells['above'] = {
                    'row': row_pointer-1,
                    'col': column_pointer
                }

    if row_pointer + 1 < len(chart):
        if chart[row_pointer + 1][column_pointer] < 9:
            below = str(column_pointer)+","+str(row_pointer+1)
            if below not in visited_cells:
                valid_adjacent_cells['below'] = {
                    'row': row_pointer+1,
                    'col': column_pointer
                }

    return valid_adjacent_cells


def get_basin(visited_cells, chart, column, row):
    """
    given a chart and a point
        get the surrounding cells
        if cell isn't in the list of processed cells

        for each low point, get the surrounding cells that aren't 9s
        do some recursion and it will get what we want.
        keep track with a visited set/list too.
    """

    coordinate = [str(column)+","+str(row)]
    visited_cells.update(coordinate)
    valid_adjacent_cells = get_valid_adjacent_cells(visited_cells, chart, row, column)
    if 'left' in valid_adjacent_cells:
        coordinate = coordinate + get_basin(visited_cells, chart, valid_adjacent_cells['left']['col'], valid_adjacent_cells['left']['row'])

    if 'right' in valid_adjacent_cells:
        coordinate = coordinate + get_basin(visited_cells, chart, valid_adjacent_cells['right']['col'], valid_adjacent_cells['right']['row'])

    if 'above' in valid_adjacent_cells:
        coordinate = coordinate + get_basin(visited_cells, chart, valid_adjacent_cells['above']['col'], valid_adjacent_cells['above']['row'])

    if 'below' in valid_adjacent_cells:
        coordinate = coordinate + get_basin(visited_cells, chart, valid_adjacent_cells['below']['col'], valid_adjacent_cells['below']['row'])

    return coordinate


def get_basins(chart, low_points):
    """
    for a chart and list of low points, get all the basins the low points are part of
    """
    basins = {}

    visited_cells = set()
    for basin_id in low_points:
        print('PROCESS BASIN: ' + str(basin_id))
        low_point = low_points.get(basin_id)
        low_point_coordinate = str(low_point['col']) + "," + str(low_point['row'])
        if low_point_coordinate not in visited_cells:
            basin = get_basin(visited_cells, chart, low_point['col'], low_point['row'])
            basins[str(basin_id)] = set(basin)

    return basins


def calculate_map_score(basins):
    basin_sizes = []
    for basin in basins:
        basin_size = len(basins[basin])
        basin_sizes.append(basin_size)

    basin_sizes.sort(reverse=True)

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == '__main__':
    # get file content
    input_from_file = get_input('input.txt')

    # input_from_file = ['2199943210',
    #                    '3987894921',
    #                    '9856789892',
    #                    '8767896789',
    #                    '9899965678']

    chart = make_chart(input_from_file)
    low_points = get_low_points(chart)

    print('low_points')
    print(low_points)

    basins = get_basins(chart, low_points)

    print('basins')
    print(basins)

    map_score = calculate_map_score(basins)

    print('Map score: ' + str(map_score))

