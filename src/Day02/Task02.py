def split_input(input):
    str_list = input.split(sep=" ", maxsplit=1)

    return {"command": str_list[0], "value": int(str_list[1])}


def solve(file_content):
    depth = 0
    height = 0
    aim = 0

    for line in file_content:
        result = split_input(line)
        value = result["value"]
        if result["command"].__eq__("forward"):
            depth += value
            height_change = value * aim
            height += height_change
        elif result["command"].__eq__("down"):
            aim += value
        elif result["command"].__eq__("up"):
            aim -= value
        else:
            raise Exception("WHAT??")

    return height * depth
