import re
import numpy as np


def part_one(inputs):
    game_num_sum = 0
    color_max = {'red': 12, 'green': 13, 'blue': 14}
    for item in inputs:
        color_totals = {'red': 0, 'green': 0, 'blue': 0}
        game_id, digits, colors = parse_input(item)
        # possible = True
        max_digit_idx = np.argmax(digits)
        print(colors[max_digit_idx], color_max[colors[max_digit_idx]], max(digits))
        if color_max[colors[max_digit_idx]] >= digits[max_digit_idx]:
            print('possible!', game_id, game_num_sum)
            game_num_sum += game_id
        print(game_id, list(zip(digits, colors))[max_digit_idx], '\n')
    #     for x in list(zip(digits, colors)):
    #         color_totals[x[1]] += x[0]
    #         if color_totals[x[1]] > color_max[x[1]]:
    #             possible = False
    #     if possible:
    #         game_num_sum += game_id
    #     else:
    #         continue
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

    # inputs = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.split('\n')
    print('Part 1 Answer: ', part_one(inputs))  # 145

