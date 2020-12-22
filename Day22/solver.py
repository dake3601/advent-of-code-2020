import fileinput
from typing import Deque, Set, Tuple
from collections import deque

Saved = Set[Tuple[Tuple[int, ...], Tuple[int, ...]]]

player1 = deque()
player2 = deque()
check = False
for line in fileinput.input():
    line = line.strip()
    if not line:
        check = True
    elif check and line.isdigit():
        player2.append(int(line))
    elif line.isdigit():
        player1.append(int(line))
player1_rec = player1.copy()
player2_rec = player2.copy()

def combat(player1: Deque[int], player2: Deque[int]) -> bool:
    while player1 and player2:
        p1 = player1.popleft()
        p2 = player2.popleft()
        if p1 > p2:
            player1.extend((p1, p2))
        else:
            player2.extend((p2, p1))
    return bool(player1)

def score(player1: Deque[int], player2: Deque[int]) -> int:
    winner = tuple(reversed(player1)) or tuple(reversed(player2))
    return sum((i + 1) * winner[i] for i in range(len(winner)))

combat(player1, player2)
result1 = score(player1, player2)
print(f'Part One = {result1}')

def combat_rec(player1: Deque[int], player2: Deque[int], prev: Saved) -> bool:
    while player1 and player2:
        if (tuple(player1), tuple(player2)) in prev:
            return True
        prev.add((tuple(player1), tuple(player2)))
        p1 = player1.popleft()
        p2 = player2.popleft()
        if len(player1) >= p1 and len(player2) >= p2:
            temp1 = deque(player1[i] for i in range(p1))
            temp2 = deque(player2[i] for i in range(p2))
            if combat_rec(temp1, temp2, set()):
                player1.extend((p1, p2))
            else:
                player2.extend((p2, p1))
        elif p1 > p2:
            player1.extend((p1, p2))
        else:
            player2.extend((p2, p1))
    return bool(player1)

combat_rec(player1_rec, player2_rec, set())
result2 = score(player1_rec, player2_rec)
print(f'Part Two = {result2}')
