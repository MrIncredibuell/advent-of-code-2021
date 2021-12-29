rows = open('input.txt').read().split('\n')
data = {}
for y, row in enumerate(rows):
    for x, value in enumerate(row):
        if value != '.':
            data[(x,y)] = value


class Cucumbers:
    def __init__(self, data):
        self.width = max([x for (x, _)  in data.keys()]) + 1
        self.height = max([y for (_, y)  in data.keys()]) + 1
        self.unblocked_east = set()
        self.unblocked_south = set()
        self.blocked_east = set()
        self.blocked_south = set()
        self.all = set()
        for (x,y), c in data.items():
            self.all.add((x,y))
            if c == '>':
                if ((x+1) % self.width, y) in data:
                    self.blocked_east.add((x,y))
                else:
                    self.unblocked_east.add((x,y))
            elif c == 'v':
                if (x, (y+1) % self.height) in data:
                    self.blocked_south.add((x,y))
                else:
                    self.unblocked_south.add((x,y))

    
    def step(self):
        count = len(self.unblocked_east) + len(self.unblocked_south)
        for (x,y) in list(self.unblocked_east):
            self.all.remove((x,y))
            self.all.add(((x+1) % self.width, y))
            self.unblocked_east.remove((x,y))
            if ((x+2) % self.width, y) in self.all:
                self.blocked_east.add(((x+1) % self.width, y))
            else:
                self.unblocked_east.add(((x+1) % self.width, y))
            if ((x+1) % self.width, (y-1) % self.height) in self.unblocked_south:
                self.unblocked_south.remove(((x+1) % self.width, (y-1) % self.height))
                self.blocked_south.add(((x+1) % self.width, (y-1) % self.height))

            if (x, (y-1) % self.height) in self.blocked_south:
                self.blocked_south.remove((x, (y-1) % self.height))
                self.unblocked_south.add((x, (y-1) % self.height))
            elif ((x-1) % self.width, y) in self.blocked_east:
                self.unblocked_east.add(((x-1) % self.width, y))
                self.blocked_east.remove(((x-1) % self.width, y))

        for (x,y) in list(self.unblocked_south):
            self.all.remove((x,y))
            self.all.add((x, (y+1) % self.height))
            self.unblocked_south.remove((x,y))
            if (x, (y+2) % self.height) in self.all:
                self.blocked_south.add((x, (y+1) % self.height))
            else:
                self.unblocked_south.add((x, (y+1) % self.height))
            if ((x-1) % self.width, (y+1) % self.height) in self.unblocked_east:
                self.unblocked_east.remove(((x-1) % self.width, (y+1) % self.height))
                self.blocked_east.add(((x-1) % self.width, (y+1) % self.height))

            if ((x-1) % self.width, y) in self.blocked_east:
                self.blocked_east.remove(((x-1) % self.width, y))
                self.unblocked_east.add(((x-1) % self.width, y))
            elif (x, (y-1) % self.height) in self.blocked_south:
                self.unblocked_south.add((x, (y-1) % self.height))
                self.blocked_south.remove((x, (y-1) % self.height))

        return count


def part1(data):
    i = 1
    cs = Cucumbers(data)
    while cs.step():
        i += 1
    return i
        
print(part1(data))