import heapq

def solution(jobs):
    answer = 0
    now = 0
    i = 0
    count = 0
    hq = []

    jobs.sort()

    while count < len(jobs):
        while i < len(jobs) and jobs[i][0] <= now:
            heapq.heappush(hq, [jobs[i][1], jobs[i][0]])
            i += 1

        if hq:
            duration, req_time = heapq.heappop(hq)
            now += duration
            answer += now - req_time
            count += 1
        else:
            now = jobs[i][0]

    return answer // len(jobs)