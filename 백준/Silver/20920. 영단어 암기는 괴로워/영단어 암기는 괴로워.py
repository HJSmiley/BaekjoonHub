import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = []
d = {}

for _ in range(n):
    word = input()
    if len(word) >= m:
        arr.append(word)
        if word in d:
            d[word] += 1
        else:
            d[word] = 0

arr = sorted(set(arr), key=lambda x: (-d[x], -len(x), x))

print(*arr, sep='\n')