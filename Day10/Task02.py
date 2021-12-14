"""
--- Part Two ---
Now, discard the corrupted lines. The remaining lines are incomplete.

Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.

You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.

In the example above, there are five incomplete lines:

[({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
[(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
(((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
{<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
<{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.
Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
So, the last completion string above - ])}> - would be scored as follows:

Start with a total score of 0.
Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
Multiply the total score by 5 to get 290, then add the value of > (4) to get a new total score of 294.
The five lines' completion strings have total scores as follows:

}}]])})] - 288957 total points.
)}>]}) - 5566 total points.
}}>}>)))) - 1480781 total points.
]]}}]}]}> - 995444 total points.
])}> - 294 total points.
Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. (There will always be an odd number of scores to consider.) In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.

Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?
"""

import statistics


terminators = {
    ')': {
        'score': 1,
        'starter': '('
    },
    ']': {
        'score': 2,
        'starter': '['
    },
    '}': {
        'score': 3,
        'starter': '{'
    },
    '>': {
        'score': 4,
        'starter': '<'
    },
}


starters = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


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
                if popped_char != terminators[char]['starter']:
                    is_dodgy = True
                    break;
            else:
                sanity_stack.append(char)
        if not is_dodgy:
            missing_chars = []
            while len(sanity_stack) > 0:
                chunk_starter = sanity_stack.pop()
                missing_chars.append(starters[chunk_starter])
            entry = {
                'line': line,
                'missing_chars': missing_chars,
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
        missing_chars = incomplete_line['missing_chars']

        line_score = 0
        for char in missing_chars:
            line_score *= 5
            line_score += terminators[char]['score']

        score_list.append(line_score)

    median = statistics.median(score_list)
    return median


if __name__ == '__main__':
    """

    """
    input = get_input('input.txt')

    # input = ['[({(<(())[]>[[{[]{<()<>>',
    #          '[(()[<>])]({[<{<<[]>>(',
    #          '{([(<{}[<>[]}>{[]{[(<()>',
    #          '(((({<>}<{<{<>}{[]{[]{}',
    #          '[[<[([]))<([[{}[[()]]]',
    #          '[{[{({}]{}}([{[{{{}}([]',
    #          '{<[[]]>}<{[{[{[]{()[[[]',
    #          '[<(<(<(<{}))><([]([]()',
    #          '<{([([[(<>()){}]>(<<{{',
    #          '<{([{{}}[<[[[<>{}]]]>[]]']

    print(input)

    incomplete_lines = get_incomplete_lines(input)

    print(incomplete_lines)

    score = find_winning_score(incomplete_lines)

    print('Score: ' + str(score))
