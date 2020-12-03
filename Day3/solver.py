import fileinput
from typing import List

values = [list(char.strip()) for char in fileinput.input()]

def tree_count(values: List[List[str]], right: int, down: int) -> int:
    trees = 0
    row, col = 0, 0
    width = len(values[0])
    height = len(values)
    while row < height - 1:
        col = (col + right) % width
        row += down
        if values[row][col] == '#':
            trees += 1
    return trees

result1 = tree_count(values, 3, 1)
print(f'Part One = {result1}')

moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result2 = 1
for r, d in moves:
    result2 *= tree_count(values, r, d)

print(f'Part Two = {result2}')
