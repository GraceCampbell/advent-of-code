import pandas as pd
from advent_2024.advent.utils import turn_90_degrees


def part_one(vals):
    vals = [[int(x) for x in val] for val in vals]
    layout = pd.DataFrame(vals)
    trailheads = layout.where(layout == 0).stack().index.tolist()
    nines = layout.where(layout == 9).stack().index.tolist()
    paths = {k: [] for k in nines}
    dirs = [(1, 0), (1, 1), (-1, 0), (-1, 1)]

        # layout.diff(i, axis=0),
        # layout.diff(i, axis=1),
        # layout.diff(-i, axis=0),
        # layout.diff(-i, axis=1)

    score = 0
    print(layout)
    for nine in nines:
        for i in range(1, 10):
            for x, y in dirs:
                if (x, y) in paths[nine]:
                    pass
                else:
                    shifted = layout.diff(i*x, axis=y)
                    print('nine', nine, 'xy', (x, y))
                    # print(shifted)
                    print(float(i), shifted.iloc[nine[0], nine[1]])
                    if shifted.iloc[nine[0], nine[1]] == float(i):
                        paths[nine].append((x, y))
                        print(i)
                        if i == 9:
                            score += 1
                            print(score)
                    # print('yes')
    return(score)


    # print(layout)
    # scores = 0

    #         print('nine', nine, 'trailhead', trailhead)
    #         x, y = nine
    #         direction = (0, 1)
    #         while x is not None:
    #             x, y, direction = move(x, y, direction, layout)
    #             print(x, y, direction)
    #             if direction in paths[nine]:
    #                 print('direction already done', direction, paths[nine])
    #                 x = None
    #                 break
    #             if (x, y) == trailhead:
    #                 scores += 1
    #             else:
    #                 if direction is not None:
    #                     paths[nine].append(direction)
    #         print('trailhead', trailhead, 'nine', nine, paths)
    #
    # return scores






    # print(layout)
    # for trailhead in trailheads:
    #     x, y, direction = trailhead[0], trailhead[1], (0, 1)
    #     print(trailhead)
    #     visited_squares = set()
    #     while x is not None:
    #         visited_squares.add((x, y, direction))
    #         x, y, direction = move(x, y, direction, layout)
    #         if (x, y) in nines:
    #
    #         print(x, y, direction)
    #     visited_square_coords = set(
    #         [(square[0], square[1]) for square in visited_squares])
    #     print(visited_square_coords)
    # return visited_square_coords, len(visited_square_coords)


def move(x, y, direction, layout):
    for _ in range(4):
        next_loc = x + direction[0], y + direction[1]
        inc = layout.iloc[x, y] - layout.iloc[next_loc]
        found_next = False
        print('next loc', next_loc)
        # print(x, y, inc, layout.iloc[next_loc])
        if inc == 1:
            found_next = True
            break
        else:
            direction = turn_90_degrees(direction)
            if all(0 <= x < layout.shape[0] and 0 <= x < layout.shape[1] for x in next_loc):
                next_loc = x + direction[0], y + direction[1]
                print('turn 90 - next loc', layout.iloc[x, y], layout.iloc[next_loc])
                inc = layout.iloc[x, y] - layout.iloc[next_loc]
                print('inc',inc)
    if found_next:
        x, y = x + direction[0], y + direction[1]
        return x, y, direction
    else:
        return None, None, None


if __name__ == '__main__':
    with open('../inputs/day_10.txt', 'r') as f:
        vals = f.read().split('\n')
    from advent_2024.test.test_day_10 import vals

    print(part_one(vals))
    # print(part_two(vals))


    # start = 0
    #
    # for trailhead in trailheads:
    #     tile = move(trailhead)
    #     if loc_map.iloc[next_tile[1], next_tile[0]] - loc_map.iloc[
    #         tile[1], tile[0]] == 1:
    #         tile = next_tile
    #
    #
    #
    #
    # print(trailheads, nines)
    # for i in range(len(vals)):
    #     for j in range(len(vals[i])):
    #         if vals[i][j] == '0':


