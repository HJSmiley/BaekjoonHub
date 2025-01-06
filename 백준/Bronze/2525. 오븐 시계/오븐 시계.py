a, b = map(int, input().split())
c = int(input())

time = a * 60 + b + c
h = time // 60
m = time % 60

if h >= 24:
    h -= 24
    
print(h, m)