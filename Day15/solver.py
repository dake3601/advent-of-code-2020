import fileinput
from typing import OrderedDict as odt, List
from collections import OrderedDict

values = [list(map(int, i.split(','))) for i in fileinput.input()][0]

def add_dict(dic: odt[int, List[int]], key:int, val:int) -> None:
        if key not in dic:
            dic[key] = [val]
        else:
            dic[key].append(val)
            dic.move_to_end(key)

def memory_game(numbers: List[int], target:int) -> int:
    speak: odt[int, List[int]] = OrderedDict()
    n = len(numbers)
    for i in range(1, n+1):
        add_dict(speak, numbers[i-1], i)
    for i in range(n+1, target+1):
        val = speak[next(reversed(speak))]
        if len(val) == 1:
            add_dict(speak, 0, i)
        else:
            add_dict(speak, val[-1]-val[-2], i)
    return next(reversed(speak))

result1 = memory_game(values, 2020)
print(f'Part One = {result1}')

result2 = memory_game(values, 30000000)
print(f'Part Two = {result2}')
