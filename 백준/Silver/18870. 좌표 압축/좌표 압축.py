import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

temp = sorted(set(arr))

dic = {temp[i]:i for i in range(len(temp))}

for i in arr:
    print(dic[i], end=' ')