from advent_2023.advent.utilities import get_digit_from_string
import numpy as np


def part_one(inputs):
    times, distances = parse(inputs)
    races = zip(times, distances)
    ways_to_win = count_ways_to_win(races)
    return np.prod(ways_to_win)


def part_two(inputs):
    time, distance = parse(inputs, single=True)
    races = zip(time, distance)
    ways_to_win = count_ways_to_win(races)
    return ways_to_win[0]


def count_ways_to_win(races):
    """
    :param races: zip object of time and distance
    """
    total_ways_to_win = []
    for time, distance in races:
        ways_to_win = 0
        time_button_held = 0
        all_counted = False
        for _ in range(time+1):
            speed = time_button_held
            time_remaining = time-time_button_held
            if speed * time_remaining > distance:
                ways_to_win += 1
                all_counted = True
            else:
                if all_counted:
                    break
            time_button_held += 1
        total_ways_to_win.append(ways_to_win)
    return total_ways_to_win


def parse(inputs, single=False):
    times = get_digit_from_string(inputs[0])
    distances = get_digit_from_string(inputs[1])
    if single:
        time = int(''.join([str(x) for x in times]))
        distance = int(''.join([str(x) for x in distances]))
        return [time], [distance]
    else:
        return times, distances


if __name__ == '__main__':
    with open('../inputs/day_06.txt', 'r') as f:
        data = f.read().split('\n')

    print(part_one(data))  # 1,155,175
    print(part_two(data))  # 35,961,505
