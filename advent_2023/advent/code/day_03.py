from collections import defaultdict
import re


def part_one(inputs):
    part_sum = 0
    num_coords = get_number_coordinates(inputs)
    for grp in num_coords:
        num = int(grp[0])
        is_part = False
        for coord in grp[1]:
            adj_coords = get_adjacents(inputs, coord)
            for adj_coord in adj_coords:
                adj_char = inputs[adj_coord[0]][adj_coord[1]]
                if not adj_char.isnumeric() and adj_char != '.':
                    is_part = True
                    break
        if is_part:
            part_sum += num
    return part_sum


def part_two(inputs):
    import numpy as np
    gear_ratio_sum = 0
    num_coords = get_number_coordinates(inputs)
    adj_parts_coords = defaultdict(set)
    for grp in num_coords:
        num = int(grp[0])
        for coord in grp[1]:
            adj_coords = get_adjacents(inputs, coord)
            for adj_coord in adj_coords:
                adj_char = inputs[adj_coord[0]][adj_coord[1]]
                if adj_char == '*':
                    adj_parts_coords[adj_coord].add(num)
                    if len(adj_parts_coords[adj_coord]) == 2:
                        break

    for key in adj_parts_coords:
        if len(adj_parts_coords[key]) == 2:
            gear_ratio_sum += np.prod(list(adj_parts_coords[key]))
    return gear_ratio_sum


def get_number_coordinates(inputs):
    number_coords = []
    for i in range(len(inputs)):
        nums = list(re.finditer(r'(\d+)', inputs[i]))
        for num in nums:
            number_coords.append((num.group(0), [(i, j) for j in range(num.start(), num.end())]))
    return number_coords


def get_adjacents(matrix, xy):
    adjacents = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            range_x = range(0, len(matrix))
            range_y = range(0, len(matrix[0]))
            (adj_x, adj_y) = (xy[0] + dx, xy[1] + dy)
            if (adj_x in range_x) and (adj_y in range_y) and (dx, dy) != (0, 0):
                adjacents.append((adj_x, adj_y))
    return adjacents


if __name__ == '__main__':
    with open('../inputs/day_03.txt', 'r') as f:
        inputs = f.read().split('\n')

    print('Part 1 Answer: ', part_one(inputs))  # 554,003
    print('Part 2 Answer: ', part_two(inputs))
