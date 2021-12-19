from collections import defaultdict


scanner_inputs = open('input.txt').read().split('\n\n')
scanners = {}
for i, scanner in enumerate(scanner_inputs):
    scanners[i] = []
    for row in scanner.split('\n')[1:]:
        x, y, z = row.split(',')
        scanners[i].append((int(x), int(y), int(z)))


def get_rotations(points):
    yield [
        (x, y, z) for (x, y, z) in points
    ]

    yield [
        (x, -y, -z) for (x, y, z) in points
    ]

    yield [
        (x, -z, y) for (x, y, z) in points
    ]

    yield [
        (x, z, -y) for (x, y, z) in points
    ]



    yield [
        (-x, -y, z) for (x, y, z) in points
    ]

    yield [
        (-x, y, -z) for (x, y, z) in points
    ]

    yield [
        (-x, z, y) for (x, y, z) in points
    ]

    yield [
        (-x, -z, -y) for (x, y, z) in points
    ]




    yield [
        (y, -x, z) for (x, y, z) in points
    ]

    yield [
        (y, x, -z) for (x, y, z) in points
    ]

    yield [
        (y, z, x) for (x, y, z) in points
    ]

    yield [
        (y, -z, -x) for (x, y, z) in points
    ]



    yield [
        (-y, x, z) for (x, y, z) in points
    ]

    yield [
        (-y, -x, -z) for (x, y, z) in points
    ]

    yield [
        (-y, -z, x) for (x, y, z) in points
    ]

    yield [
        (-y, z, -x) for (x, y, z) in points
    ]



    yield [
        (z, y, -x) for (x, y, z) in points
    ]

    yield [
        (z, -y, x) for (x, y, z) in points
    ]

    yield [
        (z, x, y) for (x, y, z) in points
    ]

    yield [
        (z, -x, -y) for (x, y, z) in points
    ]



    yield [
        (-z, y, x) for (x, y, z) in points
    ]

    yield [
        (-z, -y, -x) for (x, y, z) in points
    ]

    yield [
        (-z, -x, y) for (x, y, z) in points
    ]

    yield [
        (-z, x, -y) for (x, y, z) in points
    ]


def get_distances(points):
    dists = {}
    for (x1, y1, z1) in points:
        dists[(x1, y1, z1)] = set()
        for (x2, y2, z2) in points:
            if (x1, y1, z1) != (x2, y2, z2):
                dists[(x1, y1, z1)].add((x1 - x2, y1 - y2, z1 - z2))
    return dists

def compare_dists(a, b):
    offsets = defaultdict(int)
    for (x1, y1, z1), dists1 in a.items():
        for (x2, y2, z2), dists2 in b.items():
            if len(dists1 & dists2) >= 1:
                offsets[(x1 - x2, y1 - y2, z1 - z2)] += 1
    if offsets:
        return max([(value, offset) for (offset, value) in offsets.items()])
    return 0, (0,0,0)


def find_alignment(fixed, rotations):
    potentials = []
    for rotation in rotations:
        v, offset = compare_dists(fixed, rotation)
        if v >= 12:
            potentials.append((v, offset, rotation.keys()))
    return max(potentials)


def part1(scanners):
    rotation_dists = {}
    for s, points in scanners.items():
        rotation_dists[s] = [get_distances(r) for r in get_rotations(points)]
    overlaps = defaultdict(set)

    for s1, rotations in sorted(rotation_dists.items()):
        for s2, rotations2 in sorted(rotation_dists.items()):
            if s1 < s2:
                for i, rotation in enumerate(rotations):
                    v, _ = compare_dists(rotations2[0], rotation)
                    if v >= 12:
                        overlaps[s1].add(s2)
                        overlaps[s2].add(s1)

    fixed = set(scanners[0])
    fixed_dists = get_distances(fixed)
    del scanners[0]
    to_visit = {o: ((0,0,0), fixed_dists) for o in overlaps.get(0)}
    visited = {0}

    while to_visit:
        s, (original_offset, dists) = next(iter(to_visit.items()))
        del to_visit[s]
        _, new_offset, new_points = find_alignment(dists, rotation_dists[s])
        xo, yo, zo = new_offset
        xo += original_offset[0]
        yo += original_offset[1]
        zo += original_offset[2]

        new_dists = get_distances(new_points)

        for neighbor in overlaps[s]:
            if neighbor not in visited:
                to_visit[neighbor] = ((xo, yo, zo), new_dists)
        visited.add(s)

        for x, y, z in new_points:
            fixed.add((x + xo, y + yo, z + zo))

    return len(fixed)

        

def part2(scanners):
    scanner_locations = set()
    rotation_dists = {}
    for s, points in scanners.items():
        rotation_dists[s] = [get_distances(r) for r in get_rotations(points)]
    overlaps = defaultdict(set)

    for s1, rotations in sorted(rotation_dists.items()):
        for s2, rotations2 in sorted(rotation_dists.items()):
            if s1 < s2:
                for i, rotation in enumerate(rotations):
                    v, _ = compare_dists(rotations2[0], rotation)
                    if v >= 12:
                        overlaps[s1].add(s2)
                        overlaps[s2].add(s1)

    fixed = set(scanners[0])
    fixed_dists = get_distances(fixed)
    del scanners[0]
    to_visit = {o: ((0,0,0), fixed_dists) for o in overlaps.get(0)}
    visited = {0}

    scanner_locations.add((0,0,0))

    while to_visit:
        s, (original_offset, dists) = next(iter(to_visit.items()))
        del to_visit[s]
        _, new_offset, new_points = find_alignment(dists, rotation_dists[s])
        xo, yo, zo = new_offset
        xo += original_offset[0]
        yo += original_offset[1]
        zo += original_offset[2]

        new_dists = get_distances(new_points)
        scanner_locations.add((xo, yo, zo))

        for neighbor in overlaps[s]:
            if neighbor not in visited:
                to_visit[neighbor] = ((xo, yo, zo), new_dists)
        visited.add(s)

        for x, y, z in new_points:
            fixed.add((x + xo, y + yo, z + zo))

    dists = []
    for (x1, y1, z1) in scanner_locations:
        for (x2, y2, z2) in scanner_locations:
            dists.append(sum((abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))))
    return max(dists)

print(part1({**scanners}))
print(part2(scanners))