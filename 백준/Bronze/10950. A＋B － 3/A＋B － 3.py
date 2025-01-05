t = int(input())
arr = []

for _ in range(t):
    a, b = map(int, input().split())
    arr.append((a, b))

for a, b in arr:
    print(a+b)