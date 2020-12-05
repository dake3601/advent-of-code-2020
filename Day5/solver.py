import fileinput
from typing import List

values = [i.strip() for i in fileinput.input()]

def occupied_seats(values: List[str]) -> List[List[int]]:
    ret = []
    for pos in values:
        row = [0, 127]
        col = [0, 7]
        for i in range(7):
            if pos[i] == 'F':
                row = [row[0], row[0]+(row[1]-row[0])//2]
            elif pos[i] == 'B':
                row = [row[0]+(row[1]-row[0])//2+1, row[1]]
        for i in range(7, 10):
            if pos[i] == 'L':
                col = [col[0], col[0]+(col[1]-col[0])//2]
            if pos[i] == 'R':
                col = [col[0]+(col[1]-col[0])//2+1, col[1]]
        ret.append([row[0], col[0]])
    return ret

def all_id(seats: List[List[int]]) -> List[int]:
    ret = []
    for row, col in seats:
        ret.append(row * 8 + col)
    return ret

occupied = occupied_seats(values)
ids = all_id(occupied)

result1 = max(ids)
print(f'Part One = {result1}')

def find_seat(occupied: List[List[int]], ids: List[int]) -> int:
    my_id = 0
    for i in range(128):
        for j in range(7):
            if [i, j] not in occupied:
                temp_id = i * 8 + j
                if temp_id + 1 in ids and temp_id - 1 in ids:
                    return temp_id
    return my_id

result2 = find_seat(occupied, ids)
print(f'Part Two = {result2}')
