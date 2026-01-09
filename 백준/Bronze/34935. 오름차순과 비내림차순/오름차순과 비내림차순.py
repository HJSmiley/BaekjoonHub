_ = int(input())
lst = list(map(int, input().split()))

if len(lst) == len(set(lst)):
    print(1)
else:
    print(0)