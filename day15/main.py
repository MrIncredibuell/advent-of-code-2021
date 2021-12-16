rows = open('input.txt').read().split('\n')
data = {}
for y, row in enumerate(rows):
    for x, value in enumerate(row):
        data[(x,y)] = int(value)


def neighbors(position):
    x, y = position
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1

def part1(data):
    visited = {}
    to_visit = {(0,0): 0}

    while to_visit:
        distance, current = min((v, k) for k, v in to_visit.items())
        del to_visit[current]
        visited[current] = distance + data[current]
        for n in neighbors(current):
            if all([
                n not in visited,
                n in data,
                (n not in to_visit or to_visit[n] > visited[current])
            ]):
                to_visit[n] = visited[current]
    bottom_right = max(data.keys())

    return visited[bottom_right] - visited[(0,0)]
        
from queue import PriorityQueue
def part2(data):
    new_data = {}
    width, height = max(data.keys())
    width += 1
    height += 1

    for (x, y), risk in sorted(data.items()):
        for i in range(5):
            for j in range(5):
                m = i + j
                new_risk = (risk + m)
                if new_risk > 9:
                    new_risk = (new_risk + 1) % 10
                new_data[(x + (width * i), y + (height * j))] = new_risk
    data = new_data

    visited = {}
    to_visit = PriorityQueue()
    to_visit.put((0, (0,0)))

    while not to_visit.empty():
        distance, current = to_visit.get()
        if current in visited:
            continue
        visited[current] = distance + data[current]
        if current == (width*5-1, height*5-1):
            return visited[current] - visited[(0,0)]
        for n in neighbors(current):
            if all([
                n not in visited,
                n in data,
            ]):
                to_visit.put((visited[current], n))
    bottom_right = max(data.keys())

    return visited[bottom_right] - visited[(0,0)]

print(part1(data))
print(part2(data))