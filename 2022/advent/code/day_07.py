if __name__ == '__main__':
    with open('../inputs/day_07.txt') as f:
        vals = f.read().split('\n')

    outermost_dir = dict(files=[])
    parents = dict()
    last_val = None
    proceed = True
    current_position = outermost_dir
    current_dir = None
    print(vals)
    for val in vals:
        print(val)
        if val == '$ cd /':
            current_position = outermost_dir
        elif val == '$ cd ..':
            parent_dir = outermost_dir[parents[current_dir]]
            print('get parent', outermost_dir.get(parent_dir))
        elif val.startswith('$ cd'):
            dir_nav = val[5:]
            parents[dir_nav] = current_dir
            current_position = outermost_dir[dir_nav]
            current_dir = dir_nav
            print('parents', parents)
        elif val == '$ ls':
            continue
        elif val.startswith('dir'):
            dir_name = val[4:]
            current_position[dir_name] = dict(files=[])
        elif val[0].isdigit():
            filesize = int(val.split(' ')[0])
            current_position['files'].append(filesize)
        print('current position ', current_position.keys() if current_position else None)
        print(current_position)




    print(vals)