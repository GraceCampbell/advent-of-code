from advent_2023.advent.code.day_01 import *


def test_part_one():
    vals = """1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet""".split('\n')

    assert part_one(vals) == 142


def test_part_two():
    vals = """two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen""".split('\n')

    assert part_two(vals) == 281
