def solve(file_content):
    input = ""
    for line in file_content:
        input = input + line.strip()

    char_list = input.split(",", -1)
    char_mapped_to_int = map(int, char_list)
    fishies = list(char_mapped_to_int)

    extra_fishies = []

    day_counter = 0
    days = 80
    while day_counter < days:
        index = 0
        length = len(fishies)
        while index < length:
            if fishies[index] > 0:
                fishies[index] = fishies[index] - 1
            else:
                fishies[index] = 6
                extra_fishies.append(8)

            index += 1

            if index == length:
                fishies = fishies + extra_fishies
                extra_fishies = []
        day_counter += 1
    return len(fishies)
