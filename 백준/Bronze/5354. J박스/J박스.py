t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print('#', end='\n\n')
    else:
        print('#'*n)
        for i in range(2, n):
            print('#', end='')
            print('J'*(n-2), end='')
            print('#')
        print('#'*n, end='\n\n')