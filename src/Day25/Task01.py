# From apps
from util.point import Point


def solve(file_content):
    # build up 2D array of input
    # we can do two passes, first pass does movement of cucumbers into free spaces, second pass checks the space they left behind to see if

    sea_floor = []
    for line in file_content:
        sea_floor.append(list(line))

    has_moved = True
    steps = 0
    while has_moved:
        has_moved, sea_floor = move_cucumbers(sea_floor=sea_floor)
        steps = steps + 1
    return steps


def move_cucumbers(sea_floor):
    tracking_sea_floor = [row[:] for row in sea_floor]

    has_moved = False
    width = len(tracking_sea_floor[0])
    height = len(tracking_sea_floor)

    cucumber_locations = {}
    for row_pointer in range(0, height):
        for col_pointer in range(0, width):
            content = tracking_sea_floor[row_pointer][col_pointer]
            if content in [">", "v"]:
                locations = cucumber_locations.get(content, [])
                locations.append(Point(x=col_pointer, y=row_pointer))
                cucumber_locations[content] = locations

    # First move > cucumbers
    new_sea_floor_first_move = [row[:] for row in tracking_sea_floor]
    for location in cucumber_locations[">"]:
        next_col = (location.x + 1) % width
        if tracking_sea_floor[location.y][next_col] == ".":
            has_moved = True
            new_sea_floor_first_move[location.y][location.x] = "."
            new_sea_floor_first_move[location.y][next_col] = ">"

    # Then move v cucumbers
    new_sea_floor_second_move = [row[:] for row in new_sea_floor_first_move]
    for location in cucumber_locations["v"]:
        next_row = (location.y + 1) % height
        if new_sea_floor_first_move[next_row][location.x] == ".":
            has_moved = True
            new_sea_floor_second_move[location.y][location.x] = "."
            new_sea_floor_second_move[next_row][location.x] = "v"

    return (has_moved, new_sea_floor_second_move)
