question1_dict = {"red": 12, "green": 13, "blue": 14}


def process_line(line):
    games = line.split(": ")[1].split("; ")
    game_max = {k: 0 for k in question1_dict}
    col_max = {k: 0 for k in question1_dict}
    for hand in games:
        colors = hand.split(", ")
        for color in colors:
            val, key = color.split(" ")
            if int(val) > game_max[key]:
                game_max[key] = int(val)
            if int(val) > col_max[key]:
                col_max[key] = int(val)
    return game_max, col_max


def check_win(game_dict):
    for key, val in question1_dict.items():
        game = game_dict.get(key, 0)
        if game > val:
            return False
    else:
        return True


def sum_games(games_results):
    res = 0
    for i, val in enumerate(games_results):
        if val:
            res += i+1
    return res


def power(line_values):
    multipl = None
    for val in line_values.values():
        if multipl is None:
            multipl = val
        else:
            multipl *= val
    return multipl


with open('day2_input.txt', 'r') as file:
    scroll = file.read().splitlines()
ans1 = sum_games([check_win(process_line(line)[0]) for line in scroll])
ans2 = sum([power(process_line(line)[1]) for line in scroll])
print(f"ans1: {ans1}\nans2: {ans2}")
