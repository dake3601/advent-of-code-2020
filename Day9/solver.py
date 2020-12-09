import fileinput
from typing import List

values = [int(num) for num in fileinput.input()]
preamble = 25

def first_invalid(values: List[int], preamble: int) -> int:

    def possible(vals: List[int], target: int) -> bool:
        dic = {}
        for num in vals:
            if num in dic:
                return True
            dic[target-num] = num
        return False

    for i in range(preamble + 1, len(values)):
        if not possible(values[i-preamble:i], values[i]):
            return values[i]
    return 0

result1 = first_invalid(values, preamble)
print(f'Part One = {result1}')

def find_sum(values: List[int], target: int) -> int:
    low, high = 0, 2
    while low < len(values) and high < len(values):
        temp_sum = sum(values[low:high])
        if temp_sum == target and high - low > 1:
            return min(values[low:high]) + max(values[low:high])
        elif temp_sum < target:
            high += 1
        elif temp_sum > target:
            low += 1
        elif low >= high - 1:
            low += 1
            high = low + 2
    return 0

result2 = find_sum(values, result1)
print(f'Part Two = {result2}')
