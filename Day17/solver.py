import fileinput
from typing import DefaultDict, Tuple, List
from collections import defaultdict
from itertools import product

coord = Tuple[int, ...]
dimension = DefaultDict[coord, bool]

values = [list(line.strip()) for line in fileinput.input()]

def generate_moves(dimensions: int) -> List[coord]:
    return [i for i in product([0,1,-1], repeat = dimensions)]

def make_hash(matrix: List[List[str]], dimensions: int) -> dimension:
    space: dimension = defaultdict(bool)
    n = dimensions - 2
    base = tuple(0 for _ in range(n))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                space[(i, j) + base] = True
    return space

def add_coord(a: coord, b: coord) -> coord:
    return tuple(map(lambda x, y: x + y, a, b))

def adjacent(space: dimension, loc: coord, moves: List[coord]) -> int:
    ret = 0
    n = len(moves[0])
    base = tuple(0 for _ in range(n))
    for nearby in moves:
        if nearby == base:
            continue
        ret += space[add_coord(loc, nearby)]
    return ret

def step(space: dimension, moves: List[coord]) -> dimension:
    visited = set()
    space_new: dimension = defaultdict(bool)
    clean(space)
    for loc in space:
        for nearby in moves:
            temp_loc = add_coord(loc, nearby)
            if temp_loc in visited:
                continue
            visited.add(temp_loc)
            active = adjacent(space, temp_loc, moves)
            if space[temp_loc] and active in [2,3]:
                space_new[temp_loc] = True
            elif not space[temp_loc] and active == 3:
                space_new[temp_loc] = True
        clean(space)
    return space_new

def clean(space: dimension) -> None:
    delete = [key for key in space if not space[key]]
    for key in delete:
        del space[key]
    return

def loop(space: dimension, target: int, moves: List[coord]) -> dimension:
    for _ in range(target):
        space = step(space, moves)
    return space

def count_occupied(space: dimension) -> int:
    return len(space)

dimensions = 3
space = make_hash(values, dimensions)
moves = generate_moves(dimensions)
ret = loop(space, 6, moves)
result1 = count_occupied(ret)
print(f'Part One = {result1}')

dimensions = 4
space = make_hash(values, dimensions)
moves = generate_moves(dimensions)
ret = loop(space, 6, moves)
result2 = count_occupied(ret)
print(f'Part Two = {result2}')
