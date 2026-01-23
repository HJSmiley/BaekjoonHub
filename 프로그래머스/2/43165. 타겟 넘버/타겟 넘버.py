total = []
answer = 0


def add(n, numbers, target, idx):

    global total, answer

    if idx == n:
        if sum(total) == target:
            answer += 1
        return

    # (+)
    total.append(numbers[idx])
    add(n, numbers, target, idx + 1)
    total.pop()

    # (-)
    total.append(-numbers[idx])
    add(n, numbers, target, idx + 1)
    total.pop()


def solution(numbers, target):

    n = len(numbers)
    add(n, numbers, target, 0)

    return answer