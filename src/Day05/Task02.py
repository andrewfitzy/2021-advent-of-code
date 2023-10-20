"""
--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
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


def process_input(input_from_file):
    """
    Takes an input and converts to a dict, discarding any inputs where x1 != x2 and y1 != y2
    """
    processed_input = []
    for line in input_from_file:
        coord_list = line.split("->", -1)
        start_coord = coord_list[0].strip().split(",")
        end_coord = coord_list[1].strip().split(",")

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
        # This is a vertical line
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
    elif line["start"]["y"] == line["end"]["y"]:
        # This is a horizontal line
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
    elif line["start"]["y"] < line["end"]["y"] and line["start"]["x"] < line["end"]["x"]:
        # goes from top left to bottom right
        x = line["start"]["x"]
        y = line["start"]["y"]
        spaces = line["end"]["x"] - line["start"]["x"]
        spaces += 1
        for i in range(spaces):
            coordinates.append({"x": x + i, "y": y + i})
    elif line["start"]["y"] > line["end"]["y"] and line["start"]["x"] < line["end"]["x"]:
        # goes from bottom left to top right
        x = line["end"]["x"]
        y = line["end"]["y"]
        spaces = line["start"]["y"] - line["end"]["y"]
        spaces += 1
        for i in range(spaces):
            coordinates.append({"x": x - i, "y": y + i})
    elif line["start"]["y"] < line["end"]["y"] and line["start"]["x"] > line["end"]["x"]:
        # goes from top right to bottom left
        x = line["start"]["x"]
        y = line["start"]["y"]
        spaces = line["start"]["x"] - line["end"]["x"]
        spaces += 1
        for i in range(spaces):
            coordinates.append({"x": x - i, "y": y + i})
    elif line["start"]["y"] > line["end"]["y"] and line["start"]["x"] > line["end"]["x"]:
        # goes from bottom left to top right
        x = line["end"]["x"]
        y = line["end"]["y"]
        spaces = line["start"]["y"] - line["end"]["y"]
        spaces += 1
        for i in range(spaces):
            coordinates.append({"x": x + i, "y": y + i})

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


if __name__ == "__main__":
    # get file content
    input_from_file = get_input("input.txt")

    # input_from_file = ['0,9 -> 5,9',
    # '8,0 -> 0,8',
    # '9,4 -> 3,4',
    # '2,2 -> 2,1',
    # '7,0 -> 7,4',
    # '6,4 -> 2,0',
    # '0,9 -> 2,9',
    # '3,4 -> 1,4',
    # '0,0 -> 8,8',
    # '5,5 -> 8,2']

    processed_input = process_input(input_from_file)

    map = plot_coords(processed_input)
    # for row in map:
    #     print(row)

    result = get_result(map)
    print("RESULT: " + str(result))
