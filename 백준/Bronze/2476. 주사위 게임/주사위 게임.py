n = int(input())
prize = []

for _ in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        prize.append(10000 + a*1000)
    elif a == b or b == c or c == a:
        if a == b or b == c:
            prize.append(1000 + b*100)
        else:
            prize.append(1000 + a*100)
    else:
        prize.append(max(a, b, c)*100)

print(max(prize))