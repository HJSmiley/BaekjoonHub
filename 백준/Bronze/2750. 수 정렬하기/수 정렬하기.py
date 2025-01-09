n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

for _ in range(n):
    print(arr.pop())