"""
--- Day 11: Dumbo Octopus ---
--- Part Two ---
It seems like the individual flashes aren't bright enough to navigate. However, you might have a better option: the flashes seem to be synchronizing!

In the example above, the first time all octopuses flash simultaneously is step 195:

After step 193:
5877777777
8877777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777

After step 194:
6988888888
9988888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888

After step 195:
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. What is the first step during which all octopuses flash?
"""

LIGHT_PIXEL = '#'
DARK_PIXEL = '.'


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


def convert_image_to_2d_array(image):
    """
    takes the raw bitmap image and converts into a 2d array of values.
    """
    image_array = []
    for line in image:
        char_list = list(line.strip())
        char_mapped_to_int = map(int, char_list)
        row = list(char_mapped_to_int)
        image_array.append(row)
    return image_array


def get_adjacent_cells(row_pointer, column_pointer, height, width):
    """
    given a board and a co-ordinate, gets the adjacent cells around that point
    """
    adjacent_cells = []
    if row_pointer - 1 >= 0 and column_pointer - 1 >= 0:
        # above left
        adjacent_cells.append({'x': column_pointer - 1, 'y': row_pointer - 1})
    if row_pointer - 1 >= 0:
        # above
        adjacent_cells.append({'x': column_pointer, 'y': row_pointer - 1})
    if row_pointer - 1 >= 0 and column_pointer + 1 < width:
        # above right
        adjacent_cells.append({'x': column_pointer + 1, 'y': row_pointer - 1})

    if column_pointer - 1 >= 0:
        # left
        adjacent_cells.append({'x': column_pointer - 1, 'y': row_pointer})
    if column_pointer + 1 < width:
        # right
        adjacent_cells.append({'x': column_pointer + 1, 'y': row_pointer})

    if row_pointer + 1 < height and column_pointer - 1 >= 0:
        # below left
        adjacent_cells.append({'x': column_pointer - 1, 'y': row_pointer + 1})
    if row_pointer + 1 < height:
        # below
        adjacent_cells.append({'x': column_pointer, 'y': row_pointer + 1})
    if row_pointer + 1 < height and column_pointer + 1 < width:
        # below right
        adjacent_cells.append({'x': column_pointer + 1, 'y': row_pointer + 1})

    return adjacent_cells


def get_list_of_points(image_array):
    """
    converts a 2d array into a list of points for downstream processing
    """
    points = []
    for row_pointer in range(0, len(image_array)):
        for cell_pointer in range(0, len(image_array[row_pointer])):
            points.append({
                'x': cell_pointer,
                'y': row_pointer,
            })
    return points


def increment_points(image_array, points, step_change):
    """
    do stuff here
    """
    knock_ons = []
    flashes = 0
    for point in points:
        point_value = image_array[point['y']][point['x']]

        if point_value > 0 or (point_value == 0 and step_change):
            point_value += 1

        image_array[point['y']][point['x']] = point_value

        if point_value == 10:
            image_array[point['y']][point['x']] = 0
            flashes += 1
            adjacent_cells = get_adjacent_cells(point['y'], point['x'], len(image_array), len(image_array[0]))
            knock_ons = knock_ons + adjacent_cells

    return {
        'knock_ons': knock_ons,
        'flashes': flashes
    }


def process_steps(image_array):
    """
    Used to monitor the octopuses
    """
    synchronized_flash = 0
    while True:
        points = get_list_of_points(image_array)
        step_change = True
        step_flashes = 0
        num_of_octopods = len(points)
        while len(points) != 0:
            result = increment_points(image_array, points, step_change)
            points = result['knock_ons']
            step_flashes += result['flashes']
            step_change = False

        synchronized_flash += 1
        if step_flashes == num_of_octopods:
            return synchronized_flash


def process_file(filename, expected_result):
    """
    Given a file, a number of enhancement iterations and an expected result, process the file based on the inputs and
    assert that the result is as expected
    """
    input_from_file = get_input(filename)

    octopuses = convert_image_to_2d_array(input_from_file)

    synchronized_flash = process_steps(octopuses)

    assert synchronized_flash == expected_result, 'Output is not as expected, expected ' + str(expected_result)\
                                                  + ' but got ' + str(synchronized_flash)

    print('RESULT: Synchronized flash happens at step, ' + str(synchronized_flash) + ' for input ' + filename)


if __name__ == '__main__':
    process_file('input_example.txt', 195)

    process_file('input.txt', 437)
