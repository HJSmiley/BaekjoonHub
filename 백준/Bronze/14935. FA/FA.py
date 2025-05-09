def F(x):
    global ans

    if x == ans:
        return 'FA'
    else:
        y = int(x[0]) * len(x)
        ans = y
        return F(y)

x = input()
ans = int(x) - 1

print(F(x))