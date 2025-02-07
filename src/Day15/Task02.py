# Standard Library
import heapq
from dataclasses import dataclass, field

# From apps
from util.point import Point


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    point: Point = field(compare=False)


def solve(file_content):
    maze: list[list[str]] = []
    for line in file_content:
        maze.append(list(line))

    bigger_maze = increase_size(5, maze)

    start = Point(0, 0)
    end = Point(len(bigger_maze[0]) - 1, len(bigger_maze) - 1)

    cost = get_cheapest_path(start=start, end=end, maze=bigger_maze)
    return cost
    # return 1


def increase_size(multiplier, maze: list[list[str]]) -> list[list[str]]:
    massive_maze = []

    tmp_massive_maze = []
    # add cols first
    for row in maze:
        new_row = []
        for addition in range(0, multiplier):
            for col in row:
                new_value = int(int(col) + int(addition))
                if new_value > 9:
                    new_value = new_value - 9
                new_row.append(str(new_value))
        tmp_massive_maze.append(new_row)

    # new add rows
    for row_addition in range(0, multiplier):
        for row in tmp_massive_maze:
            new_row = []
            for col in row:
                new_value = int(int(col) + int(row_addition))
                if new_value > 9:
                    new_value = new_value - 9
                new_row.append(str(new_value))
            massive_maze.append(new_row)

    return massive_maze


def get_cheapest_path(start: Point, end: Point, maze: list[list[str]]) -> int:
    step_queue: list[PrioritizedItem] = []
    heapq.heappush(step_queue, PrioritizedItem(priority=0, point=start))

    seen = set()

    while len(step_queue) > 0:
        item = heapq.heappop(step_queue)
        if item.point == end:
            return item.priority

        moves = get_available_moves(item.point, maze)
        for move in moves:
            if move in seen:
                continue
            seen.add(move)
            new_cost = item.priority + int(maze[move.y][move.x])
            heapq.heappush(step_queue, PrioritizedItem(priority=new_cost, point=move))
    return -1


def get_available_moves(point: Point, map: list[list[str]]) -> list[Point]:
    available_moves = []
    if point.x - 1 >= 0:
        # can move left
        available_moves.append(Point(point.x - 1, point.y))
    if point.y - 1 >= 0:
        # can move up
        available_moves.append(Point(point.x, point.y - 1))
    if point.x + 1 < len(map[point.y]):
        # can move right
        available_moves.append(Point(point.x + 1, point.y))
    if point.y + 1 < len(map):
        # can move down
        available_moves.append(Point(point.x, point.y + 1))
    return available_moves
