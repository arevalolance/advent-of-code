import fileinput
import math

def solve(inp,l,h):
    a = math.floor((h+l)/2)
    b = math.ceil((h+l)/2)
    if inp == 'F' or inp == 'L':
        return l,a
    elif inp == 'B' or inp == 'R':
        return b,h
        
ids = []
for line in fileinput.input():
    data = line.strip()
    _l = 0
    _h = 127
    pp = []
    row = 0
    for char in data:
        _l,_h = solve(char,_l,_h)
        if char == 'B':
            row = _h
        elif char == 'F':
            row = _l
    a,b = 0,7
    col = 0
    for x in data[-3:]:
        a,b = solve(x,a,b)
        if x == 'R':
            col = a
        elif x == 'L':
            col = b
    ids.append(row*8+col)

for x in range(min(ids), max(ids)):
    if x not in ids:
        print(x)

print(max(ids))
