data = []
for line in open('input.txt').read().split('\n'):
    a, b = line.split(' | ')
    data.append((a.split(' '), b.split(' ')))

def part1(data):
    count = 0
    for _, results in data:
        for s in results:
            if len(s) in [2, 4, 3, 7]:
                count += 1
    return count

t, tl, tr, m, bl, br, b = range(7)

connections = {
    0: {t, tl, tr, bl, br, b},
    1: {tr, br},
    2: {t, tr, m, bl, b},
    3: {t, tr, m, br, b},
    4: {tl, tr, m, br},
    5: {t, tl, m, br, b},
    6: {t, tl, m, bl, br, b},
    7: {t, tr, br},
    8: {t, tl, tr, m, bl, br, b},
    9: {t, tl, tr, m, br, b},
}

def segment_to_digit(s, mapping):
    mapped_wires = {mapping[l] for l in s}

    digit = [k for k, v in connections.items() if v == mapped_wires][0]
    return digit

def recursive_bullshit(mapping_so_far, possible_mappings, segs):
    if len(mapping_so_far) == 7:
        for d in segs:
            try:
                segment_to_digit(d, mapping_so_far)
            except IndexError:
                return None
        return mapping_so_far
    for values in possible_mappings.values():
        if len(values) == 0:
            # have a letter with no possibuellities
            return None
    l, values = next(iter(possible_mappings.items()))
    for v in values:
        new_possibilities = {
            k: {p for p in ps if p != v}
            for k, ps in possible_mappings.items()
            if k != l
        }
        if result := recursive_bullshit(
            {
                l: v,
                **mapping_so_far,
            },
            new_possibilities,
            segs=segs,
        ):
            return result

def part2(data):
    total = 0

    for segments, results in data:
        possible_wires = {l: {t, tl, tr, m, bl, br, b} for l in 'abcdefg'}
        for s in segments + results:
            possible_numbers = {k for k, v in connections.items() if len(v) == len(s)}
            candidates = set()
            for n  in possible_numbers:
                candidates |= connections[n]
            
            for l in s:
                possible_wires[l] &= candidates
        mapping = recursive_bullshit({}, possible_wires, segs=segments+results)

        nstring = ''
        for r in results:
            nstring += str(segment_to_digit(r, mapping))
        total += int(nstring)
    return total
    

print(part1(data))
print(part2(data))