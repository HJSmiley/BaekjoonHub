def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        answer.append(sorted(array[i - 1 : j])[k - 1])
    return answer