import pandas as pd


def part_one(vals):
    starting_position = '^'
    direction = (0, -1)
    layout = pd.DataFrame([list(x) for x in vals])
    starting_loc = layout.where(layout == starting_position).dropna(how='all').dropna(axis=1)
    x, y = starting_loc.columns[0], starting_loc.index[0]

    for _ in range(layout.shape[0] * layout.shape[1] * 4):
        x, y, direction, layout = move(x, y, direction, layout)
    guard_positions = 0
    for idx, row in layout.iterrows():
        for col in row:
            if col == 'g':
                guard_positions += 1
    return guard_positions, layout


def part_two(vals):
    path_len, path = part_one(vals)
    layout = pd.DataFrame([list(x) for x in vals])
    guard_path = path.where(path == 'g').stack().index.tolist()
    obstacles = layout.where(layout == '#').stack().index.tolist()

    # has to have either one above it to the right AND straight to the left,
    # or one directly to the right and one above it to the left
    print(path)
    possible_loops = 0
    for position in guard_path:
        above_right = False
        straight_left = False
        above_left = False
        straight_right = False

        for obstacle in obstacles:
            print(obstacle, position)
            if (obstacle[1] == position[1]+1) and (obstacle[0] < position[0]):
                above_right = True
                print('above_right', above_right)
            if (obstacle[1] < position[1]) and (obstacle[0] == position[0]):
                straight_left = True
                print('straight left', straight_left)
            if (obstacle[0] == position[0]-1) and (obstacle[1] < position[1]):
                above_left = True
                print('above left', above_left)
            if (obstacle[1] > position[1]) and (obstacle[0] == position[0]):
                straight_right = True
                print('straight right', straight_right)
        if (above_right and straight_left) or (above_left and straight_right):
            possible_loops += 1
        # if (max(above_right) and max(straight_left)) or (max(above_left) and max(straight_right)):
        #     print(above_right, straight_left, above_left, straight_right)

        # for obstacle in obstacles:
        #     if (obstacle in above_right and obstacle in straight_left) or \
        #         (obstacle in above_left and obstacle in straight_right):
        # # if (max(above_right) and max(straight_left)) or (max(above_left) and max(straight_right)):
        #         print(above_right, straight_left, above_left, straight_right)
        #         possible_loops += 1
    return possible_loops
    # for i in range(layout.shape[0]):
    #     for j in range(layout.shape[1]):
    #
    #         if path.iloc[i, j] in MARKER_MAP.values():
    #             layout.iloc[i, j] = '#'
    #             for _ in range(path_len):
    #                 if direction != -999:
    #                     x, y, direction, layout = move(x, y, direction, layout)
    #                     print(layout)
    #             borders = list(layout.iloc[0].values) + list(layout.iloc[-1].values)\
    #                     + list(layout.iloc[:, 0].values) + list(layout.iloc[:, -1].values)
    #             # print(borders)
    #             # print([x not in borders for x in MARKER_MAP.values()])
    #             if all(x not in borders for x in MARKER_MAP.values()):
    #                 possible_loops += 1
    #             layout = pd.DataFrame([list(x) for x in vals])
    #             x, y, direction = get_start(layout)
    return possible_loops


def get_start(layout):
    starting_position = '^'
    direction = (0, -1)
    starting_loc = layout.where(layout == starting_position).dropna(how='all').dropna(axis=1)
    x, y = starting_loc.columns[0], starting_loc.index[0]
    return x, y, direction


def move(x, y, direction, layout):
    try:
        if direction != -999:
            for _ in range(4):
                next_loc = y + direction[1], x + direction[0]
                if next_loc[0] >= 0 or next_loc[1] >= 0:
                    if layout.iloc[next_loc] == '#':
                        direction = turn_90_degrees(direction)
                x, y = x+direction[0], y+direction[1]
                layout.iloc[y, x] = 'g'
    except IndexError:
        direction = -999
    return x, y, direction, layout


def turn_90_degrees(direction):
    if direction == (0, -1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (-1, 0)
    else:
        return (0, -1)


if __name__ == '__main__':
    with open('../inputs/day_06.txt', 'r') as f:
        vals = f.read().split('\n')
    from advent_2024.test.test_day_06 import vals
    # print(part_one(vals))
    print(part_two(vals))