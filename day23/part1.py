rows = open('input.txt').read().split('\n')
map = {}
for y, row in enumerate(rows):
    for x, value in enumerate(row):
        map[(x,y)] = value

positions = {}

for i, x in enumerate([3, 5, 7, 9]):
    for y in range(2, 4):
        positions[(x, y)] = map[(x,y)]
        map[(x,y)] = '.'

ROOM_XS = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9,
}

COSTS = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

def print_map(positions):
    s = ''
    for y in range(5):
        for x in range(14):
            if v := positions.get((x,y)):
                s += v
            else:
                s += map.get((x,y), ' ')
        s += '\n'
    return s

def is_traversable(positions, position):
    if map.get(position, '#') != '.':
        return False
    if positions.get(position, None):
        return False
    return True

def is_valid_destination(positions, old_position, position, letter):
    x, y = position
    old_x, old_y = old_position
    if position in {(3,1), (5,1), (7,1), (9, 1)}:
        return False
    if y in (2, 3) and x != ROOM_XS[letter]:
        return False
    if old_x == x:
        return False
    if old_y == y == 1:
        return False
    if y == 2 and positions.get((x, 3)) != letter:
        return False
    return True
    
def get_traversable_positions(positions, position):
    x,y = position
    for (a, b) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if is_traversable(positions, (a,b)):
            yield (a,b)


def get_candidate_moves(positions, position, letter):
    a, b = position
    if a == ROOM_XS.get(letter) and b == 3:
        return []
    to_visit = set(p for p in get_traversable_positions(positions, position))
    visited = {position}
    candidates = set()
    while to_visit and (p := to_visit.pop()):
        for x, y in get_traversable_positions(positions, p):
            if (x, y) not in visited:
                to_visit.add((x,y))
        if is_valid_destination(positions, position, p, letter):
            _, py = p
            if py in (2,3):
                return {p}
            candidates.add(p)
        visited.add(p)
    try:
        candidates.remove(position)
    except KeyError:
        pass
    
    return candidates
    

def do_move(positions, old_position, new_position):
    x, _ = new_position
    letter = positions[old_position]
        
    new_positions = {p: l for p,l in positions.items() if p != old_position}
    new_positions[new_position] = letter

    if x == ROOM_XS[letter]:
        if new_positions.get((x, 2)) == new_positions.get((x, 3)):
            del new_positions[(x,2)]
            del new_positions[(x,3)]
    return new_positions


def cost(old, new, letter):
    old_x, old_y = old
    new_x, new_y = new
    s = (old_y - 1) + abs(old_x - new_x) + (new_y - 1)
    return s * COSTS[letter]
    


CACHE = {}

def try_to_solve(positions):
    if len(positions) == 0:
        return 0

    s = str(sorted(positions.items()))
    if b := CACHE.get(s):
        return b

    best = None

    candidate_moves = []
    for position, letter in positions.items():
        candidates = get_candidate_moves(positions, position, letter)
        candidate_moves += [
            (position, letter, c) for c in candidates
        ]

    finishing_moves = [m for m in candidate_moves if m[2][1] in (2,3)]
    if finishing_moves:
        candidate_moves = [finishing_moves[0]]
    for position, letter, c in candidate_moves:
        new_positions = do_move(positions, position, c)
        value = try_to_solve(new_positions)
        if value is not None:
            value += cost(position, c, letter)
            if (best is None) or (value < best):
                best = value
    CACHE[s] = best
    return best


    


def part1(positions):
    best = try_to_solve(positions)
    print(best)
        

print(part1(positions))