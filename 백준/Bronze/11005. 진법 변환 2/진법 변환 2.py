n, b = map(int, input().split())
arr = []

arr.append(n % b)
while n // b > 0:
    n //= b
    arr.append(n % b)

for i in arr[::-1]:
    if 10 <= i <= 35:
        print(chr(i + 55), end='')
    else:
        print(i, end='')