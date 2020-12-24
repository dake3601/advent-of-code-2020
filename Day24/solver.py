import fileinput
from typing import List, Set, Tuple

coord = Tuple[int, ...]

values = [line.strip() for line in fileinput.input()]

def add_coord(a: coord, b: coord) -> coord:
    return tuple(map(lambda x, y: x + y, a, b))

def instructions(values: List[str]) -> Set[coord]:
    flip = set()
    rule = {'se': (1,-1), 'sw': (0,-1), 'nw': (-1,1), 'ne': (0,1), 'e': (1,0), 'w': (-1,0)}
    for line in values:
        current = (0,0)
        i = 0
        while i != len(line):
            if line[i:i+2] in {'se', 'sw', 'nw', 'ne'}:
                current = add_coord(current, rule[line[i:i+2]])
                i += 2
            else:
                current = add_coord(current, rule[line[i:i+1]])
                i += 1
        if current in flip:
            flip.remove(current)
        else:
            flip.add(current)
    return flip
   
flip = instructions(values)
result1 = len(flip)
print(f'Part One = {result1}')

def neighbors(area: Set[coord], pos: coord) -> int:
    adjacent = {(1,-1), (0,-1), (-1,1), (0,1), (1,0), (-1,0)}
    return sum(add_coord(pos, near) in area for near in adjacent)

def exhibit(black: Set[coord], target: int) -> int:
    tiles = {(1,-1), (0,-1), (-1,1), (0,1), (1,0), (-1,0), (0,0)}
    check = {}
    for _ in range(target):
        blacks_step = set()
        visited = set()
        for coord in black:
            if coord not in check:
                check[coord] = [add_coord(coord, tile) for tile in tiles]
            for tile in check[coord]:
                if tile in visited:
                    continue
                visited.add(tile)
                closeby = neighbors(black, tile)
                if tile in black and 0 < closeby <= 2:
                    blacks_step.add(tile)
                elif tile not in black and closeby == 2:
                    blacks_step.add(tile)
        black = blacks_step
    return len(black)

result2 = exhibit(flip, 100)
print(f'Part Two = {result2}')
