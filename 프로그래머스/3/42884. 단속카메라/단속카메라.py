def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])

    last_camera = -30001

    for route in routes:
        start, end = route

        if last_camera < start:
            answer += 1
            last_camera = end

    return answer