def solution(n, times):
    start = 1
    end = max(times) * n
    answer = end

    while start <= end:
        mid = (start + end) // 2
        people = sum(mid // t for t in times)

        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer