from enum import Enum


class Colors(Enum):
    red = 0
    green = 1
    blue = 2


def get_min_cubes(game: str) -> list[int]:
    game_num, outcomes = game.split(':')
    game_num = game_num.split(' ')[1]
    outcomes = outcomes.split(';')
    
    min_cubes = [1, 1, 1]
    for outcome in outcomes:
        for color in outcome.split(','):
            cubes, color = color.strip().split(' ')
            cubes = int(cubes)
            if min_cubes[Colors[color].value] < cubes:
                min_cubes[Colors[color].value] = cubes
    return min_cubes


if __name__ == "__main__":
    result = []
    with open("../input.txt") as f:
        lines = f.readlines()
        for line in lines:
            min_values = get_min_cubes(game=line)
            result.append(
                min_values[Colors.red.value] * min_values[Colors.green.value] * min_values[Colors.blue.value]
            )
    print(sum(result))
