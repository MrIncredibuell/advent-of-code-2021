data = open('input.txt').read().split('\n')


CLOSINGS = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}


POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def part1(data):
    score = 0
    for line in data:
        stack = []
        corrupt  = False
        for c in line:
            if corrupt:
                break
            if c in['(', '[', '{', '<']:
                stack.append(c)
            else:
                if stack[-1] != CLOSINGS[c]:
                    score += POINTS[c]
                    corrupt = True

                else:
                    stack = stack[:-1]
    return score


OPENINGS = {v:k for k,v in CLOSINGS.items()}


POINTS_2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}        


def part2(data):
    scores = []
    for line in data:
        stack = []
        corrupt  = False
        for c in line:
            if corrupt:
                break
            if c in['(', '[', '{', '<']:
                stack.append(c)
            else:
                if stack[-1] != CLOSINGS[c]:
                    corrupt = True

                else:
                    stack = stack[:-1]
        if not corrupt:
            stack.reverse()
            score = 0
            for c in stack:
                score *= 5
                score += POINTS_2[OPENINGS[c]]
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


print(part1(data))
print(part2(data))