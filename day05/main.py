from collections import defaultdict

rows = open('input.txt').read().split('\n')
data = []
for row in rows:
    p1, p2 = row.split(' -> ')
    x1, y1 = p1.split(',')
    x2, y2 = p2.split(',')
    data.append((
        (int(x1), int(y1)), (int(x2), int(y2))
    ))

def my_range(a, b):
    if a < b:
        return range(a, b + 1)
    return range(b, a + 1)

def part1(data):
    lines = []
    for (x1, y1), (x2, y2) in data:
        if x1 == x2 or y1 == y2:
            lines.append(((x1, y1), (x2, y2)))
    grid = defaultdict(int)
    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            for y in my_range(y1, y2):
                grid[(x1, y)] += 1
        else:
            for x in my_range(x1, x2):
                grid[(x, y1)] += 1
    return len([v for v in grid.values() if v > 1])

def part2(data):
    grid = defaultdict(int)
    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            for y in my_range(y1, y2):
                grid[(x1, y)] += 1
        elif y1 == y2:
            for x in my_range(x1, x2):
                grid[(x, y1)] += 1
        elif x1 < x2 and y1 < y2:
            for i in range(x2 - x1 + 1):
                grid[(x1 + i, y1 + i)] += 1
        elif x1 < x2 and y1 > y2:
            for i in range(x2 - x1 + 1):
                grid[(x1 + i, y1 - i)] += 1
        elif x1 > x2 and y1 < y2:
            for i in range(x1 - x2 + 1):
                grid[(x2 + i, y2 - i)] += 1
        elif x1 > x2 and y1 > y2:
            for i in range(x1 - x2 + 1):
                grid[(x2 + i, y2 + i)] += 1

    return len([v for v in grid.values() if v > 1])


print(part1(data))
print(part2(data))