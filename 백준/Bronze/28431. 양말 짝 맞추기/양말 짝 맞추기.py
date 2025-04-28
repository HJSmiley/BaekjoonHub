lst = []
for _ in range(5):
    s = int(input())
    if s in lst:
        lst.remove(s)
    else:
        lst.append(s)
print(*lst)