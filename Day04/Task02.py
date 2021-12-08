"""
--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
"""

from BingoProcessor import get_calls_file, process_boards_file

if __name__ == '__main__':
    # get file content
    calls = get_calls_file('calls.txt')

    board_results = process_boards_file('boards.txt', calls)

    slowest_win = 0
    slowest_win_score = 0
    for board_result in board_results:
        if board_result['call_count'] > slowest_win:
            slowest_win = board_result['call_count']
            slowest_win_score = board_result['board_value']

    print('quickest_win: ' + str(slowest_win) + " with score: " + str(slowest_win_score))
