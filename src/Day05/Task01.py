def process_input(input_from_file):
    """
    Takes an input and converts to a dict, discarding any inputs where x1 != x2 and y1 != y2
    """
    processed_input = []
    for line in input_from_file:
        coord_list = line.split("->", -1)
        start_coord = coord_list[0].strip().split(",")
        end_coord = coord_list[1].strip().split(",")

        if start_coord[0] == end_coord[0] or start_coord[1] == end_coord[1]:
            processed_input.append(
                {
                    "start": {"x": int(start_coord[0]), "y": int(start_coord[1])},
                    "end": {"x": int(end_coord[0]), "y": int(end_coord[1])},
                }
            )
    return processed_input


def get_map_dimension(processed_input):
    biggest_x = 0
    biggest_y = 0
    for line in processed_input:
        if biggest_x < line["start"]["x"]:
            biggest_x = line["start"]["x"]
        if biggest_x < line["end"]["x"]:
            biggest_x = line["end"]["x"]
        if biggest_y < line["start"]["y"]:
            biggest_y = line["start"]["y"]
        if biggest_y < line["end"]["y"]:
            biggest_y = line["end"]["y"]
    biggest_x += 1
    biggest_y += 1
    return {"width": biggest_x, "height": biggest_y}


def get_cells_to_fill(line):
    """
    lines contains a start and end point, this will work out the co-ordinates of cells in between that
    need to be incremented based on the start and end.
    """
    coordinates = []
    if line["start"]["x"] == line["end"]["x"]:
        x = line["start"]["x"]
        if line["start"]["y"] < line["end"]["y"]:
            y = line["start"]["y"]
            spaces = line["end"]["y"] - line["start"]["y"]
        else:
            y = line["end"]["y"]
            spaces = line["start"]["y"] - line["end"]["y"]
        spaces += 1
        for i in range(spaces):
            coordinates.append({"x": x, "y": y + i})

    if line["start"]["y"] == line["end"]["y"]:
        y = line["start"]["y"]
        if line["start"]["x"] < line["end"]["x"]:
            x = line["start"]["x"]
            spaces = line["end"]["x"] - line["start"]["x"]
        else:
            x = line["end"]["x"]
            spaces = line["start"]["x"] - line["end"]["x"]
        spaces += 1
        for i in range(spaces):
            coordinates.append({"x": x + i, "y": y})
    return coordinates


def plot_coords(processed_input):
    """
    takes an input and plots the points on a 2D array which is returned
    """
    dimension = get_map_dimension(processed_input)

    map = [[0 for x in range(dimension["width"])] for y in range(dimension["height"])]

    for line in processed_input:
        cells_to_fill = get_cells_to_fill(line)
        for cell in cells_to_fill:
            map[cell["y"]][cell["x"]] += 1
    return map


def get_result(map):
    """
    count the number of cells where the value is > 1
    """
    result = 0
    for row in map:
        for cell in row:
            if cell > 1:
                result += 1
    return result


def solve(file_content):
    processed_input = process_input(file_content)
    map = plot_coords(processed_input)
    result = get_result(map)
    return result
