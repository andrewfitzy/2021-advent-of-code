# Standard Library
import math
import re


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


def solve(file_content):
    pattern = r"(?P<operation>(on|off)) x=(?P<min_x>[-]?\d+)\.\.(?P<max_x>[-]?\d+),y=(?P<min_y>[-]?\d+)\.\.(?P<max_y>[-]?\d+),z=(?P<min_z>[-]?\d+)\.\.(?P<max_z>[-]?\d+)"

    cuboids = []
    from_x = math.inf
    to_x = -math.inf
    from_y = math.inf
    to_y = -math.inf
    from_z = math.inf
    to_z = -math.inf
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

        from_x = min_x_int if min_x_int < from_x else from_x
        to_x = max_x_int if max_x_int > to_x else to_x
        from_y = min_y_int if min_y_int < from_y else from_y
        to_y = max_y_int if max_y_int > to_y else to_y
        from_z = min_z_int if min_z_int < from_z else from_z
        to_z = max_z_int if max_z_int > to_z else to_z

    print(f"x={from_x}..{to_x},y={from_y}..{to_y},z={from_z}..{to_z}")

    to_x = to_x + 1
    to_y = to_y + 1
    to_z = to_z + 1

    # initialise the uber cube
    plan_dict = {}
    for x in range(from_x, to_x):
        y_dict = plan_dict.get(x, {})
        for y in range(from_y, to_y):
            z_dict = plan_dict.get(y, {})
            for z in range(from_z, to_z):
                z_dict[str(z)] = 0
            y_dict[str(y)] = z_dict
        plan_dict[str(x)] = y_dict

    # set the values on/off for the cuboids
    for cuboid in cuboids:
        for x in range(cuboid.min_x, cuboid.max_x + 1):
            for y in range(cuboid.min_y, cuboid.max_y + 1):
                for z in range(cuboid.min_z, cuboid.max_z + 1):
                    plan_dict[str(x)][str(y)][str(z)] = cuboid.operation

    # count the number of cubes that are on
    total = 0
    for x_value in plan_dict.values():
        for y_value in x_value.values():
            for z_value in y_value.values():
                if z_value == 1:
                    total = total + 1

    return total
