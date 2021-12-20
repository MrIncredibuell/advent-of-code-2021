alg, data = open('input.txt').read().split('\n\n')

grid = {}
for y, row in enumerate(data.split('\n')):
    for x, value in enumerate(row):
        grid[(x,y)] = value

def compute_pixel(grid, alg, x, y, default='.'):
    s = ''
    for i in range(-1, 2):
        for j in range(-1, 2):
            s += grid.get((x + j, y + i), default)
    s = s.replace('.', '0')
    s = s.replace('#', '1')

    n = int(s, base=2)
    return alg[n]

def step(grid, alg, default='.'):
    new_grid = {}
    x0, y0 = min(grid.keys())
    x1, y1 = max(grid.keys())

    for y in range(y0 - 1, y1 + 2):
        for x in range(x0 - 1, x1 + 2):
            new_grid[(x, y)] = compute_pixel(grid, alg, x, y, default=default)

    return new_grid

def print_grid(grid):
    x0, y0 = min(grid.keys())
    x1, y1 = max(grid.keys())
    for y in range(y0 - 1, y1 + 2):
        s = ''
        for x in range(x0 - 1, x1 + 2):
            s += grid.get((x,y), '.')
        print(s)

def part1(alg, grid):
    for i in range(2):
        grid = step(grid, alg, default = '.' if i % 2 == 0 else '#')

    return len([v for v in grid.values() if v == '#'])

        

def part2(alg, grid):
    for i in range(50):
        grid = step(grid, alg, default = '.' if i % 2 == 0 else '#')

    return len([v for v in grid.values() if v == '#'])

print(part1(alg, grid))
print(part2(alg, grid))