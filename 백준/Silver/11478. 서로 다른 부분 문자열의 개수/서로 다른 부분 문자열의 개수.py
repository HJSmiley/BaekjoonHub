s = input()
ss = set()

for i in range(len(s)):
    for j in range(len(s)):
        ss.add(s[i : i + j])

print(len(ss))