def process_input_file(file_content):
    processing_result = {}
    lines_count = 0

    for line in file_content:
        character_list = list(line.strip())

        index = 0
        for character in character_list:
            value = processing_result.get(str(index), 0)
            value += int(character)
            processing_result[str(index)] = value
            index += 1

        lines_count += 1

    threshold = lines_count / 2

    processing_result["threshold"] = threshold

    return processing_result


def solve(file_content):
    processing_result = process_input_file(file_content)

    threshold = processing_result.pop("threshold")

    gamma = ""
    epsilon = ""
    for item_count in processing_result.values():
        if item_count > threshold:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    gamma_10 = int(gamma, 2)
    epsilon_10 = int(epsilon, 2)

    power_consumption = gamma_10 * epsilon_10
    return power_consumption
