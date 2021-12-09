
data = {}
rows = open('input.txt').read().split('\n')
for y, row in enumerate(rows):
    for x, height in enumerate(row):
        data[(x,y)] = int(height)


def neighboring_heights(data, x, y):
    heights = [
        data.get((x + 1, y)),
        data.get((x - 1, y)),
        data.get((x, y + 1)),
        data.get((x, y - 1)),
    ]

    return [h for h in heights if h is not None]


def part1(data):
    mins = []
    for (x,y), h in data.items():
        hs = neighboring_heights(data, x, y)
        if h < min(hs):
            mins.append(h)
    return sum([h+1 for h in mins])


def get_neighbors(data, x, y):
    neighbors = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

    return [n for n in neighbors if n in data]


def grow_basin(data, basin):
    found = True
    while found == True:
        found = False
        for x,y in basin:
            ns = get_neighbors(data, x, y)
            for a, b in ns:
                if (a,b) in basin:
                    continue
                if data[(a,b)] == 9:
                    continue
                new_ns = get_neighbors(data, a, b)
                neighbor_mins = {
                    data[n]: n for n in new_ns
                }
                lowest = min(neighbor_mins.keys())
                flows_to = [
                    v for k, v in neighbor_mins.items()
                    if k == lowest
                ]
                should_join = True
                for v in flows_to:
                    if v not in basin:
                        should_join = False
                if should_join:
                    found = True
                    basin.append((a,b))
    return basin


def part2(data):
    mins = []
    for (x,y), h in data.items():
        hs = neighboring_heights(data, x, y)
        if h < min(hs):
            mins.append((x,y))

    basins = []
    for m in mins:
        basins.append(grow_basin(data, [m]))

    basins = sorted(basins, key=lambda k: len(k))[-3:]

    result = 1
    for b in basins:
        result *= len(b)
    return result


print(part1(data))
print(part2(data))