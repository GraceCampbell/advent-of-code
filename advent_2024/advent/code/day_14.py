import numpy as np
import pandas as pd
import re

from math import floor

WIDTH = 101
HEIGHT = 103


def part_one(vals, width=WIDTH, height=HEIGHT):
    bathroom = pd.DataFrame(np.zeros((height, width)))
    p_v = [parse(val) for val in vals]
    for _ in range(100):
        for p, v in p_v:
            old_p, old_v = p, v
            p, v = move_robot(p, v)
            p_v[p_v.index((old_p, old_v))] = (p, v)
    for p, v in p_v:
        p[0] = p[0] % width
        p[1] = p[1] % height
        bathroom.iloc[p[1], p[0]] += 1

    middle_vert  = floor(width/2)
    middle_horiz = floor(height/2)

    q1 = bathroom.iloc[:middle_horiz, :middle_vert]
    q2 = bathroom.iloc[middle_horiz+1:, :middle_vert]
    q3 = bathroom.iloc[:middle_horiz, middle_vert+1:]
    q4 = bathroom.iloc[middle_horiz+1:, middle_vert+1:]

    safety_factor = 1
    for q in [q1, q2, q3, q4]:
        safety_factor = safety_factor * get_bots_in_quadrant(q)

    return safety_factor


def part_two(vals, width=WIDTH, height=HEIGHT):
    bathroom = pd.DataFrame(np.zeros((height, width)))
    p_v = [parse(val) for val in vals]
    count = 0
    while count < 10500:
        count += 1
        layout = bathroom.copy()
        for p, v in p_v:
            old_p, old_v = p, v
            p, v = move_robot(p, v)
            p_v[p_v.index((old_p, old_v))] = (p, v)
        new_locs = [(p[0] % width, p[1] % height) for p, v in p_v]

        for p in new_locs:
            layout.iloc[p[1], p[0]] += 1

        # Good lord this took so much guessing to try to figure out
        ones_only = layout.applymap(lambda x: 1 if x > 0 else x)

        if ones_only.sum().sum() == 500:
            picture = []
            for index, row in layout.iterrows():
                line = ''.join(' ' if val == 0.0 else str(int(val)) for val in row)
                picture.append(line)
            print(count)
            print('\n'.join(picture))


def get_bots_in_quadrant(q):
    robots = 0
    for idx, row in q.iterrows():
        robots += row.sum()
    return robots


def move_robot(p, v):
    new_loc = [p + v for p, v in zip(p, v)]
    return new_loc, v


def parse(val):
    p, v = val.split(' ')
    digits = re.compile(r'(-?\d+)')
    p_int = list(map(int, digits.findall(p)))
    v_int = list(map(int, digits.findall(v)))
    return p_int, v_int


if __name__ == '__main__':
    with open('../inputs/day_14.txt', 'r') as f:
        vals = f.read().split('\n')
    # from advent_2024.test.test_day_14 import vals

    # print(part_one(vals))
    print(part_two(vals))