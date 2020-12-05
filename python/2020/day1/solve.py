def solve(data):
    ans1 = 0
    ans2 = 0
    for x in range(0, len(data)): 
        for y in range(x,len(data)):
            i = data[x]
            j = data[y]
            if ((i+j) == 2020):
                ans1 = i*j
                break
            for z in range(y, len(data)):
                k = data[z]
                if((i+j+k) == 2020):
                    ans2 = i*j*k
                    break
    return ans1,ans2

with open("in.txt") as input:
    nums = []
    for row in input:
        nums.append(int(row))
    nums.sort()
    ans = solve(nums)
    print(ans)
