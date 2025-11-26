result = "GLOBAL"
lst = ["l", "k", "p"]

for _ in range(3):
    s = input()
    if s[0] in lst:
        lst.remove(s[0])

if len(lst) == 0:
    print("GLOBAL")
else:
    print("PONIX")