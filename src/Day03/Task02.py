def get_most_common_value(lines_to_process, index, favoured_value):
    lines_count = 0
    value = 0
    for line in lines_to_process:
        value += int(line[index])
        lines_count += 1

    tmp_threshold = lines_count / 2

    if value > tmp_threshold:
        return 1
    elif value == tmp_threshold:
        return favoured_value

    return 0


def get_least_common_value(lines_to_process, index, favoured_value):
    lines_count = 0
    value = 0
    for line in lines_to_process:
        value += int(line[index])
        lines_count += 1

    tmp_threshold = lines_count / 2

    if value < tmp_threshold:
        return 1
    elif value == tmp_threshold:
        return favoured_value

    return 0


def filter_values(lines_to_process, index, value):
    filtered_values = []
    for line in lines_to_process:
        if line[index] == str(value):
            filtered_values.append(line)
    return filtered_values


def solve(file_content):
    # Get the most popular entry
    oxy_gen_lines = file_content.copy()
    oxy_gen_rating = ""

    word_length = len(oxy_gen_lines[0])
    i = 0
    while i < word_length:
        # get most common value
        processing_result = get_most_common_value(oxy_gen_lines, i, 1)

        # filter list by that value
        oxy_gen_lines = filter_values(oxy_gen_lines, i, processing_result)

        i += 1

        if len(oxy_gen_lines) == 1:
            oxy_gen_rating = oxy_gen_lines[0]
            break

    # Get the least popular entry
    co2_scrub_lines = file_content.copy()
    co2_scrub_rating = ""

    word_length = len(co2_scrub_lines[0])
    i = 0
    while i < word_length:
        # get most common value
        processing_result = get_least_common_value(co2_scrub_lines, i, 0)

        # filter list by that value
        co2_scrub_lines = filter_values(co2_scrub_lines, i, processing_result)

        i += 1

        if len(co2_scrub_lines) == 1:
            co2_scrub_rating = co2_scrub_lines[0]
            break

    oxy_gen_rating_10 = int(oxy_gen_rating, 2)
    co2_scrub_rating_10 = int(co2_scrub_rating, 2)

    life_support_rating = oxy_gen_rating_10 * co2_scrub_rating_10

    return life_support_rating
