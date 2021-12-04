rows =  open('input.txt').read().split('\n')
called = [int(x) for x in rows[0].split(',')]
boards = []
rows = rows[2:]

cards = []

while rows:
    card_rows = [r.strip().split(' ') for r in rows[:5]]
    card  = []
    for r in card_rows:
        card.append([int(x) for x in r if x != ''])
    rows = rows[6:]
    cards.append(card)


class Card:
    def __init__(self, rows):
        self.grid = {}
        self.values = {}
        self.checked = {}
        for y in range(len(rows)):
            for x in range(len(rows[y])):
                self.grid[(x, y)] = rows[y][x]
                self.values[rows[y][x]] = (x, y)
        self.width, self.height = len(rows[0]), len(rows)

    def __repr__(self):
        return str(self.grid)

    def play(self, n):
        self.checked[n] = True

    def is_win(self):
        for i in range(self.height):
            found = True
            for j in range(self.width):
                if not (self.checked.get(self.grid[j, i], False)):
                    found = False
            if found:
                return True
        
        for j in range(self.height):
            found = True
            for i in range(self.width):
                if not (self.checked.get(self.grid[j, i], False)):
                    found = False
            if found:
                return True

    def score(self, n):
        s = 0
        for (x, y) in self.grid:
            if not (self.checked.get(self.grid[(x,y)], None)):
                s += self.grid[(x,y)]
        return s * n
        


def part1(called, cards):
    cards = [
        Card(card) for card in cards
    ]
    for i, n in enumerate(called):
        for card in cards:
            card.play(n)
            if card.is_win():
                return card.score(n)
        

def part2(called, cards):
    cards = [
        Card(card) for card in cards
    ]
    for n in called:
        for card in cards[:]:
            card.play(n)
            if card.is_win():
                if len(cards) == 1:
                    return card.score(n)
                cards.remove(card)
        
            

print(part1(called, cards))
print(part2(called, cards))