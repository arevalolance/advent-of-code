import fileinput

def solve(data, i):
    x,y = 0,0
    if data[i] == '^':
        y += 1
    elif data[i] == '>':
        x += 1
    elif data[i] == 'v':
        y -= 1
    elif data[i] == '<':
        x -= 1
    return x,y

houses = 0
c = set()
for line in fileinput.input():
    x,y,_x,_y = 0,0,0,0
    data = line.strip()
    for i in range(0, len(data)):
        if i % 2 == 0:
            a,b = solve(data, i)
            x += a
            y += b
        else:
            a,b = solve(data, i)
            _x += a
            _y += b
        
        c.add(str(x) + " " + str(y))
        c.add(str(_x) + " " + str(_y))

print(len(c))
