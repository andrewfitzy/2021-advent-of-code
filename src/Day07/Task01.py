# Standard Library
import statistics


def get_crabs(file_content):
    input = ""
    for line in file_content:
        input = input + line.strip()
    char_list = input.split(",", -1)
    char_mapped_to_int = map(int, char_list)
    return list(char_mapped_to_int)


def get_fuel_cost(crabs, target_fuel):
    """
    will check each item in crabs and calculate how far from target_fuel it is
    """
    total_fuel = 0
    for crab in crabs:
        fuel = abs(target_fuel - crab)
        total_fuel = total_fuel + fuel
    return total_fuel


def solve(file_content):
    # get file content
    crabs = get_crabs(file_content)

    median = statistics.median(crabs)

    return get_fuel_cost(crabs, median)
