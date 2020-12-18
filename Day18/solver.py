import fileinput
from typing import Callable, List

values = [[c for c in l.strip() if c != ' '] for l in fileinput.input()]

def solver_1(line: List[str]) -> int:
    l, r = 0, 0
    for _ in range(line.count('(')):
        for i in range(len(line)):
            if line[i] == '(':
                l = i
            elif line[i] == ')':
                r = i
                break
        line = line[:l] + [str(solver_1(line[l+1:r]))] + line[r+1:]
        
    ret = 0
    add = False
    mul = False
    for c in line:
        if add:
            ret += int(c)
        elif mul:
            ret *= int(c)
        elif c.isdigit():
            ret = int(c)
        add = c == '+'
        mul = c == '*'
    return ret

def total(values: List[List[str]], solver: Callable[[List[str]], int]) -> int:
    ret = 0
    for line in values:
        ret += solver(line)
    return ret

result1 = total(values, solver_1)
print(f'Part One = {result1}')

def solver_2(line: List[str]) -> int:
    l, r = 0, 0
    for _ in range(line.count('(')):
        for i in range(len(line)):
            if line[i] == '(':
                l = i
            elif line[i] == ')':
                r = i
                break
        line = line[:l] + [str(solver_2(line[l+1:r]))] + line[r+1:]
    
    for _ in range(line.count('+')):
        loc = line.index('+')
        l = int(line[loc-1])
        r = int(line[loc+1])
        line = line[:loc-1] + [str(r+l)] + line[loc+2:]
    
    ret = 1
    for c in line:
        if c.isdigit():
            ret *= int(c)
    return ret

result2 = total(values, solver_2)
print(f'Part Two = {result2}')
