from itertools import product


def part_one(puzzle_input):
    grid = [list(x) for x in puzzle_input]
    cols = len(grid[0])
    rows = len(grid)

    accessible_rolls = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                found_accessible_rolls, new_grid = find_accessible_rolls(grid, i, j)
                accessible_rolls += found_accessible_rolls

    return accessible_rolls


def part_two(puzzle_input):
    grid = [list(x) for x in puzzle_input]
    cols = len(grid[0])
    rows = len(grid)
    accessible_rolls = part_one(puzzle_input)
    final_accessible_rolls = 0

    while accessible_rolls != 0:
        accessible_rolls = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    found_accessible_rolls, new_grid = find_accessible_rolls(grid, i, j, remove=True)
                    accessible_rolls += found_accessible_rolls
                    grid = new_grid
        final_accessible_rolls += accessible_rolls


    return final_accessible_rolls


def find_accessible_rolls(grid, i, j, remove=False):
    cols = len(grid[0])
    rows = len(grid)
    adjacent = 0
    for combo in product([-1, 0, 1], [-1, 0, 1]):
        if combo == (0, 0):
            pass
        else:
            i_val = i + combo[0]
            j_val = j + combo[1]
            if i_val == rows or j_val == cols or i_val == -1 or j_val == -1:
                pass
            elif grid[i_val][j_val] == '@':
                adjacent += 1
    if adjacent < 4:
        if remove:
            grid[i][j] = '.'
        return 1, grid
    else:
        return 0, grid


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        vals = f.read().split('\n')

    test_input = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''.split('\n')

    assert part_one(test_input) == 13
    assert part_two(test_input) == 43

    print(part_one(vals))  # 1363
    print(part_two(vals))  # 8184
