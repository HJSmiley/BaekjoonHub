n = int(input())
dic = {}

for _ in range(n):
    num = int(input())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

dic = sorted(dic, key = lambda x: (-dic[x], x))

print(dic[0])