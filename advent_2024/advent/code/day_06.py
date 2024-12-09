import pandas as pd


def part_one(vals):
    layout = pd.DataFrame([list(x) for x in vals])
    x, y, direction = get_start(layout)
    visited_squares = set()
    while x > -99:
        visited_squares.add((x, y, direction))
        x, y, direction = move(x, y, direction, layout)
    visited_square_coords = set([(square[0], square[1]) for square in visited_squares])
    return visited_square_coords, len(visited_square_coords)


def part_two(vals):
    path, _ = part_one(vals)
    possible_loops = 0
    for coord in path:
        end = False
        layout = pd.DataFrame([list(x) for x in vals])
        x, y, direction = get_start(layout)
        visited_squares = set([(x, y, direction)])
        layout.iloc[coord[1], coord[0]] = '#'
        while not end:
            if x > -99:
                x, y, direction = move(x, y, direction, layout)
                if (x, y, direction) in visited_squares:
                    possible_loops += 1
                    end = True
                visited_squares.add((x, y, direction))
            else:
                end = True
    return possible_loops


def get_start(layout):
    starting_position = '^'
    direction = (0, -1)
    starting_loc = layout.where(layout == starting_position).dropna(how='all').dropna(axis=1)
    x, y = starting_loc.columns[0], starting_loc.index[0]
    return x, y, direction


def move(x, y, direction, layout):
    next_loc = y + direction[1], x + direction[0]
    if not all(0 <= x < layout.shape[0] and 0 <= x < layout.shape[1] for x in next_loc):
        return -99, -99, (-99, -99)
    while layout.iloc[next_loc] == '#':
        direction = turn_90_degrees(direction)
        next_loc = y + direction[1], x + direction[0]
    x, y = x + direction[0], y + direction[1]
    return x, y, direction


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

    _, res = part_one(vals)
    print(res)
    print(part_two(vals))