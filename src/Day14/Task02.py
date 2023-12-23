# Standard Library
from collections import Counter, defaultdict


def process_input(input):
    processed_input = defaultdict(str)
    for entry in input:
        parts = entry.split(" -> ", -1)
        processed_input[parts[0]] = parts[1]

    return processed_input


def process_polymer(steps, template, template_pairs, mapping_dict):
    template_counter = Counter(template)
    i = 0
    while i < steps:
        new_pairs = Counter()
        for pair, pair_count in template_pairs.items():
            # GIVEN NN -> C and an NN pair, create NC and CN
            new_pairs[pair[0] + mapping_dict[pair]] += pair_count
            new_pairs[mapping_dict[pair] + pair[1]] += pair_count

            template_counter[mapping_dict[pair]] += pair_count
        template_pairs = new_pairs
        i += 1
    return template_counter


def calculate_score(final_polymer):
    return max(final_polymer.values()) - min(final_polymer.values())


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

    steps = 40
    processed_input = process_input(input)

    template_pairs = Counter([template[i : i + 2] for i in range(len(template) - 1)])

    final_polymer = process_polymer(steps, template, template_pairs, processed_input)

    polymer_score = calculate_score(final_polymer)

    return polymer_score
