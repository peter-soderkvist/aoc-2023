from enum import Enum


class Colors(Enum):
    red = 12
    green = 13
    blue = 14


def is_game_possible(game: str) -> int:
    game_num, outcomes = game.split(':')
    game_num = game_num.split(' ')[1]
    outcomes = outcomes.split(';')
    for outcome in outcomes:
        for color in outcome.split(','):
            cubes, color = color.strip().split(' ')
            if int(cubes) > Colors[color].value:
                return 0
    return int(game_num)


if __name__ == "__main__":
    result = []
    with open("../input.txt") as f:
        lines = f.readlines()
        for line in lines:
            result.append(is_game_possible(game=line))
    print(sum(result))
