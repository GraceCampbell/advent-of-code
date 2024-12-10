def part_one(vals):
    files = [int(x) for x in vals[::2]]
    free_space = [int(x) for x in vals[1::2]]
    ids = [(i, x) for i, x in enumerate(files)]

    new_arr = []
    for i in range(len(files)):
        new_arr.extend([ids[i][0]] * ids[i][1])
        new_arr.extend([-99] * free_space[i]) if i < len(free_space) else None

    checksum = 0
    last_idx = -1
    max_free = max(free_space)

    for i in range(0,len([x for x in new_arr if x > -99])):
        if new_arr[i] == -99:
            if new_arr[last_idx] == -99:
                new_str = ''.join([str(x) if x != -99 else '.' for x in new_arr[last_idx-max_free:last_idx+1]])
                last_idx -= len(new_str) - len(new_str.rstrip("."))
            mult = int(new_arr[last_idx])
            checksum += mult * i
            last_idx -= 1
        else:
            checksum += int(new_arr[i]) * i
    return checksum


def part_two(vals):

    files = [int(x) for x in vals[::2]]
    free_space = [int(x) for x in vals[1::2]]
    ids = [(i, x) for i, x in enumerate(files)]

    new_arr = []
    for i in range(len(files)):
        new_arr.extend([ids[i][0]] * ids[i][1])
        new_arr.extend([-99] * free_space[i]) if i < len(free_space) else None
    print(new_arr.index(9))

    files = [(i, int(x)) for i, x in enumerate(vals[::2])]
    free_space = dict()
    s = 0
    for space, file in zip(enumerate(vals[1::2]), files):
        s += file[1]
        free_space[space[0]+s] = int(space[1])
        s += int(space[1])-1
    # print(files)
    # print(free_space)
    checksum = 0

    for key, val in sorted(files, reverse=True):
        print(free_space)
        valid_keys = [k for k, v in free_space.items() if v >= val]
        print(valid_keys)
        # print(valid_keys)
        first_valid = int(min(valid_keys)) if valid_keys else None
        print('first valid', first_valid)
        print(new_arr.index(key))
        # print(first_valid)
        # print(first_valid)
        # print(files[max(files)])
        # print(free_space[min(free_space)])
        if first_valid is not None:
            for j in range(val):
                print(key, first_valid + j)
                checksum += key * (first_valid+j)
            # del files[max(files)]
            del free_space[first_valid]
            if first_valid-val > 0:
                free_space[first_valid+val] = key
            free_space[new_arr.index(key)] = val
            # figure out how to get the index of the number that was moved
        # del free_space[first_valid]
    print(checksum)

    # print(files, max(files), files[max(files)])
    # for i in range(len(files)-1, -1, -1):
    #     file = min(files)
    #     print(file)
    #     if files[i] == free_space[min(free_space)]:
    #         del free_space[min(free_space)]
    #         del files[i]
    #     for j in range(files[file]):
    #         checksum += files[file] * j
    #         print(j, files[file], files[file] * j)
    #         print(files[file])
    #         del files[file]
    #     last_idx = files[file]

    # if files[max_file] == free_space[min(free_space)]:


    # for i in range(files[max(files)]):
    #     files[max(files)] = files[min(files)]
    #     print(i, max(files) * i)
    # files[min(files)]





if __name__ == '__main__':
    with open('../inputs/day_09.txt', 'r') as f:
        vals = f.read()
    from advent_2024.test.test_day_09 import vals

    # print(part_one(vals))
    print(part_two(vals))
