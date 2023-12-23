def get_calls(file_content):
    input = ""
    for line in file_content:
        if len(line) == 0:
            break
        input = input + line.strip()
    char_list = input.split(",", -1)
    char_mapped_to_int = map(int, char_list)
    return list(char_mapped_to_int)


def has_winning_row(board):
    """
    Check if the board has a winning row, return true if so
    """
    row_count = 0
    while row_count < len(board):
        cell_count = 0
        star_count = 0
        while cell_count < len(board[row_count]):
            if "*" == board[row_count][cell_count]:
                star_count += 1
            else:
                break
            cell_count += 1
        if star_count == len(board[row_count]):
            return True
        row_count += 1
    return False


def has_winning_column(board):
    """
    Check if the board has a winning column, return true if so
    """
    columns = len(board[0])
    cell_count = 0
    while cell_count < columns:
        star_count = 0
        row_count = 0
        while row_count < len(board):
            if "*" == board[row_count][cell_count]:
                star_count += 1
            else:
                break
            row_count += 1
        if star_count == columns:
            return True
        cell_count += 1
    return False


def is_winning_board(board):
    """
    check whether a row is winning
    check whether a column is winning
    """
    return has_winning_row(board) or has_winning_column(board)


def final_value_of_board(board, call):
    """
    add all the remaining values
    times by call
    """
    unmarked_total = 0
    row_count = 0
    while row_count < len(board):
        cell_count = 0
        while cell_count < len(board[row_count]):
            if "*" != board[row_count][cell_count]:
                unmarked_total += board[row_count][cell_count]
            cell_count += 1
        row_count += 1
    return unmarked_total * call


def process_board(board, calls):
    """
    will evaluate the board
    """
    call_count = 0
    for call in calls:
        row_count = 0
        while row_count < len(board):
            cell_count = 0
            while cell_count < len(board[row_count]):
                if call == board[row_count][cell_count]:
                    board[row_count][cell_count] = "*"
                cell_count += 1
            row_count += 1
        call_count += 1
        if is_winning_board(board):
            board_value = final_value_of_board(board, call)
            return {
                "call_count": call_count,
                "board_value": board_value,
            }
    return -1  # should never happen for the puzzle


def process_boards(file_content, calls):
    """
    will read in a board and then evaluate it
    """
    results_list = []

    board = []
    count = 0
    for line in file_content:
        if count >= 2:
            tmp_row = line.strip()
            if len(tmp_row) > 0:
                char_list = tmp_row.split()
                char_mapped_to_int = map(int, char_list)
                row = list(char_mapped_to_int)
                board.append(row)
            else:
                result = process_board(board, calls)
                results_list.append(result)
                board = []
        count += 1
    result = process_board(board, calls)
    results_list.append(result)
    return results_list
