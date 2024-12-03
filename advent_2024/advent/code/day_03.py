import re

def part_one(vals):
    insts = re.findall(r'mul\((\d+),(\d+)\)', vals)
    result = 0
    for inst in insts:
        num1, num2 = inst
        result += int(num1) * int(num2)
    return result


def part_two(vals):
    insts = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", vals)
    result = 0
    enabled = True
    for inst in insts:
        num1, num2, do, dont = inst
        if do == "do()":
            enabled = True
        if dont == "don't()":
            enabled = False
        if enabled:
            if num1 != '':
                result += int(num1) * int(num2)
    return result


if __name__ == '__main__':
    with open('../inputs/day_03.txt', 'r') as f:
        vals = f.read()

    print(part_one(vals))
    print(part_two(vals))
