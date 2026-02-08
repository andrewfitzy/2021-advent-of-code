# Standard Library
from functools import cache

game = {"0": {"position": 0, "score": 0}, "1": {"position": 0, "score": 0}}


def get_next_position(current_position, moves):
    max_position = 10
    next_position = (current_position + moves) % max_position
    if next_position != 0:
        return next_position

    return max_position


@cache
def play_game(winning_mark, player_one_pos, player_one_score, player_two_pos, player_two_score):
    if player_one_score >= winning_mark:
        return 1, 0
    elif player_two_score >= winning_mark:
        return 0, 1

    number_wins = (0, 0)

    for roll_1 in [1, 2, 3]:
        for roll_2 in [1, 2, 3]:
            for roll_3 in [1, 2, 3]:
                next_pos = get_next_position(player_one_pos, roll_1 + roll_2 + roll_3)
                score = player_one_score + next_pos
                universe_wins = play_game(winning_mark, player_two_pos, player_two_score, next_pos, score)
                number_wins = number_wins[0] + universe_wins[1], number_wins[1] + universe_wins[0]

    return number_wins


def solve(file_content):
    game["0"]["position"] = int(file_content[0].split(" ")[4])
    game["1"]["position"] = int(file_content[1].split(" ")[4])
    result = play_game(21, game["0"]["position"], game["0"]["score"], game["1"]["position"], game["1"]["score"])

    return max(result)
