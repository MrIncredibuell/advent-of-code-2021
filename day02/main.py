data = []
rows = open('input.txt').read().split('\n')
for row in rows:
    direction, distance = row.split(' ')
    data.append((direction, int(distance)))

def part1(data):
    x, z = 0, 0

    for direction, distance in data:
        if direction == 'forward':
            x += distance
        if direction == 'up':
            z -= distance
        if direction == 'down':
            z += distance

    return x * z

        

def part2(data):
    x, z, aim = 0, 0, 0

    for direction, distance in data:
        if direction == 'forward':
            x += distance
            z += aim * distance
        if direction == 'up':
            aim -= distance
        if direction == 'down':
            aim += distance

    return x * z

print(part1(data))
print(part2(data))