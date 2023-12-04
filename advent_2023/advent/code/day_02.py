import re
import numpy as np


def part_one(inputs):
    game_num_sum = 0
    color_max = {'red': 12, 'green': 13, 'blue': 14}
    for item in inputs:
        game_id, digits, colors = parse_input(item)
        max_digit_idx = np.argmax(digits)
        if color_max[colors[max_digit_idx]] >= digits[max_digit_idx]:
            game_num_sum += game_id
    return game_num_sum


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

    print('Part 1 Answer: ', part_one(inputs))  # 145

