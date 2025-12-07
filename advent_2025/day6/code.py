import re

from bin.ud.ud_run_test import split_text


def part_one(puzzle_input):
    rows = puzzle_input.split('\n')
    rows_split = [
        re.findall('\d+|\*|\+', row) for row in rows
        if re.findall('\d+|\*|\+', row)
    ]
    math_problems = [list(row) for row in zip(*rows_split)]

    grand_total = 0
    for math_problem in math_problems:
        values, operator = math_problem[:-1], math_problem[-1]
        grand_total += calculate_subtotal(values, operator)
    return grand_total


def part_two(puzzle_input):
    rows = [list(x) for x in puzzle_input.split('\n') if x != '']
    max_length = max([len(rows[i]) for i in range(len(rows))])

    # Add space padding to the end of rows that need it
    adjusted_rows = [
        row + [' '] * (max_length - len(row))
        if len(row) < max_length else row
        for row in rows
    ]

    # Get indices where numbers should be split, leaving space padding intact
    split_idxs = [
        i for i in range(max_length)
        if sum([0 if row[i] == ' ' else 1 for row in adjusted_rows]) == 0
    ]

    rows_split = []
    for row in adjusted_rows:
        new_row = []
        last_idx = 0
        for i in range(len(split_idxs) + 1):
            if i < len(split_idxs):
                idx = split_idxs[i]
                to_append = row[last_idx:idx]
            else:
                to_append = row[last_idx:]
            new_row.append(''.join(to_append))
            last_idx = idx + 1
        rows_split.append(new_row)

    math_problems = [list(row) for row in zip(*rows_split)]

    grand_total = 0
    for math_problem in math_problems:
        values, operator = math_problem[:-1], math_problem[-1].strip()
        # Rearrange the values top to bottom
        new_vals = [
            int(''.join([value[i] for value in values]))
            for i in range(len(values[0]))
        ]

        grand_total += calculate_subtotal(new_vals, operator)

    return grand_total


def calculate_subtotal(values, operator):
    subtotal = 0 if operator == '+' else 1
    for value in values:
        if operator == '+':
            subtotal += int(value)
        elif operator == '*':
            subtotal *= int(value)
    return subtotal


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        vals = f.read()

    test_input = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
'''

    assert part_one(test_input) == 4277556
    assert part_two(test_input) == 3263827

    print(part_one(vals))  # 6757749566978
    print(part_two(vals))  # 10603075273949


