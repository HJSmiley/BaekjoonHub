word = input().upper()
dic = dict()

for c in word:
    if c not in dic:
        dic[c] = 0
    else:
        dic[c] += 1

lst = [k for k, v in dic.items() if max(dic.values()) == v]

if len(lst) == 1:
    print(*lst)
else:
    print("?")