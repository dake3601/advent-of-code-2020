import fileinput
from typing import List

values = [int(i) for i in fileinput.input()]
target = 2020

def add_two(values: List[int], target: int) -> int:
    dic = {}
    for num in values:
        if num in dic:
            return dic[num] * num
        dic[target-num] = num
    return -1

result1 = add_two(values, target)
print(f'Part One = {result1}')

def add_three(values: List[int], target:int) -> int:
    nums = sorted(values)
    for i in range(len(nums)-2):
        if i > target and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                return nums[i] * nums[left] * nums[right]
    return -1

result2 = add_three(values, target)
print(f'Part Two = {result2}')
