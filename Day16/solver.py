import fileinput
from typing import Dict, List, Set

ranges = {}
ranges_set = set()
your_list = []
near_list = []
your_bool = False
near_bool = False
for line in fileinput.input():
    line = line.strip()
    if not line:
        continue
    elif line == 'your ticket:':
        your_bool = True
    elif line == 'nearby tickets:':
        near_bool = True
    elif your_bool:
        your_list = [int(i) for i in line.split(',')]
        your_bool = False
    elif near_bool:
        near_list.append([int(i) for i in line.split(',')])
    else:
        start = line.find(':') + 2
        ranges[line[:start-2]] = set()
        for r in line[start:].split(' or '):
            low, high = r.split('-')
            for num in range(int(low), int(high)+1):
                ranges_set.add(num)
                ranges[line[:start-2]].add(num)

def error_rate(nearby: List[List[int]], valid: Set[int]) -> int:
    error = 0
    for line in nearby: 
        for num in line:
            if num not in valid:
                error += num
    return error

result1 = error_rate(near_list, ranges_set)
print(f'Part One = {result1}')

def clean_nearby(nearby: List[List[int]], valid: Set[int]) -> List[List[int]]:
    nearby_valid = []
    for line in nearby: 
        if all(map(lambda x: x in valid, line)):
            nearby_valid.append(line)
    return nearby_valid

def find_field(nearby: List[List[int]], ranges: Dict[str, Set[int]]) -> Dict[str, int]:
    poss = {}
    ordered = [list(i) for i in zip(*nearby)]
    for key, val in ranges.items():
        poss[key] = set()
        for col in range(len(ordered)):
            if all(map(lambda x: x in val, ordered[col])):
                poss[key].add(col)
    while any(map(lambda val: len(val) != 1, poss.values())):
        for key, val in poss.items():
            if len(val) == 1:
                (elem,) = val
                for k in poss:
                    if k != key:
                        poss[k].discard(elem)
    for key in poss:
        (elem,) = poss[key]
        poss[key] = elem
    return poss

def departure(fields: Dict[str, int], yours: List[int]) -> int:
    ret = 1
    for key, val in fields.items():
        if key[:9] == 'departure':
            ret *= yours[val]
    return ret

nearby_valid = clean_nearby(near_list, ranges_set)
fields = find_field(nearby_valid, ranges)
result2 = departure(fields, your_list)
print(f'Part Two = {result2}')
