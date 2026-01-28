def solution(answers):
    answer = []
    n = len(answers)

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    all = [0, 0, 0]

    for i in range(n):
        if answers[i] == first[i % 5]:
            all[0] += 1
        if answers[i] == second[i % 8]:
            all[1] += 1
        if answers[i] == third[i % 10]:
            all[2] += 1

    for j in range(3):
        if all[j] == max(all):
            answer.append(j + 1)

    return answer