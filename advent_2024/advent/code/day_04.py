from itertools import product


def part_one(vals):
    xmas = 0
    for i in range(len(vals)):
        for j in range(len(vals[i])):
            for pair in product([0, 1, -1], [0, 1, -1]):
                is_xmas = find_xmas(i, j, pair[0], pair[1], vals)
                if is_xmas:
                    xmas += 1
    return xmas


def part_two(vals):
    mas = 0
    for i in range(len(vals)):
        for j in range(len(vals[i])):
            is_mas = find_mas(i, j, vals)
            if is_mas:
                mas += 1
    return mas


# These are both really ugly but they work.
# I cannot stand matrix traversal problems so this is the best I'm going to do

def find_xmas(i, j, ir, jr, vals):
    if i+ir*3 >= 0 and i+ir*3 <= len(vals)-1 and j+jr*3 >= 0 and j+jr*3 <= len(vals[i])-1:
        if vals[i][j] == 'X':
            if vals[i+ir*1][j+jr*1] == 'M':
                if vals[i+ir*2][j+jr*2] == 'A':
                    if vals[i+ir*3][j+jr*3] == 'S':
                        return True


def find_mas(i, j, vals):
    if i-1 >= 0 and i+1 <= len(vals)-1 and j-1 >= 0 and j+1 <= len(vals[i])-1:
        current_letter = vals[i][j]
        up_left = vals[i-1][j-1]
        up_right = vals[i-1][j+1]
        down_left = vals[i+1][j-1]
        down_right = vals[i+1][j+1]
        mas = 0
        if current_letter == 'A':
            if up_left == 'M' and down_right == 'S':
                mas += 1
            if up_right == 'M' and down_left == 'S':
                mas += 1
            if down_left == 'M' and up_right == 'S':
                mas += 1
            if down_right == 'M' and up_left == 'S':
                mas += 1
        if mas == 2:
            return True


if __name__ == '__main__':
    with open('../inputs/day_04.txt', 'r') as f:
        vals = f.read().split('\n')

    print(part_one(vals))
    print(part_two(vals))
