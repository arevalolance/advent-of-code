import fileinput
import re

def part_one(p):
    p = set(p)
    p.add('cid')
    p.remove('cid')
    return len(p) == 7

def height_check(v):
    if 'cm' in v: # if height is in centimeters
        n, r = v.split('cm', maxsplit=1)
        return r == '' and 150 <= int(n) <= 193
    if 'in' in v: # if height is in inches
        n, r = v.split('in', maxsplit=1)
        return r == '' and 59 <= int(n) <= 76
    return False


def part_two(pair):
    key, value = pair.split(':')
    if key == "byr":
        return 1920 <= int(value) <= 2002
    elif key == "iyr":
        return 2010 <= int(value) <= 2020
    elif key == "eyr":
        return 2020 <= int(value) <= 2030
    elif key == "hgt":
        return height_check(v)
    elif key == "hcl":
        return re.fullmatch(r'#[0-9a-f]{6}', value)
    elif key == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif key == "pid":
        return re.fullmatch(r'[0-9]{9}', value)
    elif key == "cid":
        return True

# valid = all 7 present, cid is optional 
# invalid missing hgt
all_pp = []
curr_pp = set()
for line in fileinput.input():
    line = line.strip()
    if not line:
        all_pp.append(curr_pp)
        curr_pp = set()
    else:
        pairs = line.split(' ')
        for pair in pairs:
            k, v = pair.split(':')
            if part_one(k):
                curr_pp.add(pair)
            # if part_two(pair):
                # curr_pp.add(k)

print(len(all_pp))
print(len(list(x for x in all_pp if part_one(x))))