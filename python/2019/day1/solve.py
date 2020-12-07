import fileinput
import math

lines = list(fileinput.input())
#lines.append('')

fuel = 0
for line in lines:
    line = line.strip()
    mass = int(line)
    req = 0 
    while mass != 0:
        mass = math.floor(mass/3) - 2
        if mass <= 0:
            break
        req += mass
    fuel += req
print(fuel)
