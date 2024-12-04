from advent_2024.advent.code.day_04 import *


def test_part1():
    vals = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX""".split('\n')
    assert part_one(vals) == 18


def test_part2():
    vals=""".M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........""".split('\n')
    assert part_two(vals) == 9

