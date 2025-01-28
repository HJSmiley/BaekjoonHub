n = int(input())

for i in range(1, n+1):
    lst = list(map(str, input().split()))
    print(f'Case #{i}: ', end='')
    while lst:
        print(lst.pop(), end=' ')
    print()