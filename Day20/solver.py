import fileinput
from typing import Any, Dict, List

tiles = {}
tile = 0
for line in fileinput.input():
    line = line.strip()
    if not line:
        continue
    elif line[:4] == 'Tile':
        tile = int(line[5:-1])
        tiles[tile] = []
    else:
        tiles[tile].append([i == '#' for i in line])

def borders(matrix: List[List[Any]]) -> List[List[Any]]:
    N = matrix[0]
    S = matrix[-1]
    rot = list(zip(*matrix)) 
    W = list(rot[0])
    E = list(rot[-1])
    return [N, S, W, E]

def adjacents(tiles: Dict[int, List[List[bool]]]) -> Dict[int, List[int]]:
    sides = {}
    for tile in tiles:
        sides[tile] = borders(tiles[tile])

    adjacent = {}
    for tile in sides:
        adjacent[tile] = []
        count = 0
        for i in range(4):
            line = sides[tile][i]
            for t in sides:
                if t == tile:
                    continue
                for l in sides[t]:
                    if sum(line) == sum(l) and (line == l or line[::-1] == l):
                        adjacent[tile].append(t)
                        count += 1
    return adjacent

def corners(adjacent: Dict[int, List[int]]) -> int:
    ret = 1
    for tile in adjacent:
        if len(adjacent[tile]) == 2:
            ret *= tile
    return ret

adjacent = adjacents(tiles)
result1 = corners(adjacent)
print(f'Part One = {result1}')

def rotate(matrix: List[List[Any]]) -> None:
    matrix[:] = [list(i) for i in zip(*matrix[::-1])]
    return None

def flip_y(matrix: List[List[Any]]) -> None:
    for i in range(len(matrix)):
            matrix[i][:] = matrix[i][::-1]
    return None

def flip_x(matrix: List[List[Any]]) -> None:
    rotate(matrix)
    rotate(matrix)
    flip_y(matrix)
    return None

def neighbors(matrix: List[List[int]], size: int, row: int, col: int) -> int:
        ret = 0
        if 0 <= row+1 < size*2-1:
            ret += matrix[row+1][col] != 0
        if 0 <= row-1 < size*2-1:
            ret += matrix[row-1][col] != 0
        if 0 <= col+1 < size*2-1:
            ret += matrix[row][col+1] != 0
        if 0 <= col-1 < size*2-1:
            ret += matrix[row][col-1] != 0
        return ret

def build(tiles: Dict[int, List[List[bool]]]) -> List[List[List[List[bool]]]]:
    size = int(len(tiles)**(1/2))
    matrix = [[[] for _ in range(size*2-1)] for _ in range(size*2-1)]
    m = [[0 for _ in range(size*2-1)] for _ in range(size*2-1)]
    row, col = size-1, size-1
    
    tile = 0
    for key in adjacent:
        if len(adjacent[key]) == 2:
            tile = key
            break
    
    visited = {tile}
    stack = [(tile, row, col)]
    matrix[row][col] = tiles[tile]
    m[row][col] = tile

    while stack:
        tile, row, col = stack.pop()
        N, S, W, E = borders(tiles[tile])
        c = neighbors(m, size, row, col)
        while c < len(adjacent[tile]):
            for t in tiles:
                if t in visited:
                    continue
                N_t, S_t, W_t, E_t = borders(tiles[t])
                if N == S_t:
                    matrix[row-1][col] = tiles[t]
                    m[row-1][col] = t
                    stack.append((t, row-1, col))
                    visited.add(t)
                    c += 1
                elif N == S_t[::-1]:
                    flip_y(tiles[t])
                    matrix[row-1][col] = tiles[t]
                    m[row-1][col] = t
                    stack.append((t, row-1, col))
                    visited.add(t)
                    c += 1
                elif S == N_t:
                    matrix[row+1][col] = tiles[t]
                    m[row+1][col] = t
                    stack.append((t, row+1, col))
                    visited.add(t)
                    c += 1
                elif S == N_t[::-1]:
                    flip_y(tiles[t])
                    matrix[row+1][col] = tiles[t]
                    m[row+1][col] = t
                    stack.append((t, row+1, col))
                    visited.add(t)
                    c += 1
                elif E == W_t:
                    matrix[row][col+1] = tiles[t]
                    m[row][col+1] = t
                    stack.append((t, row, col+1))
                    visited.add(t)
                    c += 1
                elif E == W_t[::-1]:
                    flip_x(tiles[t])
                    matrix[row][col+1] = tiles[t]
                    m[row][col+1] = t
                    stack.append((t, row, col+1))
                    visited.add(t)
                    c += 1
                elif W == E_t:
                    matrix[row][col-1] = tiles[t]
                    m[row][col-1] = t
                    stack.append((t, row, col-1))
                    visited.add(t)
                    c += 1
                elif W == E_t[::-1]:
                    flip_x(tiles[t])
                    matrix[row][col-1] = tiles[t]
                    m[row][col-1] = t
                    stack.append((t, row, col-1))
                    visited.add(t)
                    c += 1
            
            for temp in tiles:
                if temp not in visited:
                    rotate(tiles[temp])

    while len(m) != size:
        for i in range(len(m)):
            if sum(m[i]) == 0:
                del m[i]
                del matrix[i]
                break
    
    rem = []
    m_rot = [list(i) for i in zip(*m[::-1])]
    for i in range(len(m_rot)):
        if sum(m_rot[i]) == 0:
            rem.append(i)
    
    rem.sort(reverse=True)
    for i in rem:
        for j in range(len(m)):
            del matrix[j][i]
    return matrix

def reformat(matrix: List[List[List[List[bool]]]]) -> List[List[bool]]:
    size = len(matrix)
    total = [[] for _ in range(size*8)]
    for row in range(size):
        for col in range(size):
            for i in range(1,9):
                total[row*8+i-1].extend(matrix[row][col][i][1:-1])
    return total

def find_monster(ret: List[List[bool]]) -> int:
    monsters = 0
    x = [[0, -1, 1, -6, -7, -12, -13, -18], [-2, -5, -8, -11, -14, -17]]
    for i in range(len(ret)-2):
        for j in range(18, len(ret[0])-1):
            if not ret[i][j]:
                continue
            temp = True
            for k in range(2):
                for l in x[k]:
                    temp &= ret[i+k+1][j+l]
                    if not temp:
                        break
                if not temp:
                    break
            monsters += temp
    return monsters

def roughness(sea: List[List[bool]]) -> int:
    ones = sum([sum(i) for i in sea])
    monsters = 0
    for _ in range(4):
        rotate(sea)
        monsters = find_monster(sea)
        if monsters:
            return ones-monsters*15
        flip_x(sea)
        monsters = find_monster(sea)
        if monsters:
            return ones-monsters*15
        flip_x(sea)
    return ones

matrix = build(tiles)
sea = reformat(matrix)
result2 = roughness(sea)
print(f'Part Two = {result2}')
