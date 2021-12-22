rows = open('input.txt').read().split('\n')

steps = []
for row in rows:
    on, dimensions = row.split(' ')
    step = [on == 'on']
    dimensions = dimensions.split(',')
    for d in dimensions:
        _, bounds = d.split('=')
        minb, maxb = bounds.split('..')
        step.append((int(minb), int(maxb)))
    steps.append(step)


def find_overlap(cubea, cubeb):
    overlap_dimensions = []
    for i, (mina, maxa) in enumerate(cubea):
        minb, maxb = cubeb[i]
        if maxa < minb or mina > maxb:
            return None
        if mina <= minb <= maxb <= maxa:
            overlap_dimensions.append((minb, maxb))
            continue
        if minb <= mina <= maxa <= maxb:
            overlap_dimensions.append((mina, maxa))
            continue
        if mina <= minb <= maxa <= maxb:
            overlap_dimensions.append((minb, maxa))
            continue
        if minb <= mina <= maxb <= maxa:
            overlap_dimensions.append((mina, maxb))
    return overlap_dimensions


def split_cube(parent, baby):
    (minxp, maxxp), (minyp, maxyp), (minzp, maxzp) = parent
    if len(baby) != 3:
        print(baby)
    (minxb, maxxb), (minyb, maxyb), (minzb, maxzb) = baby
    candidates = [
        ((minxp, minxb - 1), (minyp, minyb - 1), (minzp, minzb - 1)),
        ((minxp, minxb - 1), (minyp, minyb - 1), (minzb, maxzb)),
        ((minxp, minxb - 1), (minyp, minyb - 1), (maxzb + 1, maxzp)),
        ((minxp, minxb - 1), (minyb, maxyb), (minzp, minzb - 1)),
        ((minxp, minxb - 1), (minyb, maxyb), (minzb, maxzb)),
        ((minxp, minxb - 1), (minyb, maxyb), (maxzb + 1, maxzp)),
        ((minxp, minxb - 1), (maxyb + 1, maxyp), (minzp, minzb - 1)),
        ((minxp, minxb - 1), (maxyb + 1, maxyp), (minzb, maxzb)),
        ((minxp, minxb - 1), (maxyb + 1, maxyp), (maxzb + 1, maxzp)),

        ((minxb, maxxb), (minyp, minyb - 1), (minzp, minzb - 1)),
        ((minxb, maxxb), (minyp, minyb - 1), (minzb, maxzb)),
        ((minxb, maxxb), (minyp, minyb - 1), (maxzb + 1, maxzp)),
        ((minxb, maxxb), (minyb, maxyb), (minzp, minzb - 1)),
        # ((minxb, maxxb), (minyb, maxyb), (minzb, maxzb)),
        ((minxb, maxxb), (minyb, maxyb), (maxzb + 1, maxzp)),
        ((minxb, maxxb), (maxyb + 1, maxyp), (minzp, minzb - 1)),
        ((minxb, maxxb), (maxyb + 1, maxyp), (minzb, maxzb)),
        ((minxb, maxxb), (maxyb + 1, maxyp), (maxzb + 1, maxzp)),

        ((maxxb+ 1, maxxp), (minyp, minyb - 1), (minzp, minzb - 1)),
        ((maxxb+ 1, maxxp), (minyp, minyb - 1), (minzb, maxzb)),
        ((maxxb+ 1, maxxp), (minyp, minyb - 1), (maxzb + 1, maxzp)),
        ((maxxb+ 1, maxxp), (minyb, maxyb), (minzp, minzb - 1)),
        ((maxxb+ 1, maxxp), (minyb, maxyb), (minzb, maxzb)),
        ((maxxb+ 1, maxxp), (minyb, maxyb), (maxzb + 1, maxzp)),
        ((maxxb+ 1, maxxp), (maxyb + 1, maxyp), (minzp, minzb - 1)),
        ((maxxb+ 1, maxxp), (maxyb + 1, maxyp), (minzb, maxzb)),
        ((maxxb+ 1, maxxp), (maxyb + 1, maxyp), (maxzb + 1, maxzp)),
    ]

    actuals = []
    for ((minx, maxx), (miny, maxy), (minz, maxz)) in candidates:
        if minx <= maxx and miny <= maxy and minz <= maxz:
            actuals.append(((minx, maxx), (miny, maxy), (minz, maxz)))

    return set(actuals)




def do_step(ons, step):
    on, xs, ys, zs = step
    new_ons = set()

    for cube in ons:
        overlap = find_overlap((xs, ys, zs), cube)
        if overlap:
            new_ons |= split_cube(cube, overlap)
            
        else:
            new_ons.add(cube)
    if on:
        new_ons.add((xs, ys, zs))
    return new_ons



def part1(steps):
    ons = set()
    for step in steps:
        ons = do_step(ons, step)

    total = 0
    for cube in ons:
        overlap = find_overlap(cube, ((-50,50), (-50,50), (-50,50)))
        if overlap:
            ((minx, maxx), (miny, maxy), (minz, maxz)) = overlap
            total += (maxx - minx + 1) * (maxy - miny + 1) * (maxz - minz + 1)
    return total
    
        

def part2(steps):
    ons = set()
    for step in steps:
        ons = do_step(ons, step)

    total = 0
    for cube in ons:
        ((minx, maxx), (miny, maxy), (minz, maxz)) = cube
        total += (maxx - minx + 1) * (maxy - miny + 1) * (maxz - minz + 1)
    return total

print(part1(steps))
print(part2(steps))
