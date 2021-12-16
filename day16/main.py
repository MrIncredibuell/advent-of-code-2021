from dataclasses import dataclass

data = open('input.txt').read()

@dataclass
class Packet:
    version: int
    type_id: int
    subpackets: list = None
    value: int = None

    def get_value(self):
        if self.value:
            return self.value
        elif self.type_id == 0:
            v = 0
            for s in self.subpackets or []:
                v += s.get_value()
            return v
        elif self.type_id == 1:
            v = 1
            for s in self.subpackets or []:
                v *= s.get_value()
            return v
        elif self.type_id == 2:
            return min([s.get_value() for s in self.subpackets])
        elif self.type_id == 3:
            return max([s.get_value() for s in self.subpackets])
        elif self.type_id == 5:
            return 1 if self.subpackets[0].get_value() > self.subpackets[1].get_value() else 0
        elif self.type_id == 6:
            return 1 if self.subpackets[0].get_value() < self.subpackets[1].get_value() else 0
        elif self.type_id == 7:
            return 1 if self.subpackets[0].get_value() == self.subpackets[1].get_value() else 0





def parse_packets(binary):
    i = 0
    version = int(binary[:3], base=2)
    type_id = int(binary[3:6], base=2)
    i += 6
    if type_id == 4:
        value = ''
        while binary[i] == '1':
            value += binary[i+1:i+5]
            i += 5
        value += binary[i+1:i+5]
        i += 5
        value = int(value, base=2)
        p = Packet(
            version=version,
            type_id=type_id,
            value=value,
        )
        return p, i
    else:
        if binary[i] == '0':
            l = 15
            i += 1
            length = int(binary[i:i+l], base=2)
            i += l
            subs = []
            end_of_subs = i + length
            while i < end_of_subs and end_of_subs - i > 6:
                s, j = parse_packets(binary[i:])
                subs.append(s)
                i += j
            i = end_of_subs
            p = Packet(
                version=version,
                type_id=type_id,
                subpackets=subs,
            )
            return p, i
        else:
            l = 11
            i += 1
            n = int(binary[i:i+l], base=2)
            i += l
            subs = []
            for x in range(n):
                s, j = parse_packets(binary[i:])
                subs.append(s)
                i += j
            p = Packet(
                version=version,
                type_id=type_id,
                subpackets=subs
            )
            return p, i


def recursive_version_sum(p):
    s = p.version
    for sub in p.subpackets or []:
        s += recursive_version_sum(sub)
    return s

def part1(data):
    h = int(data, base=16)
    binary = "{0:b}".format(h)
    while (len(binary) % 4) != 0:
        binary = '0' + binary

    version_sum = 0
    i = 0
    while len(binary) - i > 7:
        p, j = parse_packets(binary[i:])
        i += j
        version_sum +=recursive_version_sum(p)
    return version_sum


def part2(data):
    h = int(data, base=16)
    binary = "{0:b}".format(h)
    while (len(binary) % 4) != 0:
        binary = '0' + binary

    i = 0
    while len(binary) - i > 7:
        p, j = parse_packets(binary[i:])
        return p.get_value()

print(part1(data))
print(part2(data))