a, b, c = map(int, input().split())

lst1 = [a == b + c, a == b - c, a == b * c, a == b // c, c == a + b, c == a - b, c == a * b, c == a // b]
lst2 = [f'{a}={b}+{c}', f'{a}={b}-{c}', f'{a}={b}*{c}', f'{a}={b}/{c}', f'{a}+{b}={c}', f'{a}-{b}={c}', f'{a}*{b}={c}', f'{a}/{b}={c}']

for i in range(8):
    if lst1[i]:
        print(lst2[i])
        break