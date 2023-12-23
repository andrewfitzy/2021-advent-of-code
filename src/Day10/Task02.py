# Standard Library
import statistics

terminators = {
    ")": {"score": 1, "starter": "("},
    "]": {"score": 2, "starter": "["},
    "}": {"score": 3, "starter": "{"},
    ">": {"score": 4, "starter": "<"},
}


starters = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def get_incomplete_lines(input):
    """
    Use a stack to find the lines that are not dodgy, just incomplete and complete them
    """
    incomplete_lines = []
    for line in input:
        tmp_line = line.strip()
        char_list = list(tmp_line)

        is_dodgy = False
        sanity_stack = []
        for char in char_list:
            if char in terminators:
                popped_char = sanity_stack.pop()
                if popped_char != terminators[char]["starter"]:
                    is_dodgy = True
                    break
            else:
                sanity_stack.append(char)
        if not is_dodgy:
            missing_chars = []
            while len(sanity_stack) > 0:
                chunk_starter = sanity_stack.pop()
                missing_chars.append(starters[chunk_starter])
            entry = {
                "line": line,
                "missing_chars": missing_chars,
            }

            incomplete_lines.append(entry)
    return incomplete_lines


def find_winning_score(incomplete_lines):
    """
    Given an input like:
    [
      {
        line: ['[','(','>'],
        first_dogy_char: '>'
      }
    ]

    This function will determine the cost of the dodgy character per line and sum them together
    """
    score_list = []
    for incomplete_line in incomplete_lines:
        missing_chars = incomplete_line["missing_chars"]

        line_score = 0
        for char in missing_chars:
            line_score *= 5
            line_score += terminators[char]["score"]

        score_list.append(line_score)

    median = statistics.median(score_list)
    return median


def solve(file_content):
    incomplete_lines = get_incomplete_lines(file_content)
    score = find_winning_score(incomplete_lines)
    return score
