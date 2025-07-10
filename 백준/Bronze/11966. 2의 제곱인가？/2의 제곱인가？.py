n = int(input())
sq = [2**i for i in range(31)]

if n in sq:
    print(1)
else:
    print(0)