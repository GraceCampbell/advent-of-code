import pandas as pd
from itertools import combinations


def part_one(vals):
    return get_antinodes(vals)


def part_two(vals):
    return get_antinodes(vals, harmonics=True)


def get_antinodes(vals, harmonics=False):
    loc_map = pd.DataFrame([list(x) for x in vals])
    frequencies = set([x for col in loc_map.columns for x in loc_map[col] if x != '.'])

    locations = []
    for freq in frequencies:
        antennas = loc_map.where(loc_map == freq).stack().index.tolist()
        for pair in combinations(antennas, 2):
            ant1, ant2 = sorted(pair, key=lambda x: x[0], reverse=True)
            idx_diff, col_diff = ant1[0] - ant2[0], ant1[1] - ant2[1]
            antinode1 = ant1[0] + idx_diff, ant1[1] + col_diff
            antinode2 = ant2[0] - idx_diff, ant2[1] - col_diff
            if harmonics == True:
                # Keep going until one goes out of bounds
                while all(0 <= x < loc_map.shape[0] and 0 <= x < loc_map.shape[1] for x in antinode1):
                    locations.append(antinode1)
                    antinode1 = antinode1[0] + idx_diff, antinode1[1] + col_diff
                while all(0 <= x < loc_map.shape[0] and 0 <= x < loc_map.shape[1] for x in antinode2):
                    locations.append(antinode2)
                    antinode2 = antinode2[0] - idx_diff, antinode2[1] - col_diff
                locations.extend([ant1, ant2])
            # Single check for out of bounds
            if all(0 <= x < loc_map.shape[0] and 0 <= x < loc_map.shape[1] for x in antinode1):
                locations.append(antinode1)
            if all(0 <= x < loc_map.shape[0] and 0 <= x < loc_map.shape[1] for x in antinode2):
                locations.append(antinode2)
    return len(set(locations))


if __name__ == '__main__':
    with open('../inputs/day_08.txt', 'r') as f:
        vals = f.read().split('\n')

    print(part_one(vals))
    print(part_two(vals))
