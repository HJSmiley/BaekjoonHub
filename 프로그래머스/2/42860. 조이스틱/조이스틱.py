def solution(name):
    length = len(name)
    answer = 0

    for c in name:
        answer += min(ord(c) - ord("A"), ord("Z") - ord(c) + 1)

    move = length - 1

    for left in range(length):
        next_idx = left + 1

        while next_idx < length and name[next_idx] == "A":
            next_idx += 1

        right = length - next_idx

        move = min(
            move,
            2 * left + right,
            left + 2 * right,
        )

    return answer + move