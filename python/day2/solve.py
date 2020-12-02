def part_one(key, char, _min, _max):
    if int(_min) <= key.count(char) <= int(_max):
        return 1
    return 0

def part_two(key, char, _min, _max):
    if ((key[int(_min) - 1] == char) ^ (key[int(_max) - 1] == char)):
        return 1
    return 0

with open("in.txt") as input:
    valid_one = 0
    valid_two = 0
    for line in input:
        key = line.split(' ')[-1]
        char = line.split(' ')[1][:-1]
        _min, _max = line.split(' ')[0].split('-')
        valid_one += part_one(key, char, _min, _max)
        valid_two += part_two(key, char, _min, _max)
    print(valid_one)
    print(valid_two)
