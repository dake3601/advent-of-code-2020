import fileinput
from typing import List
import string

values = []
temp = ''
for line in fileinput.input():
    line = line.strip()
    if not line:
        values.append(temp.strip())
        temp = ''
    else:
        temp += line + ' '
if temp:
    values.append(temp.strip())

def count_anyone(values: List[str]) -> int:
    total = 0
    for answers in values:
        temp = set(answers)
        temp.add(' ')
        total += len(temp) - 1
    return total

result1 = count_anyone(values)
print(f'Part One = {result1}')

def count_everyone(values: List[str]) -> int:
    total = 0
    for answers in values:
        temp = set(string.ascii_lowercase)
        for person in answers.split():
            temp = temp.intersection(set(person))
        total += len(temp)
    return total

result2 = count_everyone(values)
print(f'Part Two = {result2}')
