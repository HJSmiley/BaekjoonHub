n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

B.sort(reverse=True)
A.sort()

for i in range(n):
    ans += A[i] * B[i]

print(ans)