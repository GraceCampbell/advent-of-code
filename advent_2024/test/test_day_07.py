from advent_2024.advent.code.day_07 import *

vals = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split('\n')


def test_part1():
    assert part_one(vals) == 3749


def test_part2():
    assert part_two(vals) == 11387
