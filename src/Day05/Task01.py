"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
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

    result = get_result(map)
    print("RESULT: " + str(result))
