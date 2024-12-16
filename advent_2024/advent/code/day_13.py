import re


def part_one(vals):
    behaviors = parse_behaviors(vals)
    return get_token_count(behaviors)


def part_two(vals):
    behaviors = parse_behaviors(vals, corrected=True)
    return get_token_count(behaviors)


def get_token_count(behaviors, ):
    tokens = 0
    for a, b, prize in behaviors:
        # Thank you internet for this formula bc I definitely don't remember
        # anything about linear algebra :) sorry if that's kind of cheating
        A = (prize[0] * b[1] - prize[1] * b[0]) / (a[0] * b[1] - a[1] * b[0])
        B = (a[0] * prize[1] - a[1] * prize[0]) / (a[0] * b[1] - a[1] * b[0])
        if A == int(A) and B == int(B):
            tokens += A * 3 + B
    return tokens


def parse_behaviors(vals, corrected=False):
    behaviors = []
    for val in vals:
        parts = val.split('\n')
        x = [int(x) for x in re.findall(r'\+(\d+)', parts[0])]
        y = [int(x) for x in re.findall(r'\+(\d+)', parts[1])]
        prize = [int(x) for x in re.findall(r'=(\d+)', parts[2])]
        if corrected:
            prize = [x + 10_000_000_000_000 for x in prize]
        behaviors.append((x, y, prize))
    return behaviors


if __name__ == '__main__':
    with open('../inputs/day_13.txt', 'r') as f:
        vals = f.read().split('\n\n')

    print(part_one(vals))
    print(part_two(vals))
