# Standard Library
import heapq
import types
from dataclasses import dataclass, field
from typing import Any

# From apps
from util.point import Point

content = types.SimpleNamespace()
content.SPACE = " "
content.WALL = "#"
content.VACANT = "."

amphipod = types.SimpleNamespace()
amphipod.AMBER = "A"
amphipod.BRONZE = "B"
amphipod.COPPER = "C"
amphipod.DESERT = "D"

EXPECTED = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "A", "#", "B", "#", "C", "#", "D", "#", "#", "#"],
    [" ", " ", "#", "A", "#", "B", "#", "C", "#", "D", "#", " ", " "],
    [" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
]

AMPHIPODS = {
    amphipod.AMBER: 1,
    amphipod.BRONZE: 10,
    amphipod.COPPER: 100,
    amphipod.DESERT: 1000,
}

TARGET_ROOMS = {
    amphipod.AMBER: {Point(3, 2), Point(3, 3)},
    amphipod.BRONZE: {Point(5, 2), Point(5, 3)},
    amphipod.COPPER: {Point(7, 2), Point(7, 3)},
    amphipod.DESERT: {Point(9, 2), Point(9, 3)},
}

JUNCTIONS = {Point(3, 1), Point(5, 1), Point(7, 1), Point(9, 1)}

HALLWAY_STOP_POINTS = {Point(1, 1), Point(2, 1), Point(4, 1), Point(6, 1), Point(8, 1), Point(10, 1), Point(11, 1)}

HALLWAY = 1


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)
    route: Any = field(compare=False)


def solve(file_content):
    floor_plan = get_floor_plan(file_content)
    routes = build_all_routes(floor_plan)

    cost = get_cheapest_solution(floor_plan, routes)
    return cost


###
###
### Below is task setup, processing the board and routes into useful structures
###
###
def get_floor_plan(file_content):
    line_length = 0
    floor_plan = []
    for line in file_content:
        input_line = []
        if len(line) > line_length:
            line_length = len(line)
        padding = []
        if len(line) < line_length:
            side_padding = int((line_length - len(line)) / 2)
            padding = [" "] * side_padding

        for pad in padding:
            input_line.append(pad)

        for character in line:
            input_line.append(character)

        for pad in padding:
            input_line.append(pad)

        floor_plan.append(input_line)
    return floor_plan


def build_all_routes(floor_plan):
    routes = {}
    # #############
    # #...........#
    # ###B#C#B#D###
    #   #A#D#C#A#
    #   #########

    # Build a list of possible routes, keyed on the start point and giving a route to the list of stopping points
    # for example
    # {
    #   "0,0": [[0,1], [0,1, 0,2], [0,1, 0,2, 0,3]],
    #   "0,1": [[0,0], [0,2], [0,2, 0,3]],
    #   ...
    # }
    points = []
    for row in range(len(floor_plan)):
        for col in range(len(floor_plan[row])):
            if (
                content.SPACE != floor_plan[row][col]
                and content.WALL != floor_plan[row][col]
                and Point(col, row) not in JUNCTIONS
            ):
                points.append(Point(col, row))

    for start_point in range(len(points)):
        destination_routes = []
        for end_point in range(len(points)):
            if start_point == end_point:
                continue
            path = get_route(points[start_point], points[end_point], floor_plan)
            destination_routes.append(path)
        routes[points[start_point]] = destination_routes

    return routes


def get_route(start, end, floor_plan):
    # Get the shortest path from start to end, just a list of co-ords
    step_queue = []
    heapq.heappush(step_queue, PrioritizedItem(0, [start], []))

    while len(step_queue) > 0:
        item = heapq.heappop(step_queue)

        if end == item.item[-1]:
            return item.item

        moves = get_next_steps(item.item[-1], floor_plan)
        for move in moves:
            new_cost = item.priority + 1
            new_route = item.item.copy()
            new_route.append(move)
            heapq.heappush(step_queue, PrioritizedItem(new_cost, new_route, []))
    return []


