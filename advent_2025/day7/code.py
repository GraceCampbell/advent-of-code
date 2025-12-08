from collections import defaultdict


def part_one(puzzle_input):
    splitters = defaultdict(list)
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            if puzzle_input[i][j] == '^':
                splitters[j].append(i)

    splits = 0
    for col, row in splitters.items():
        print('col', 'row', col, row)
        if len(row) == 1:
            splits += 1
        else:
            valid_vals = []
            for i in range(len(row)):
                if i == 0:
                    valid_vals.append(row[i])
                else:
                    print('checking between vals', row[i - 1], row[i])
                    print('vals to check', splitters[col - 1] + splitters[col + 1])
                    for x in splitters[col-1]+splitters[col+1]:
                        if row[i-1] < x < row[i]:
                            valid_vals.append(row[i])
                    print('valid', set(valid_vals))
            splits += len(set(valid_vals))
        print('splits', splits)
    print(splits)
    return splits


def part_two(puzzle_input):
    pass


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        vals = f.read().split('\n')

    test_input = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''.split('\n')

    assert part_one(test_input) == 21
    assert part_two(test_input) == 40

    print(part_one(vals))  # 1573
    # print(part_two(vals))  # 3145 is too low