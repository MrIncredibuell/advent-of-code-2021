positions = [int(x[-1]) for x in open('input.txt').read().split('\n')]


class die():
    i = 1
    rolls = 0
    
    def roll(self):
        self.rolls += 1
        value = self.i
        self.i += 1
        if self.i > 100:
            self.i = 1
        return value


def part1(positions):
    positions = [positions[0] - 1, positions[1] -1]
    scores = [0, 0]
    player = 0
    d = die()
    while len([s for s in scores if s >= 1000]) == 0:
        positions[player] += d.roll() + d.roll() + d.roll()
        positions[player] = positions[player] % 10
        scores[player] += positions[player] + 1
        player = (player + 1) % 2
    return d.rolls * min(scores)


def split_worlds(positions, scores, player, cache):
    WIN_SCORE = 21
    if rate := cache.get((positions, scores, player)):
        return rate
    if len([s for s in scores if s >= WIN_SCORE]) > 0:
        if scores[0] >= WIN_SCORE:
            return [1,0]
        else:
            return [0,1]

    next_player = (player + 1) % 2
    total_rate = [0, 0]

    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                temp_positions = list(positions[:])
                temp_scores = list(scores[:])
                temp_positions[player] += i + j + k
                temp_positions[player] = temp_positions[player] % 10
                temp_scores[player] += temp_positions[player] + 1
                rate = split_worlds(
                    tuple(temp_positions),
                    tuple(temp_scores),
                    next_player,
                    cache,
                )
                for x, v in enumerate(rate):
                    total_rate[x] += v
    cache[(positions, scores, player)] = total_rate
    return total_rate


def part2(positions):
    positions = [positions[0] - 1, positions[1] -1]
    scores = [0, 0]
    player = 0
    cache = {}
    result = split_worlds(
        tuple(positions),
        tuple(scores),
        player,
        cache
    )
    
    return max(result)


print(part1(positions))
print(part2(positions))