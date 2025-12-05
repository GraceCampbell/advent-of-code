def part_one(puzzle_input):
    fresh_ranges, ingredient_list = parse_input(puzzle_input)

    fresh_ingredients = []
    for ingredient in ingredient_list:
        for r in fresh_ranges:
            if r[0] <= ingredient <= r[1]+1:
                fresh_ingredients.append(ingredient)

    return len(set(fresh_ingredients))


def part_two(puzzle_input):
    fresh_ranges, _ = parse_input(puzzle_input)
    fresh_ranges_sorted = sorted(fresh_ranges, key=lambda x: (x[0], x[1]))

    fresh_ingredients = 0
    max_counted = 0
    for i in range(len(fresh_ranges_sorted)):
        new_fresh_ingredients = fresh_ranges_sorted[i][1] - fresh_ranges_sorted[i][0] + 1
        fresh_ingredients += new_fresh_ingredients
        if fresh_ranges_sorted[i][0] <= max_counted:
            if fresh_ranges_sorted[i][1] <= max_counted:
                pass
            else:
                adjusted_ingredients = max_counted - fresh_ranges_sorted[i][0] + 1
                fresh_ingredients -= new_fresh_ingredients - adjusted_ingredients

        max_counted = fresh_ranges_sorted[i][1] if fresh_ranges_sorted[i][1] > max_counted else max_counted

    return fresh_ingredients



def parse_input(puzzle_input):
    fresh_ranges, ingredients = puzzle_input.split('\n\n')
    fresh_ranges_int = [
        (int(x.split('-')[0]), int(x.split('-')[1]))
        for x in fresh_ranges.split('\n')
    ]
    ingredients_int = [int(x) for x in ingredients.split('\n')]
    return fresh_ranges_int, ingredients_int



if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        vals = f.read()

    test_input = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

    assert part_one(test_input) == 3
    assert part_two(test_input) == 14

    print(part_one(vals))  # 773
    print(part_two(vals))  # 332067203034711
