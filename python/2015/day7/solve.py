import fileinput
import math

print(123 & 456)
print(123 | 456)
print('left',123 << 2)
print('right',456 >> 2)
print(~123)
print(~456)

gates = dict()
def solve(q):
    if 'AND' in q:
        return q[0] and q[2]
    elif 'OR' in q:
        return q[0] and q[2]
    elif 'LSHIFT' in q:
        return q[0] << q[2]
    elif 'RSHIFT' in q:
        return q[0] >> q[2]
    elif 'NOT' in q:
        return ~q[0]
 
for line in fileinput.input():
    line = line.strip()
    q = line.split('->')
    print(q)
    act = q[0].split()
    print(solve(act))
