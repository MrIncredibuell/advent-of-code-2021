
data = [int(x) for x in open('input.txt').read().split(',')]

def part1(data):
    best = None
    for i in range(min(data), max(data)+1):
        current =  sum([abs(x-i) for x in data])
        if best == None or current < best:
            best = current
    return best
        

def distance(x1, x2):
    diff = abs(x1 - x2)
    return int((diff + 1) * (diff) / 2)

def part2(data):
    best = None
    for i in range(min(data), max(data)+1):
        current =  sum([distance(i, x) for x in data])
        if best == None or current < best:
            best = current
    return best

print(part1(data))
print(part2(data))