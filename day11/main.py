data = {}
for y, row in enumerate(open('input.txt').read().split('\n')):
    for x, v in enumerate(row):
        data[(x,y)] = int(v)


def neighbors(grid, position):
    x, y = position
    ns = [
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    ]
    return [p for p in ns if p in grid]

def do_turn(grid):
    to_flash = set()
    flashed = set()
    for p in grid:
        grid[p] += 1
        if grid[p] > 9:
            to_flash.add(p)
    while to_flash:
        p = next(iter(to_flash))
        for n in neighbors(grid, p):
            grid[n] += 1
            if grid[n] > 9 and n not in flashed:
                to_flash.add(n)
        to_flash.remove(p)
        flashed.add(p)
    for p in flashed:
        grid[p] = 0
    return len(flashed)


def part1(data):
    data = {**data}
    flash_count = 0
    for i in range(100):
        flash_count += do_turn(data)
    return flash_count
    

def part2(data):
    data = {**data}
    turn = 0
    while True:
        turn += 1
        if do_turn(data) == len(data):
            return turn

print(part1(data))
print(part2(data))