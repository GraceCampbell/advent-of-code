from advent_2023.advent.utilities import get_digit_from_string


def part_one(inputs):
    seeds, maps = parse(inputs)
    return get_min_location(seeds, maps)


def part_two(inputs):
    seeds, maps = parse(inputs)
    seed_pairs = list(zip(seeds[::2], seeds[1::2]))
    locations = []
    for pair in seed_pairs:
        for i in range(pair[0], pair[0]+pair[1]+1):
            locations.append(get_min_location([i], maps))
    return min(locations)


def get_min_location(seeds, maps):
    locations = []
    for seed in seeds:
        next_key = seed
        for key in maps:
            for item in maps[key]:
                destination = item[0]
                source = item[1]
                len_range = item[2]
                if source <= next_key <= source+len_range:
                    next_key += destination-source
                    break
        locations.append(next_key)
    return min(locations)


def parse(data):
    map_split = data.split('\n\n')
    seeds = get_digit_from_string(map_split[0])
    maps = {
        tuple(split.split(':\n')[0][:-4].split('-to-')): [
            get_digit_from_string(keys) for keys in split.split(':\n')[1].split('\n')
        ] for split in map_split[1:]
    }
    return seeds, maps


if __name__ == '__main__':
    with open('../inputs/day_05.txt', 'r') as f:
        data = f.read()

    print(part_one(data))  # 278,755,257
    print(part_two(data))

