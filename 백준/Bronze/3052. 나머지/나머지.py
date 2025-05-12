s = set()

for _ in range(10):
    n = int(input()) % 42
    if n not in s:
        s.add(n)

print(len(s))