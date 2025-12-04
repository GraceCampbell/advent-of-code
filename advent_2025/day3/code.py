def get_output_joltage(puzzle_input, count_batteries):
    total_output_joltage = 0

    for bank in puzzle_input:
        batteries = [int(battery) for battery in list(bank)]

        turned_on = []
        last_max = (0, 0)

        # Get the highest battery that has enough batteries after it
        # and start the search from there
        to_search = batteries[:-count_batteries]
        max_idx = to_search.index(max(to_search))
        from_max = batteries[max_idx:]

        for i in range(len(from_max)):
            turned_on.append(from_max[i])
            if i == 0:
                last_max = (i, from_max[i])
            else:
                curr = from_max[i]
                prev = from_max[i - 1]
                if len(turned_on) == count_batteries and len(from_max[i:]) == 0:
                    break
                elif len(from_max[i+1:]) + len(turned_on) > count_batteries:
                    if curr > prev:
                        # If current battery is higher than previous,
                        # iterate through all batteries since the last max battery
                        # and remove the lowest ones
                        for j in range(len(turned_on) - 1):
                            if len(from_max[i+1:]) + len(turned_on) > count_batteries:
                                less_than_max = [
                                    (i, turned_on[i]) for i in range(len(turned_on)-1)
                                    if turned_on[i] <= last_max[1]
                                       and turned_on[i] < curr
                                       and i > last_max[0]
                                ]
                                if less_than_max:
                                    sorted_less_than_max = sorted(less_than_max, key=lambda x: x[1])
                                    lowest = sorted_less_than_max[0][0]
                                    turned_on.pop(lowest)
                        if curr > last_max[1]:
                            last_max = (i, curr)
                    elif curr <= prev and len(turned_on) > count_batteries:
                        for _ in range(len(turned_on) - 1):
                            if len(turned_on) > count_batteries:
                                lowest = min(turned_on)
                                turned_on.pop(turned_on.index(lowest))

        # If we've made it through the possible batteries and there's still too many,
        # just start removing the lowest ones
        if len(turned_on) > count_batteries:
            for _ in range(len(turned_on) - 1):
                if len(turned_on) > count_batteries:
                    lowest = min(turned_on)
                    turned_on.pop(turned_on.index(lowest))

        max_joltage = int(''.join([str(x) for x in turned_on]))
        total_output_joltage += max_joltage

    return total_output_joltage


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        vals = f.read().split('\n')

    test_input = '''987654321111111
811111111111119
234234234234278
818181911112111'''.split('\n')

    assert get_output_joltage(test_input, 2) == 357
    assert get_output_joltage(test_input, 12) == 3121910778619

    print(get_output_joltage(vals, 2))  # 17376
    print(get_output_joltage(vals, 12)) # 172119830406258
