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

        # get triangular number
        actual_fuel_cost = int(fuel * (fuel + 1) / 2)

        total_fuel = total_fuel + actual_fuel_cost
    return total_fuel


def get_crabs_extremes(crabs):
    """
    find the lowest and highest numbers
    """
    lowest_crab = 999999
    highest_crab = 0
    for crab in crabs:
        lowest_crab = crab if crab < lowest_crab else lowest_crab
        highest_crab = crab if crab > highest_crab else highest_crab

    return {
        "highest": highest_crab,
        "lowest": lowest_crab,
    }


def solve(file_content):
    # get file content
    crabs = get_crabs(file_content)

    # find lowest and highest numbers, no point starting lower than lowest or going higher then highest
    crab_extremes = get_crabs_extremes(crabs)

    best_outcome = 999999999999
    index = crab_extremes["lowest"]
    while index < crab_extremes["highest"]:
        fuel_cost = get_fuel_cost(crabs, index)
        if fuel_cost < best_outcome:
            best_outcome = fuel_cost
        index += 1
    return best_outcome
