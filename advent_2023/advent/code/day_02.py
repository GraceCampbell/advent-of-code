import numpy as np
import re

COLOR_MAX = {'red': 12, 'green': 13, 'blue': 14}


def part_one(inputs):
    game_num_sum = 0
    for game in inputs:
        game_id, cube_totals = get_max_per_color(game)
        possible = True
        for color in cube_totals:
            if cube_totals[color] > COLOR_MAX[color]:
                possible = False
        if possible:
            game_num_sum += game_id
    return game_num_sum


def part_two(inputs):
    power_sum = 0
    for game in inputs:
        game_id, cube_totals = get_max_per_color(game)
        power_sum += np.prod(list(cube_totals.values()))
    return power_sum


def get_max_per_color(game):
    game_id, digits, colors = parse_input(game)
    return game_id, dict(sorted([x for x in zip(colors, digits)]))


def get_digit_from_string(x):
    return [int(x) for x in re.findall(r'(\d+)', x)]


def get_color_from_string(x):
    return re.findall(r'\b(blue|red|green)\b', x)


def parse_input(item):
    item_split = item.split(': ')
    game_num = get_digit_from_string(item_split[0])[0]
    digits = get_digit_from_string(*item_split[1:])
    colors = get_color_from_string(*item_split[1:])
    return game_num, digits, colors


if __name__ == '__main__':
    with open('../inputs/day_02.txt', 'r') as f:
        inputs = f.read().split('\n')

    print('Part 1 Answer: ', part_one(inputs))  # 2207
    print('Part 2 Answer: ', part_two(inputs))  # 2207

