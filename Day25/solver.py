import fileinput
from typing import Set

keys = {int(line.strip()) for line in fileinput.input()}

def transform(keys: Set[int]):
    magic_number = 20201227
    subject = 7
    val = 1
    loop_size = 0
    while val not in keys:
        val = (val * subject) % magic_number
        loop_size += 1
    keys.remove(val)
    subject = keys.pop()
    val = 1
    for _ in range(loop_size):
        val = (val * subject) % magic_number
    return val

result1 = transform(keys)
print(f'Part One = {result1}')
