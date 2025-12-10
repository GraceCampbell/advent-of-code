def part_one(puzzle_input):
    tiles = [x.split(',') for x in puzzle_input]
    area = 0
    for tile1 in tiles:
        for tile2 in tiles:
            x1, y1 = int(tile1[0]), int(tile1[1])
            x2, y2 = int(tile2[0]), int(tile2[1])

            rectangle_area = (y2-y1-1) * (x2-x1-1)
            if rectangle_area > area:
                area = rectangle_area
    print(area)
    return area


def part_two(puzzle_input):
    pass



if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        vals = f.read().split('\n')

    test_input = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''.split('\n')

    assert part_one(test_input) == 50
    # assert part_two(test_input) == 40

    print(part_one(vals))  # 4773451098
    # print(part_two(vals))  #