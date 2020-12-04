import fileinput
from typing import List

values = []
temp = ''
for line in fileinput.input():
    line = line.strip()
    if not line:
        values.append(temp)
        temp = ''
    else:
        temp += line + ' '
if temp:
    values.append(temp)

def count_valid(values: List[str]) -> int:
    valid = 0
    for pasw in values:
        requires = 0
        for field in ['byr:', 'iyr:','eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']:
            if field in pasw:
                requires += 1
        if requires == 7:
            valid +=1 
    return valid

result1 = count_valid(values)
print(f'Part One = {result1}')

def count_valid2(values: List[str]) -> int:
    valid = 0
    values_list = [i.split() for i in values]
    needs = ['byr:', 'iyr:','eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    for pasw in values_list:
        requires = 0
        for field in pasw:
            check = field[4:]
            if field[:4] == needs[0]: #byr
                if len(check) == 4 and check.isnumeric() and 2002 >= int(check) >= 1920:
                    requires += 1
            elif field[:4] == needs[1]: #iyr
                if len(check) == 4 and check.isnumeric() and 2020 >= int(check) >= 2010:
                    requires += 1
            elif field[:4] == needs[2]: #eyr
                if len(check) == 4 and check.isnumeric() and 2030 >= int(check) >= 2020:
                    requires += 1
            elif field[:4] == needs[3]: #hgt
                if check[:-2].isnumeric():
                    if check[-2:] == 'cm':
                        if 193 >= int(check[:-2]) >= 150:
                            requires += 1
                    elif check[-2:] == 'in':
                        if 76 >= int(check[:-2]) >= 59:
                            requires += 1
            elif field[:4] == needs[4]: #hcl
                if check[0] == '#' and len(check) == 7 and all(c in '0123456789abcdef' for c in check[1:]):
                    requires += 1
            elif field[:4] == needs[5]: #ecl
                if len(check) == 3 and check in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    requires += 1
            elif field[:4] == needs[6]: #pid
                if len(check) == 9 and check.isnumeric():
                    requires += 1
        if requires == 7:
            valid += 1
    return valid

result2 = count_valid2(values)
print(f'Part Two = {result2}')
