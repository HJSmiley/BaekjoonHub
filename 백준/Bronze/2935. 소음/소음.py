a = len(input()) - 1
op = input()
b = len(input()) - 1

if op == '+':
    if a == b:
        print(2*(10**a))
    else:
        n = [0 for _ in range(max(a, b)+1)]
        n[-max(a, b)-1] = 1
        n[-min(a, b)-1] = 1
        print(*n, sep='')
else:
    print(10**(a+b))