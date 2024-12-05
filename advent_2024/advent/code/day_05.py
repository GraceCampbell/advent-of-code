from math import floor


def part_one(vals):
    rules, updates = parse_input(vals)
    correct_updates = get_evaluated_updates(rules, updates)
    return get_middle_page_numbers(correct_updates)


def part_two(vals):
    rules, updates = parse_input(vals)
    incorrect_updates = get_evaluated_updates(rules, updates, incorrect=True)

    ordered_updates = []
    for update in incorrect_updates:
        relevant_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
        # key: page - values: all pages that must come before it
        ordered_rules = {}
        for k, v in relevant_rules:
            ordered_rules.setdefault(v, set()).add(k)
        orders = {k: len(v) for k, v in ordered_rules.items()}
        # Assign any page with nothing before it to correct ranking
        first_page = set([x[0] for x in relevant_rules]) - set([x[1] for x in relevant_rules])
        if first_page:
            orders[list(first_page)[0]] = 0
        ordered_updates.append(sorted(update, key=orders.get))

    return get_middle_page_numbers(ordered_updates)


def get_evaluated_updates(rules, updates, incorrect=False):
    evaluated_updates = []
    for update in updates:
        right_order = True
        order = dict({v: k for k, v in enumerate(update)})
        for rule in rules:
            if rule[0] in order and rule[1] in order:
                if order[rule[0]] > order[rule[1]]:
                    right_order = False
        if incorrect:
            if not right_order:
                evaluated_updates.append(update)
        else:
            if right_order:
                evaluated_updates.append(update)
    return evaluated_updates


def get_middle_page_numbers(updates):
    page_numbers = 0
    for update in updates:
        middle_idx = floor(len(update) / 2)
        page_numbers += int(update[middle_idx])
    return page_numbers


def parse_input(vals):
    rules = [x.split('|') for x in vals if '|' in x]
    updates = [x.split(',') for x in vals if ',' in x]

    return rules, updates


if __name__ == '__main__':
    with open('../inputs/day_05.txt', 'r') as f:
        vals = f.read().split('\n')

    print(part_one(vals))
    print(part_two(vals))
