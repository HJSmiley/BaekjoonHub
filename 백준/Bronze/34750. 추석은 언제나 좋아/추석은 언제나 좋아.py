n = int(input())

if n >= 1000000:
    print(n // 5, n - n // 5)
elif n >= 500000:
    print(n // 100 * 15, n - n // 100 * 15)
elif n >= 100000:
    print(n // 10, n - n // 10)
else:
    print(n // 20, n - n // 20)