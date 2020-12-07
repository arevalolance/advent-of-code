import fileinput

lines = list(fileinput.input())
#lines.append('')

for line in lines:
    line = line.strip()
    k = line.split('\"')
    for i in k:
        if not i:
            for j in i:
          
