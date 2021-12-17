x, y = open('input.txt').read()[len('target area: '):].split(', ')
xs = [int(v) for v in x[2:].split('..')]
ys = [int(v) for v in y[2:].split('..')]

class TooFarError(Exception):
    def __init__(self, too_far_x, too_far_y):
        self.too_far_x = too_far_x
        self.too_far_y = too_far_y

class TooShortError(Exception):
    pass

def fire(velocity, xs, ys):
    x, y = (0, 0)
    vx, vy = velocity
    left_x, right_x = xs
    lower_y, upper_y = ys
    max_y = 0
    while True:
        x += vx
        y += vy
        if y > max_y:
            max_y = y
        if (left_x <= x <= right_x) and (lower_y <= y <= upper_y):
            return max_y
        too_far_x = x > right_x
        too_far_y = y < lower_y
        if too_far_x or too_far_y:
            raise TooFarError(too_far_x, too_far_y)
        if vx == 0 and y < lower_y:
            if left_x > x:
                raise TooShortError()
        vy -= 1
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1


def part1(xs, ys):
    max_y = 0
    for vx in range(1, xs[1] + 1):
        vy = ys[0]
        done = False
        while not done:
            try:
                y = fire((vx, vy), xs, ys)
                if y > max_y:
                    max_y = y
            except TooFarError as err:
                if err.too_far_x:
                    done = True
            except:
                done = True
            vy += 1
            if vy > 1000:
                done = True
    return max_y
        

def part2(xs, ys):
    solutions = set()
    max_y = 0
    for vx in range(1, xs[1] + 1):
        vy = ys[0]
        done = False
        while not done:
            try:
                y = fire((vx, vy), xs, ys)
                solutions.add((vx, vy))
            except TooFarError as err:
                if err.too_far_x:
                    done = True
            except:
                done = True
            vy += 1
            if vy > 1000:
                done = True
    return len(solutions)

print(part1(xs, ys))
print(part2(xs, ys))