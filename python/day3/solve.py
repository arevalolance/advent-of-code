def solve(input, dx, dy):
    x = dx
    y = dy
    trees = 0
    
    while True:
        xpos = x % len(input[0])
        if input[y][xpos] == "#":
            trees += 1
        
        x += dx
        y += dy
        if y >= len(input):
            break
    return trees

with open("in.txt") as input:
    data = []
    for line in input:
        data.append([x for x in line.strip()])
    print(solve(data,3,1))
    a = solve(data,1,1)
    b = solve(data,3,1)
    c = solve(data,5,1)
    d = solve(data,7,1)
    e = solve(data,1,2)
    print(a*b*c*d*e)