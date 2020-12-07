import fileinput

def is_nice(inp):
    warn = ['ab','cd','pq','xy']
    
    # check if contains non valid
    for item in warn:
        if item in inp:
            print(inp, "ohno")
            return 0

    #check vowels
    vc = (inp.count('a') + inp.count('e') + inp.count('i') +
            inp.count('o') + inp.count('u'))
    if vc < 3:
        return 0

    # repeating
    r = 0
    if any([inp[i] == inp[i+1] for i in range(len(inp)-1)]):
        return 1
    else:
        return 0

def new_nice(inp):
    if not any([inp[i] == inp[i+2] for i in range(len(inp)-2)]):
        return False
    if any([(inp.count(inp[i:i+2])>=2) for i in range(len(inp)-2)]): 
        return True

    return False 
  
nice = 0
for line in fileinput.input():
    data = line.strip()
    nice += new_nice(data)
print(nice)
