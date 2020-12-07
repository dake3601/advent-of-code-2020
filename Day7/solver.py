import fileinput
from typing import List, Set

rules = [line.strip().split() for line in fileinput.input()]

def contain(rules: List[List[str]], target: str) -> int:
    colors = {}
    total = 0

    for rule in rules:
        colors[rule[0]+' '+rule[1]] = []
        for i in range(4, len(rule), 4):
            rule_contents = rule[i:i+4]
            if rule_contents != ['no', 'other', 'bags.']:
                colors[rule[0]+' '+rule[1]].append(rule_contents[1]+' '+rule_contents[2])

    def helper(values: List[str], visited: Set[str]) -> bool:
        if target in values:
            return True
        for val in values:
            if val in visited:
                continue
            visited.add(val)
            if helper(colors[val], visited):
                return True
        return False

    for key, values in colors.items():
        if key == target:
            continue
        total += helper(values, {key})
    return total

result1 = contain(rules, 'shiny gold')
print(f'Part One = {result1}')

def contain_total(rules: List[List[str]], target: str) -> int:
    colors = {}

    for rule in rules:
        colors[rule[0]+' '+rule[1]] = []
        for i in range(4, len(rule), 4):
            rule_contents = rule[i:i+4]
            if rule_contents != ['no', 'other', 'bags.']:
                colors[rule[0]+' '+rule[1]].append([int(rule_contents[0]), rule_contents[1]+' '+rule_contents[2]])

    def helper(origin: str) -> int:
        bags = 0
        for color in colors[origin]:
            bags += color[0] + color[0] * helper(color[1])
        return bags

    return helper(target)

result2 = contain_total(rules, 'shiny gold')
print(f'Part Two = {result2}')
