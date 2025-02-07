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

    start = Point(0, 0)
    end = Point(len(maze[0]) - 1, len(maze) - 1)

    cost = get_cheapest_path(start=start, end=end, maze=maze)
    return cost


def get_cheapest_path(start: Point, end: Point, maze: list[list[str]]) -> int:
    step_queue: list[PrioritizedItem] = []
    heapq.heappush(step_queue, PrioritizedItem(priority=0, point=start))

    seen = set()
    count = 0  # 17,961,753

    while len(step_queue) > 0:
        count = count + 1
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
