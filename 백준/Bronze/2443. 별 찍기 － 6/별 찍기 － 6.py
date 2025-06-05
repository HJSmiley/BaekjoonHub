n = int(input())
i = 0

for j in range(2*n-1, 0, -2):
    print(' ' * i, end='')
    print('*' * j)
    i += 1