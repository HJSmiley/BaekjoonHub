from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        x = q.popleft()
        count = 0
        for tmp in q:
            count += 1
            if x > tmp:
                break
        answer.append(count)
        
    return answer