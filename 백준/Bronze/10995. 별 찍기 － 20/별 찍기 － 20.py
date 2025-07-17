n = int(input())

if n == 1:
    print('*')
else:
    for i in range(n):
        if i % 2 == 0:
            print('* '*(n-1) + '*')
        else:
            print(' *'*n)