def get_next_steps(point, floor_plan):
    # This one gets the possible next steps from a given point. If the possible next step is a wall or empty space
    # it's not returned as a possibility
    available_moves = []
    out_of_bounds = [content.WALL, content.SPACE]
    if point.x - 1 >= 0 and floor_plan[point.y][point.x - 1] not in out_of_bounds:
        # can move left
        available_moves.append(Point(point.x - 1, point.y))

    if point.y - 1 >= 0 and floor_plan[point.y - 1][point.x] not in out_of_bounds:
        # can move up
        available_moves.append(Point(point.x, point.y - 1))

    if point.x + 1 < len(floor_plan[point.y]) and floor_plan[point.y][point.x + 1] not in out_of_bounds:
        # can move right
        available_moves.append(Point(point.x + 1, point.y))

    if point.y + 1 < len(floor_plan) and floor_plan[point.y + 1][point.x] not in out_of_bounds:
        # can move down
        available_moves.append(Point(point.x, point.y + 1))

    return available_moves


###
###
### This is where the actual processing happens to find the cheapest combination of moves.
###
###
def get_cheapest_solution(floor_plan, routes):
    step_queue = []
    heapq.heappush(step_queue, PrioritizedItem(priority=0, item=floor_plan, route=set()))

    seen = set()
    lowest_cost = float("inf")
    while len(step_queue) > 0:
        item = heapq.heappop(step_queue)

        if is_complete(item.item):
            return item.priority

        current = transform_plan(item.item)
        moves = get_available_moves(item.item, routes)
        for cost, plan in moves:
            plan_str = transform_plan(plan)
            from_to = (current, plan_str)
            if from_to in seen:
                continue
            seen.add(from_to)

            if plan_str in item.route:
                continue

            new_cost = item.priority + cost
            new_route = item.route.copy()
            new_route.add(plan_str)
            heapq.heappush(step_queue, PrioritizedItem(priority=new_cost, item=plan, route=new_route))

    return lowest_cost


def get_available_moves(map, routes):
    # Amber amphipods require 1 energy per step, Bronze amphipods require 10 energy, Copper amphipods require 100, and Desert ones require 1000.
    available_moves = []

    for row in range(len(map)):
        for col in range(len(map[row])):
            # check the space contains an amphipod
            if map[row][col] in AMPHIPODS.keys():
                possible_paths = routes[Point(col, row)]
                for path in possible_paths:
                    # current point always first point in the path
                    steps = path[1:]  # slicing as first element is the current space
                    target = steps[-1]

                    if not is_valid_option(col, row, target, steps, map):
                        continue

                    # copy the map
                    target_map = [row[:] for row in map]

                    # modify the map to move the piece
                    target_map[target.y][target.x] = map[row][col]
                    target_map[row][col] = content.VACANT

                    # calculate cost
                    moved_amphipod = target_map[target.y][target.x]
                    movement_cost = AMPHIPODS[moved_amphipod] * len(steps)

                    # add to available_moves
                    available_moves.append((movement_cost, target_map))

    return available_moves


def is_valid_option(col, row, target_location, path_to_target, floor_plan):
    # get the contents of the target room
    item = floor_plan[row][col]

    # Check the target is empty
    if floor_plan[target_location.y][target_location.x] != content.VACANT:
        return False

    # check we're not moving around inside the hallway
    if row == HALLWAY and target_location.y == row:
        return False

    # check we're not moving around inside the room
    if target_location.y == 2 and row == 3:
        return False

    # can the path be followed? if not return
    for step in path_to_target:
        # are all the steps on the path empty?
        if content.VACANT != floor_plan[step.y][step.x]:
            return False

    if target_location in HALLWAY_STOP_POINTS:
        # Do this after checking we can get to the target.
        return True

    # If target isn't a stop point, its a room, check if target room is one for the amphipod
    if target_location not in TARGET_ROOMS[item]:
        return False

    # check if target room is empty or contains only amphipods of the same type already
    valid_contents = {item, content.VACANT}
    for target_room in TARGET_ROOMS[item]:
        if floor_plan[target_room.y][target_room.x] not in valid_contents:
            return False

    # # check if target is furthest into the room
    # if target_location.y == 2 and floor_plan[3][target_location.x] == content.VACANT:
    #     return False
    remaining_rooms = range(target_location.y + 1, len(floor_plan))
    for room in remaining_rooms:
        if floor_plan[room][target_location.x] == content.VACANT:
            # exit on first empty room found past the current one
            return False

    # If all checks pass it's a valid move
    return True


def is_complete(plan):
    if EXPECTED == plan:
        return True
    return False


def transform_plan(plan):
    plan_txt = ""
    for row in plan:
        plan_txt = plan_txt + "".join(row)
    return plan_txt
