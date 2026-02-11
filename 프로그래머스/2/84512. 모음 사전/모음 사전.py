def solution(word):
    answer = 0

    weights = []
    val = 0
    for i in range(5):
        val = val * 5 + 1
        weights.append(val)
    weights.sort(reverse=True)

    vowels = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}

    for i, char in enumerate(word):
        answer += vowels[char] * weights[i] + 1

    return answer