def solution(brown, yellow):
    for i in range(5000):
        for j in range(5000):
            if 2 * (i - 2) + 2 * j == brown and i * j == brown + yellow:
                return [j, i]
    return