import fileinput
from typing import Any, Dict, List, Set

rules = {}
combs = set()
check = False
for line in fileinput.input():
    line = line.strip()
    if not line:
        check = True
    elif check:
        combs.add(line)
    else:
        i, *temp = line.split()
        i = int(i[:-1])
        if len(temp) == 3 and '|' in temp:
            rules[i] = [[int(temp[0])], [int(temp[2])]]
        elif len(temp) == 5  and '|' in temp:
            rules[i] = [[int(temp[0]), int(temp[1])], [int(temp[3]), int(temp[4])]]
        elif len(temp) == 1 and not temp[0].isdigit():
            rules[i] = [temp[0][1]]
        else:
            rules[i] = [int(num) for num in temp]

def gen(rules: Dict[int, List[Any]], start: int, memo: Dict[int, Set[str]]) -> Set[str]:
    def helper(nums: List[int]) -> Set[str]:
        ret = set()
        for i in range(len(nums)):
            vals = memo.get(nums[i]) or gen(rules, nums[i], memo)
            if not i:
                ret = vals
            else:
                ret = {word + c for word in ret for c in vals}
        return ret
    
    val = rules[start]
    if type(val[0]) == str:
        memo[start] = set([val[0]])
    elif type(val[0]) == int:
        memo[start] = helper(val)
    elif type(val[0]) == list:
        memo[start] = set()
        for nums in val:
            memo[start].update(helper(nums))
    return memo[start]

memo = {}
ret = gen(rules, 0, memo)
result1 = len(combs.intersection(ret))
print(f'Part One = {result1}')

def gen_loop(combs: Set[str], r42: Set[str], r31: Set[str], div: int) -> int:
    total = 0 
    for word in combs:
        check = True
        balance = 0
        for i in range(0, len(word), div):
            if i != len(word) - div and word[i:i+div] in r42:
                balance += 1
            elif i != 0 and i != div and word[i:i+div] in r31:
                balance -= 1
            else:
                check = False
                break
        total += check and balance > 0
    return total

result2 = gen_loop(combs, memo[42], memo[31], 8)
print(f'Part Two = {result2}')
