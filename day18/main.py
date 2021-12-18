from math import floor, ceil

class Node:
    def __init__(self, parent, left, right, depth):
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth

    def __repr__(self):
        return f'[{self.left},{self.right}]'

    def magnitude(self):
        m = 0
        if isinstance(self.left, Node):
            m += self.left.magnitude() * 3
        else:
            m += self.left * 3

        if isinstance(self.right, Node):
            m += self.right.magnitude() * 2
        else:
            m += self.right * 2

        return m
         


def parse_row(row, parent=None):
    pair = []
    node = Node(parent=parent, left=None, right=None, depth=1 if parent is None else parent.depth + 1)
    if row[0] != '[':
        raise Exception('Expected ]')
    if row[1] == '[':
        new_pair, offset = parse_row(row[1:], parent=node)
        pair.append(new_pair)
        offset += 1
    else:
        pair.append(int(row[1]))
        offset = 2
    if row[offset] != ',':
        raise Exception('Expected ,')
    offset += 1
    if row[offset] == '[':
        new_pair, new_offset = parse_row(row[offset:], parent=node)
        pair.append(new_pair)
        offset += new_offset
    else:
        pair.append(int(row[offset]))
        offset += 1
    if row[offset] != ']':
        raise Exception('Expected ]')
    offset += 1
    node.left, node.right = pair
    return node, offset

data = [parse_row(row)[0] for row in open('input.txt').read().split('\n')]

class Explosion(Exception):
    pass

def recursive_explode(node, path):
    if node.depth == 4:
        if isinstance(node.left, Node):
            current = node
            if isinstance(node.right, Node):
                current_right = node.right
                while isinstance(current_right.right, Node):
                    current_right = current_right.right
                current_right.left += node.left.right
            else:
                node.right += node.left.right
            for direction in path:
                current = current.parent
                if direction == 'r':
                    if isinstance(current.left, Node):
                        current = current.left
                        while isinstance(current.right, Node):
                            current = current.right
                        current.right += node.left.left
                    else:
                        current.left += node.left.left
                    break
            node.left = 0
                
            raise Explosion()

        if isinstance(node.right, Node):
            current = node
            if isinstance(node.left, Node):
                current_left = node.left
                while isinstance(current_left.left, Node):
                    current_left = current_left.left
                current_left.right += node.right.left
            else:
                node.left += node.right.left
            for direction in path:
                current = current.parent
                if direction == 'l':
                    if isinstance(current.right, Node):
                        current = current.right
                        while isinstance(current.left, Node):
                            current = current.left
                        current.left += node.right.right
                    else:
                        current.right += node.right.right
                    break
            node.right = 0
                
            raise Explosion()

    if isinstance(node.left, Node):
        recursive_explode(node.left, ['l'] + path)

    if isinstance(node.right, Node):
        recursive_explode(node.right, ['r'] + path)

class Split(Exception):
    pass

def recursive_split(node):
    if isinstance(node.left, Node):
        recursive_split(node.left)

    elif node.left >= 10:
        left = floor(node.left / 2)
        right = ceil(node.left / 2)
        node.left = Node(parent=node, left=left, right=right, depth=node.depth + 1)
        raise Split()

    if isinstance(node.right, Node):
        recursive_split(node.right)

    elif node.right >= 10:
        left = floor(node.right / 2)
        right = ceil(node.right / 2)
        node.right = Node(parent=node, left=left, right=right, depth=node.depth + 1)
        raise Split()

def reduce(node):
    keep_going = True
    while keep_going:
        try:
            recursive_explode(node, [])
            recursive_split(node)
            keep_going = False
        except (Explosion, Split):
            pass

def add(a, b):
    n, _ = parse_row(f'[{str(a)},{str(b)}]')
    reduce(n)
    return n


def part1(data):
    current = data[0]
    for node in data[1:]:
        current = add(current, node)

    return current.magnitude()

def part2(data):
    seen = set()
    for i, a in enumerate(data):
        for j, b in enumerate(data):
            if i != j:
                seen.add(add(a,b).magnitude())
    return max(seen)

print(part1(data))
print(part2(data))