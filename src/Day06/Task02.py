def get_fishies(file_content):
    """
    Takes a string array and returns a list of ints from the file
    """
    input = ""
    for line in file_content:
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


def solve(file_content):
    days = 256
    fishies = get_fishies(file_content)
    number_of_fish = process_fishies(fishies, days)
    return number_of_fish
