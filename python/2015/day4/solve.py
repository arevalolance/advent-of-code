import fileinput
import hashlib

data = 'yzbqklnj' 
ctr = 0
while True:
    data = data[:8] + str(ctr)
    result = hashlib.md5(data.encode())
    hexhash = result.hexdigest()
    if hexhash[:6] == '000000':
        print(data[:8]+str(ctr), hexhash)
        break
    else:
        ctr += 1

