from collections import Counter


def part_one(puzzle_input):
    zero_count = 0
    start = 50

    for step in puzzle_input:
        direction = -1 if step[0] == 'L' else 1
        units = int(step[1:])

        steps, start = move_dial(direction, units, start)
        if steps[-1] == 0:
            zero_count += 1

    return zero_count


def part_two(puzzle_input):

    zero_count = 0
    start = 50

    for step in puzzle_input:
        direction = -1 if step[0] == 'L' else 1
        units = int(step[1:])

        steps, start = move_dial(direction, units, start)
        counts = Counter(steps)

        zero_count += counts[0]

    return zero_count


def move_dial(direction, units, start):
    steps = []
    for i in range(units):
        start += direction
        if start == 100:
            start = 0
        elif start == -1:
            start = 99
        steps.append(start)
    return steps, start


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        vals = f.read().split('\n')

    test_input = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''.split('\n')

    assert part_one(test_input) == 3
    assert part_two(test_input) == 6

    print(part_one(vals))
    print(part_two(vals))