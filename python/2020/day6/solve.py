import fileinput
import string

lines = list(fileinput.input())
lines.append('')
a1 = 0
a2 = 0

any_ans = set()
all_ans = set(string.ascii_lowercase)

for line in lines:
    line = line.strip()
    if not line:
        a1 += len(any_ans)
        a2 += len(all_ans)
        any_ans = set()
        all_ans = set(string.ascii_lowercase)
    else:
        for char in line:
            any_ans.add(char)

        for char in string.ascii_lowercase:
            if char not in line and char in all_ans:
                all_ans.remove(char)

print(a1,a2)
