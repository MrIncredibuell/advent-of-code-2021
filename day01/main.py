data = [int(x) for x in open('input.txt').read().split('\n')]

def part1(data):
    r = 0
    for i, x in enumerate(data[:-1]):
        if data[i+1] > x:
            r += 1
    return r
        

def part2(data):
    r = 0
    for i in range(len(data) - 3):
        if sum(data[i:i+3]) < sum(data[i+1:i+4]):
            r += 1
    return r

print(part1(data))
print(part2(data))