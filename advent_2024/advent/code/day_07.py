from itertools import product


def part_one(vals):
    return get_calibration_result(vals)


def part_two(vals):
    return get_calibration_result(vals, operators=('+', '*', '||'))


def get_calibration_result(vals, operators=('+', '*')):
    equations = [x.replace(':', '').split(' ') for x in vals]
    calibration_result = 0
    for equation in equations:
        possible = False
        test_value = int(equation[0])
        eq_values = equation[1:]
        operator_combos = product(operators, repeat=len(eq_values) - 1, )
        for operator_combo in operator_combos:
            eq_values = equation[1:]
            evaluation_result = 0
            for operator in operator_combo:
                if operator == '||':
                    evaluation_result = int(''.join(eq_values[:2]))
                else:
                    evaluation_result = eval(f'{operator}'.join(eq_values[:2]))
                try:
                    eq_values = [str(evaluation_result)] + eq_values[2:]
                except IndexError:
                    continue
            if evaluation_result == test_value:
                possible = True
                break
        if possible:
            calibration_result += test_value
    return calibration_result


if __name__ == '__main__':
    with open('../inputs/day_07.txt', 'r') as f:
        vals = f.read().split('\n')

    print(part_one(vals))
    print(part_two(vals))