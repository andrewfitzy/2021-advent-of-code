# From apps
from Day04.BingoProcessor import get_calls, process_boards


def solve(file_content):
    # get file content
    calls = get_calls(file_content)

    board_results = process_boards(file_content, calls)

    quickest_win = 999999
    quickest_win_score = 0
    for board_result in board_results:
        if board_result["call_count"] < quickest_win:
            quickest_win = board_result["call_count"]
            quickest_win_score = board_result["board_value"]

    print("quickest_win: " + str(quickest_win) + " with score: " + str(quickest_win_score))
    return quickest_win_score
