"""
--- Part Two ---
Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!

How many lanternfish would there be after 256 days?
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


def get_start_position(fishies):
    """
    iterate through the input working out how many of each fish we have
    """
    fishies_tracker = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    index = 0
    length = len(fishies)
    while index < length:
        fishy_value = fishies[index]
        fishies_tracker[fishy_value] = fishies_tracker[fishy_value] + 1
        index += 1

    return fishies_tracker


def get_total_fishies(fishies):
    """
    Add up all the fish values to get the grand total
    """
    total = 0
    index = 0
    length = len(fishies)
    while index < length:
        fishy_value = fishies[index]
        total = total + fishy_value
        index += 1

    return total


def process_fishies(fishies, days):
    fishies_tracker = get_start_position(fishies)

    day = 0
    while day < days:
        index = 0
        length = len(fishies_tracker)
        spawned_fish = 0
        while index < length:
            value = fishies_tracker.pop(0)

            if index == 0:
                spawned_fish = value
            else:
                fishies_tracker.append(value)

            index += 1

        fishies_tracker[6] = fishies_tracker[6] + spawned_fish
        fishies_tracker.append(spawned_fish)

        day += 1

    return get_total_fishies(fishies_tracker)


if __name__ == "__main__":
    # define days
    days = 256

    # get file content
    fishies = get_file_input("input.txt")

    # process
    number_of_fish = process_fishies(fishies, days)

    # print the answer
    print("Total fishies after " + str(days) + " days: " + str(number_of_fish))
