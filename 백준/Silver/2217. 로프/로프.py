N = int(input())

ropes = [int(input()) for _ in range(N)]
ropes.sort()

max_w = 0

for i in range(N):
    can_w = ropes[i]
    can_up_w = can_w * (N - i)
    
    if can_up_w > max_w:
        max_w = can_up_w

print(max_w)