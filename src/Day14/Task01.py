def process_input(input):
    processed_input = {}
    for entry in input:
        parts = entry.split(" -> ", -1)
        processed_input[parts[0]] = parts[1]

    return processed_input


def process_polymer(steps, template, processed_input):
    template_list = list(template)
    i = 0
    while i < steps:
        new_template = []
        template_length = len(template_list)
        while template_length > 1:
            front = template_list.pop(0)
            next = template_list[0]

            pair = front + next

            element = processed_input[pair]
            new_template.append(front)
            new_template.append(element)

            template_length -= 1

        last_item = template_list.pop(0)
        new_template.append(last_item)
        template_list = new_template
        i += 1
    return template_list


def calculate_score(final_polymer):
    polymer_summary = {}
    for element in final_polymer:
        current_element_score = polymer_summary.get(element, 0)
        current_element_score += 1
        polymer_summary[element] = current_element_score

    most_common_element_value = 0
    least_common_element_value = 999999
    for entry in polymer_summary:
        if polymer_summary[entry] > most_common_element_value:
            most_common_element_value = polymer_summary[entry]

        if polymer_summary[entry] < least_common_element_value:
            least_common_element_value = polymer_summary[entry]
    score = most_common_element_value - least_common_element_value
    return score


def solve(file_content):
    template = ""
    input = []
    for file_line in file_content:
        if len(template) == 0:
            template = file_line
            continue

        if len(file_line) == 0:
            continue

        input.append(file_line)

    steps = 10
    processed_input = process_input(input)

    final_polymer = process_polymer(steps, template, processed_input)

    polymer_score = calculate_score(final_polymer)

    return polymer_score
