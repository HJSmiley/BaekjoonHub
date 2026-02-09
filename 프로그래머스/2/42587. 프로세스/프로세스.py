from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(priorities[i], i) for i in range(len(priorities))])

    while q:
        x = q.popleft()
        if any(x[0] < tmp[0] for tmp in q):
            q.append(x)
        else:
            answer += 1
            if x[1] == location:
                return answer
    return