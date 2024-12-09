from advent_2024.advent.code.day_06 import *

vals = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split('\n')


def test_day1():
    _, res = part_one(vals)
    assert res == 41


def test_day2():
    assert part_two(vals) == 6
