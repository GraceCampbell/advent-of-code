def part_one(vals):
    for _ in range(25):
        vals = blink(vals)
    return sum([x for x in vals.values()])


def part_two(vals):
    for _ in range(75):
        vals = blink(vals)
    return sum([x for x in vals.values()])


def blink(vals):
    new_vals = dict()
    for val in vals:
        if int(val) == 0:
            if new_vals.get('1') is None:
                new_vals['1'] = vals[val]
            else:
                new_vals['1'] += vals[val]
        elif len(val) % 2 == 0:
            halfway = int(len(val) / 2)
            for v in [parse_zero(val[:halfway]), parse_zero(val[halfway:])]:
                if int(v) == 0:
                    if new_vals.get('0') is None:
                        new_vals['0'] = vals[val]
                    else:
                        new_vals['0'] += vals[val]
                else:
                    if new_vals.get(v) is None:
                        new_vals[v] = vals[val]
                    else:
                        new_vals[v] += vals[val]
        else:
            new_val = str(int(val) * 2024).lstrip('0')
            if new_vals.get(new_val) is None:
                new_vals[new_val] = vals[val]
            else:
                new_vals[new_val] += vals[val]
    return new_vals


def parse_zero(val):
    return val.lstrip('0') if int(val) != 0 else val


if __name__ == '__main__':
    with open('../inputs/day_11.txt', 'r') as f:
        vals = f.read().split()

    vals = {k: 1 for k in vals}
    print(part_one(vals))
    print(part_two(vals))
