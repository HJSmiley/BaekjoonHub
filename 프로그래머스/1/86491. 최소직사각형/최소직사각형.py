def solution(sizes):
    # sort([w, h])
    for size in sizes:
        size.sort()

    # maxW와 maxH 각각 갱신
    h = w = answer = 0
    for size in sizes:
        if size[0] > h:
            h = size[0]
        if size[1] > w:
            w = size[1]

    answer = w * h
    
    return answer