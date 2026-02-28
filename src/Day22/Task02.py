# Standard Library
import re
from collections import Counter


class Cuboid:
    operation = 0
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0

    def __init__(self, operation, min_x, max_x, min_y, max_y, min_z, max_z):
        self.operation = operation
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.min_z = min_z
        self.max_z = max_z

    def __str__(self):
        return (
            f"{self.operation} x={self.min_x}..{self.man_x},y={self.min_y}..{self.man_y},z={self.min_z}..{self.man_z}"
        )

    def as_tuple(self):
        return (self.min_x, self.max_x, self.min_y, self.max_y, self.min_z, self.max_z)

    def intersects(self, area):
        if (
            (self.min_x <= area[1] and self.max_x >= area[0])
            and (self.min_y <= area[3] and self.max_y >= area[2])
            and (self.min_z <= area[5] and self.max_z >= area[4])
        ):
            return True
        return False

    def get_intersection_area(self, area):
        inter_min_x = max(self.min_x, area[0])
        inter_max_x = min(self.max_x, area[1])
        inter_min_y = max(self.min_y, area[2])
        inter_max_y = min(self.max_y, area[3])
        inter_min_z = max(self.min_z, area[4])
        inter_max_z = min(self.max_z, area[5])

        if inter_min_x <= inter_max_x and inter_min_y <= inter_max_y and inter_min_z <= inter_max_z:
            return (inter_min_x, inter_max_x, inter_min_y, inter_max_y, inter_min_z, inter_max_z)
        return None


def solve(file_content):
    pattern = r"(?P<operation>(on|off)) x=(?P<min_x>[-]?\d+)\.\.(?P<max_x>[-]?\d+),y=(?P<min_y>[-]?\d+)\.\.(?P<max_y>[-]?\d+),z=(?P<min_z>[-]?\d+)\.\.(?P<max_z>[-]?\d+)"

    cuboids = []
    for line in file_content:
        match = re.match(pattern, line)
        results = match.groupdict()

        min_x_int = int(results["min_x"])
        max_x_int = int(results["max_x"])
        min_y_int = int(results["min_y"])
        max_y_int = int(results["max_y"])
        min_z_int = int(results["min_z"])
        max_z_int = int(results["max_z"])
        cuboid = Cuboid(
            operation=1 if results["operation"] == "on" else 0,
            min_x=min_x_int if min_x_int <= max_x_int else max_x_int,
            max_x=max_x_int if min_x_int <= max_x_int else min_x_int,
            min_y=min_y_int if min_y_int <= max_y_int else max_y_int,
            max_y=max_y_int if min_y_int <= max_y_int else min_y_int,
            min_z=min_z_int if min_z_int <= max_z_int else max_z_int,
            max_z=max_z_int if min_z_int <= max_z_int else min_z_int,
        )
        cuboids.append(cuboid)

    areas = Counter()
    for cuboid in cuboids:
        updated_areas = Counter()
        updated_areas[cuboid.as_tuple()] += cuboid.operation

        for area, value in areas.items():
            if cuboid.intersects(area):
                intersection_area = cuboid.get_intersection_area(area)
                updated_areas[intersection_area] -= value

        areas.update(updated_areas)

    total = 0

    for area, value in areas.items():
        total = total + (get_volume(area) * value)

    return total


def get_volume(area):
    return (area[1] - area[0] + 1) * (area[3] - area[2] + 1) * (area[5] - area[4] + 1)
