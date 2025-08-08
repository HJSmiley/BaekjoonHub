a = int(input())
b = int(input())
c = int(input())
res = str(a * b * c)

dic = {i: 0 for i in range(10)}

for i in res:
    dic[int(i)] += 1

for j in dic:
    print(dic[j])