import numpy as np


def find_invalid_ids(puzzle_input, at_least_twice=False):
    """
    at_least_twice=True for part 2
    """
    invalid_ids_sum = 0
    for id_range in puzzle_input:
        start, end = id_range.split('-')
        for i in range(int(start), int(end) + 1):
            id_str = str(i)
            halfway = len(id_str) // 2
            # First check if two halves of the ID are the same
            if id_str[:halfway] == id_str[halfway:]:
                invalid_ids_sum += i
            # If not, and it's part 2, move on to next checks
            elif at_least_twice:
                num_digits = len(id_str)
                num_unique_digits = len(set(id_str))
                if num_digits > num_unique_digits:
                    if num_unique_digits == 1:
                        invalid_ids_sum += i
                    else:
                        limit = num_digits // num_unique_digits
                        for step in range(num_unique_digits, limit + 1):
                            if has_repeated_digit_sequence(
                                id_str, num_digits, step
                            ):
                                invalid_ids_sum += i
                                break

    return invalid_ids_sum


def has_repeated_digit_sequence(id_str, range_len, step):
    idx = 0
    sequences = []
    for _ in range(range_len):
        sequence = id_str[idx:idx + step]
        sequences.append(sequence) if sequence != '' else None
        idx += step
    if len(set(sequences)) == 1 and len(sequences) > 1:
        return True


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        vals = f.read().split(',')

    test_input = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''.split(',')

    assert find_invalid_ids(test_input) == 1227775554
    assert find_invalid_ids(test_input, at_least_twice=True) == 4174379265

    print(find_invalid_ids(vals))
    print(find_invalid_ids(vals, at_least_twice=True))
