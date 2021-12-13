s1, s2 = open('input.txt').read().split('\n\n')
dots = set()
for line in s1.split('\n'):
    x, y = line.split(',')
    dots.add((int(x), int(y)))

folds = []
for line in s2.split('\n'):
    axis, value = line.split('=')
    folds.append((axis[-1], int(value)))

def part1(dots, folds):
    for axis, value in folds[:1]:
        new_dots = set()
        if axis == 'x':
            for x, y in dots:
                if x > value:
                    new_dots.add(((2 * value - x), y))
                else:
                    new_dots.add((x, y))
        elif axis == 'y':
            for x, y in dots:
                if y > value:
                    new_dots.add((x, (2 * value - y)))
                else:
                    new_dots.add((x, y))
        dots = new_dots
    return len(dots)

        
def print_dots(dots):
    max_x, max_y = 0, 0
    for x, y in dots:
        max_x = max(x, max_x)
        max_y = max(y, max_y)
    
    for y in range(max_y + 1):
        s = []
        for x in range(max_x + 1):
            if (x, y) in dots:
                s.append('#')
            else:
                s.append(' ')
        print(''.join(s))

def part2(dots, folds):
    for axis, value in folds:
        new_dots = set()
        if axis == 'x':
            for x, y in dots:
                if x > value:
                    new_dots.add(((2 * value - x), y))
                else:
                    new_dots.add((x, y))
        elif axis == 'y':
            for x, y in dots:
                if y > value:
                    new_dots.add((x, (2 * value - y)))
                else:
                    new_dots.add((x, y))
        dots = new_dots

    print_dots(dots)
    print()


print(part1(dots, folds))
part2(dots, folds)