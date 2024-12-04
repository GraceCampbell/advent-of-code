def part_one(inputs):
    calibration_sum = 0
    for line in inputs:
        digits = [x for x in line if x.isnumeric()]
        calibration_sum += combine_first_and_last_digit(digits)
    return calibration_sum


def part_two(inputs):
    import re
    calibration_sum = 0
    num_str_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    for line in inputs:
        digits = re.findall(rf'{"|".join(num_str_map.keys())}|\d', line)
        digits_mapped = [num_str_map[x] if x.isalpha() else x for x in digits]
        calibration_sum += combine_first_and_last_digit(digits_mapped)
    return calibration_sum


def combine_first_and_last_digit(digits):
    """
    Returns first digit & last digit combined, as integer
    """
    last_idx = -1
    if len(digits) == 1:
        last_idx = 0
    return int(''.join([digits[0], digits[last_idx]]))


if __name__ == '__main__':
    with open('../inputs/day_01.txt', 'r') as f:
        vals = f.read().split('\n')

    print('Part 1 Answer: ', part_one(vals))  # 54,561
    print('Part 2 Answer: ', part_two(vals))  # 54,076
