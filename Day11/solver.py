import fileinput
from typing import List, Callable

values = [list(line.strip()) for line in fileinput.input()]

def adjacent(matrix:List[List[str]], m:int, n:int, i:int, j:int) -> List[str]:
    ret = []
    if 0 <= i-1 < m:
        ret.append(matrix[i-1][j])
    if 0 <= i+1 < m:
        ret.append(matrix[i+1][j])
    if 0 <= j-1 < n:
        ret.append(matrix[i][j-1])
    if 0 <= j+1 < n:
        ret.append(matrix[i][j+1])
    if 0 <= i-1 < m and 0 <= j-1 < n:
        ret.append(matrix[i-1][j-1])
    if 0 <= i-1 < m and 0 <= j+1 < n:
        ret.append(matrix[i-1][j+1])
    if 0 <= i+1 < m and 0 <= j-1 < n:
        ret.append(matrix[i+1][j-1])
    if 0 <= i+1 < m and 0 <= j+1 < n:
        ret.append(matrix[i+1][j+1])
    return ret

def step_1(seats: List[List[str]]) -> List[List[str]]:
    m = len(seats)
    n = len(seats[0])
    seats_step = [line.copy() for line in seats]
    for i in range(m):
        for j in range(n):
            if seats[i][j] in ['L', '#']:
                temp_adjacent = adjacent(seats, m, n, i ,j)
                occupied = 0
                for char in temp_adjacent:
                    if char == '#':
                        occupied += 1
                if seats[i][j] == 'L' and occupied == 0:
                    seats_step[i][j] = '#'
                elif seats[i][j] == '#' and occupied >= 4:
                    seats_step[i][j] = 'L'
    return seats_step

def seats_loop(seats: List[List[str]], step: Callable[[List[List[str]]],List[List[str]]]) -> List[List[str]]:
    prev = seats
    while True:
        current = step(prev)  
        if current == prev:
            return current
        prev = current

def count_occupied(seats: List[List[str]]) -> int:
    occupied = 0
    for i in range(len(seats)):
        for char in seats[i]:
            occupied += char == '#'
    return occupied

result1 = count_occupied(seats_loop(values, step_1))
print(f'Part One = {result1}')

def adjacent_until(matrix:List[List[str]], m:int, n:int, i:int, j:int) -> List[str]:
    ret = []
    temp_i, temp_j = i, j
    while 0 <= i-1 < m:
        if matrix[i-1][j] in ["#", 'L']:
            ret.append(matrix[i-1][j])
            break
        i -= 1
    i, j = temp_i, temp_j
    while 0 <= i+1 < m:
        if matrix[i+1][j] in ["#", 'L']:
            ret.append(matrix[i+1][j])
            break
        i += 1
    i, j = temp_i, temp_j
    while 0 <= j-1 < n:
        if matrix[i][j-1] in ["#", 'L']:
            ret.append(matrix[i][j-1])
            break
        j -= 1
    i, j = temp_i, temp_j
    while 0 <= j+1 < n:
        if matrix[i][j+1] in ["#", 'L']:
            ret.append(matrix[i][j+1])
            break
        j += 1
    i, j = temp_i, temp_j
    while 0 <= i-1 < m and 0 <= j-1 < n:
        if matrix[i-1][j-1] in ["#", 'L']:
            ret.append(matrix[i-1][j-1])
            break
        i -= 1; j -= 1
    i, j = temp_i, temp_j
    while 0 <= i-1 < m and 0 <= j+1 < n:
        if matrix[i-1][j+1] in ["#", 'L']:
            ret.append(matrix[i-1][j+1])
            break
        i -= 1; j += 1
    i, j = temp_i, temp_j
    while 0 <= i+1 < m and 0 <= j-1 < n:
        if matrix[i+1][j-1] in ["#", 'L']:
            ret.append(matrix[i+1][j-1])
            break
        i += 1; j -= 1
    i, j = temp_i, temp_j
    while 0 <= i+1 < m and 0 <= j+1 < n:
        if matrix[i+1][j+1] in ["#", 'L']:
            ret.append(matrix[i+1][j+1])
            break
        i += 1; j += 1
    return ret

def step_2(seats: List[List[str]]) -> List[List[str]]:
    m = len(seats)
    n = len(seats[0])
    seats_step = [line.copy() for line in seats]
    for i in range(m):
        for j in range(n):
            if seats[i][j] in ['L', '#']:
                temp_adjacent = adjacent_until(seats, m, n, i ,j)
                occupied = 0
                for char in temp_adjacent:
                    if char == '#':
                        occupied += 1
                if seats[i][j] == 'L' and occupied == 0:
                    seats_step[i][j] = '#'
                elif seats[i][j] == '#' and occupied >= 5:
                    seats_step[i][j] = 'L'
    return seats_step

result2 = count_occupied(seats_loop(values, step_2))
print(f'Part Two = {result2}')
