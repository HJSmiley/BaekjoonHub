n = int(input())
res = {}

for i in range(1, n + 1):
    res[i] = int(input())

if res[1] == min(res.values()):
    print("ez")
elif res[1] == max(res.values()):
    print("hard")
else:
    print("?")