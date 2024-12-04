if __name__ == '__main__':
    with open('../inputs/day_20.txt', 'r') as f:
        vals = f.read().split('\n')

    vals = '''1
2
-3
3
-2
0
4'''.split('\n')
    vals = [int(x) for x in vals]
    for i in range(len(vals)):
        print(vals)
        print(i, vals[i])
        distance = i + vals[i] if vals[i] > 0 else i - vals[i]
        print('distance',distance)
        orig_vals = vals.copy()
        if distance > len(vals):
            from_front = len(vals) - distance
            print('from front', from_front)
            vals = vals[:from_front] + [vals[i]] + vals[from_front:]
        elif distance < 0:
            from_back = 0 - len(vals) - i
            vals = vals[:from_back] + [vals[i]] + vals[from_back:]
        else:
            vals = vals[:distance] + [vals[i]] + vals[distance:]
        vals.pop(orig_vals.index(vals[i]))

    zero_idx = vals.index(0)
    print(vals.index(0))

