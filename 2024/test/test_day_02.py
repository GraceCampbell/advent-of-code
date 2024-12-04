from advent_2024.advent.code.day_02 import *

vals = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''.split('\n')


def test_part1():
    assert part_one(vals) == 2


def test_part2():
    assert part_two(vals) == 4