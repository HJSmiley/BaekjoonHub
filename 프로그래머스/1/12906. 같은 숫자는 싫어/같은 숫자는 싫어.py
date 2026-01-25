from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = [arr.popleft()]
    while arr:
        tmp = arr.popleft()
        if tmp == answer[-1]:
            continue
        answer.append(tmp)
    return answer