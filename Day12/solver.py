import fileinput
from typing import Tuple

values = tuple((line[0], int(line[1:])) for line in fileinput.input())

def distance(instructions: Tuple[Tuple[str, int]]) -> int:
    east, north, direction = 0, 0, 0
    dir_east = [1,0,-1,0] # East, South, West, North.
    dir_north = [0,-1,0,1]
    vals_east = {'E':1, 'W':-1, 'N':0, 'S':0}
    vals_north = {'E':0, 'W':0, 'N':1, 'S':-1}
    for rule, val in instructions:
        if rule in vals_east:
            east += vals_east[rule] * val
            north += vals_north[rule] * val
        elif rule == 'R':
            direction = (direction + val//90) % 4
        elif rule == 'L':
            direction = (direction - val//90 + 4) % 4
        elif rule == 'F':
            east += dir_east[direction] * val
            north += dir_north[direction] * val
    return abs(east) + abs(north)

result1 = distance(values)
print(f'Part One = {result1}')

def waypoint(instructions: Tuple[Tuple[str, int]]) -> int:
    east, north = 0, 0
    east_w, north_w = 10, 1
    vals_east = {'E':1, 'W':-1, 'N':0, 'S':0}
    vals_north = {'E':0, 'W':0, 'N':1, 'S':-1}
    dirs_north = {'R': 1, 'L':-1}
    dirs_east = {'R': -1, 'L':1}
    for rule, val in instructions:
        if rule in vals_east:
            east_w += vals_east[rule] * val
            north_w += vals_north[rule] * val
        elif rule == 'F':
            north += north_w * val
            east += east_w * val
        elif rule in dirs_north:
            for _ in range(val//90):
                east_w, north_w = north_w * dirs_north[rule], \
                                    east_w * dirs_east[rule]
    return abs(east) + abs(north)

result2 = waypoint(values)
print(f'Part Two = {result2}')
