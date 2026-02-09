from collections import defaultdict

def solution(clothes):
    answer = 1
    dt = defaultdict(list)

    for a, b in clothes:
        dt[b].append(a)

    for key in dt:
        answer *= len(dt[key]) + 1

    return answer - 1