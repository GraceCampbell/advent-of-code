from advent_2024.advent.code.day_10 import *


vals = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split('\n')


def test_day1():
    assert part_one(vals) == 36


def test_day2():
    assert part_two(vals) == 2858
