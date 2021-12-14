from collections import defaultdict
from functools import lru_cache

lines = open('input.txt').read().split('\n')
start = lines[0]

rules = {}
for line in lines[2:]:
    a, b = line.split(' -> ')
    rules[a] = b


def part1(start, rules,):
    s = start[:]
    for _ in range(10):
        i = 0
        while i <= len(s) + 2:
            if new := rules.get(s[i:i + 2]):
                i += 1
                s = ''.join([s[:i], new, s[i:]])
            i += 1
    
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1
    return max(counts.values()) - min(counts.values())


def part2(start, rules):
    d = 40
    counts = defaultdict(int)
    cache = defaultdict(dict)
    for (l,r), m in rules.items():
        cache[(1, l, r)] = {m:1}
    
    for i in range(2, d + 1):
        for (l,r), m in rules.items():
            new_counts = defaultdict(int)
            for k,v in cache[(i-1, l, m)].items():
                new_counts[k] += v
            for k,v in cache[(i-1, m, r)].items():
                new_counts[k] += v
            new_counts[m] += 1
            cache[(i, l, r)] = new_counts

    for c in start:
        counts[c] += 1

    for i in range(len(start) - 1):
        for k, v in cache[(d, start[i], start[i+1])].items():
            counts[k] += v
    
    return max(counts.values()) - min(counts.values())



print(part1(start, rules))
print(part2(start, rules))