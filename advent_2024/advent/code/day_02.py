def part_one(vals):
    safe_count = 0
    reports = get_reports(vals)
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
    return safe_count


def part_two(vals):
    safe_count = 0
    reports = get_reports(vals)
    for report in reports:
        for i in range(len(report)):
            report_minus_one = report[:i] + report[i + 1:]
            if is_safe_report(report_minus_one):
                safe_count += 1
                break
    return safe_count


def is_safe_report(report):
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    abs_diffs = [abs(x) for x in diffs]
    all_inc_or_dec = abs(sum([-1 if x < 0 else 1 for x in diffs])) == len(diffs)
    one_to_three_diff = min(abs_diffs) >= 1 and max(abs_diffs) <= 3
    if all_inc_or_dec and one_to_three_diff:
        return True


def get_reports(vals):
    return [list(map(int, x.split())) for x in vals]


if __name__ == '__main__':
    with open('../inputs/day_02.txt', 'r') as f:
        vals = f.read().split('\n')

    print(part_one(vals))
    print(part_two(vals))