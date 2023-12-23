LIGHT_PIXEL = "#"
DARK_PIXEL = "."


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
        adjacent_cells.append({"x": column_pointer - 1, "y": row_pointer - 1})
    if row_pointer - 1 >= 0:
        # above
        adjacent_cells.append({"x": column_pointer, "y": row_pointer - 1})
    if row_pointer - 1 >= 0 and column_pointer + 1 < width:
        # above right
        adjacent_cells.append({"x": column_pointer + 1, "y": row_pointer - 1})

    if column_pointer - 1 >= 0:
        # left
        adjacent_cells.append({"x": column_pointer - 1, "y": row_pointer})
    if column_pointer + 1 < width:
        # right
        adjacent_cells.append({"x": column_pointer + 1, "y": row_pointer})

    if row_pointer + 1 < height and column_pointer - 1 >= 0:
        # below left
        adjacent_cells.append({"x": column_pointer - 1, "y": row_pointer + 1})
    if row_pointer + 1 < height:
        # below
        adjacent_cells.append({"x": column_pointer, "y": row_pointer + 1})
    if row_pointer + 1 < height and column_pointer + 1 < width:
        # below right
        adjacent_cells.append({"x": column_pointer + 1, "y": row_pointer + 1})

    return adjacent_cells


def get_list_of_points(image_array):
    """
    converts a 2d array into a list of points for downstream processing
    """
    points = []
    for row_pointer in range(0, len(image_array)):
        for cell_pointer in range(0, len(image_array[row_pointer])):
            points.append(
                {
                    "x": cell_pointer,
                    "y": row_pointer,
                }
            )
    return points


def increment_points(image_array, points, step_change):
    """
    do stuff here
    """
    knock_ons = []
    flashes = 0
    for point in points:
        point_value = image_array[point["y"]][point["x"]]

        if point_value > 0 or (point_value == 0 and step_change):
            point_value += 1

        image_array[point["y"]][point["x"]] = point_value

        if point_value == 10:
            image_array[point["y"]][point["x"]] = 0
            flashes += 1
            adjacent_cells = get_adjacent_cells(point["y"], point["x"], len(image_array), len(image_array[0]))
            knock_ons = knock_ons + adjacent_cells

    return {"knock_ons": knock_ons, "flashes": flashes}


def process_steps(iterations, image_array):
    """
    Used to monitor the octopuses
    """
    flashes = 0
    for iteration in range(iterations):
        points = get_list_of_points(image_array)
        step_change = True
        while len(points) != 0:
            result = increment_points(image_array, points, step_change)
            points = result["knock_ons"]
            flashes += result["flashes"]
            step_change = False

    return flashes


def solve(file_content):
    """
    Given a file, a number of enhancement iterations and an expected result, process the file based on the inputs and
    assert that the result is as expected
    """
    octopuses = convert_image_to_2d_array(file_content)

    flashes = process_steps(100, octopuses)

    return flashes
