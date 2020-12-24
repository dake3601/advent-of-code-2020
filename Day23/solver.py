import fileinput
from typing import Dict, Tuple

class Node():
    def __init__(self, val: int, next: 'Node' = None) -> None:
        self.val = val
        self.next = next

values = ()
for line in fileinput.input():
    values = tuple(int(i) for i in line)

def run_game(vals: Tuple[int, ...], turns: int) -> Dict[int, 'Node']:
    index = {}
    head = current = Node(-1)
    for i in range(len(vals)):
        current.val = vals[i]
        index[vals[i]] = current
        if i == len(vals) - 1:
            current.next = head
        else:
            current.next = Node(vals[i+1])
        current = current.next
    for i in range(turns):
        get = current.val - 1
        picked = current.next
        current.next = current.next.next.next.next
        while get == 0 or get == picked.val or get == picked.next.val or get == picked.next.next.val:
            get = get - 1 if get != 0 else len(vals)
        index[get].next, picked.next.next.next = picked, index[get].next
        current = current.next
    return index

def small_game(vals: Tuple[int, ...]) -> str:
    index = run_game(vals, 100)
    current: 'Node' = index[1].next
    ret = ''
    while current.val != 1:
        ret += str(current.val)
        current = current.next
    return ret

result1 = small_game(values)
print(f'Part One = {result1}')

def big_game(vals: Tuple[int, ...]) -> int:
    index = run_game(vals + tuple(i for i in range(max(vals)+1, 10**6+1)), 10**7)
    return index[1].next.val * index[1].next.next.val

result2 = big_game(values)
print(f'Part Two = {result2}')
