"""
map a character to its score
"""
terminators = {
    ")": {"score": 3, "starter": "("},
    "]": {"score": 57, "starter": "["},
    "}": {"score": 1197, "starter": "{"},
    ">": {"score": 25137, "starter": "<"},
}


def get_dodgy_lines(input):
    """
    Use a stack to find the lines that are dodgy
    """
    dodgy_lines = []
    for line in input:
        tmp_line = line.strip()
        char_list = list(tmp_line)

        sanity_stack = []
        for char in char_list:
            if char in terminators:
                popped_char = sanity_stack.pop()
                if popped_char != terminators[char]["starter"]:
                    entry = {
                        "line": line,
                        "first_dogy_char": char,
                    }
                    dodgy_lines.append(entry)
                    break
            else:
                sanity_stack.append(char)
    return dodgy_lines


def calculate_syntax_error_score(dodgy_lines):
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
    score = 0
    for line in dodgy_lines:
        score += terminators[line["first_dogy_char"]]["score"]
    return score


def solve(file_content):
    dodgy_lines = get_dodgy_lines(file_content)
    error_score = calculate_syntax_error_score(dodgy_lines)
    return error_score
