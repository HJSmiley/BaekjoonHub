from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    n = len(progresses)
    
    while progresses:
        tmp = []
        for i in range(n):
            progresses[i] += speeds[i]
        while progresses and progresses[0] >= 100:
            tmp.append(progresses.popleft())
            speeds.popleft()
            n -= 1
        if tmp:
            answer.append(len(tmp))

    return answer