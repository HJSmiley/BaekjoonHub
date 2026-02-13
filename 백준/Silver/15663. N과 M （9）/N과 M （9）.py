from itertools import permutations

_, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = sorted(set(permutations(nums, m)))
for i in answer:
    print(*i)