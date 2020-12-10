import fileinput
from typing import List

values = [int(num) for num in fileinput.input()]

def jolts_1x3(joltages: List[int]) -> int:
    jolts = [0] + sorted(joltages)
    diff_1 = 0
    diff_3 = 1
    for i in range(1, len(jolts)):
        if jolts[i] - jolts[i-1] == 1:
            diff_1 += 1
        elif jolts[i] - jolts[i-1] == 3:
            diff_3 += 1
    return diff_1 * diff_3

result1 = jolts_1x3(values)
print(f'Part One = {result1}')

def arrangements(joltages: List[int]) -> int:
    jolts = [0] + sorted(joltages) + [max(joltages) + 3]
    n = len(jolts)
    
    memo = [0 for _ in range(n)]
    memo[0] = 1

    for i in range(1, n):
        for j in range(i):
            if jolts[i] - jolts[j] <= 3:
                memo[i] += memo[j]
    
    return memo[-1]

result2 = arrangements(values)
print(f'Part Two = {result2}')
