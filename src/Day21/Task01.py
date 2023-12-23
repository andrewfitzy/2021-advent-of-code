game = {"0": {"position": 0, "score": 0}, "1": {"position": 0, "score": 0}}

die = {
    "numberOfRolls": 0,
    "lastRoll": 0,
}


def is_won(winning_mark):
    for player, game_state in game.items():
        if game_state["score"] >= winning_mark:
            return True
    return False


def get_moves():
    i = 0
    rolls_total = 0
    while i < 3:
        i += 1
        die["numberOfRolls"] += 1
        die["lastRoll"] += 1
        if die["lastRoll"] == 101:
            die["lastRoll"] = 1
        rolls_total += die["lastRoll"]
    return rolls_total


def play_game(winning_mark):
    i = 0
    while True:
        moves = get_moves()

        player = i % 2

        mod_moves = moves % 10
        game[str(player)]["position"] += mod_moves
        if game[str(player)]["position"] > 10:
            game[str(player)]["position"] -= 10

        game[str(player)]["score"] += game[str(player)]["position"]

        if is_won(winning_mark):
            winner = player
            loser = 0 if winner == 1 else 1
            break
        i += 1

    return {
        "winner": winner,
        "loser": loser,
    }


def get_score(loser):
    return game[str(loser)]["score"] * die["numberOfRolls"]


def solve(file_content):
    game["0"]["position"] = int(file_content[0].split(" ")[4])
    game["1"]["position"] = int(file_content[1].split(" ")[4])
    result = play_game(1000)
    loser_score = get_score(result["loser"])
    return loser_score
