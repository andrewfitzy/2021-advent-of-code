def is_won(game, winning_mark):
    for _, game_state in game.items():
        if game_state["score"] >= winning_mark:
            return True
    return False


def get_moves(die):
    # gets the moves
    i = 0
    rolls_total = 0
    while i < 3:
        i += 1
        die["numberOfRolls"] += 1
        die["lastRoll"] += 1
        if die["lastRoll"] > 100:
            die["lastRoll"] = 1
        rolls_total += die["lastRoll"]
    return rolls_total


def play_game(game, die, winning_mark):
    i = 0

    while True:
        moves = get_moves(die)

        player = i % 2

        mod_moves = moves % 10
        game[str(player)]["position"] += mod_moves
        if game[str(player)]["position"] > 10:
            game[str(player)]["position"] -= 10

        game[str(player)]["score"] += game[str(player)]["position"]

        if is_won(game, winning_mark):
            winner = player
            loser = 0 if winner == 1 else 1
            break
        i += 1

    return {
        "winner": winner,
        "loser": loser,
    }


def get_score(game, die, loser):
    return game[str(loser)]["score"] * die["numberOfRolls"]


def solve(file_content):
    game = {
        "0": {"position": int(file_content[0].split(" ")[4]), "score": 0},
        "1": {"position": int(file_content[1].split(" ")[4]), "score": 0},
    }

    die = {
        "numberOfRolls": 0,
        "lastRoll": 0,
    }

    result = play_game(game, die, 1000)
    loser_score = get_score(game, die, result["loser"])
    return loser_score
