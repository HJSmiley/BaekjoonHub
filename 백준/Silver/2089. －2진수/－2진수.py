n = int(input())
ans = []

if n == 0:
    print(0)

while n:
    if n % (-2):
        ans.append(1)
        n = n // (-2) + 1
    else:
        ans.append(0)
        n //= (-2)

print(*ans[::-1], sep='')