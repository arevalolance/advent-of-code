import fileinput
import numpy as np

grid = np.zeros((1000,1000), 'int32')

for line in fileinput.input():
    data = line.strip()
    _l = data.split()
    
    if _l[0] == 'turn':
        x,y = _l[2].split(',')
        _x,_y = _l[4].split(',')
        x,y,_x,_y = int(x), int(y), int(_x), int(_y)

        if _l[1] == 'on':
            grid[x:_x+1, y:_y+1] += 1
        else:
            assert _l[1] == 'off'
            grid[x:_x+1,y:_y+1] -= 1
            grid[grid<0] = 0
    else:
        assert _l[0] == 'toggle'
        x,y = _l[1].split(',')
        _x,_y = _l[3].split(',')
        x,y,_x,_y = int(x), int(y), int(_x), int(_y)
        grid[x:_x+1, y:_y+1] += 2

print(np.sum(grid))
