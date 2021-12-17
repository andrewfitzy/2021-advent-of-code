"""
--- Day 14: Extended Polymerization ---
--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
"""

"""
How about, template is 

n n

n b n
n g
"""
from time import perf_counter as pfc
from collections import deque, Counter, defaultdict

def get_input(filename):
    """
    Takes a filename and returns a list of co-ordinates from the file
    """
    output = []
    with open(filename) as f:
        for line in f:
            tmp_line = line.strip()
            output.append(tmp_line)
    return output


def process_input(input):
    processed_input = defaultdict(str)
    for entry in input:
        parts = entry.split(' -> ', -1)
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


if __name__ == '__main__':
    """

    """
    start = pfc()
    steps = 40

    template = 'OOBFPNOPBHKCCVHOBCSO'
    # template = 'NNCB'

    input = get_input('input.txt')
    # input = ['CH -> B',
    #          'HH -> N',
    #          'CB -> H',
    #          'NH -> C',
    #          'HB -> C',
    #          'HC -> B',
    #          'HN -> C',
    #          'NN -> C',
    #          'BH -> H',
    #          'NC -> B',
    #          'NB -> B',
    #          'BN -> B',
    #          'BB -> N',
    #          'BC -> B',
    #          'CC -> N',
    #          'CN -> C']

    print('Input: ' + str(input))

    processed_input = process_input(input)

    print('Input: ' + str(processed_input))

    template_pairs = Counter([template[i:i + 2] for i in range(len(template) - 1)])

    print('template_pairs: ' + str(template_pairs))

    final_polymer = process_polymer(steps, template, template_pairs, processed_input)

    print('final_polymer: ' + str(final_polymer))

    polymer_score = calculate_score(final_polymer)

    print('polymer_score: ' + str(polymer_score))
    print('Execution time: ', pfc()-start)
