data = open('input.txt').read().split('\n')

def part1(data):
    gamma = []
    epsilon = []
    for i in range(len(data[0])):
        count = 0
        for row in data:
            if row[i] == '1':
                count += 1
        if count > len(data) / 2:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    gamma = int(''.join(gamma), base=2)
    epsilon = int(''.join(epsilon), base=2)
    return gamma * epsilon

def part2_helper(i, data, keep_most_common):
    if len(data) == 1:
        return int(''.join(data[0]), base=2)
    ones = []
    zeroes = []
    for row in data:
        if row[i] == '1':
            ones.append(row)
        else:
            zeroes.append(row)

    if keep_most_common:
        if len(ones) >= len(zeroes):
            return part2_helper(i+1, ones, keep_most_common)
        else:
            return part2_helper(i+1, zeroes, keep_most_common)
    else:
        if len(ones) < len(zeroes):
            return part2_helper(i+1, ones, keep_most_common)
        else:
            return part2_helper(i+1, zeroes, keep_most_common)


def part2(data):
    oxygen = part2_helper(0, data, True)
    co2 = part2_helper(0, data, False)
    return oxygen * co2

print(part1(data))
print(part2(data))