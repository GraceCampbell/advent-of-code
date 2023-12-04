from advent_2023.advent.code.day_03 import *

inputs = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split('\n')


def test_part_one():
    assert part_one(inputs) == 4361


def test_part_two():
    assert part_two(inputs) == 467835
