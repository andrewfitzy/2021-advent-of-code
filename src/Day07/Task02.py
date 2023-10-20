"""
--- Part Two ---
The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?

As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

Move from 16 to 5: 66 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 0 to 5: 15 fuel
Move from 4 to 5: 1 fuel
Move from 2 to 5: 6 fuel
Move from 7 to 5: 3 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 14 to 5: 45 fuel
This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?
"""


def get_file_input(filename):
    """
    Takes a filename and returns a list of ints from the file
    """
    input = ""
    with open(filename) as f:
        for line in f:
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


if __name__ == "__main__":
    # get file content
    crabs = get_file_input("input.txt")

    # find lowest and highest numbers, no point starting lower than lowest or going higher then highest
    crab_extremes = get_crabs_extremes(crabs)

    best_outcome_index = 0
    best_outcome = 999999999999
    index = crab_extremes["lowest"]
    while index < crab_extremes["highest"]:
        fuel_cost = get_fuel_cost(crabs, index)
        if fuel_cost < best_outcome:
            best_outcome = fuel_cost
            best_outcome_index = index

        index += 1

    print("Use this horizontal position: " + str(best_outcome_index))
    print("Will cost this fuel overall: " + str(best_outcome))
