first = [500]*1 + [300]*2 + [200]*3 + [50]*4 + [30]*5 + [10]*6
second = [512]*1 + [256]*2 + [128]*4 + [64]*8 + [32]*16

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if 1<=a<=21 and 1<=b<=31:
        res = (first[a-1] + second[b-1]) * 10000
    elif 1<=a<=21:
        res = first[a-1] * 10000
    elif 1<=b<=31:
        res = second[b-1] * 10000
    else:
        res = 0

    print(res)