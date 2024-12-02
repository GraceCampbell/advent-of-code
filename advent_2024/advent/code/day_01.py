from collections import Counter

def part_one(vals):
    list1, list2 = split_lists(vals)
    total = 0
    for i, j in zip(list1, list2):
        total += abs(i-j)
    return total

def part_two(vals):
    list1, list2 = split_lists(vals)
    counts = Counter(list2)
    similarity_score = 0
    for i in list1:
        similarity_score += i* counts[i]
    return similarity_score


def split_lists(vals):
    list1 = sorted([int(x.split()[0]) for x in vals])
    list2 = sorted([int(x.split()[1]) for x in vals])
    return list1, list2


if __name__ == '__main__':
    with open('../inputs/day_01.txt', 'r') as f:
        vals = f.read().split('\n')

    print(part_one(vals))
    print(part_two(vals))
