cnt = 0
max_cnt = -1

for _ in range(10):
    o, i = map(int, input().split())
    cnt -= o
    cnt += i
    max_cnt = max(cnt, max_cnt)

print(max_cnt)