from collections import defaultdict
data = defaultdict(list)
for row in open('input.txt').read().split('\n'):
    s, d = row.split('-')
    data[s].append(d)
    data[d].append(s)


def part1(data):
    visited = defaultdict(set)
    visited['start'].add(tuple())
    to_visit = set(['start'])
    while to_visit:
        current = to_visit.pop()
        for neighbor in data[current]:
            for existing_path in visited[current]:
                if (neighbor == neighbor.upper()) or (neighbor not in existing_path):
                    new_path = tuple([*existing_path, current])
                    if new_path not in visited[neighbor]:
                        visited[neighbor].add(new_path)
                        to_visit.add(neighbor)
    return len(visited['end'])

def part2(data):
    visited = defaultdict(set)
    visited['start'].add(tuple())
    to_visit = set(['start'])
    has_double_lookup = {}
    while to_visit:
        current = to_visit.pop()
        current_is_small = current == current.lower()
        for neighbor in data[current]:
            for existing_path in visited[current]:
                if existing_path in has_double_lookup:
                    has_double = has_double_lookup[existing_path]
                else:
                    has_double = 2 in {existing_path.count(x) for x in existing_path if x == x.lower()}
                    has_double_lookup[existing_path] = has_double
                has_double = has_double or (current_is_small and current in existing_path)
                can_visit = any([
                    (neighbor not in existing_path),
                    (neighbor == neighbor.upper()),
                    (neighbor not in {'start', 'end'} and (not has_double) ),
                ])
                if can_visit:
                    new_path = tuple([*existing_path, current])
                    if new_path not in visited[neighbor]:
                        visited[neighbor].add(new_path)
                        if neighbor not in ('start', 'end'):
                            to_visit.add(neighbor)
    return len(visited['end'])

print(part1(data))
print(part2(data))