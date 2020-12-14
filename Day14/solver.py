import fileinput
from typing import Any, List

values = [line for line in fileinput.input()]
for i in range(len(values)):
    if values[i][:4] == 'mask':
        values[i] = values[i][-37:-1]
    elif values[i][:3] == 'mem':
        address, _, val = values[i].split()
        mem = int(''.join([i for i in address if i.isdigit()]))
        values[i] = [mem, int(val)]

def int_to_bit(val: int, size:int) -> str:
    return format(val, 'b').zfill(size)

def bitmask_add(msk: str, bit:str, ele:str) -> str:
    return ''.join([msk[i] if msk[i] != ele else bit[i] for i in range(36)])

def sum_memory(memory: List[Any]) -> int:
    mem = {}
    bitmask = ''
    for val in memory:
        if len(val) == 36:
            bitmask = val
        elif len(val) == 2:
            bit = int_to_bit(val[1], 36)
            mem[val[0]] = bitmask_add(bitmask, bit, 'X')
    return sum(map(lambda num: int(num, 2), mem.values()))

result1 = sum_memory(values)
print(f'Part One = {result1}')

def sum_combinations(memory: List[Any]) -> int:
    mem = {}
    bitmask = ''
    for val in memory:
        if len(val) == 36:
            bitmask = val
        elif len(val) == 2:
            bit = int_to_bit(val[0], 36)
            loc = bitmask_add(bitmask, bit, '0')
            count = loc.count('X')
            for num in range(2**count):
                comb = list(int_to_bit(num, count))
                b_tmp = ''.join([i if i != 'X' else comb.pop() for i in loc])
                mem[int(b_tmp, 2)] = val[1]
    return sum(mem.values())

result2 = sum_combinations(values)
print(f'Part Two = {result2}')
