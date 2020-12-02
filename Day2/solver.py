import fileinput
from typing import List

values = [i for i in fileinput.input()]

def count_valid(values: List[str]) -> int:
    valid = 0
    for lock in values:
        vals, char, pasw = lock.split()
        low, high = vals.split('-')
        char = char[0]
        if int(high) >= pasw.count(char) >= int(low):
            valid += 1
    return valid

result1 = count_valid(values)
print(f'Part One = {result1}')

def check_one(values: List[str]) -> int:
    valid = 0
    for lock in values:
        vals, char, pasw = lock.split()
        low, high = vals.split('-')
        low, high = int(low)-1, int(high)-1
        char = char[0]
        n = len(pasw)-1
        if low == high or low > n:
            continue
        if high > n:
            if pasw[low] == char:
                valid += 1
            continue
        low_check = pasw[low] == char
        high_check = pasw[high] == char
        if low_check and not high_check:
            valid += 1
        elif not low_check and high_check:
            valid += 1
    return valid

result2 = check_one(values)
print(f'Part Two = {result2}')