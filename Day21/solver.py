import fileinput
from typing import Counter as cnt, Dict, Set
from collections import Counter

pairs: Dict[str, Set[str]] = {}
count: cnt[str] = Counter()
for line in fileinput.input():
    line = line.strip()
    l = line.index('(')
    count.update(line[:l].split())
    for aller in line[l+10:-1].split(', '):
        if pairs.get(aller) is None:
            pairs[aller] = set(line[:l].split())
        else:
            pairs[aller] &= set(line[:l].split())

def safe_ingredients(pairs: Dict[str, Set[str]], count: cnt[str]) -> int:
    allergic = set().union(*pairs.values())
    return sum(count[food] for food in count if food not in allergic)

result1 = safe_ingredients(pairs, count)
print(f'Part One = {result1}')

def dangerous_list(pairs: Dict[str, Set[str]]) -> str:
    while any(map(lambda key: len(pairs[key]) != 1 , pairs.keys())):
        for food in pairs:
            if len(pairs[food]) == 1:
                for f in pairs:
                    if food == f:
                        continue
                    pairs[f] -= pairs[food]
    
    ordered = sorted([[k, pairs[k].pop()] for k in pairs], key=lambda x: x[0])
    return ','.join([food for _, food in ordered])

result2 = dangerous_list(pairs)
print(f'Part One = {result2}')
