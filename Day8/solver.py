import fileinput
from typing import List

values = [line.strip().split() for line in fileinput.input()]

def find_accumulator(values: List[List[str]]) -> List[int]:
    values_copy = [i.copy() for i in values]
    accumulator = 0
    i = 0
    while i < len(values_copy):
        rule = values_copy[i][0]
        values_copy[i][0] = '###'
        count = int(values_copy[i][1][1:])
        if values_copy[i][1][0] == '-':
            count *= -1
        if rule == '###':
            return [0, accumulator]
        elif rule == 'nop':
            i += 1
        elif rule == 'acc':
            accumulator += count
            i += 1
        elif rule == 'jmp':
            i += count
    return [1, accumulator]

_, result1 = find_accumulator(values)
print(f'Part One = {result1}')

def accumulator_fix(values: List[List[str]]) -> int:
    change = {'nop': 'jmp', 'jmp': 'nop'}
    for i in range(len(values)):
        if values[i][0] == 'acc':
            continue
        values[i][0] = change[values[i][0]]
        no_loop, accumulator = find_accumulator(values)
        values[i][0] = change[values[i][0]]
        if no_loop:
            return accumulator
    return 0

result2 = accumulator_fix(values)
print(f'Part Two = {result2}')
