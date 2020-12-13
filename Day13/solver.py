import fileinput
from typing import List

target, values = zip(fileinput.input())
target = int(target[0])
values = values[0].split(',')

def find_earliest(ids: List[str], target: int) -> int:
    vals = [int(i) for i in ids if i.isdigit()]
    min_time = []
    min_global, min_index = float('inf'), 0
    for i, num in enumerate(vals):
        least_time = target//num * num
        if least_time < target:
            least_time += num
        min_local = least_time - target
        min_time.append(min_local)
        if min_local < min_global:
            min_global, min_index = min_local, i
    return vals[min_index] * min_time[min_index]

result1 = find_earliest(values, target)
print(f'Part One = {result1}')

def find_timestamp(ids: List[str]) -> int:
    buses = [[int(num), i] for i, num in enumerate(ids) if num.isdigit()]
    vals, timestamp = zip(*buses)
    remainders = [-time%val for val, time in zip(vals, timestamp)]
    x, step = 0, 1
    for val, rem  in zip(vals, remainders):
        while x % val != rem:
            x += step
        step *= val
    return x

result2 = find_timestamp(values)
print(f'Part Two = {result2}')
