n = int(input())
lst = []

for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        lst.append(b)

if len(lst) == 0:
    print(-1)
else:
    print(sorted(lst)[0])