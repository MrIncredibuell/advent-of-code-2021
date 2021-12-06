from collections import defaultdict
data = [int(x) for x in open('input.txt').read().split(',')]

def part1(data, max_days=80):
    timer_counts = defaultdict(int)
    for fish in data:
        timer_counts[fish] += 1

    for d in range(max_days):
        new_timer_counts = defaultdict(int)
        for k, v in timer_counts.items():
            if k == 0:
                new_timer_counts[8] += v
                new_timer_counts[6] += v
            else:
                new_timer_counts[k-1] += v
        timer_counts = new_timer_counts
    return sum(timer_counts.values())


def part2(data):
    return part1(data, max_days=256)

print(part1(data))
print(part2(data))