from advent_2024.advent.code.day_01 import *

vals = """3   4
4   3
2   5
1   3
3   9
3   3""".split('\n')

def test_part1():
    assert part_one(vals) == 11


def test_part2():
    assert part_two(vals) == 31
