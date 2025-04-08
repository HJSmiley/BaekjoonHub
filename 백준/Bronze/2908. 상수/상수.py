a, b = map(str, input().split())
max = max(int(a[::-1]), int(b[::-1]))
print(max)