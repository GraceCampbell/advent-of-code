import pandas as pd
import numpy as np

direction_map = {
    # idx, col
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}


def part_one(vals):
    layout = pd.DataFrame([list(x) for x in vals[0].split('\n')])
    moves = vals[1]

    for direction in moves:
        layout = move(layout, direction)

    rows, cols = np.where(layout == 'O')
    boxes = list(zip(rows, cols))
    gps_sum = 0
    for box in boxes:
        gps_sum += (box[0] * 100) + box[1]
    return gps_sum


# def part_two(vals):
#     moves = vals[1]
#
#     scaled_up = []
#     for val in vals[0].split('\n'):
#         row = []
#         for tile in list(val):
#             if tile == '#':
#                 row.extend(['#','#'])
#             elif tile == 'O':
#                 row.extend(['[',']'])
#             elif tile == '.':
#                 row.extend(['.','.'])
#             elif tile == '@':
#                 row.extend(['@','.'])
#         scaled_up.append(row)
#
#
#     layout = pd.DataFrame(scaled_up)
#     print(layout)
#
#     for direction in moves:
#         idx, col = get_start(layout)
#         coord = direction_map(direction)
#         next_loc = idx + coord[0], col + coord[1]
#         if layout[next_loc] == '#':
#             pass
#         elif layout[next_loc] == '.':
#             layout.iloc[idx, col] = '.'
#             layout.iloc[next_loc] = '@'
#         else:
#             if layout[next_loc] == '[':
#                 unit = layout[next_loc[0], next_loc[1]+1]
#             elif layout[next_loc] == ']':
#                 unit = layout[next_loc[0], next_loc[1]-1]

def move(layout, direction):
    move_right = turn_frame(layout, direction)
    idx, col = get_start(move_right)
    next_loc = idx, col+1
    if move_right.iloc[next_loc] == '#':
        pass
    elif move_right.iloc[next_loc] == 'O':
        section = move_right.iloc[next_loc[0], next_loc[1]:]
        empties = section.where(section == '.').dropna(how='all').dropna()
        obstacles = section.where(section == '#').dropna(how='all').dropna()
        if empties.shape == (0,):
            pass
        else:
            first_empty_idx = empties.index.min()
            first_obstacle_idx = obstacles.index.min()
            if first_obstacle_idx < first_empty_idx:
                pass
            else:
                slice_ = move_right.iloc[next_loc[0], next_loc[1]:first_empty_idx+1]
                move_right.iloc[next_loc[0], slice_.index] = ['.']+[x for x in slice_ if x != '.']
                move_right.iloc[idx, col] = '.'
                move_right.iloc[next_loc] = '@'
    else:
        move_right.iloc[idx, col] = '.'
        move_right.iloc[next_loc] = '@'

    return turn_frame(move_right, direction)


def turn_frame(layout, direction):
    if direction == '^':
        layout = layout.iloc[::-1, ::-1].T.reset_index(drop=True)
        layout.columns = list(range(layout.shape[1]))
    elif direction == 'v':
        layout = layout.T.reset_index(drop=True)
        layout.columns = list(range(layout.shape[1]))
    elif direction == '<':
        layout = layout.iloc[::-1, ::-1].reset_index(drop=True)
        layout.columns = list(range(layout.shape[1]))
    else:
        layout = layout
    return layout


def get_start(layout):
    starting_position = '@'
    starting_loc = layout.where(
        layout == starting_position
    ).dropna(how='all').dropna(axis=1)
    idx, col = starting_loc.index[0], starting_loc.columns[0]
    return idx, col


if __name__ == '__main__':
    with open('../inputs/day_15.txt', 'r') as f:
        vals = f.read().split('\n\n')
    from advent_2024.test.test_day_15 import vals

    print(part_one(vals))
    # print(part_two(vals))
