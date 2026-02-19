import heapq

def solution(operations):
    answer = []
    max_hq = []
    min_hq = []
    deleted = [False] * len(operations)

    for idx, op in enumerate(operations):
        if op == "D 1":
            while max_hq and not deleted[max_hq[0][1]]:
                heapq.heappop(max_hq)
            if max_hq:
                _, i = heapq.heappop(max_hq)
                deleted[i] = False
        elif op == "D -1":
            while min_hq and not deleted[min_hq[0][1]]:
                heapq.heappop(min_hq)
            if min_hq:
                _, i = heapq.heappop(min_hq)
                deleted[i] = False
        else:
            num = int(op.split()[1])
            heapq.heappush(min_hq, (num, idx))
            heapq.heappush(max_hq, (-num, idx))
            deleted[idx] = True

    while max_hq and not deleted[max_hq[0][1]]:
        heapq.heappop(max_hq)
    while min_hq and not deleted[min_hq[0][1]]:
        heapq.heappop(min_hq)

    if not max_hq or not min_hq:
        return [0, 0]

    return [-max_hq[0][0], min_hq[0][0]]