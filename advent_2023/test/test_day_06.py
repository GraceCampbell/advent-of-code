from advent_2023.advent.code.day_06 import *


data = """Time:      7  15   30
Distance:  9  40  200""".split('\n')


def test_part_one():
    assert part_one(data) == 288


def test_part_two():
    assert part_two(data) == 71503
